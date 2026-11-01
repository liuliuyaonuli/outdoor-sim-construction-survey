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
    'documentation': '📘', 'devkit': '🧰', 'product': '🔗',
}


def links(resources):
    return ' · '.join(f'[{ICONS.get(kind, "🔗")} {kind.title()}]({url})' for kind, url in resources.items())


def entry(paper, anchor=False):
    prefix = f'<a id="paper-{paper["citation_key"]}"></a>' if anchor else ''
    resources = {'paper': paper['paper_url'], **paper['resources']}
    resources = {key: value for key, value in resources.items() if value}
    return (f'- {prefix}**{paper["title"]}**' + '\\' + '\n'
            f'  <sub>{html.escape(paper["publication"])}</sub> · {links(resources)}\n')


def main():
    featured = load('featured.json')
    related = load('methodological-references.json')
    inventory = load('papers.json')
    candidates = load('candidates.json')
    resources = load('resources.json')
    curation = load('curation.json')
    topics = curation['topics']
    counts = Counter(p['topic'].split('.')[0] for p in featured)
    assert len({p['citation_key'] for p in featured + related}) == len(featured) + len(related)
    assert {p['topic'] for p in featured} == {t['id'] for t in topics}

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

---

A reading guide to the environment construction methods directly discussed in the survey. The technical topics follow **Sections 3.1–3.4** of the manuscript; simulation platforms, data, and response references are listed separately under [Supporting resources](#resources).

本页精选综述正文直接讨论的构建方法，按“生成、重建、变换及混合编排”的技术路线组织。方法借鉴、完整文献台账和待核验候选可在[补充阅读](#further-reading)中查阅。

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
                '- [📚 Further Reading](#further-reading)',
                '- [🤝 Contributing](#contributing)',
                '''
**Resource key:** 📄 Paper · 💻 Code · 🌐 Project · 📘 Documentation · 🗃️ Dataset

Methods appear once in the guide, under their principal technical discussion. Publication labels follow the manuscript bibliography; entries within each topic are ordered by year, newest first. A paper link identifies a research source, while the other links identify available supporting resources.
'''])

    for number, (icon, title, anchor, description) in sections.items():
        out.append(f'\n---\n\n<a id="{anchor}"></a>\n\n## {icon} {number}. {title}\n\n{description}\n')
        for topic in topics:
            if not topic['id'].startswith(number + '.'): continue
            out.append(f'\n<a id="{topic["anchor"]}"></a>\n\n### {topic["icon"]} {topic["id"]} {topic["title"]}\n\n{topic["description"]}\n')
            members = sorted((p for p in featured if p['topic'] == topic['id']), key=lambda p: (-p['year'], p['title'].casefold()))
            out.extend(entry(p, anchor=True) for p in members)
        if number == '2':
            out.append('The navigation-structure example **SE(2) Navigation Mesh** is discussed separately in [Methodological references](docs/methodological-references.md#navigation-structure).\n')
        if number == '3':
            out.append('The abstract road-network example **TraSculptor** is discussed separately in [Methodological references](docs/methodological-references.md#abstract-road-graph).\n')
        out.append('[↑ Back to contents](#contents)\n')

    out.append('''
---

<a id="hybrid"></a>

## 🤖 4. Hybrid Construction and Automated Orchestration

Hybrid pipelines connect different construction operations. Orchestration selects and executes tools, maintains construction state, and uses feedback to revise intermediate results. This section follows Section 3.4 of the survey.
''')
    out.extend(entry(p, anchor=True) for p in sorted((p for p in featured if p['topic'].startswith('4.')), key=lambda p: (-p['year'], p['title'].casefold())))
    out.append('''
Related examples already listed above include [3D-GPT](#paper-sun2023gpt3dv1) and [CityX](#paper-zhang2024cityxv1) for language-to-tool orchestration, and [DroneWiS](#paper-zhang2024dronewisv1) for geometry-dependent wind augmentation. Indoor and game-world examples—**MUSE**, **MAGIC**, and **PhyScensis**—are explained in [Methodological references](docs/methodological-references.md).

[↑ Back to contents](#contents)

---

<a id="resources"></a>

## 🧰 5. Supporting Resources

These resources support the simulation uses and evaluation settings discussed in Sections 4–5 and Table 4. They are separate from the selected-method count above.
''')
    resource_groups = [
        ('platform', '🏗️ Simulation Platforms', 'Environment execution, configurable scenes, and repeatable trials.'),
        ('scene-data', '🗃️ Scene Data and Evaluation Inputs', 'Observations and scene inputs used in the reviewed experiments.'),
        ('assets', '🧩 Asset Resources', 'Object resources compared within construction and perception pipelines.'),
        ('response-reference', '📏 Response References', 'Measurements or external model outputs used to assess environmental and vehicle responses.'),
    ]
    for kind, title, description in resource_groups:
        out.append(f'\n### {title}\n\n{description}\n\n| Resource | Role in the reviewed experiments | Links |\n| :--- | :--- | :--- |')
        out.extend(f'| **{r["name"]}** | {r["role"]} | {links(r["links"])} |' for r in resources if r['kind'] == kind)

    out.append(f'''

---

<a id="further-reading"></a>

## 📚 Further Reading

| Collection | What it contains |
| :--- | :--- |
| [🧭 Methodological references](docs/methodological-references.md) | {len(related)} explicitly scoped examples from indoor authoring, game worlds, legged navigation, and abstract road graphs. |
| [📚 Extended reading and full inventory](docs/extended-reading.md) | The original {len(inventory)} records, plus the {sum(p['inventory_id'] is None for p in featured)} manuscript methods added during curation. This includes papers beyond the current homepage scope. |
| [🔎 Candidate review queue](docs/candidates.md) | {len(candidates)} boundary candidates with unresolved scope or classification questions. |
| [📝 Selection and source notes](docs/selection-notes.md) | Inclusion rationale, manuscript correspondence, and a record of where the original entries are displayed. |

The {sum(p['provisional'] for p in inventory)} provisional additions from the original supplement remain in extended reading. They are not promoted to this manuscript-aligned homepage solely because they were present in the collection.

<a id="contributing"></a>

## 🤝 Contributing

Suggestions and corrections are welcome through [Issues](https://github.com/liuliuyaonuli/outdoor-sim-construction-survey/issues) or pull requests. For a new paper, provide its full title, venue or preprint status, a stable paper URL, and its proposed technical topic. Explain the connection to outdoor environment construction and identify any limits in the output or evaluation scope.

<a id="acknowledgments"></a>

## 💐 Acknowledgments

The presentation is inspired by [Awesome-Self-Evolving-Agents](https://github.com/ANative-Lab/Awesome-Self-Evolving-Agents). The selection and technical organization follow this survey's manuscript. Credit for the linked research and software belongs to the respective authors.

<div align="center">

🌱 **Create** &nbsp; · &nbsp; 🧭 **Recover** &nbsp; · &nbsp; 🛠️ **Transform**

[↑ Back to top](#top)

</div>
''')

    docs = ROOT / 'docs'
    docs.mkdir(exist_ok=True)
    (ROOT / 'README.md').write_text('\n'.join(out).strip() + '\n')

    related_out = ['''# 🧭 Methodological References

These five papers are explicitly used as methodological references in Chapter 3 of the survey. Their scope is identified here so that they can inform construction design without being grouped into the main outdoor-method list.

[← Survey reading guide](../README.md)
''']
    related_anchors = {'Navigation structure': 'navigation-structure', 'Abstract road graph': 'abstract-road-graph',
                       'Indoor scene authoring': 'indoor-scene-authoring', 'Multi-scene game worlds': 'multi-scene-game-worlds',
                       'Indoor physical arrangement': 'indoor-physical-arrangement'}
    for p in related:
        related_out.append(f'\n<a id="{related_anchors[p["scope"]]}"></a>\n\n## {p["scope"]}\n\n**Survey section {p["survey_section"]}.** {p["reason"]}\n')
        related_out.append(entry(p))
    related_out.append('\n[Machine-readable records](../data/methodological-references.json) · [Selection notes](selection-notes.md)\n')
    (docs / 'methodological-references.md').write_text('\n'.join(related_out).strip() + '\n')

    selected_ids = {p['inventory_id'] for p in featured if p['inventory_id']}
    related_ids = {p['inventory_id'] for p in related if p['inventory_id']}
    extended = [f'''# 📚 Extended Reading and Full Inventory

This is the broader collection behind the survey reading guide. It retains the **{len(inventory)} original inventory records**, including related indoor methods and **{sum(p['provisional'] for p in inventory)} provisional supplement entries**, and adds the **{sum(p['inventory_id'] is None for p in featured)} manuscript methods** that were missing from that inventory. Entries here are not all selected for the current homepage.

**Status key:** `Homepage` = selected method; `Methodological reference` = separately scoped example; `Extended reading` = retained outside the homepage; `Provisional` = supplement entry awaiting further review.

[← Survey reading guide](../README.md) · [Selection notes](selection-notes.md) · [Candidate review queue](candidates.md)
''']
    for task in ['Synthesis', 'Reconstruction', 'Transformation']:
        rows = sorted((p for p in inventory if p['task'] == task), key=lambda p: (-p['year'], p['title'].casefold()))
        extended.append(f'\n## {task} — original inventory\n')
        for p in rows:
            status = 'Homepage' if p['id'] in selected_ids else 'Methodological reference' if p['id'] in related_ids else 'Provisional' if p['provisional'] else 'Extended reading'
            extended.append(entry(p) + f'  <sub>Inventory {p["id"]} · {status}</sub>\n')
    extended.append('\n## Additional Methods from the Manuscript\n\nThese seven papers were added from the manuscript bibliography when the homepage was aligned with its technical discussion.\n')
    extended.extend(entry(p) for p in featured if p['inventory_id'] is None)
    extended.append('\nThe original inventory is preserved in [data/papers.json](../data/papers.json). Curated metadata and bibliography keys are in [data/featured.json](../data/featured.json). The homepage uses the curated publication labels where they differ from the historical inventory.\n')
    (docs / 'extended-reading.md').write_text('\n'.join(extended).strip() + '\n')

    queue = [f'''# 🔎 Candidate Review Queue

These {len(candidates)} records have unresolved questions about the primary construction task, output scope, or eligibility. Suggested tasks are carried over from the source supplement and remain provisional. These records are not included in the selected-method count.

[← Survey reading guide](../README.md) · [Extended reading](extended-reading.md)
''']
    for p in candidates:
        queue.append(f'- **{p["title"]}**' + '\\' + f'\n  [📄 Paper]({p["paper_url"]}) · <sub>Suggested task: {html.escape(p["suggested_task"])}</sub>\n')
    queue.append('\n[Machine-readable queue](../data/candidates.json)\n')
    (docs / 'candidates.md').write_text('\n'.join(queue).strip() + '\n')

    dispositions = Counter(r['destination'] for r in curation['inventory_dispositions'])
    notes = [f'''# 📝 Selection and Source Notes

[← Survey reading guide](../README.md)

## Selection Basis

The homepage follows the construction methods directly discussed in **Chapter 3 of the manuscript**, rather than reproducing every bibliography item or the whole literature inventory. The chapter cites **{len(featured) + len(related)} distinct studies**: **{len(featured)} selected methods** are on the homepage, and **{len(related)} explicitly scoped methodological references** are on a supplementary page.

The survey's technical subdivisions determine the homepage topics. An environment-generation method is not placed in a separate language-agent category solely because it invokes an LLM; procedural control, asset assembly, learned structure generation, and visual-prior-guided construction remain distinct routes. Repeated citations and secondary operations do not create duplicate homepage entries.

The five methodological references are separated because of the roles stated in the manuscript: SE(2) Navigation Mesh (legged-robot navigation structure), TraSculptor (abstract road graphs), MUSE (indoor authoring), MAGIC (game-world connectivity), and PhyScensis (indoor physical arrangement). This placement identifies their relevance without treating them as full outdoor construction systems.

Platforms, data, assets, and response references are drawn from **Sections 4–5 and Table 4**. Their resource rows are not additional selected methods; some platforms are also discussed as construction methods.

## Original Inventory Dispositions

| Destination | Original records |
| :--- | ---: |
| Selected for the homepage | {dispositions['homepage']} |
| Methodological references | {dispositions['methodological-references']} |
| Retained in extended reading | {dispositions['extended-reading']} |
| **Original inventory total** | **{len(inventory)}** |

Seven additional methods came from the manuscript bibliography: Infinigen, MetaDrive, XCube, SceneDreamer, CityDreamer, LucidDreamer, and DreamScene360. They are included in the homepage and extended reading, with no invented inventory IDs.

The **25 provisional supplement entries** remain outside the homepage. The separate **seven boundary candidates** remain in the review queue. A record's absence from the homepage is a presentation decision for this manuscript-aligned guide, not a finding that the paper is invalid or irrelevant to all related research.

## Publication Metadata and Links

Curated titles, years, and publication labels follow `references.bib`; version-specific paper URLs are retained when the manuscript cites a particular version. Existing author-maintained links are reused from the inventory. The seven newly added methods were linked through publisher, arXiv, or author-maintained sources. The historical inventory retains its original metadata for traceability.

PandaSet links to its development kit, and CarSim links to the product page; the reviewed vehicle-response experiments use CarSim 2022.1. Project links for GoogleEarth views, Vid2Sim videos, and LiDARsim assets identify the reviewed resource context, without implying a new independent dataset release.

## Source Correspondence

| Homepage topic | Manuscript section | Methods |
| :--- | :--- | ---: |
''']
    notes[0] = notes[0].rstrip()
    for topic in topics:
        notes.append(f'| {topic["id"]} {topic["title"]} | {topic["survey_section"]} | {sum(p["topic"] == topic["id"] for p in featured)} |')
    notes.append('''

The bibliography key and discussion sections for each selected study are recorded in [featured.json](../data/featured.json). [curation.json](../data/curation.json) records all original inventory dispositions and SHA-256 hashes of the manuscript source files used for this selection. Source prose, unpublished manuscript files, figures, and paper PDFs are not copied into this repository.

## Files and Maintenance

| File | Purpose |
| :--- | :--- |
| [data/featured.json](../data/featured.json) | Curated methods, current bibliography metadata, and manuscript correspondence. |
| [data/methodological-references.json](../data/methodological-references.json) | The five separately scoped references. |
| [data/resources.json](../data/resources.json) | Supporting resource roles, links, and source citation keys. |
| [data/curation.json](../data/curation.json) | Topic definitions, source fingerprints, and inventory dispositions. |
| [data/papers.json](../data/papers.json) | The unchanged 177-record historical inventory. |
| [data/candidates.json](../data/candidates.json) | The unchanged seven-record boundary queue. |

To update the displayed guide, edit the relevant curated records and run:

```bash
python3 scripts/render_readme.py
```

The renderer uses only the Python standard library. It renders the homepage and supplemental Markdown from the repository data; it does not automatically promote inventory records into the homepage.
''')
    (docs / 'selection-notes.md').write_text('\n'.join(notes).strip() + '\n')
    print(f'Rendered {len(featured)} selected methods, {len(related)} methodological references, {len(resources)} supporting resources, and all original inventory/candidate records.')


if __name__ == '__main__':
    main()
