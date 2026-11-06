#!/usr/bin/env python3
"""Render the curated reading list and supplements from repository JSON data."""

from collections import Counter
import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((ROOT / 'data' / name).read_text())


ICONS = {
    'paper': '📄', 'code': '💻', 'project': '🌐', 'dataset': '🗃️',
    'documentation': '📘', 'devkit': '🧰', 'product': '🔗', 'preprint': '📝',
}


def links(resources):
    return ' · '.join(f'[{ICONS.get(kind, "🔗")} {kind.title()}]({url})' for kind, url in resources.items())


def entry(paper, anchor=False):
    prefix = f'<a id="paper-{paper["citation_key"]}"></a>' if anchor else ''
    resources = {'paper': paper['paper_url'], **paper['resources']}
    resources = {key: value for key, value in resources.items() if value}
    result = (f'- {prefix}**{paper["title"]}**' + '\\' + '\n'
              f'  <sub>{html.escape(paper["publication"])}</sub> · {links(resources)}')
    for extension in paper.get('extensions', []):
        result += ('\\' + '\n' + f'  <sub>↳ Journal extension: {html.escape(extension["title"])} · {html.escape(extension["publication"])}</sub> '
                   f'· [📄 Journal paper]({extension["paper_url"]})')
    return result + '\n'


