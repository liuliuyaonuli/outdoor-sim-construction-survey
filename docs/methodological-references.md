# 🧭 Methodological References

These 14 papers supply scoped methodological examples: indoor environments, general physical-world construction, game worlds, navigation structure, and abstract road graphs. The manuscript snapshot contains 10 of these; later additions retain their scope and provenance separately.

[← Survey reading guide](../README.md)


<a id="deitke2022procthor"></a>

## Indoor procedural environments

**Survey section 3.1.1.** Room-layout and interactive-asset generation for houses; a transferable procedural example rather than outdoor construction.

- **ProcTHOR: Large-Scale Embodied AI Using Procedural Generation**\
  <sub>NeurIPS 2022</sub> · [📄 Paper](https://proceedings.neurips.cc/paper_files/paper/2022/file/27c546ab1e4f1d7d638e6a8dfbad9a07-Paper-Conference.pdf)


<a id="yang2024physcene"></a>

## Indoor constrained layout synthesis

**Survey section 3.1.3.** Collision, layout, and reachability guidance for indoor embodied scenes; explicitly introduced as a methodological reference.

- **PhyScene: Physically Interactable 3D Scene Synthesis for Embodied AI**\
  <sub>CVPR 2024</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Yang_PhyScene_Physically_Interactable_3D_Scene_Synthesis_for_Embodied_AI_CVPR_2024_paper.html) · [🌐 Project](https://physcene.github.io)


<a id="navigation-structure"></a>

## Navigation structure

**Survey section 3.2.4.** Recovers orientation-dependent traversability for legged robotics. The survey uses it to explain how embodiment affects recovered navigation structure, rather than as a complete outdoor environment construction pipeline.

- **SE(2) Navigation Mesh**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2607.01454v1)


<a id="abstract-road-graph"></a>

## Abstract road graph

**Survey section 3.3.2.** Edits road-network structure and attributes for traffic planning. It operates at the graph layer; corresponding 3D road surfaces require separate instantiation.

- **TraSculptor: Visual Analytics for Enhanced Decision-Making in Road Traffic Planning**\
  <sub>IEEE TVCG 2025</sub> · [📄 Paper](https://doi.org/10.1109/TVCG.2025.3532498) · [💻 Code](https://github.com/akihaisland/TraSculptor)


<a id="indoor-scene-authoring"></a>

## Indoor scene authoring

**Survey section 3.4.** Provides a methodological example of persistent requirements, scene state, and preservation checks across successive edits.

- **MUSE: Agentic 3D Scene Authoring via Memory-Grounded Incremental Requirement Satisfaction**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2606.14168v1) · [🌐 Project](https://xujay111.github.io/muse_githubio/)


<a id="multi-scene-game-worlds"></a>

## Multi-scene game worlds

**Survey section 3.4.** Provides a methodological example of portal-connectivity verification and feedback-driven placement repair.

- **MAGIC: Transition-Aware Generation of Navigable Multi-Scene Game Worlds with Large Language Models**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2607.11594v1) · [💻 Code](https://github.com/sereneee1201/MAGIC/)


<a id="indoor-physical-arrangement"></a>

## Indoor physical arrangement

**Survey section 3.4.** Provides a methodological example of solver feedback for revising spatial and physical predicates.

- **PhyScensis: Physics-Augmented LLM Agents for Complex Physical Scene Arrangement**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2602.14968v1)


<a id="xia2026sage"></a>

## Indoor agentic verification

**Survey section 3.4.** Tool use and semantic, visual, and stability critics for indoor scene generation; outdoor checks require additional task-specific design.

- **SAGE: Scalable Agentic 3D Scene Generation for Embodied AI**\
  <sub>CVPR 2026</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Xia_SAGE_Scalable_Agentic_3D_Scene_Generation_for_Embodied_AI_CVPR_2026_paper.html)


<a id="wang2026worldagentv1"></a>

## General physical-world verification

**Survey section 3.4.** World specifications and geometry/simulation feedback illustrate verification-guided orchestration; retained as a general physical-world reference.

- **WorldAgent: Verification-Guided Agentic Physical World Construction**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2609.33208v1) · [🌐 Project](https://wclw1021.github.io/WorldAgent_Web/) · <sub>⏳ Code pending</sub>


<a id="zhang2026code2worlds2v1"></a>

## Physical-world compilation

**Survey section 3.4.** Visual-to-MuJoCo compilation and simulator checks illustrate physical preparation and feedback for embodied worlds.

- **Code2Worlds-2: Physically Plausible Agent Harness for Embodied World Simulation**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2610.17651v1) · [💻 Code](https://github.com/AIGeeksGroup/Code2Worlds-2)


<a id="research2026persist"></a>

## Game worlds with persistent 3D state

**Suggested survey section 3.1.4.** Game-world evidence in Craftium/OpenWorldCreative; retained as a scoped mechanism reference.

- **Beyond Pixel Histories: World Models with Persistent 3D State**\
  <sub>ICML 2026</sub> · [📄 Paper](https://proceedings.mlr.press/v306/garcin26a.html) · [💻 Code](https://github.com/francelico/PERSIST) · [📝 Preprint](https://arxiv.org/abs/2603.03482)


<a id="research2026puffinworld"></a>

## General native-3D multimodal models

**Suggested survey section 3.1.4.** General mechanism with outdoor examples; a persistent global map and robot-control loop have not been established.

- **Puffin-World: Scaling a Unified Multimodal Model with Native 3D World States**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2609.04196) · [🌐 Project](https://kangliao929.github.io/projects/puffin-world/) · [💻 Code](https://github.com/KangLiao929/Puffin)


<a id="research2026scenerig"></a>

## Indoor reconstruction and simulation feedback

**Suggested survey section 3.4.** Primarily indoor manipulation; robot-policy results do not establish outdoor applicability.

- **SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images**\
  <sub>CoRL Agentic Robotics Workshop 2026 (accepted)</sub> · [📄 Paper](https://arxiv.org/abs/2610.28585)


<a id="research2026wedge"></a>

## Indoor policy-conditioned environment generation

**Suggested survey section 3.4.** Already cited in the supplied manuscript; ProcTHOR/HM3D evidence remains explicitly indoor.

- **From Failures to Learnable Worlds: Policy-Conditioned Environment Generation for Navigation Agents**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2610.19420) · [🌐 Project](https://zhangyuejoslin.github.io/WEDGE/)


[Machine-readable records](../data/methodological-references.json) · [Selection notes](selection-notes.md)
