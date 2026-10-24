#!/usr/bin/env python3
"""Generate English and Chinese READMEs from one bilingual catalog (stdlib only)."""
from pathlib import Path
from html import escape
import argparse
import json
import re
from urllib.parse import quote, urlencode, urlparse

ROOT = Path(__file__).resolve().parents[1]

def newest_first(works):
    """Keep catalog order within a publication year."""
    return sorted(works, key=lambda w: -w['year'])


def validate_catalog(data):
    """Require one primary home per work and explicit placeholders for empty topics."""
    for key in ('areas', 'topics', 'technologies', 'works'):
        ids = [item['id'] for item in data[key]]
        assert len(ids) == len(set(ids)), f'Duplicate {key} IDs'
    areas = {a['id'] for a in data['areas']}
    topics = {t['id']: t for t in data['topics']}
    technologies = {t['id'] for t in data['technologies']}
    titles = [re.sub(r'[\W_]+', '', (w.get('paper_title') or w['name']).casefold()) for w in data['works']]
    assert len(titles) == len(set(titles)), 'Duplicate normalized paper titles'
    arxiv_ids = [re.sub(r'v\d+$', '', w['arxiv'].rstrip('/').rsplit('/', 1)[-1])
                 for w in data['works'] if w.get('arxiv')]
    assert len(arxiv_ids) == len(set(arxiv_ids)), 'Duplicate arXiv papers'
    numbers = [t['number'] for t in data['topics']]
    assert len(numbers) == len(set(numbers)), 'Duplicate topic numbers'
    assert {t['area'] for t in data['topics']} == areas, 'Missing or unknown research area'
    for work in data['works']:
        assert work.get('paper_title'), f'Missing specific paper title: {work["id"]}'
        assert work.get('paper_label') != 'Reference', f'Background reference in paper catalog: {work["id"]}'
        assert work['paper'], f'Missing source: {work["id"]}'
        assert work['primary_topic'] in topics, f'Unknown primary topic: {work["id"]}'
        assert work['primary_topic'] in work['topics'], f'Primary topic missing from tags: {work["id"]}'
        assert len(work['topics']) == len(set(work['topics'])), f'Duplicate topic tags: {work["id"]}'
        assert set(work['topics']) <= topics.keys(), f'Unknown topic tag: {work["id"]}'
        assert set(work['technology']) <= technologies, f'Unknown technique: {work["id"]}'
        assert type(work['year']) is int, f'Invalid year: {work["id"]}'
        citation = work.get('citation_snapshot')
        if citation:
            assert type(citation['cited_by_count']) is int and citation['cited_by_count'] >= 0, f'Invalid citation count: {work["id"]}'
            assert citation['record_id'] and citation['source_url'] and citation['as_of'], f'Missing citation provenance: {work["id"]}'
    for topic in data['topics']:
        members = [w for w in data['works'] if w['primary_topic'] == topic['id']]
        tagged = [w for w in data['works'] if topic['id'] in w['topics']]
        assert bool(members) != topic['reserved'], f'Incorrect reserved status: {topic["id"]}'
        assert not topic['reserved'] or not tagged, f'Reserved topic has tagged works: {topic["id"]}'


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


def resources(work):
    if work.get('arxiv'):
        items = [badge('arXiv', work['arxiv'].rsplit('/', 1)[-1], 'B31B1B', work['arxiv'], 'arxiv')]
    else:
        items = [badge(work['paper_label'], 'Read', '2563EB', work['paper'])]
    if work.get('hf_paper'):
        items.append(badge('Hugging Face', 'Paper', 'FFD21E', work['hf_paper'], 'huggingface', 'FFD21E'))
    if work.get('hf_model'):
        items.append(badge('Hugging Face', 'Model', 'FFD21E', work['hf_model'], 'huggingface', 'FFD21E'))
    if work['project']:
        items.append(badge('Project', 'Page', '087F8C', work['project']))
    if work['github']:
        items.append(badge('GitHub', 'Code', '181717', work['github'], 'github'))
        slug = repository_slug(work['github'])
        for metric, color in [('stars', 'C58A18'), ('forks', '64748B')]:
            src = f'https://img.shields.io/github/{metric}/{slug}?style=flat-square&label={metric}&color={color}'
            target = work['github'] + ('/stargazers' if metric == 'stars' else '/forks')
            items.append(f'[![GitHub {metric}]({src})]({target})')
    return ' '.join(items)


