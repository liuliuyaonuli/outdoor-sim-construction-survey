<a id="top"></a>

<div align="center">

# 🌍 Outdoor 3D Simulation<br>Environment Construction Survey

**Automated Construction of Outdoor 3D Simulation Environments for Autonomous Systems**

面向自主系统的室外三维仿真环境自动构建

**🚗 Autonomous Driving &nbsp; · &nbsp; 🚁 Aerial Robotics &nbsp; · &nbsp; 🌲 Outdoor Worlds**

<p>
  <kbd>📚 53 selected methods</kbd> &nbsp;
  <kbd>🗂️ 12 technical topics</kbd> &nbsp;
  <kbd>🧰 12 supporting resources</kbd>
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
<p><strong>新环境生成 · 27 methods</strong></p>
<p>Rules → assets → learned structures → visual priors.</p>
<p><sub>Diversity + constraints</sub></p>
<a href="#synthesis">Explore synthesis →</a>
</td>
<td width="33%" valign="top">
<h3>🧭 Reconstruction</h3>
<p><strong>真实环境重建 · 13 methods</strong></p>
<p>Maps → geometry → neural scenes → environmental properties.</p>
<p><sub>Reality correspondence</sub></p>
<a href="#reconstruction">Explore reconstruction →</a>
</td>
<td width="33%" valign="top">
<h3>🛠️ Transformation</h3>
<p><strong>现有环境变换 · 11 methods</strong></p>
<p>Completion → object editing → appearance and physics.</p>
<p><sub>Change + preservation</sub></p>
<a href="#transformation">Explore transformation →</a>
</td>
</tr>
</table>

**🤖 Hybrid construction and orchestration:** 2 additional methods connect construction stages through executable tools and feedback.

<a id="contents"></a>

## 🗂️ Contents