def main():
    featured = load('featured.json')
    related = load('methodological-references.json')
    inventory = load('papers.json')
    candidates = load('candidates.json')
    resources = load('resources.json')
    curation = load('curation.json')
    supporting = load('supporting-references.json')
    resolutions = {r['candidate_id']: r for r in curation.get('candidate_resolutions', [])}
    active_candidates = [p for p in candidates if p['id'] not in resolutions]
    selected_ids = {p['inventory_id'] for p in featured if p['inventory_id']}
    related_ids = {p['inventory_id'] for p in related if p['inventory_id']}
    pending_provisional = [p for p in inventory if p['provisional'] and p['id'] not in selected_ids]
    additional = [p for p in featured + related + supporting if p['inventory_id'] is None]
    topics = curation['topics']
    counts = Counter(p['topic'].split('.')[0] for p in featured)
    assert len({p['citation_key'] for p in featured + related}) == len(featured) + len(related)
    assert {p['topic'] for p in featured} == {t['id'] for t in topics}
    assert len(featured) + len(related) + len(supporting) + sum(len(p.get('extensions', [])) for p in featured) == curation['counts']['chapter3_citations']

    sections = {
        '1': ('🌱', 'Synthesis of New Environments', 'synthesis', 'Create new environments using procedural rules, asset composition, learned structures, or visual priors.'),
        '2': ('🧭', 'Reconstruction of Real Environments', 'reconstruction', 'Recover a digital counterpart of a specific real place or observed environmental state.'),
        '3': ('🛠️', 'Transformation of Existing Environments', 'transformation', 'Modify an existing digital environment while maintaining the content and relationships required by the task.'),
    }
    out = [f'''<a id="top"></a>

<div align="center">

# 🌍 Outdoor 3D Simulation<br>Environment Construction Survey

**Automated Construction of Outdoor 3D Simulation Environments for Autonomous Systems**

面向自主系统的室外三维仿真环境自动构建

**🚗 Autonomous Driving &nbsp; · &nbsp; 🚁 Aerial Robotics &nbsp; · &nbsp; 🌲 Outdoor Worlds**

<p>
  <kbd>📚 {len(featured)} selected methods</kbd> &nbsp;
  <kbd>🗂️ {len(topics)} technical topics</kbd> &nbsp;
  <kbd>🧰 {len(resources)} supporting resources</kbd>
</p>

<p>
  <a href="#synthesis">🌱 Synthesis</a> &nbsp; · &nbsp;
  <a href="#reconstruction">🧭 Reconstruction</a> &nbsp; · &nbsp;
  <a href="#transformation">🛠️ Transformation</a> &nbsp; · &nbsp;
  <a href="#hybrid">🤖 Orchestration</a> &nbsp; · &nbsp;
  <a href="#resources">🧰 Resources</a>
</p>

</div>

<p align="center">
  <a href="assets/taxonomy-timeline.png"><img src="assets/taxonomy-timeline.png" alt="Timeline of selected research in synthesis, reconstruction, and transformation of outdoor 3D simulation environments" width="100%"></a>
  <br>
  <sub>Selected methods across synthesis, reconstruction, and transformation. Click the image to enlarge.</sub>
</p>

---

A curated collection of research on automatically constructing outdoor 3D simulation environments. Explore environment synthesis, reconstruction, transformation, and hybrid pipelines, together with [simulation platforms, datasets, and evaluation resources](#resources).

面向室外自主系统的三维仿真环境构建论文与资源，按“生成、重建、变换及混合编排”组织，提供论文、代码、项目与数据集链接。

**Updated {curation['last_synced']}.**

<table>
<tr>
<td width="33%" valign="top">
<h3>🌱 Synthesis</h3>
<p><strong>新环境生成 · {counts['1']} methods</strong></p>
<p>Rules → assets → learned structures → visual priors.</p>
<p><sub>Diversity + constraints</sub></p>
<a href="#synthesis">Explore synthesis →</a>
</td>
<td width="33%" valign="top">
<h3>🧭 Reconstruction</h3>
<p><strong>真实环境重建 · {counts['2']} methods</strong></p>
<p>Maps → geometry → neural scenes → environmental properties.</p>
<p><sub>Reality correspondence</sub></p>
<a href="#reconstruction">Explore reconstruction →</a>
</td>
<td width="33%" valign="top">
<h3>🛠️ Transformation</h3>
<p><strong>现有环境变换 · {counts['3']} methods</strong></p>
<p>Completion → object editing → appearance and physics.</p>
<p><sub>Change + preservation</sub></p>
<a href="#transformation">Explore transformation →</a>
</td>
</tr>
</table>

**🤖 Hybrid construction and orchestration:** {counts['4']} additional methods connect construction stages through executable tools and feedback.

<a id="contents"></a>

## 🗂️ Contents
''']
    for number, (icon, title, anchor, _) in sections.items():
        out.append(f'- [{icon} **{number}. {title}**](#{anchor})')
        out.extend(f'  - [{topic["id"]} {topic["title"]}](#{topic["anchor"]})'
                   for topic in topics if topic['id'].startswith(number + '.'))
    out.extend(['- [🤖 **4. Hybrid Construction and Automated Orchestration**](#hybrid)',
                '- [🧰 **5. Supporting Resources**](#resources)',
                '- [🤝 Contributing](#contributing)',
                '''
**Resource key:** 📄 Paper · 💻 Code · 🌐 Project · 📘 Documentation · 🗃️ Dataset

Papers are grouped by technical approach and ordered by year, newest first within each topic.
'''])

    for number, (icon, title, anchor, description) in sections.items():
        out.append(f'\n---\n\n<a id="{anchor}"></a>\n\n## {icon} {number}. {title}\n\n{description}\n')
        for topic in topics:
            if not topic['id'].startswith(number + '.'): continue
            out.append(f'\n<a id="{topic["anchor"]}"></a>\n\n### {topic["icon"]} {topic["id"]} {topic["title"]}\n\n{topic["description"]}\n')
            members = sorted((p for p in featured if p['topic'] == topic['id']), key=lambda p: (-p['year'], p['title'].casefold()))
            display_groups = curation.get('display_groups', {}).get(topic['id'])
            if display_groups:
                grouped = [key for group in display_groups for key in group['citation_keys']]
                assert len(grouped) == len(set(grouped)) and set(grouped) == {p['citation_key'] for p in members}, topic['id']
                for group in display_groups:
                    out.append(f'\n#### {group["title"]}\n')
                    out.extend(entry(p, anchor=True) for p in members if p['citation_key'] in group['citation_keys'])
            else:
                out.extend(entry(p, anchor=True) for p in members)
        out.append('[↑ Back to contents](#contents)\n')

    out.append('''
---

<a id="hybrid"></a>

## 🤖 4. Hybrid Construction and Automated Orchestration

Hybrid pipelines connect different construction operations. Orchestration selects and executes tools, maintains construction state, and uses feedback to revise intermediate results.
''')
    out.extend(entry(p, anchor=True) for p in sorted((p for p in featured if p['topic'].startswith('4.')), key=lambda p: (-p['year'], p['title'].casefold())))
    out.append('''
Related examples include [3D-GPT](#paper-sun2023gpt3dv1) and [CityX](#paper-zhang2024cityxv1) for language-to-tool orchestration, and [DroneWiS](#paper-zhang2024dronewisv1) for geometry-dependent wind augmentation.

[↑ Back to contents](#contents)

---

<a id="resources"></a>

## 🧰 5. Supporting Resources

Platforms, scene data, assets, and benchmarks for constructing and evaluating simulation environments.
''')
    resource_groups = [
        ('platform', '🏗️ Simulation Platforms', 'Environment execution, configurable scenes, and repeatable trials.'),
        ('scene-data', '🗃️ Scene Data and Evaluation Inputs', 'Observations and scene inputs used in the reviewed experiments.'),
        ('assets', '🧩 Asset Resources', 'Object resources compared within construction and perception pipelines.'),
        ('runtime-method', '🔌 Runtime Integration', 'Methods that connect construction outputs to rendering, sensor operators, and simulator state.'),
        ('evaluation', '📊 Evaluation Frameworks', 'View extrapolation, world-generation control, policy learning, and scenario-based safety evaluation.'),
        ('response-reference', '📏 Response References', 'Measurements or external model outputs used to assess environmental and vehicle responses.'),
    ]
    for kind, title, description in resource_groups:
        out.append(f'\n### {title}\n\n{description}\n\n| Resource | Purpose | Links |\n| :--- | :--- | :--- |')
        out.extend(f'| **{r["name"]}** | {r["role"]} | {links(r["links"])} |' for r in resources if r['kind'] == kind)

    out.append('''

---

<a id="contributing"></a>

## 🤝 Contributing

Suggestions and corrections are welcome through [Issues](https://github.com/liuliuyaonuli/outdoor-sim-construction-survey/issues) or pull requests. To suggest a paper, include its title, paper link, and relevant topic.

<div align="center">

🌱 **Create** &nbsp; · &nbsp; 🧭 **Recover** &nbsp; · &nbsp; 🛠️ **Transform**

[↑ Back to top](#top)

</div>
''')

    docs = ROOT / 'docs'
    docs.mkdir(exist_ok=True)
    (ROOT / 'README.md').write_text('\n'.join(out).strip() + '\n')

    related_out = [f'''# 🧭 Methodological References

These {len(related)} papers supply scoped methodological examples for Chapter 3: indoor environments, general physical-world construction, game worlds, navigation structure, and abstract road graphs.

[← Survey reading guide](../README.md)
''']
    related_anchors = {'Navigation structure': 'navigation-structure', 'Abstract road graph': 'abstract-road-graph',
                       'Indoor scene authoring': 'indoor-scene-authoring', 'Multi-scene game worlds': 'multi-scene-game-worlds',
                       'Indoor physical arrangement': 'indoor-physical-arrangement'}
    for p in related:
        related_out.append(f'\n<a id="{p.get("anchor", related_anchors.get(p["scope"], p["citation_key"]))}"></a>\n\n## {p["scope"]}\n\n**Survey section {p["survey_section"]}.** {p["reason"]}\n')
        related_out.append(entry(p))
    related_out.append('\n[Machine-readable records](../data/methodological-references.json) · [Selection notes](selection-notes.md)\n')
    (docs / 'methodological-references.md').write_text('\n'.join(related_out).strip() + '\n')

    extended = [f'''# 📚 Extended Reading and Full Inventory

This collection retains the **{len(inventory)} original inventory records** and adds **{len(additional)} current manuscript references** that were absent from that inventory. Historical provisional flags are retained in the original JSON; current placement and displayed publication metadata follow the updated curation.

**Status key:** `Homepage` = selected method; `Methodological reference` = separately scoped example; `Extended reading` = retained outside the homepage; `Provisional` = supplement entry awaiting further review.

[← Survey reading guide](../README.md) · [Selection notes](selection-notes.md) · [Candidate review queue](candidates.md)
''']
    for task in ['Synthesis', 'Reconstruction', 'Transformation']:
        rows = sorted((p for p in inventory if p['task'] == task), key=lambda p: (-p['year'], p['title'].casefold()))
        extended.append(f'\n## {task} — original inventory\n')
        for p in rows:
            status = 'Homepage' if p['id'] in selected_ids else 'Methodological reference' if p['id'] in related_ids else 'Provisional' if p['provisional'] else 'Extended reading'
            current = next((r for r in featured + related + supporting if r['inventory_id'] == p['id']), p)
            extended.append(entry(current) + f'  <sub>Inventory {p["id"]} · {status}</sub>\n')
    extended.append(f'\n## Additional References from the Manuscript\n\nThese {len(additional)} references came from the manuscript bibliography. Their placement is described in the source notes; presence in this archive does not by itself indicate homepage selection.\n')
    extended.extend(entry(p) for p in additional)
    extended.append('\nThe original inventory is preserved in [data/papers.json](../data/papers.json). Curated metadata and bibliography keys are in [data/featured.json](../data/featured.json). The homepage uses the curated publication labels where they differ from the historical inventory.\n')
    (docs / 'extended-reading.md').write_text('\n'.join(extended).strip() + '\n')

    queue = [f'''# 🔎 Candidate Review Queue

There are **{len(active_candidates)} unresolved records** from the historical seven-record queue. Suggested tasks remain provisional. Resolved cases appear below with their current manuscript placement.

[← Survey reading guide](../README.md) · [Extended reading](extended-reading.md)
''']
    for p in active_candidates:
        queue.append(f'- **{p["title"]}**' + '\\' + f'\n  [📄 Paper]({p["paper_url"]}) · <sub>Suggested task: {html.escape(p["suggested_task"])}</sub>\n')
    queue.append('\n## Resolved Since the Original Queue\n')
    for p in candidates:
        if p['id'] in resolutions:
            key = resolutions[p['id']]['citation_key']
            queue.append(f'- **{p["title"]}** — included under [image- and video-prior-guided synthesis](../README.md#paper-{key}) based on the current manuscript discussion.\n')
    queue.append('\n[Historical queue](../data/candidates.json) · [Resolution records](../data/curation.json)\n')
    (docs / 'candidates.md').write_text('\n'.join(queue).strip() + '\n')

    dispositions = Counter(r['destination'] for r in curation['inventory_dispositions'])
    notes = [f'''# 📝 Selection and Source Notes

[← Survey reading guide](../README.md)

## Selection Basis

The homepage follows construction methods directly discussed in **Chapter 3 of the manuscript**. The current bibliography has **{curation['counts']['bibliography_entries']} entries**; Chapter 3 cites **{curation['counts']['chapter3_citations']}** of them. The homepage contains **{len(featured)} method families**, with **{len(related)} methodological examples**, **{len(supporting)} supporting references**, and **{sum(len(p.get('extensions', [])) for p in featured)} associated journal extension** accounted for separately.

The survey's technical subdivisions determine the homepage topics. An environment-generation method is not placed in a separate language-agent category solely because it invokes an LLM; procedural control, asset assembly, learned structure generation, and visual-prior-guided construction remain distinct routes. Repeated citations and secondary operations do not create duplicate homepage entries.

The methodological-reference page identifies indoor, game-world, navigation, graph-level, and general physical-world examples. COLMAP papers, general surface representations, instruction-based editing mechanisms, asset/map references, and a driving-NeRF survey are listed in supporting literature. CityDreamer4D is associated with CityDreamer as a journal extension and does not increase the method-family count.

Platforms, data, assets, and response references are drawn from **Sections 4–5 and Table 4**. Their resource rows are not additional selected methods; some platforms are also discussed as construction methods.

## Original Inventory Dispositions

| Destination | Original records |
| :--- | ---: |
| Selected for the homepage | {dispositions['homepage']} |
| Methodological references | {dispositions['methodological-references']} |
| Retained in extended reading | {dispositions['extended-reading']} |
| **Original inventory total** | **{len(inventory)}** |

There are {len(additional)} current manuscript references outside the original inventory. They retain their bibliography keys and have no invented inventory IDs.

Of the historical 25 provisional entries, **{25-len(pending_provisional)} now appear on the homepage** because they are explicitly discussed in the updated manuscript. The remaining **{len(pending_provisional)}** stay in extended reading. **{len(active_candidates)} of the original seven boundary candidates remain unresolved**; SceneFrom3D is now assigned to synthesis based on its current discussion. These dispositions are recorded separately from the unchanged historical input files.

## Publication Metadata and Links

Curated titles, years, and publication labels follow `references.bib`; version-specific paper URLs are retained when the manuscript cites a particular version. Existing author-maintained links are reused from the inventory. The historical JSON retains its original metadata for traceability; the extended-reading display uses current curated metadata for matched records.

PandaSet links to its development kit, and CarSim links to the product page; the reviewed vehicle-response experiments use CarSim 2022.1. Project links for GoogleEarth views, Vid2Sim videos, and LiDARsim assets identify the reviewed resource context, without implying a new independent dataset release.

## Source Correspondence

| Homepage topic | Manuscript section | Methods |
| :--- | :--- | ---: |
''']
    notes[0] = notes[0].rstrip()
    for topic in topics:
        notes.append(f'| {topic["id"]} {topic["title"]} | {topic["survey_section"]} | {sum(p["topic"] == topic["id"] for p in featured)} |')
    notes.append(f'''

The bibliography key and discussion sections for each selected study are recorded in [featured.json](../data/featured.json). [curation.json](../data/curation.json) records all original inventory dispositions and SHA-256 hashes of the manuscript source files used for this selection. Source prose, unpublished manuscript files, figures, and paper PDFs are not copied into this repository.

## Files and Maintenance

| File | Purpose |
| :--- | :--- |
| [data/featured.json](../data/featured.json) | Curated methods, current bibliography metadata, and manuscript correspondence. |
| [data/methodological-references.json](../data/methodological-references.json) | The {len(related)} separately scoped references. |
| [data/supporting-references.json](../data/supporting-references.json) | Technical background, resource references, and related surveys. |
| [data/resources.json](../data/resources.json) | Supporting resource roles, links, and source citation keys. |
| [data/curation.json](../data/curation.json) | Topic definitions, source fingerprints, and inventory dispositions. |
| [data/papers.json](../data/papers.json) | The unchanged 177-record historical inventory. |
| [data/candidates.json](../data/candidates.json) | The unchanged seven-record boundary queue. |
| [data/latest-update.json](../data/latest-update.json) | Added methods and metadata/classification changes in this update. |

To update the displayed guide, edit the relevant curated records and run:

```bash
python3 scripts/render_readme.py
```

The renderer uses only the Python standard library. It renders the homepage and supplemental Markdown from the repository data; it does not automatically promote inventory records into the homepage.

For a manuscript refresh, run `python3 scripts/sync_manuscript.py /path/to/manuscript`, review the updated records and scope policies in `data/curation.json`, then run the renderer. The sync reads the supplied manuscript directory and writes only repository metadata.
''')
    (docs / 'selection-notes.md').write_text('\n'.join(notes).strip() + '\n')
    supporting_out = ['# 📘 Supporting Literature\n\nTechnical background, resource references, and surveys used in Chapter 3.\n\n[← Survey reading guide](../README.md)\n']
    for category, title in [('technical-background', 'Technical Background'), ('resource-reference', 'Map and Asset References'), ('survey', 'Related Surveys')]:
        supporting_out.append(f'\n## {title}\n')
        for p in supporting:
            if p['category'] == category:
                supporting_out.extend([entry(p), p['reason'] + '\n'])
    (docs / 'supporting-literature.md').write_text('\n'.join(supporting_out).strip() + '\n')
    update = load('latest-update.json')
    old_counts = update['previous_counts']
    update_out = [f'''# 🗓️ Manuscript Update — {update['date']}

[← Survey reading guide](../README.md)

| Collection | Previous | Current |
| :--- | ---: | ---: |
| Homepage method families | {old_counts['homepage_methods']} | {len(featured)} |
| Methodological examples | {old_counts['methodological_references']} | {len(related)} |
| Supporting resources | {old_counts['resource_entries']} | {len(resources)} |

## Publication and Scope Changes

- **R3D2** now carries the manuscript's CVPR Workshop 2026 publication label; its consulted arXiv version remains linked.
- **DroneWiS** now uses the ASE 2024 Tool Demonstrations title and publication DOI.
- **CityDreamer4D** is linked as CityDreamer's journal extension, rather than counted as another method family.
- **SceneFrom3D** moved from the boundary queue to synthesis, following its explicit discussion in Section 3.1.4.
- **{25-len(pending_provisional)} historical provisional entries** now appear in the selected list. The remaining {len(pending_provisional)} retain their extended-reading status.
- The original 177-record inventory and seven-record candidate input files are preserved; current placements are tracked separately.

## Newly Included Methods ({len(update['added_methods'])})
''']
    for topic in topics:
        added = [p for p in update['added_methods'] if p['topic'] == topic['id']]
        if added:
            update_out.append(f'\n### {topic["id"]} {topic["title"]}\n')
            update_out.extend(f'- [{p["title"]}](../README.md#paper-{p["citation_key"]})' for p in added)
    (docs / 'updates.md').write_text('\n'.join(update_out).strip() + '\n')
    print(f'Rendered {len(featured)} selected methods, {len(related)} methodological references, {len(resources)} supporting resources, and all original inventory/candidate records.')


if __name__ == '__main__':
    main()
