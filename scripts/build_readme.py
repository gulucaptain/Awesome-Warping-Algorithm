#!/usr/bin/env python3
"""Render the GitHub-native README from a single curated catalog (stdlib only)."""
from pathlib import Path
import argparse
import json
import re
from urllib.parse import quote, urlparse

ROOT = Path(__file__).resolve().parents[1]
BADGE = 'https://img.shields.io/badge/'


def badge(label, value, color, url=None):
    message = quote(value.replace('-', '--'), safe='')
    source = f'{BADGE}{quote(label, safe="")}-{message}-{color}?style=flat-square'
    image = f'![{label}: {value}]({source})'
    return f'[{image}]({url})' if url else image


def resource(label, url, color):
    # Plain-text links remain available through image alt text.
    return badge(label, 'Read' if label in ('Paper', 'Reference') else 'Visit', color, url) if url else badge(label, '未核实', '89939E')


def repository_slug(url):
    parsed = urlparse(url)
    if parsed.netloc.lower() != 'github.com' or not re.fullmatch(r'/[^/]+/[^/]+/?', parsed.path):
        raise ValueError(f'Not a repository root: {url}')
    return parsed.path.strip('/')


def resources(work):
    items = [resource(work['paper_label'], work['paper'], '2563EB'),
             resource('Project', work['project'], '087F8C'),
             resource('GitHub', work['github'], '243247')]
    if work['github']:
        slug = repository_slug(work['github'])
        for metric, color in [('stars', 'C58A18'), ('forks', '64748B')]:
            src = f'https://img.shields.io/github/{metric}/{slug}?style=flat-square&label={metric}&color={color}'
            items.append(f'[![GitHub {metric}]({src})]({work["github"]}{"/stargazers" if metric == "stars" else "/forks"})')
    return ' '.join(items)


def render():
    data = json.loads((ROOT / 'data/catalog.json').read_text())
    works = data['works']
    ids = [w['id'] for w in works]
    assert len(ids) == len(set(ids)), 'Duplicate work IDs'
    by_id = {w['id']: w for w in works}
    classic = [w for w in works if w['era'] == 'classic']
    recent = [w for w in works if w['era'] == 'recent']
    repos = {w['github'].lower().rstrip('/') for w in works if w['github']}
    stats = ' '.join([badge('Works', str(len(works)), '243247', '#recent'),
                      badge('Classics', str(len(classic)), '64748B', '#classics'),
                      badge('Recent', str(len(recent)), '087F8C', '#recent'),
                      badge('GitHub repos', str(len(repos)), '2563EB', '#topics')])
    tech_rows = ['| 技术族 | 核心表示 | 文献入口 |', '| --- | --- | --- |']
    for tech in data['technologies']:
        label = tech['id']
        members = [w for w in works if label in w['technology']]
        refs = ' · '.join(f'[{w["name"]}](#{w["id"]})' for w in members)
        tech_rows.append(f'| <a id="{label.lower()}"></a>**{label} · {tech["name"]}** | {tech["description"]} | {refs} |')
    topic_rows = ['| Topic / 领域 | 关注的问题 | 文献入口 |', '| --- | --- | --- |']
    for topic in data['topics']:
        refs = ' · '.join(f'[{by_id[aid]["name"]}](#{aid})' for aid in topic['works'])
        topic_rows.append(f'| <a id="{topic["id"]}"></a>**{topic["name"]}**<br>{topic["english"]} | {topic["question"]} | {refs} |')

    def entry(work):
        tags = ' '.join(f'[`{t}`](#{t.lower()})' for t in work['technology'])
        note = {'framework': '通用实现框架，计数属于整个仓库',
                'unofficial': '非官方复现',
                'reimplementation': '复现代码；仓库自述为 reimplementation',
                'official': '作者实现'}.get(work['code_kind'])
        result = [f'<a id="{work["id"]}"></a>',
                  f'#### {work["name"]}',
                  '', f'**{work["publication"]}** · {tags}',
                  '', resources(work), '', work['summary'] + '。']
        if note:
            slug = repository_slug(work['github'])
            result += ['', f'<sub>{note} · <a href="{work["github"]}">{slug}</a></sub>']
        # Retain caveats and historical publication notes without widening the list.
        result += ['', '<details>', '<summary>方法边界与备注</summary>', '', work['caveat'], '', '</details>', '']
        return '\n'.join(result)

    recent_parts = []
    for year in sorted({w['year'] for w in recent}, reverse=True):
        members = [w for w in recent if w['year'] == year]
        recent_parts += [f'<a id="year-{year}"></a>\n### {year} · {len(members)} works\n',
                         '\n'.join(entry(w) for w in members),
                         '[↑ 返回年份导航](#recent)\n\n---\n']
    classic_parts = []
    for group in dict.fromkeys(w['group'] for w in classic):
        members = [w for w in classic if w['group'] == group]
        classic_parts += [f'### {group}\n', '\n'.join(entry(w) for w in members),
                          '[↑ 返回经典方法](#classics)\n\n---\n']
    template = (ROOT / 'docs/README.template.md').read_text()
    for key, value in {'STATS': stats, 'DATE': data['updated'],
                       'TECHNOLOGIES': '\n'.join(tech_rows), 'TOPICS': '\n'.join(topic_rows),
                       'RECENT': '\n'.join(recent_parts), 'CLASSICS': '\n'.join(classic_parts)}.items():
        template = template.replace('{{' + key + '}}', value)
    assert '{{' not in template, 'Unfilled template token'
    anchors = re.findall(r'<a id="([^"]+)"></a>', template)
    assert len(anchors) == len(set(anchors)), 'Duplicate anchor'
    internal = re.findall(r'\]\(#([^\)]+)\)', template)
    assert not set(internal) - set(anchors), 'Broken internal anchor'
    assert all(w['paper'] for w in works), 'Each record needs a primary source'
    assert all(w['topics'] for w in works), 'Each record needs a topic'
    return template


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if README is out of date')
    args = parser.parse_args()
    output = render()
    path = ROOT / 'README.md'
    if args.check:
        if not path.exists() or path.read_text() != output:
            raise SystemExit('README is out of date; run python3 scripts/build_readme.py')
        print('README, counts, catalog IDs and internal links are consistent.')
    else:
        path.write_text(output)
        print('Updated README.md')
