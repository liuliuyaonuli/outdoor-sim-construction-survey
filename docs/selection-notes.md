# 📝 Selection and Source Notes

[← Survey reading guide](../README.md)

## Selection Basis

The homepage follows the construction methods directly discussed in **Chapter 3 of the manuscript**, rather than reproducing every bibliography item or the whole literature inventory. The chapter cites **58 distinct studies**: **53 selected methods** are on the homepage, and **5 explicitly scoped methodological references** are on a supplementary page.

The survey's technical subdivisions determine the homepage topics. An environment-generation method is not placed in a separate language-agent category solely because it invokes an LLM; procedural control, asset assembly, learned structure generation, and visual-prior-guided construction remain distinct routes. Repeated citations and secondary operations do not create duplicate homepage entries.

The five methodological references are separated because of the roles stated in the manuscript: SE(2) Navigation Mesh (legged-robot navigation structure), TraSculptor (abstract road graphs), MUSE (indoor authoring), MAGIC (game-world connectivity), and PhyScensis (indoor physical arrangement). This placement identifies their relevance without treating them as full outdoor construction systems.

Platforms, data, assets, and response references are drawn from **Sections 4–5 and Table 4**. Their resource rows are not additional selected methods; some platforms are also discussed as construction methods.

## Original Inventory Dispositions

| Destination | Original records |
| :--- | ---: |
| Selected for the homepage | 46 |
| Methodological references | 5 |
| Retained in extended reading | 126 |
| **Original inventory total** | **177** |

Seven additional methods came from the manuscript bibliography: Infinigen, MetaDrive, XCube, SceneDreamer, CityDreamer, LucidDreamer, and DreamScene360. They are included in the homepage and extended reading, with no invented inventory IDs.

The **25 provisional supplement entries** remain outside the homepage. The separate **seven boundary candidates** remain in the review queue. A record's absence from the homepage is a presentation decision for this manuscript-aligned guide, not a finding that the paper is invalid or irrelevant to all related research.

## Publication Metadata and Links

Curated titles, years, and publication labels follow `references.bib`; version-specific paper URLs are retained when the manuscript cites a particular version. Existing author-maintained links are reused from the inventory. The seven newly added methods were linked through publisher, arXiv, or author-maintained sources. The historical inventory retains its original metadata for traceability.

PandaSet links to its development kit, and CarSim links to the product page; the reviewed vehicle-response experiments use CarSim 2022.1. Project links for GoogleEarth views, Vid2Sim videos, and LiDARsim assets identify the reviewed resource context, without implying a new independent dataset release.

## Source Correspondence

| Homepage topic | Manuscript section | Methods |
| :--- | :--- | ---: |
| 1.1 Rule- and Constraint-Driven Procedural Generation | 3.1.1 | 8 |
| 1.2 Asset Retrieval and Compositional Environment Assembly | 3.1.2 | 5 |
| 1.3 Learning-Based Generation of 3D Structures and Scene Representations | 3.1.3 | 8 |
| 1.4 3D Environment Generation with Image and Video Priors | 3.1.4 | 6 |
| 2.1 Geospatial Data- and Map-Driven Structured Reconstruction | 3.2.1 | 2 |
| 2.2 Explicit Geometry Recovery and Multisensor Fusion | 3.2.2 | 3 |
| 2.3 Scene Reconstruction with Neural Fields and Gaussian Representations | 3.2.3 | 5 |
| 2.4 Recovering Simulation-Relevant Structures and Properties | 3.2.4 | 3 |
| 3.1 Geometric Completion, Local Repair, and Spatial Expansion | 3.3.1 | 2 |
| 3.2 Object, Semantic, and Topological Editing | 3.3.2 | 4 |
| 3.3 Transformations of Appearance, Physics, and Environmental Properties | 3.3.3 | 5 |
| 4.1 Hybrid Construction and Automated Orchestration | 3.4 | 2 |


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
