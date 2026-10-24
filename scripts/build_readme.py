#!/usr/bin/env python3
"""Generate English and Chinese READMEs from one bilingual catalog (stdlib only)."""
from pathlib import Path
import argparse
import json
import re
from urllib.parse import quote, urlencode, urlparse

ROOT = Path(__file__).resolve().parents[1]
GROUPS = {
    '参数化几何与运动估计': 'Parametric geometry and motion estimation',
    '控制点、样条与局部形状': 'Control points, splines and local shape',
    '拓扑保持与医学配准': 'Topology preservation and medical registration',
    '可微采样与抗混叠': 'Differentiable sampling and antialiasing',
    '特征对齐、动画与三维形变': 'Feature alignment, animation and 3D deformation',
}


def badge(label, value, color, url=None, logo=None, logo_color='white'):
    # Shields uses doubled dashes / underscores to escape literal separators.
    escape = lambda text: quote(text.replace('_', '__').replace('-', '--'), safe='')
    options = {'style': 'flat-square'}
    if logo:
        options.update(logo=logo, logoColor=logo_color)
    source = f'https://img.shields.io/badge/{escape(label)}-{escape(value)}-{color}?{urlencode(options)}'
    result = f'![{label}: {value}]({source})'
    return f'[{result}]({url})' if url else result


def repository_slug(url):
    parsed = urlparse(url)
    if parsed.netloc.lower() != 'github.com' or not re.fullmatch(r'/[^/]+/[^/]+/?', parsed.path):
        raise ValueError(f'Not a repository root: {url}')
    return parsed.path.strip('/')


def resources(work, lang):
    unverified = '未核实' if lang == 'zh-CN' else 'Unverified'
    if work.get('arxiv'):
        items = [badge('arXiv', work['arxiv'].rsplit('/', 1)[-1], 'B31B1B', work['arxiv'], 'arxiv')]
    else:
        items = [badge(work['paper_label'], 'Read', '2563EB', work['paper'])]
    if work.get('hf_paper'):
        items.append(badge('Hugging Face', 'Paper', 'FFD21E', work['hf_paper'], 'huggingface', 'FFD21E'))
    if work.get('hf_model'):
        items.append(badge('Hugging Face', 'Model', 'FFD21E', work['hf_model'], 'huggingface', 'FFD21E'))
    items.append(badge('Project', 'Page' if work['project'] else unverified,
                       '087F8C' if work['project'] else '89939E', work['project']))
    items.append(badge('GitHub', 'Code' if work['github'] else unverified,
                       '181717' if work['github'] else '89939E', work['github'], 'github'))
    if work['github']:
        slug = repository_slug(work['github'])
        for metric, color in [('stars', 'C58A18'), ('forks', '64748B')]:
            src = f'https://img.shields.io/github/{metric}/{slug}?style=flat-square&label={metric}&color={color}'
            target = work['github'] + ('/stargazers' if metric == 'stars' else '/forks')
            items.append(f'[![GitHub {metric}]({src})]({target})')
    return ' '.join(items)


