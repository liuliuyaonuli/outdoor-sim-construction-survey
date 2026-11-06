# 📝 Selection and Source Notes

[← Survey reading guide](../README.md)

## Selection Basis

The homepage follows construction methods directly discussed in **Chapter 3 of the manuscript**. The current bibliography has **240 entries**; Chapter 3 cites **146** of them. The homepage contains **125 method families**, with **10 methodological examples**, **10 supporting references**, and **1 associated journal extension** accounted for separately.

The survey's technical subdivisions determine the homepage topics. An environment-generation method is not placed in a separate language-agent category solely because it invokes an LLM; procedural control, asset assembly, learned structure generation, and visual-prior-guided construction remain distinct routes. Repeated citations and secondary operations do not create duplicate homepage entries.

The methodological-reference page identifies indoor, game-world, navigation, graph-level, and general physical-world examples. COLMAP papers, general surface representations, instruction-based editing mechanisms, asset/map references, and a driving-NeRF survey are listed in supporting literature. CityDreamer4D is associated with CityDreamer as a journal extension and does not increase the method-family count.

Platforms, data, assets, and response references are drawn from **Sections 4–5 and Table 4**. Their resource rows are not additional selected methods; some platforms are also discussed as construction methods.

## Original Inventory Dispositions

| Destination | Original records |
| :--- | ---: |
| Selected for the homepage | 63 |
| Methodological references | 8 |
| Retained in extended reading | 106 |
| **Original inventory total** | **177** |

There are 74 current manuscript references outside the original inventory. They retain their bibliography keys and have no invented inventory IDs.

Of the historical 25 provisional entries, **7 now appear on the homepage** because they are explicitly discussed in the updated manuscript. The remaining **18** stay in extended reading. **6 of the original seven boundary candidates remain unresolved**; SceneFrom3D is now assigned to synthesis based on its current discussion. These dispositions are recorded separately from the unchanged historical input files.

## Publication Metadata and Links

Curated titles, years, and publication labels follow `references.bib`; version-specific paper URLs are retained when the manuscript cites a particular version. Existing author-maintained links are reused from the inventory. The historical JSON retains its original metadata for traceability; the extended-reading display uses current curated metadata for matched records.

PandaSet links to its development kit, and CarSim links to the product page; the reviewed vehicle-response experiments use CarSim 2022.1. Project links for GoogleEarth views, Vid2Sim videos, and LiDARsim assets identify the reviewed resource context, without implying a new independent dataset release.

## Source Correspondence

| Homepage topic | Manuscript section | Methods |
| :--- | :--- | ---: |
| 1.1 Rule- and Constraint-Driven Procedural Generation | 3.1.1 | 18 |
| 1.2 Asset Retrieval and Compositional Environment Assembly | 3.1.2 | 7 |
| 1.3 Learning-Based Generation of 3D Structures and Scene Representations | 3.1.3 | 21 |
| 1.4 3D Environment Generation with Image and Video Priors | 3.1.4 | 12 |
| 2.1 Geospatial Data- and Map-Driven Structured Reconstruction | 3.2.1 | 4 |
| 2.2 Explicit Geometry Recovery and Multisensor Fusion | 3.2.2 | 3 |
| 2.3 Scene Reconstruction with Neural Fields and Gaussian Representations | 3.2.3 | 29 |
| 2.4 Recovering Simulation-Relevant Structures and Properties | 3.2.4 | 5 |
| 3.1 Geometric Completion, Local Repair, and Spatial Expansion | 3.3.1 | 3 |
| 3.2 Object, Semantic, and Topological Editing | 3.3.2 | 8 |
| 3.3 Transformations of Appearance, Physics, and Environmental Properties | 3.3.3 | 11 |
| 4.1 Hybrid Construction and Automated Orchestration | 3.4 | 4 |


The bibliography key and discussion sections for each selected study are recorded in [featured.json](../data/featured.json). [curation.json](../data/curation.json) records all original inventory dispositions and SHA-256 hashes of the manuscript source files used for this selection. Source prose, unpublished manuscript files, figures, and paper PDFs are not copied into this repository.

## Files and Maintenance

| File | Purpose |
| :--- | :--- |
| [data/featured.json](../data/featured.json) | Curated methods, current bibliography metadata, and manuscript correspondence. |
| [data/methodological-references.json](../data/methodological-references.json) | The 10 separately scoped references. |
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
