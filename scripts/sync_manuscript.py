#!/usr/bin/env python3
"""Refresh curated metadata from a supplied manuscript directory."""

import argparse
from collections import Counter
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((ROOT / 'data' / name).read_text())


def save(name, value):
    (ROOT / 'data' / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def parse_bibliography(text):
    """Read braced, quoted, and bare BibTeX fields without altering URL syntax."""
    entries = {}
    for block in re.split(r'(?m)(?=^@\w+\s*\{)', text):
        match = re.match(r'@(\w+)\s*\{\s*([^,]+),', block)
        if not match:
            continue
        record = {'type': match[1].lower(), 'key': match[2]}
        for field in re.finditer(r'(?m)^\s*(\w+)\s*=\s*', block):
            start = field.end()
            if block[start] == '{':
                depth, end = 1, start + 1
                while end < len(block) and depth:
                    if block[end] == '{' and block[end - 1] != '\\':
                        depth += 1
                    elif block[end] == '}' and block[end - 1] != '\\':
                        depth -= 1
                    end += 1
                value = block[start + 1:end - 1]
            elif block[start] == '"':
                end = start + 1
                while end < len(block) and (block[end] != '"' or block[end - 1] == '\\'):
                    end += 1
                value = block[start + 1:end]
            else:
                value = block[start:].split(',')[0].strip()
            record[field[1].lower()] = value
        if record['key'] in entries:
            raise ValueError('Duplicate bibliography key: ' + record['key'])
        entries[record['key']] = record
    return entries


def plain(value):
    return value.replace('{', '').replace('}', '').replace('\\&', '&').replace('~', ' ')


def normalize(value):
    return re.sub('[^a-z0-9]', '', unicodedata.normalize('NFKD', plain(value)).casefold())


def arxiv_ids(value):
    return set(re.findall(r'(\d{4}\.\d{4,5})', value))


def publication(record):
    venue = plain(record.get('booktitle', record.get('journal', '')))
    year = plain(record['year'])
    if re.search(r'arxiv', venue, re.I):
        label = 'arXiv'
    elif 'CVPR' in venue or 'Computer Vision and Pattern Recognition' in venue:
        label = 'CVPR Workshop' if re.search('workshop', venue, re.I) else 'CVPR'
    elif 'Findings of the Association for Computational Linguistics' in venue:
        label = 'Findings of ACL'
    else:
        markers = [
            ('Pattern Analysis', 'IEEE TPAMI'), ('Visualization and Computer Graphics', 'IEEE TVCG'),
            ('SIGGRAPH Asia', 'SIGGRAPH Asia'), ('Transactions on Graphics', 'ACM TOG'),
            ('Computer Graphics Forum', 'Computer Graphics Forum'),
            ('International Conference on Computer Vision', 'ICCV'), ('(ICCV)', 'ICCV'),
            ('European Conference on Computer Vision', 'ECCV'), ('ECCV', 'ECCV'),
            ('Learning Representations', 'ICLR'), ('Neural Information Processing Systems', 'NeurIPS'),
            ('Robotics and Automation', 'ICRA'), ('Intelligent Robots and Systems', 'IROS'),
            ('Automated Software Engineering', 'ASE Demo'), ('Artificial Intelligence', 'AAAI'),
            ('IJCAI', 'IJCAI'), ('Joint Conference on Artificial Intelligence', 'IJCAI'),
            ('Computer Graphics and Interactive Techniques', 'SIGGRAPH'),
            ('Computer graphics and interactive techniques', 'SIGGRAPH'),
            ('Programming Language Design', 'PLDI'), ('Solar Energy', 'Solar Energy'),
            ('Computer Aided Verification', 'CAV'), ('European Robotics Forum', 'ERF'),
            ('Nature Communications', 'Nature Communications'), ('Computer Modeling in Engineering', 'CMES'),
            ('Photogrammetry', 'ISPRS Archives'),
        ]
        label = next((name for marker, name in markers if marker in venue), '')
    if not label:
        label = 'arXiv' if record['type'] == 'misc' else venue or 'Published'
    if label in ['ECCV', 'ERF']:
        conference_year = re.search(r'\b(20\d{2})\b', venue)
        if conference_year and conference_year[1] != year:
            return f'{label} {conference_year[1]} (proceedings {year})'
    return f'{label} {year}'


def citation_groups(text):
    groups = {}
    current = ''
    for line in text.splitlines():
        if line.lstrip().startswith('%'):
            continue
        heading = re.match(r'\\(?:subsection|subsubsection)\{(.+)\}', line)
        if heading:
            current = heading[1]
        for citation in re.findall(r'\\cite\w*\s*\{([^}]+)\}', line):
            for key in (k.strip() for k in citation.split(',')):
                groups.setdefault(key, [])
                if current not in groups[key]:
                    groups[key].append(current)
    return groups


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manuscript', type=Path)
    args = parser.parse_args()
    source = args.manuscript.resolve()
    bib = parse_bibliography((source / 'references.bib').read_text())
    groups = citation_groups((source / 'sections/chapter03.tex').read_text())
    curation = load('curation.json')
    policies = curation['citation_policies']
    old = {r['citation_key']: r for name in ['featured.json', 'methodological-references.json'] for r in load(name)}
    inventory, candidates = load('papers.json'), load('candidates.json')
    topic_for = {t['title']: t for t in curation['topics']}
    topic_for['Hybrid Construction and Automated Orchestration'] = curation['topics'][-1]

    def match_inventory(record):
        title = normalize(record['title'])
        hits = [p for p in inventory if normalize(p['title']) == title]
        if not hits:
            identifiers = arxiv_ids(record.get('url', '') + record.get('howpublished', ''))
            hits = [p for p in inventory if identifiers & arxiv_ids(p.get('paper_url') or '')]
        if len(hits) > 1:
            raise ValueError('Ambiguous inventory match: ' + record['key'])
        return hits[0] if hits else None

    def build(key, force_topic=None):
        b = bib[key]
        previous = old.get(key, {})
        original = next((p for p in inventory if p['id'] == previous.get('inventory_id')), None) or match_inventory(b)
        paper_url = b.get('url') or ('https://doi.org/' + b['doi'] if b.get('doi') else previous.get('paper_url') or (original or {}).get('paper_url'))
        if not paper_url:
            raise ValueError('Missing research URL: ' + key)
        paper_url = paper_url.replace('\\url{', '').rstrip('}')
        previous_url = previous.get('paper_url', '')
        if paper_url.startswith('https://doi.org/') and paper_url.casefold() == previous_url.casefold():
            paper_url = previous_url
        if re.search(r'\s', paper_url):
            raise ValueError('Whitespace in URL: ' + key)
        topic = topic_for.get((groups.get(key) or [''])[0])
        record = {
            'citation_key': key, 'title': plain(b['title']), 'year': int(b['year']),
            'publication': publication(b), 'paper_url': paper_url,
            'resources': previous.get('resources', (original or {}).get('resources', {})).copy(),
            'topic': force_topic or (topic['id'] if topic else None),
            'survey_section': topic['survey_section'] if topic else '3.2',
            'cited_in': groups.get(key, []),
            'inventory_id': original['id'] if original else None,
            'selection_basis': 'Directly discussed in manuscript Chapter 3',
        }
        if previous.get('scope'):
            record.update({f: previous[f] for f in ['scope', 'reason']})
        return record

    featured, related, supporting, extensions = [], [], [], []
    classified = []
    for key in groups:
        rule = policies.get(key, {'destination': 'homepage'})
        destination = rule['destination']
        record = build(key)
        classified.append({'citation_key': key, 'destination': destination, 'reason': rule.get('reason', 'Direct outdoor construction discussion')})
        if destination == 'homepage':
            if record['topic'] is None:
                raise ValueError('Unmapped technical topic: ' + key)
            featured.append(record)
        elif destination == 'methodological-reference':
            record.update({'scope': rule['scope'], 'reason': rule['reason'], 'anchor': rule['anchor']})
            related.append(record)
        elif destination == 'journal-extension':
            record['parent_key'] = rule['parent_key']
            extensions.append(record)
        else:
            record.update({'category': destination, 'reason': rule['reason']})
            supporting.append(record)
    featured_by_key = {p['citation_key']: p for p in featured}
    for extension in extensions:
        featured_by_key[extension.pop('parent_key')].setdefault('extensions', []).append(extension)

    selected_ids = {p['inventory_id'] for p in featured if p['inventory_id']}
    related_ids = {p['inventory_id'] for p in related if p['inventory_id']}
    supporting_ids = {p['inventory_id'] for p in supporting if p['inventory_id']}
    curation['inventory_dispositions'] = [
        {'inventory_id': p['id'], 'destination': 'homepage' if p['id'] in selected_ids else 'methodological-references' if p['id'] in related_ids else 'supporting-literature' if p['id'] in supporting_ids else 'extended-reading',
         'reason': 'Placed according to current manuscript discussion and scope'} for p in inventory
    ]
    candidate_resolutions = []
    for candidate in candidates:
        hit = next((p for p in featured if normalize(p['title']) == normalize(candidate['title'])), None)
        if hit:
            candidate_resolutions.append({'candidate_id': candidate['id'], 'citation_key': hit['citation_key'], 'destination': 'homepage', 'reason': 'Current manuscript explicitly discusses this construction task'})
    curation['candidate_resolutions'] = candidate_resolutions
    curation['classified_citations'] = classified
    curation['source_documents'] = [
        {'file': name, 'sha256': hashlib.sha256((source / name).read_bytes()).hexdigest()}
        for name in ['sections/chapter03.tex', 'sections/chapter04.tex', 'sections/chapter05.tex', 'tables/table4.tex', 'references.bib']
    ]
    curation['last_synced'] = date.today().isoformat()
    curation['counts'].update({
        'homepage_methods': len(featured), 'methodological_references': len(related),
        'supporting_literature': len(supporting), 'journal_extensions': len(extensions),
        'chapter3_citations': len(groups), 'bibliography_entries': len(bib),
        'added_from_manuscript': sum(p['inventory_id'] is None for p in featured),
        'active_boundary_candidates': len(candidates) - len(candidate_resolutions),
        'provisional_promoted': sum(p['provisional'] and p['id'] in selected_ids for p in inventory),
    })
    save('featured.json', featured)
    save('methodological-references.json', related)
    save('supporting-references.json', supporting)
    save('curation.json', curation)
    print(json.dumps({'counts': curation['counts'], 'topics': dict(Counter(p['topic'] for p in featured))}, indent=2))


if __name__ == '__main__':
    main()