def render(lang):
    data = json.loads((ROOT / 'data/catalog.json').read_text())
    works = data['works']
    chinese = lang == 'zh-CN'
    ids = [w['id'] for w in works]
    assert len(ids) == len(set(ids)), 'Duplicate work IDs'
    by_id = {w['id']: w for w in works}
    classic = [w for w in works if w['era'] == 'classic']
    recent = [w for w in works if w['era'] == 'recent']
    repos = {w['github'].lower().rstrip('/') for w in works if w['github']}
    labels = ['项工作', '个代码仓库', '类基础技术', '个应用领域'] if chinese else ['works', 'repositories', 'techniques', 'topics']
    values = [len(works), len(repos), len(data['technologies']), len(data['topics'])]
    stats = ' &nbsp; · &nbsp; '.join(f'<b>{n}</b> {label}' for n, label in zip(values, labels))
    tech_rows = ['| 技术族 | 核心表示 | 文献入口 |' if chinese else '| Technique family | Core representation | Works |', '| --- | --- | --- |']
    for tech in data['technologies']:
        info = tech if chinese else tech['en']
        members = [w for w in works if tech['id'] in w['technology']]
        refs = ' · '.join(f'[{w["name"]}](#{w["id"]})' for w in members)
        tech_rows.append(f'| <a id="{tech["id"].lower()}"></a>**{tech["id"]} · {info["name"]}** | {info["description"]} | {refs} |')
    topic_rows = ['| 领域 | 关注的问题 | 文献入口 |' if chinese else '| Topic | Core question | Works |', '| --- | --- | --- |']
    for topic in data['topics']:
        name = f'**{topic["name"]}**<br>{topic["english"]}' if chinese else f'**{topic["english"]}**'
        question = topic['question'] if chinese else topic['question_en']
        refs = ' · '.join(f'[{by_id[aid]["name"]}](#{aid})' for aid in topic['works'])
        topic_rows.append(f'| <a id="{topic["id"]}"></a>{name} | {question} | {refs} |')

    def entry(work):
        info = work if chinese else work['en']
        tags = ' '.join(f'[`{t}`](#{t.lower()})' for t in work['technology'])
        notes = {
            'framework': ('通用实现框架，计数属于整个仓库', 'Shared framework; counts refer to the entire repository'),
            'unofficial': ('非官方复现', 'Unofficial reimplementation'),
            'reimplementation': ('复现代码；仓库自述为 reimplementation', 'Reimplementation, as described by the repository'),
            'official': ('作者实现', 'Author implementation'),
        }
        note = notes[work['code_kind']][0 if chinese else 1] if work['code_kind'] else None
        publication = info['publication'].replace('**', '')
        title = work.get('paper_title') or work['name']
        result = [f'<a id="{work["id"]}"></a>', f'#### {title} ({work["venue"]})', '',
                  tags, '', resources(work, lang), '',
                  info['summary'].rstrip('。.') + ('。' if chinese else '.')]
        if note:
            result += ['', f'<sub>{note} · <a href="{work["github"]}">{repository_slug(work["github"])}</a></sub>']
        result += ['', '<details>', '<summary>' + ('方法边界与备注' if chinese else 'Limitations and notes') + '</summary>', '', ('**发表记录：** ' if chinese else '**Publication history:** ') + publication, '', info['caveat']]
        if work.get('arxiv') and work['paper'] != work['arxiv']:
            label = '正式论文 / 原始来源' if chinese else 'Publication / primary source'
            result += ['', f'[{label}]({work["paper"]})']
        result += ['', '</details>', '']
        return '\n'.join(result)

    recent_parts = []
    for year in sorted({w['year'] for w in recent}, reverse=True):
        members = [w for w in recent if w['year'] == year]
        count = f'{len(members)} 项工作' if chinese else f'{len(members)} works'
        back = '↑ 返回年份导航' if chinese else '↑ Back to years'
        recent_parts += [f'<a id="year-{year}"></a>\n### {year} · {count}\n',
                         '\n---\n\n'.join(entry(w) for w in members), f'[{back}](#recent)\n\n---\n']
    classic_parts = []
    for group in dict.fromkeys(w['group'] for w in classic):
        members = [w for w in classic if w['group'] == group]
        back = '↑ 返回经典方法' if chinese else '↑ Back to classics'
        classic_parts += [f'### {group if chinese else GROUPS[group]}\n',
                          '\n---\n\n'.join(entry(w) for w in members), f'[{back}](#classics)\n\n---\n']
    name = 'README.zh-CN.template.md' if chinese else 'README.template.md'
    template = (ROOT / 'docs' / name).read_text()
    for key, value in {'STATS': stats, 'DATE': data['updated'], 'TECHNOLOGIES': '\n'.join(tech_rows),
                       'TOPICS': '\n'.join(topic_rows), 'RECENT': '\n'.join(recent_parts),
                       'CLASSICS': '\n'.join(classic_parts)}.items():
        template = template.replace('{{' + key + '}}', value)
    assert '{{' not in template, 'Unfilled template token'
    anchors = re.findall(r'<a id="([^"]+)"></a>', template)
    assert len(anchors) == len(set(anchors)), 'Duplicate anchor'
    assert not set(re.findall(r'\]\(#([^\)]+)\)', template)) - set(anchors), 'Broken anchor'
    assert all(w['paper'] and w['topics'] for w in works), 'Missing source or topic'
    if not chinese:
        assert not re.search(r'[\u4e00-\u9fff]', template.replace('简体中文', '')), 'Untranslated English page text'
    return template


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check both generated READMEs without writing')
    args = parser.parse_args()
    for lang, filename in [('en', 'README.md'), ('zh-CN', 'README.zh-CN.md')]:
        output = render(lang)
        target = ROOT / filename
        if args.check:
            if not target.exists() or target.read_text() != output:
                raise SystemExit(f'{filename} is out of date; run python3 scripts/build_readme.py')
        else:
            target.write_text(output)
    print('Both READMEs, catalog counts, translations and internal links are consistent.' if args.check else 'Updated README.md and README.zh-CN.md')