- [🌱 **1. Synthesis of New Environments**](#synthesis)
  - [1.1 Rule- and Constraint-Driven Procedural Generation](#synthesis-procedural)
  - [1.2 Asset Retrieval and Compositional Environment Assembly](#synthesis-assembly)
  - [1.3 Learning-Based Generation of 3D Structures and Scene Representations](#synthesis-learning)
  - [1.4 3D Environment Generation with Image and Video Priors](#synthesis-visual-priors)
- [🧭 **2. Reconstruction of Real Environments**](#reconstruction)
  - [2.1 Geospatial Data- and Map-Driven Structured Reconstruction](#reconstruction-geospatial)
  - [2.2 Explicit Geometry Recovery and Multisensor Fusion](#reconstruction-geometry)
  - [2.3 Scene Reconstruction with Neural Fields and Gaussian Representations](#reconstruction-neural)
  - [2.4 Recovering Simulation-Relevant Structures and Properties](#reconstruction-properties)
- [🛠️ **3. Transformation of Existing Environments**](#transformation)
  - [3.1 Geometric Completion, Local Repair, and Spatial Expansion](#transformation-completion)
  - [3.2 Object, Semantic, and Topological Editing](#transformation-editing)
  - [3.3 Transformations of Appearance, Physics, and Environmental Properties](#transformation-properties)
- [🤖 **4. Hybrid Construction and Automated Orchestration**](#hybrid)
- [🧰 **5. Supporting Resources**](#resources)
- [📚 Further Reading](#further-reading)
- [🤝 Contributing](#contributing)

**Resource key:** 📄 Paper · 💻 Code · 🌐 Project · 📘 Documentation · 🗃️ Dataset

Methods appear once in the guide, under their principal technical discussion. Publication labels follow the manuscript bibliography; entries within each topic are ordered by year, newest first. A paper link identifies a research source, while the other links identify available supporting resources.


---

<a id="synthesis"></a>

## 🌱 1. Synthesis of New Environments

Create new environments using procedural rules, asset composition, learned structures, or visual priors.


<a id="synthesis-procedural"></a>

### 🌳 1.1 Rule- and Constraint-Driven Procedural Generation

Rules and intermediate structures control roads, buildings, terrain, and natural environments.

- <a id="paper-liu2026landcraft"></a>**LandCraft: Designing the Structured 3D Landscapes via Text Guidance**\
  <sub>AAAI 2026</sub> · [📄 Paper](https://doi.org/10.1609/aaai.v40i9.37686)

- <a id="paper-capek2025flightforge"></a>**FlightForge: Advancing UAV Research with Procedural Generation of High-Fidelity Simulation and Integrated Autonomy**\
  <sub>ICRA 2025</sub> · [📄 Paper](https://doi.org/10.1109/ICRA55743.2025.11127704)

- <a id="paper-zhang2024cityxv1"></a>**CityX: Controllable Procedural Content Generation for Unbounded 3D Cities**\
  <sub>arXiv 2024</sub> · [📄 Paper](https://arxiv.org/abs/2407.17572v1)

- <a id="paper-sun2023gpt3dv1"></a>**3D-GPT: Procedural 3D Modeling with Large Language Models**\
  <sub>arXiv 2023</sub> · [📄 Paper](https://arxiv.org/abs/2310.12945v1) · [🌐 Project](https://chuny1.github.io/3DGPT/3dgpt.html)

- <a id="paper-raistrick2023infinigen"></a>**Infinite Photorealistic Worlds Using Procedural Generation**\
  <sub>CVPR 2023</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Raistrick_Infinite_Photorealistic_Worlds_Using_Procedural_Generation_CVPR_2023_paper.html) · [🌐 Project](https://infinigen.org/)

- <a id="paper-genevaux2013hydrology"></a>**Terrain Generation Using Procedural Models Based on Hydrology**\
  <sub>ACM TOG 2013</sub> · [📄 Paper](https://doi.org/10.1145/2461912.2461996)

- <a id="paper-muller2006buildings"></a>**Procedural Modeling of Buildings**\
  <sub>ACM TOG 2006</sub> · [📄 Paper](https://doi.org/10.1145/1141911.1141931)

- <a id="paper-parish2001cities"></a>**Procedural Modeling of Cities**\
  <sub>SIGGRAPH 2001</sub> · [📄 Paper](https://doi.org/10.1145/383259.383292)


<a id="synthesis-assembly"></a>

### 🧩 1.2 Asset Retrieval and Compositional Environment Assembly

Spatial units and object assets are assembled under layout, connection, and placement constraints.

- <a id="paper-huang2025majutsucityv2"></a>**MajutsuCity: Language-driven Aesthetic-adaptive City Generation with Controllable 3D Assets and Layouts**\
  <sub>CVPR 2026</sub> · [📄 Paper](https://arxiv.org/abs/2511.20415) · [🌐 Project](https://longhz140516.github.io/MajutsuCity/)

- <a id="paper-lu2026yocity"></a>**Yo'City: Personalized and Boundless 3D Realistic City Scene Generation via Self-Critic Expansion**\
  <sub>CVPR 2026</sub> · [📄 Paper](https://arxiv.org/abs/2511.18734)

- <a id="paper-bian2025holodeck2"></a>**Holodeck 2.0: Vision-Language-Guided 3D World Generation with Editing**\
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2508.05899v1)

- <a id="paper-wu2025metaurban"></a>**MetaUrban: An Embodied AI Simulation Platform for Urban Micromobility**\
  <sub>ICLR 2025</sub> · [📄 Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ad63cdaffe7c95c5f9c12276cdd893f9-Abstract-Conference.html) · [🌐 Project](https://metadriverse.github.io/metaurban)

- <a id="paper-li2023metadrive"></a>**MetaDrive: Composing Diverse Driving Scenarios for Generalizable Reinforcement Learning**\
  <sub>IEEE TPAMI 2023</sub> · [📄 Paper](https://doi.org/10.1109/TPAMI.2022.3190471) · [💻 Code](https://github.com/metadriverse/metadrive) · [📘 Documentation](https://metadrive-simulator.readthedocs.io/en/latest/)


<a id="synthesis-learning"></a>

### 🌐 1.3 Learning-Based Generation of 3D Structures and Scene Representations

Learned distributions generate scene parameters, layouts, voxels, neural fields, or Gaussian representations.

- <a id="paper-vu2026aeroscenev2"></a>**AeroScene: Progressive Scene Synthesis for Aerial Robotics**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2603.23224v2)

- <a id="paper-xie2025gaussiancity"></a>**Generative Gaussian Splatting for Unbounded 3D City Generation**\
  <sub>CVPR 2025</sub> · [📄 Paper](https://arxiv.org/abs/2406.06526) · [🌐 Project](https://haozhexie.com/project/gaussian-city)

- <a id="paper-hu2025cadd"></a>**Large Scene Generation with Cube-Absorb Discrete Diffusion**\
  <sub>ICCV 2025</sub> · [📄 Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Hu_Large_Scene_Generation_with_Cube-Absorb_Discrete_Diffusion_ICCV_2025_paper.html)

- <a id="paper-xie2024citydreamer"></a>**CityDreamer: Compositional Generative Model of Unbounded 3D Cities**\
  <sub>CVPR 2024</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Xie_CityDreamer_Compositional_Generative_Model_of_Unbounded_3D_Cities_CVPR_2024_paper.html)

- <a id="paper-ren2024xcube"></a>**XCube: Large-Scale 3D Generative Modeling using Sparse Voxel Hierarchies**\
  <sub>CVPR 2024</sub> · [📄 Paper](https://arxiv.org/abs/2312.03806) · [💻 Code](https://github.com/nv-tlabs/XCube) · [🌐 Project](https://research.nvidia.com/labs/toronto-ai/xcube/)

- <a id="paper-chen2023scenedreamer"></a>**SceneDreamer: Unbounded 3D Scene Generation From 2D Image Collections**\
  <sub>IEEE TPAMI 2023</sub> · [📄 Paper](https://doi.org/10.1109/TPAMI.2023.3321857) · [💻 Code](https://github.com/FrozenBurning/SceneDreamer)

- <a id="paper-devaranjan2020metasim2"></a>**Meta-Sim2: Unsupervised Learning of Scene Structure for Synthetic Data Generation**\
  <sub>ECCV 2020</sub> · [📄 Paper](https://doi.org/10.1007/978-3-030-58520-4_42) · [🌐 Project](https://nv-tlabs.github.io/meta-sim-structure/)

- <a id="paper-kar2019metasim"></a>**Meta-Sim: Learning to Generate Synthetic Datasets**\
  <sub>ICCV 2019</sub> · [📄 Paper](https://arxiv.org/abs/1904.11621)


<a id="synthesis-visual-priors"></a>

### 🎨 1.4 3D Environment Generation with Image and Video Priors

Images, panoramas, and videos supply visual priors that are lifted or fused into spatial environments.

- <a id="paper-hyworld2026v1"></a>**HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2604.14268v1) · [💻 Code](https://github.com/Tencent-Hunyuan/HY-World-2.0)

- <a id="paper-hunyuan2025worldv2"></a>**HunyuanWorld 1.0: Generating Immersive, Explorable, and Interactive 3D Worlds from Words or Pixels**\
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2507.21809v2) · [💻 Code](https://github.com/Tencent-Hunyuan/HunyuanWorld-1.0)

- <a id="paper-lu2025infinicube"></a>**InfiniCube: Unbounded and Controllable Dynamic 3D Driving Scene Generation with World-Guided Video Models**\
  <sub>ICCV 2025</sub> · [📄 Paper](https://arxiv.org/abs/2412.03934) · [🌐 Project](https://research.nvidia.com/labs/toronto-ai/infinicube/)

- <a id="paper-chung2025luciddreamer"></a>**LucidDreamer: Domain-Free Generation of 3D Gaussian Splatting Scenes**\
  <sub>IEEE TVCG 2025</sub> · [📄 Paper](https://doi.org/10.1109/TVCG.2025.3611489) · [💻 Code](https://github.com/luciddreamer-cvlab/LucidDreamer)

- <a id="paper-yu2025wonderworld"></a>**WonderWorld: Interactive 3D Scene Generation from a Single Image**\
  <sub>CVPR 2025</sub> · [📄 Paper](https://arxiv.org/abs/2406.09394) · [🌐 Project](https://kovenyu.com/WonderWorld/)

- <a id="paper-zhou2024dreamscene360"></a>**DreamScene360: Unconstrained Text-to-3D Scene Generation with Panoramic Gaussian Splatting**\
  <sub>ECCV 2024</sub> · [📄 Paper](https://doi.org/10.1007/978-3-031-72658-3_19)

[↑ Back to contents](#contents)


---

<a id="reconstruction"></a>

## 🧭 2. Reconstruction of Real Environments

Recover a digital counterpart of a specific real place or observed environmental state.


<a id="reconstruction-geospatial"></a>

### 🗺️ 2.1 Geospatial Data- and Map-Driven Structured Reconstruction

Georeferenced maps and elevation data establish the structure of a specific site.

- <a id="paper-sanchez2026agricultural"></a>**Semi-Automated Generation of Realistic Simulation Environments from Geospatial Data for Agricultural Robot Navigation**\
  <sub>CMES 2026</sub> · [📄 Paper](https://doi.org/10.32604/cmes.2026.080739)

- <a id="paper-raskoti2025elevation"></a>**Elevation Aware 2D/3D Co-simulation Framework for Large-scale Traffic Flow and High-fidelity Vehicle Dynamics**\
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2512.11249v1)


<a id="reconstruction-geometry"></a>

### 📡 2.2 Explicit Geometry Recovery and Multisensor Fusion

Calibrated observations and sensor fusion recover explicit samples, surfaces, and object geometry.

- <a id="paper-kostrzewa2025photogrammetry"></a>**Open-Source vs. Commercial Photogrammetry: Comparing Accuracy and Efficiency of OpenDroneMap and Agisoft Metashape**\
  <sub>ISPRS Archives 2025</sub> · [📄 Paper](https://doi.org/10.5194/isprs-archives-XLVIII-1-W4-2025-65-2025)

- <a id="paper-zhang2024resimad"></a>**ReSimAD: Zero-Shot 3D Domain Transfer for Autonomous Driving with Source Reconstruction and Target Simulation**\
  <sub>ICLR 2024</sub> · [📄 Paper](https://arxiv.org/abs/2309.05527) · [💻 Code](https://github.com/PJLab-ADG/3DTrans)

- <a id="paper-manivasagam2020lidarsim"></a>**LiDARsim: Realistic LiDAR Simulation by Leveraging the Real World**\
  <sub>CVPR 2020</sub> · [📄 Paper](https://arxiv.org/abs/2006.09348)


<a id="reconstruction-neural"></a>

### 🚗 2.3 Scene Reconstruction with Neural Fields and Gaussian Representations

Neural fields and Gaussian representations recover captured outdoor scenes, appearance, and dynamics.

- <a id="paper-nvidia2026instantnurec"></a>**Instant NuRec: Feed-Forward 3D Gaussian Reconstruction for Driving Scene Simulation**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2607.14203v1) · [🌐 Project](https://research.nvidia.com/labs/sil/projects/instant-nurec) · [💻 Code](https://github.com/nvidia/instant-nurec)

- <a id="paper-qian2026sat3dgen"></a>**Sat3DGen: Comprehensive Street-Level 3D Scene Generation from Single Satellite Image**\
  <sub>ICLR 2026</sub> · [📄 Paper](https://arxiv.org/abs/2605.14984) · [💻 Code](https://github.com/qianmingduowan/Sat3DGen)

- <a id="paper-wang2026urbangs"></a>**Urban-GS: A Unified 3D Gaussian Splatting Framework for Compact and High-Fidelity Aerial-to-Street Reconstruction**\
  <sub>CVPR 2026</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Urban-GS_A_Unified_3D_Gaussian_Splatting_Framework_for_Compact_and_CVPR_2026_paper.pdf)

- <a id="paper-xie2025vid2sim"></a>**Vid2Sim: Realistic and Interactive Simulation from Video for Urban Navigation**\
  <sub>CVPR 2025</sub> · [📄 Paper](https://arxiv.org/abs/2501.06693) · [🌐 Project](https://metadriverse.github.io/vid2sim/)

- <a id="paper-tonderski2024neurad"></a>**NeuRAD: Neural Rendering for Autonomous Driving**\
  <sub>CVPR 2024</sub> · [📄 Paper](https://arxiv.org/abs/2311.15260)


<a id="reconstruction-properties"></a>

### 🌬️ 2.4 Recovering Simulation-Relevant Structures and Properties

Recovery extends to persistent surfaces, calibrated facility behavior, and environmental fields.

- <a id="paper-xu2025streetunveiler"></a>**3D StreetUnveiler with Semantic-aware 2DGS - a simple baseline**\
  <sub>ICLR 2025</sub> · [📄 Paper](https://arxiv.org/abs/2405.18416) · [🌐 Project](https://streetunveiler.github.io)

- <a id="paper-schnerring2025solar"></a>**A simulation environment for UAV-based real-time condition monitoring of solar tower power plants**\
  <sub>Solar Energy 2025</sub> · [📄 Paper](https://doi.org/10.1016/j.solener.2025.113803)

- <a id="paper-achermann2024windseer"></a>**WindSeer: real-time volumetric wind prediction over complex terrain aboard a small uncrewed aerial vehicle**\
  <sub>Nature Communications 2024</sub> · [📄 Paper](https://doi.org/10.1038/s41467-024-47778-4)

The navigation-structure example **SE(2) Navigation Mesh** is discussed separately in [Methodological references](docs/methodological-references.md#navigation-structure).

[↑ Back to contents](#contents)


---

<a id="transformation"></a>

## 🛠️ 3. Transformation of Existing Environments

Modify an existing digital environment while maintaining the content and relationships required by the task.


<a id="transformation-completion"></a>

### 🧱 3.1 Geometric Completion, Local Repair, and Spatial Expansion

Missing regions are completed while preserving alignment with the surrounding environment.

- <a id="paper-gao2026gscompleterv2"></a>**GSCompleter: A Distillation-Free Plugin for Metric-Aware 3D Gaussian Splatting Completion in Seconds**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2604.20155v2) · [🌐 Project](https://yuhuoo.github.io/projects/gscompleter/)

- <a id="paper-chen2025gsroadpatching"></a>**GS-RoadPatching: Inpainting Gaussians via 3D Searching and Placing for Driving Scenes**\
  <sub>SIGGRAPH Asia 2025</sub> · [📄 Paper](https://doi.org/10.1145/3757377.3763892) · [🌐 Project](https://shanzhaguoo.github.io/GS-RoadPatching/)


<a id="transformation-editing"></a>

### ✏️ 3.2 Object, Semantic, and Topological Editing

Structured scene representations expose object edits, semantic selection, and contextual integration.

- <a id="paper-park2026simsplatv2"></a>**SIMSplat: Language-Aligned 4D Gaussian Splatting for Driving Scenario Generation**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2510.02469v2)

- <a id="paper-miao2025falcongymv1"></a>**Performance-Guided Refinement for Visual Aerial Navigation using Editable Gaussian Splatting in FalconGym 2.0**\
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2510.02248v1)

- <a id="paper-ljungbergh2025r3d2v1"></a>**R3D2: Realistic 3D Asset Insertion via Diffusion for Autonomous Driving Simulation**\
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2506.07826v1)

- <a id="paper-yang2023unisim"></a>**UniSim: A Neural Closed-Loop Sensor Simulator**\
  <sub>CVPR 2023</sub> · [📄 Paper](https://arxiv.org/abs/2308.01898v1) · [🌐 Project](https://waabi.ai/research/unisim/)


<a id="transformation-properties"></a>

### 🌦️ 3.3 Transformations of Appearance, Physics, and Environmental Properties

Scene variants change illumination, weather, physical properties, or geometry-dependent environmental fields.

- <a id="paper-chen2026musyncv1"></a>**muSync-GS: Physics-Synchronized Driving Video Synthesis for Weather and Geometric Road Hazards**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2608.04412v1)

- <a id="paper-qian2026weatheredit"></a>**WeatherEdit: Controllable Weather Editing with 4D Gaussian Field**\
  <sub>AAAI 2026</sub> · [📄 Paper](https://doi.org/10.1609/aaai.v40i10.37802) · [🌐 Project](https://jumponthemoon.github.io/w-edit/)

- <a id="paper-lv2026relightablev2"></a>**Zero-Shot UAV Navigation in Forests via Relightable 3D Gaussian Splatting**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2602.07101v2)

- <a id="paper-dai2025rainygs"></a>**RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting**\
  <sub>CVPR 2025</sub> · [📄 Paper](https://arxiv.org/abs/2503.21442)

- <a id="paper-zhang2024dronewisv1"></a>**DroneWiS: Automated Simulation Testing of small Unmanned Aerial Systems in Realistic Windy Conditions**\
  <sub>arXiv 2024</sub> · [📄 Paper](https://arxiv.org/abs/2408.16559v1)

The abstract road-network example **TraSculptor** is discussed separately in [Methodological references](docs/methodological-references.md#abstract-road-graph).

[↑ Back to contents](#contents)


---

<a id="hybrid"></a>

## 🤖 4. Hybrid Construction and Automated Orchestration

Hybrid pipelines connect different construction operations. Orchestration selects and executes tools, maintains construction state, and uses feedback to revise intermediate results. This section follows Section 3.4 of the survey.

- <a id="paper-wang2026worldgen"></a>**WorldGen: From Text to Traversable and Interactive 3D Worlds**\
  <sub>CVPR 2026</sub> · [📄 Paper](https://arxiv.org/abs/2511.16825)

- <a id="paper-zhou2025scenex"></a>**SceneX: Procedural Controllable Large-Scale Scene Generation**\
  <sub>AAAI 2025</sub> · [📄 Paper](https://doi.org/10.1609/aaai.v39i10.33174) · [🌐 Project](https://zhouzq1.github.io/SceneX/)


Related examples already listed above include [3D-GPT](#paper-sun2023gpt3dv1) and [CityX](#paper-zhang2024cityxv1) for language-to-tool orchestration, and [DroneWiS](#paper-zhang2024dronewisv1) for geometry-dependent wind augmentation. Indoor and game-world examples—**MUSE**, **MAGIC**, and **PhyScensis**—are explained in [Methodological references](docs/methodological-references.md).

[↑ Back to contents](#contents)

---

<a id="resources"></a>

## 🧰 5. Supporting Resources

These resources support the simulation uses and evaluation settings discussed in Sections 4–5 and Table 4. They are separate from the selected-method count above.


### 🏗️ Simulation Platforms

Environment execution, configurable scenes, and repeatable trials.

| Resource | Role in the reviewed experiments | Links |
| :--- | :--- | :--- |
| **CARLA** | Scenario execution, synchronization, and replay | [📘 Documentation](https://carla.readthedocs.io/en/latest/) |
| **MetaDrive** | Procedural driving environments and repeatable scenario configuration | [📘 Documentation](https://metadrive-simulator.readthedocs.io/en/latest/) |
| **MetaUrban** | Interactive urban environments for navigation evaluation | [🌐 Project](https://metadriverse.github.io/metaurban) |

### 🗃️ Scene Data and Evaluation Inputs

Observations and scene inputs used in the reviewed experiments.

| Resource | Role in the reviewed experiments | Links |
| :--- | :--- | :--- |
| **GoogleEarth views** | Rendered city views used to evaluate visual quality and cross-view consistency | [🌐 Project](https://haozhexie.com/project/gaussian-city) |
| **Waymo Open Dataset** | Driving observations for reconstruction, editing, and transfer experiments | [🗃️ Dataset](https://waymo.com/open/) |
| **PandaSet** | Camera and LiDAR observations for sensor fidelity and transfer evaluation | [🧰 Devkit](https://github.com/scaleapi/pandaset-devkit) |
| **KITTI** | Real observations and labels for detection transfer evaluation | [🗃️ Dataset](https://www.cvlibs.net/datasets/kitti/) |
| **DL3DV** | Multiview scene observations for completion and preservation evaluation | [🗃️ Dataset](https://huggingface.co/DL3DV) |
| **Vid2Sim videos** | Monocular urban video inputs for reconstruction and navigation experiments | [🌐 Project](https://metadriverse.github.io/vid2sim/) |

### 🧩 Asset Resources

Object resources compared within construction and perception pipelines.

| Resource | Role in the reviewed experiments | Links |
| :--- | :--- | :--- |
| **LiDARsim assets** | Reconstructed objects and CAD vehicles compared in perception experiments | [📄 Paper](https://arxiv.org/abs/2006.09348) |

### 📏 Response References

Measurements or external model outputs used to assess environmental and vehicle responses.

| Resource | Role in the reviewed experiments | Links |
| :--- | :--- | :--- |
| **WindSeer measurements** | Field measurements used to assess wind prediction | [📄 Paper](https://doi.org/10.1038/s41467-024-47778-4) |
| **CarSim** | Vehicle-response reference; the reviewed muSync-GS experiments use CarSim 2022.1 | [🔗 Product](https://www.carsim.com/products/carsim/) |


---

<a id="further-reading"></a>

## 📚 Further Reading

| Collection | What it contains |
| :--- | :--- |
| [🧭 Methodological references](docs/methodological-references.md) | 5 explicitly scoped examples from indoor authoring, game worlds, legged navigation, and abstract road graphs. |
| [📚 Extended reading and full inventory](docs/extended-reading.md) | The original 177 records, plus the 7 manuscript methods added during curation. This includes papers beyond the current homepage scope. |
| [🔎 Candidate review queue](docs/candidates.md) | 7 boundary candidates with unresolved scope or classification questions. |
| [📝 Selection and source notes](docs/selection-notes.md) | Inclusion rationale, manuscript correspondence, and a record of where the original entries are displayed. |

The 25 provisional additions from the original supplement remain in extended reading. They are not promoted to this manuscript-aligned homepage solely because they were present in the collection.

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