def render(lang, data=None):
    if data is None:
        data = json.loads((ROOT / 'data/catalog.json').read_text())
    validate_catalog(data)
    works = data['works']
    chinese = lang == 'zh-CN'
    repos = {w['github'].lower().rstrip('/') for w in works if w['github']}
    labels = ['篇论文', '个代码仓库', '个研究板块', '个主题'] if chinese else ['Papers', 'Repositories', 'Research areas', 'Topics']
    values = [len(works), len(repos), len(data['areas']), len(data['topics'])]
    stats = ' &nbsp; · &nbsp; '.join(f'<b>{n}</b> {label}' for n, label in zip(values, labels))
    tech_rows = ['| 技术族 | 核心表示 | 文献入口 |' if chinese else '| Technique family | Core representation | Works |', '| --- | --- | --- |']
    for tech in data['technologies']:
        info = tech if chinese else tech['en']
        members = newest_first([w for w in works if tech['id'] in w['technology']])
        refs = ' · '.join(f'[{w["name"]}](#{w["id"]})' for w in members)
        tech_rows.append(f'| <a id="{tech["id"].lower()}"></a>**{tech["id"]} · {info["name"]}** | {info["description"]} | {refs} |')
    headers = ['研究板块', 'Topic', '主条目 / 状态'] if chinese else ['Research area', 'Topic', 'Primary entries / status']
    topic_rows = ['<table>', '<thead>', '<tr>' + ''.join(f'<th align="left">{header}</th>' for header in headers) + '</tr>', '</thead>', '<tbody>']
    for area in data['areas']:
        area_name = area['name'] if chinese else area['english']
        area_topics = [t for t in data['topics'] if t['area'] == area['id']]
        for index, topic in enumerate(area_topics):
            topic_name = topic['name'] if chinese else topic['english']
            count = sum(w['primary_topic'] == topic['id'] for w in works)
            status = ('待扩展' if chinese else 'Reserved') if topic['reserved'] else str(count)
            topic_rows.append('<tr>')
            if index == 0:
                topic_rows.append(f'<td rowspan="{len(area_topics)}" valign="middle"><a href="#area-{area["id"]}">{area["number"]}. {escape(area_name)}</a></td>')
            topic_rows += [f'<td><a href="#{topic["id"]}">{topic["number"]} {escape(topic_name)}</a></td>',
                           f'<td>{status}</td>', '</tr>']
    topic_rows += ['</tbody>', '</table>']

    def entry(work):
        info = work if chinese else work['en']
        tags = ' '.join(f'[`{t}`](#{t.lower()})' for t in work['technology'])
        title = work.get('paper_title') or work['name']
        result = [f'<a id="{work["id"]}"></a>', f'#### {title} ({work["venue"]})', '',
                  resources(work) + ' &nbsp; ' + tags, '',
                  info['summary'].rstrip('。.') + ('。' if chinese else '.'), '']
        return '\n'.join(result)

    catalog_parts = []
    for area in data['areas']:
        area_name = area['name'] if chinese else area['english']
        catalog_parts += [f'<a id="area-{area["id"]}"></a>\n## {area["number"]}. {area_name}\n']
        for topic in data['topics']:
            if topic['area'] != area['id']:
                continue
            tid = topic['id']
            topic_name = topic['name'] if chinese else topic['english']
            aliases = '\n'.join(f'<a id="{alias}"></a>' for alias in topic['aliases'])
            members = newest_first([w for w in works if w['primary_topic'] == tid])
            scope = topic['question'] if chinese else topic['question_en']
            scope_label = '本类关注' if chinese else 'Scope'
            count_label = f'{len(members)} 篇论文 · 按年份从新到旧排列' if chinese else f'{len(members)} papers · Newest first'
            if topic['reserved']:
                count_label = '待扩展 · 暂无收录论文' if chinese else 'Reserved · No papers collected yet'
            catalog_parts += [aliases, f'<a id="{tid}"></a>\n### {topic["number"]} {topic_name}\n',
                              f'> **{scope_label}** · {scope}\n>\n> **{count_label}**', '', '---\n']
            if topic['reserved']:
                catalog_parts += [('**待扩展：** 已预留方向，尚未收录论文。后续优先收录与空间对应、重投影、形变、噪声输运或时空对齐直接相关的工作。'
                                   if chinese else '**Reserved:** No papers collected yet. Future entries should directly connect to spatial correspondence, reprojection, deformation, noise transport or spatiotemporal alignment.'), '']
            else:
                catalog_parts += ['\n---\n\n'.join(entry(w) for w in members)]
                related = newest_first([w for w in works if tid in w['topics'] and w['primary_topic'] != tid])
                if related:
                    label = f'关联阅读 · {len(related)} 篇其他 Topic 的论文' if chinese else f'Related reading · {len(related)} papers in other topics'
                    refs = '\n'.join(f'- [{w["name"]}](#{w["id"]}) ({w["year"]})' for w in related)
                    catalog_parts += ['---\n', '<details>', f'<summary>{label}</summary>', '', refs, '', '</details>', '']
            back = '↑ 返回 Topic 导航' if chinese else '↑ Back to topic navigation'
            top = f'↑ {topic["number"]} 本类开头' if chinese else f'↑ Start of {topic["number"]}'
            catalog_parts += [f'[{top}](#{tid}) · [{back}](#topics)\n\n---\n']
    name = 'README.zh-CN.template.md' if chinese else 'README.template.md'
    template = (ROOT / 'docs' / name).read_text()
    reserved_count = sum(t['reserved'] for t in data['topics'])
    reserved_note = (f'，其中 {reserved_count} 个待扩展' if chinese else f', including {reserved_count} reserved topics') if reserved_count else ''
    for key, value in {'STATS': stats, 'DATE': data['updated'],
                       'AREA_COUNT': str(len(data['areas'])), 'TOPIC_COUNT': str(len(data['topics'])),
                       'RESERVED_NOTE': reserved_note,
                       'TECH_COUNT': str(len(data['technologies'])), 'TECHNOLOGIES': '\n'.join(tech_rows),
                       'TOPICS': '\n'.join(topic_rows), 'CATALOG': '\n'.join(catalog_parts)}.items():
        template = template.replace('{{' + key + '}}', value)
    assert '{{' not in template, 'Unfilled template token'
    anchors = re.findall(r'<a id="([^"]+)"></a>', template)
    assert len(anchors) == len(set(anchors)), 'Duplicate anchor'
    targets = re.findall(r'\]\(#([^\)]+)\)', template) + re.findall(r'href="#([^"]+)"', template)
    assert not set(targets) - set(anchors), 'Broken anchor'
    assert all(anchors.count(w['id']) == 1 for w in works), 'Missing or repeated work entry'
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
