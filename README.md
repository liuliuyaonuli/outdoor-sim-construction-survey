<a id="top"></a>

<div align="center">

# 🌍 Outdoor 3D Simulation<br>Environment Construction Survey

**Automated Construction of Outdoor 3D Simulation Environments for Autonomous Systems**

面向自主系统的室外三维仿真环境自动构建

**🚗 Autonomous Driving &nbsp; · &nbsp; 🚁 Aerial Robotics &nbsp; · &nbsp; 🌲 Outdoor Worlds**

<p>
  <kbd>📚 125 selected methods</kbd> &nbsp;
  <kbd>🗂️ 12 technical topics</kbd> &nbsp;
  <kbd>🧰 28 supporting resources</kbd>
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

A curated collection of research on automatically constructing outdoor 3D simulation environments. Explore environment synthesis, reconstruction, transformation, and hybrid pipelines, together with [simulation platforms, datasets, and evaluation resources](#resources).

面向室外自主系统的三维仿真环境构建论文与资源，按“生成、重建、变换及混合编排”组织，提供论文、代码、项目与数据集链接。

**Updated 2026-11-06.**

<table>
<tr>
<td width="33%" valign="top">
<h3>🌱 Synthesis</h3>
<p><strong>新环境生成 · 58 methods</strong></p>
<p>Rules → assets → learned structures → visual priors.</p>
<p><sub>Diversity + constraints</sub></p>
<a href="#synthesis">Explore synthesis →</a>
</td>
<td width="33%" valign="top">
<h3>🧭 Reconstruction</h3>
<p><strong>真实环境重建 · 41 methods</strong></p>
<p>Maps → geometry → neural scenes → environmental properties.</p>
<p><sub>Reality correspondence</sub></p>
<a href="#reconstruction">Explore reconstruction →</a>
</td>
<td width="33%" valign="top">
<h3>🛠️ Transformation</h3>
<p><strong>现有环境变换 · 22 methods</strong></p>
<p>Completion → object editing → appearance and physics.</p>
<p><sub>Change + preservation</sub></p>
<a href="#transformation">Explore transformation →</a>
</td>
</tr>
</table>

**🤖 Hybrid construction and orchestration:** 4 additional methods connect construction stages through executable tools and feedback.

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
- [🤝 Contributing](#contributing)

**Resource key:** 📄 Paper · 💻 Code · 🌐 Project · 📘 Documentation · 🗃️ Dataset

Papers are grouped by technical approach and ordered by year, newest first within each topic.


---

<a id="synthesis"></a>

## 🌱 1. Synthesis of New Environments

Create new environments using procedural rules, asset composition, learned structures, or visual priors.


<a id="synthesis-procedural"></a>

### 🌳 1.1 Rule- and Constraint-Driven Procedural Generation

Rules and intermediate structures control roads, buildings, terrain, and natural environments.


#### Infrastructure and natural-world rules

- <a id="paper-capek2025flightforge"></a>**FlightForge: Advancing UAV Research with Procedural Generation of High-Fidelity Simulation and Integrated Autonomy**\
  <sub>ICRA 2025</sub> · [📄 Paper](https://doi.org/10.1109/ICRA55743.2025.11127704)

- <a id="paper-raistrick2023infinigen"></a>**Infinite Photorealistic Worlds Using Procedural Generation**\
  <sub>CVPR 2023</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Raistrick_Infinite_Photorealistic_Worlds_Using_Procedural_Generation_CVPR_2023_paper.html) · [🌐 Project](https://infinigen.org/)

- <a id="paper-niese2022urbanforestry"></a>**Procedural Urban Forestry**\
  <sub>ACM TOG 2022</sub> · [📄 Paper](https://research.google/pubs/procedural-urban-forestry/)

- <a id="paper-genevaux2013hydrology"></a>**Terrain Generation Using Procedural Models Based on Hydrology**\
  <sub>ACM TOG 2013</sub> · [📄 Paper](https://doi.org/10.1145/2461912.2461996)

- <a id="paper-galin2010roads"></a>**Procedural Generation of Roads**\
  <sub>Computer Graphics Forum 2010</sub> · [📄 Paper](https://onlinelibrary.wiley.com/doi/10.1111/j.1467-8659.2009.01612.x)

- <a id="paper-muller2006buildings"></a>**Procedural Modeling of Buildings**\
  <sub>ACM TOG 2006</sub> · [📄 Paper](https://doi.org/10.1145/1141911.1141931)

- <a id="paper-parish2001cities"></a>**Procedural Modeling of Cities**\
  <sub>SIGGRAPH 2001</sub> · [📄 Paper](https://doi.org/10.1145/383259.383292)


#### Constraint languages and task-specific simulators

- <a id="paper-bajpai2026agrigen"></a>**AgriGen: Large-Scale Scene Generation Framework for Photorealistic Agricultural Robotics Simulation**\
  <sub>ICRA Workshop on Agricultural Robotics 2026</sub> · [📄 Paper](https://baj31415.github.io/agrigen/)

- <a id="paper-vecchio2025midgard"></a>**MIDGARD: A Robot Navigation Simulator for Outdoor Unstructured Environments**\
  <sub>ERF 2024 (proceedings 2025)</sub> · [📄 Paper](https://researchportal.hw.ac.uk/en/publications/midgard-a-robot-navigation-simulator-for-outdoor-unstructured-env/)

- <a id="paper-wu2025urbansim"></a>**Towards Autonomous Micromobility through Scalable Urban Simulation**\
  <sub>CVPR 2025</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_Towards_Autonomous_Micromobility_through_Scalable_Urban_Simulation_CVPR_2025_paper.html) · [🌐 Project](https://metadriverse.github.io/urban-sim/)

- <a id="paper-vin2023scenic3"></a>**3D Environment Modeling for Falsification and Beyond with Scenic 3.0**\
  <sub>CAV 2023</sub> · [📄 Paper](https://arxiv.org/abs/2307.03325v1)

- <a id="paper-fremont2019scenic"></a>**Scenic: A Language for Scenario Specification and Scene Generation**\
  <sub>PLDI 2019</sub> · [📄 Paper](https://people.eecs.berkeley.edu/~sseshia/pubdir/pldi19-scenic.pdf)


#### Language and intermediate procedural controls

- <a id="paper-liu2026landcraft"></a>**LandCraft: Designing the Structured 3D Landscapes via Text Guidance**\
  <sub>AAAI 2026</sub> · [📄 Paper](https://doi.org/10.1609/aaai.v40i9.37686)

- <a id="paper-duan2025latticeworld"></a>**LatticeWorld: A Multimodal Large Language Model-Empowered Framework for Interactive Complex World Generation**\
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2509.05263v2)

- <a id="paper-tang2025unrealllm"></a>**UnrealLLM: Towards Highly Controllable and Interactable 3D Scene Generation by LLM-powered Procedural Content Generation**\
  <sub>Findings of ACL 2025</sub> · [📄 Paper](https://aclanthology.org/2025.findings-acl.994/)

- <a id="paper-liu2025worldcraft"></a>**WorldCraft: Photo-Realistic 3D World Creation and Customization via LLM Agents**\
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2502.15601v2)

- <a id="paper-zhang2024cityxv1"></a>**CityX: Controllable Procedural Content Generation for Unbounded 3D Cities**\
  <sub>arXiv 2024</sub> · [📄 Paper](https://arxiv.org/abs/2407.17572v1)

- <a id="paper-sun2023gpt3dv1"></a>**3D-GPT: Procedural 3D Modeling with Large Language Models**\
  <sub>arXiv 2023</sub> · [📄 Paper](https://arxiv.org/abs/2310.12945v1) · [🌐 Project](https://chuny1.github.io/3DGPT/3dgpt.html)


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

- <a id="paper-zhuang2025simworldrobotics"></a>**SimWorld-Robotics: Synthesizing Photorealistic and Dynamic Urban Environments for Multimodal Robot Navigation and Collaboration**\
  <sub>NeurIPS 2025</sub> · [📄 Paper](https://papers.neurips.cc/paper_files/paper/2025/hash/4a81c1aad3064fb8243b8938a49ecca0-Abstract-Conference.html)

- <a id="paper-deng2024citycraftv1"></a>**CityCraft: A Real Crafter for 3D City Generation**\
  <sub>arXiv 2024</sub> · [📄 Paper](https://arxiv.org/abs/2406.04983v1)

- <a id="paper-li2023metadrive"></a>**MetaDrive: Composing Diverse Driving Scenarios for Generalizable Reinforcement Learning**\
  <sub>IEEE TPAMI 2023</sub> · [📄 Paper](https://doi.org/10.1109/tpami.2022.3190471) · [💻 Code](https://github.com/metadriverse/metadrive) · [📘 Documentation](https://metadrive-simulator.readthedocs.io/en/latest/)


<a id="synthesis-learning"></a>

### 🌐 1.3 Learning-Based Generation of 3D Structures and Scene Representations

Learned distributions generate scene parameters, layouts, voxels, neural fields, or Gaussian representations.


#### Scene parameters, layouts, and relational control

- <a id="paper-vu2026aeroscenev2"></a>**AeroScene: Progressive Scene Synthesis for Aerial Robotics**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2603.23224v2)

- <a id="paper-liu2025outdoorscenegraphs"></a>**Controllable 3D Outdoor Scene Generation via Scene Graphs**\
  <sub>ICCV 2025</sub> · [📄 Paper](https://arxiv.org/abs/2503.07152) · [💻 Code](https://github.com/yuhengliu02/control-3d-scene)

- <a id="paper-devaranjan2020metasim2"></a>**Meta-Sim2: Unsupervised Learning of Scene Structure for Synthetic Data Generation**\
  <sub>ECCV 2020</sub> · [📄 Paper](https://doi.org/10.1007/978-3-030-58520-4_42) · [🌐 Project](https://nv-tlabs.github.io/meta-sim-structure/)

- <a id="paper-kar2019metasim"></a>**Meta-Sim: Learning to Generate Synthetic Datasets**\
  <sub>ICCV 2019</sub> · [📄 Paper](https://arxiv.org/abs/1904.11621)


#### Hierarchical and semantic spatial representations

- <a id="paper-tze2026pritti"></a>**PrITTI: Primitive-based Generation of Controllable and Editable 3D Semantic Urban Scenes**\
  <sub>CVPR 2026</sub> · [📄 Paper](https://raniatze.github.io/pritti/)

- <a id="paper-liang2025cymbadiff"></a>**CymbaDiff: Structured Spatial Diffusion for Sketch-based 3D Semantic Urban Scene Generation**\
  <sub>NeurIPS 2025</sub> · [📄 Paper](https://arxiv.org/abs/2510.13245v3)

- <a id="paper-bian2025dynamiccity"></a>**DynamicCity: Large-Scale 4D Occupancy Generation from Dynamic Scenes**\
  <sub>ICLR 2025</sub> · [📄 Paper](https://openreview.net/forum?id=M7KyLjuN0A)

- <a id="paper-hu2025cadd"></a>**Large Scene Generation with Cube-Absorb Discrete Diffusion**\
  <sub>ICCV 2025</sub> · [📄 Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Hu_Large_Scene_Generation_with_Cube-Absorb_Discrete_Diffusion_ICCV_2025_paper.html)

- <a id="paper-li2025uniscene"></a>**UniScene: Unified Occupancy-Centric Driving Scene Generation**\
  <sub>CVPR 2025</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Li_UniScene_Unified_Occupancy-centric_Driving_Scene_Generation_CVPR_2025_paper.html)

- <a id="paper-lee2024semcity"></a>**SemCity: Semantic Scene Generation with Triplane Diffusion**\
  <sub>CVPR 2024</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Lee_SemCity_Semantic_Scene_Generation_with_Triplane_Diffusion_CVPR_2024_paper.html)

- <a id="paper-ren2024xcube"></a>**XCube: Large-Scale 3D Generative Modeling using Sparse Voxel Hierarchies**\
  <sub>CVPR 2024</sub> · [📄 Paper](https://arxiv.org/abs/2312.03806) · [💻 Code](https://github.com/nv-tlabs/XCube) · [🌐 Project](https://research.nvidia.com/labs/toronto-ai/xcube/)


#### Compositional city representations

- <a id="paper-xie2025gaussiancity"></a>**Generative Gaussian Splatting for Unbounded 3D City Generation**\
  <sub>CVPR 2025</sub> · [📄 Paper](https://arxiv.org/abs/2406.06526) · [🌐 Project](https://haozhexie.com/project/gaussian-city)

- <a id="paper-xie2024citydreamer"></a>**CityDreamer: Compositional Generative Model of Unbounded 3D Cities**\
  <sub>CVPR 2024</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Xie_CityDreamer_Compositional_Generative_Model_of_Unbounded_3D_Cities_CVPR_2024_paper.html)\
  <sub>↳ Journal extension: Compositional Generative Model of Unbounded 4D Cities · IEEE TPAMI 2026</sub> · [📄 Journal paper](https://doi.org/10.1109/TPAMI.2025.3603078)

- <a id="paper-lin2023infinicity"></a>**InfiniCity: Infinite-Scale City Synthesis**\
  <sub>ICCV 2023</sub> · [📄 Paper](https://hubert0527.github.io/infinicity/)

- <a id="paper-chen2023scenedreamer"></a>**SceneDreamer: Unbounded 3D Scene Generation From 2D Image Collections**\
  <sub>IEEE TPAMI 2023</sub> · [📄 Paper](https://doi.org/10.1109/tpami.2023.3321857) · [💻 Code](https://github.com/FrozenBurning/SceneDreamer)


#### Persistent worlds and local expansion

- <a id="paper-joshi2026worldflow3dv1"></a>**WorldFlow3D: Flowing Through 3D Distributions for Unbounded World Generation**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2603.29089v1) · [🌐 Project](https://light.princeton.edu/worldflow3d)

- <a id="paper-lee2025nuiscene"></a>**NuiScene: Exploring Efficient Generation of Unbounded Outdoor Scenes**\
  <sub>ICCV 2025</sub> · [📄 Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Lee_NuiScene_Exploring_Efficient_Generation_of_Unbounded_Outdoor_Scenes_ICCV_2025_paper.html) · [🗃️ Dataset](https://github.com/3dlg-hcvc/NuiScene43-Dataset)

- <a id="paper-wu2024blockfusion"></a>**BlockFusion: Expandable 3D Scene Generation using Latent Tri-plane Extrapolation**\
  <sub>ACM TOG 2024</sub> · [📄 Paper](https://arxiv.org/abs/2401.17053)

- <a id="paper-chai2023persistentnature"></a>**Persistent Nature: A Generative Model of Unbounded 3D Worlds**\
  <sub>CVPR 2023</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Chai_Persistent_Nature_A_Generative_Model_of_Unbounded_3D_Worlds_CVPR_2023_paper.html)


#### Terrain and sensor-oriented world generation

- <a id="paper-zyrianov2025lidardm"></a>**LidarDM: Generative LiDAR Simulation in a Generated World**\
  <sub>ICRA 2025</sub> · [📄 Paper](https://zyrianov.org/lidardm/LidarDM_ICRA2025.pdf)

- <a id="paper-hu2024terraindiffusion"></a>**Terrain Diffusion Network: Climatic-Aware Terrain Generation with Geological Sketch Guidance**\
  <sub>AAAI 2024</sub> · [📄 Paper](https://ojs.aaai.org/index.php/AAAI/article/view/29150)


<a id="synthesis-visual-priors"></a>

### 🎨 1.4 3D Environment Generation with Image and Video Priors

Images, panoramas, and videos supply visual priors that are lifted or fused into spatial environments.

- <a id="paper-li2026flymiragev1"></a>**FlyMirage: A Fully Automated Generation Pipeline for Diverse and Scalable UAV Flight Data via Generative World Model**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2605.19600v1)

- <a id="paper-hyworld2026v1"></a>**HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2604.14268v1) · [💻 Code](https://github.com/Tencent-Hunyuan/HY-World-2.0)

- <a id="paper-ost2026lsd3d"></a>**LSD-3D: Large-Scale 3D Driving Scene Generation with Geometry Grounding**\
  <sub>AAAI 2026</sub> · [📄 Paper](https://arxiv.org/abs/2508.19204v1)

- <a id="paper-kim2026scenefrom3dv1"></a>**SceneFrom3D: Geometry-Conditioned Outdoor 3D Scene Generation via View Scheduling with Object-Level Control**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2607.04540v1)

- <a id="paper-zhu2026worldsplat"></a>**WorldSplat: Gaussian-Centric Feed-Forward 4D Scene Generation for Autonomous Driving**\
  <sub>ICLR 2026</sub> · [📄 Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6fa4a1def9d60b5bf6078e13c900c45c-Abstract-Conference.html)

- <a id="paper-guo2025dist4d"></a>**DiST-4D: Disentangled Spatiotemporal Diffusion with Metric Depth for 4D Driving Scene Generation**\
  <sub>ICCV 2025</sub> · [📄 Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Guo_DiST-4D_Disentangled_Spatiotemporal_Diffusion_with_Metric_Depth_for_4D_Driving_ICCV_2025_paper.html)

- <a id="paper-mao2025dreamdrive"></a>**DreamDrive: Generative 4D Scene Modeling from Street View Images**\
  <sub>ICRA 2025</sub> · [📄 Paper](https://research.nvidia.com/labs/aspire/publication/mao.li.etal.icra2025/)

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

- <a id="paper-jannussi2026cam2simv1"></a>**Cam2Sim: Neural Scenario Reconstruction for Closed-Loop Autonomous Driving Simulation**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2607.04770v1)

- <a id="paper-sanchez2026agricultural"></a>**Semi-Automated Generation of Realistic Simulation Environments from Geospatial Data for Agricultural Robot Navigation**\
  <sub>CMES 2026</sub> · [📄 Paper](https://doi.org/10.32604/cmes.2026.080739)

- <a id="paper-hari2026simscene"></a>**SimScene: Automated Photorealistic Scene Reconstruction for Geographically Scalable Physical AI**\
  <sub>CVPR Workshop 2026</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026W/ReGen4D/html/hari_SimScene_Automated_Photorealistic_Scene_Reconstruction_for_Geographically_Scalable_Physical_AI_CVPRW_2026_paper.html)

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


#### City-scale and multiscale representations

- <a id="paper-liu2025citygaussian"></a>**CityGaussian: Real-Time High-Quality Large-Scale Scene Rendering with Gaussians**\
  <sub>ECCV 2024 (proceedings 2025)</sub> · [📄 Paper](https://doi.org/10.1007/978-3-031-72640-8_15)

- <a id="paper-liu2025citygaussianv2"></a>**CityGaussianV2: Efficient and Geometrically Accurate Reconstruction for Large-Scale Scenes**\
  <sub>ICLR 2025</sub> · [📄 Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d218ec74edbfc494fa7d7a253951c603-Abstract-Conference.html)

- <a id="paper-lin2024vastgaussian"></a>**VastGaussian: Vast 3D Gaussians for Large Scene Reconstruction**\
  <sub>CVPR 2024</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Lin_VastGaussian_Vast_3D_Gaussians_for_Large_Scene_Reconstruction_CVPR_2024_paper.html)

- <a id="paper-tancik2022blocknerf"></a>**Block-NeRF: Scalable Large Scene Neural View Synthesis**\
  <sub>CVPR 2022</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Tancik_Block-NeRF_Scalable_Large_Scene_Neural_View_Synthesis_CVPR_2022_paper.html)

- <a id="paper-xiangli2022bungeenerf"></a>**BungeeNeRF: Progressive Neural Radiance Field for Extreme Multi-Scale Scene Rendering**\
  <sub>ECCV 2022</sub> · [📄 Paper](https://doi.org/10.1007/978-3-031-19824-3_7)

- <a id="paper-turki2022meganerf"></a>**Mega-NeRF: Scalable Construction of Large-Scale NeRFs for Virtual Fly-Throughs**\
  <sub>CVPR 2022</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Turki_Mega-NERF_Scalable_Construction_of_Large-Scale_NeRFs_for_Virtual_Fly-Throughs_CVPR_2022_paper.html)

- <a id="paper-rematas2022urbanradiance"></a>**Urban Radiance Fields**\
  <sub>CVPR 2022</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Rematas_Urban_Radiance_Fields_CVPR_2022_paper.html)


#### Dynamic and object-decomposed scenes

- <a id="paper-chen2025omnire"></a>**OmniRe: Omni Urban Scene Reconstruction**\
  <sub>ICLR 2025</sub> · [📄 Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d4938496368e1c5806138bea8837595c-Abstract-Conference.html)

- <a id="paper-yang2024emernerf"></a>**EmerNeRF: Emergent Spatial-Temporal Scene Decomposition via Self-Supervision**\
  <sub>ICLR 2024</sub> · [📄 Paper](https://proceedings.iclr.cc/paper_files/paper/2024/hash/47fc64d05a394955b1ae2487bfef1ab0-Abstract-Conference.html)

- <a id="paper-zhou2024hugs"></a>**HUGS: Holistic Urban 3D Scene Understanding via Gaussian Splatting**\
  <sub>CVPR 2024</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Zhou_HUGS_Holistic_Urban_3D_Scene_Understanding_via_Gaussian_Splatting_CVPR_2024_paper.html)

- <a id="paper-fischer2024multilevelscenegraphs"></a>**Multi-Level Neural Scene Graphs for Dynamic Urban Environments**\
  <sub>CVPR 2024</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Fischer_Multi-Level_Neural_Scene_Graphs_for_Dynamic_Urban_Environments_CVPR_2024_paper.html)

- <a id="paper-tonderski2024neurad"></a>**NeuRAD: Neural Rendering for Autonomous Driving**\
  <sub>CVPR 2024</sub> · [📄 Paper](https://arxiv.org/abs/2311.15260)

- <a id="paper-yan2024streetgaussians"></a>**Street Gaussians: Modeling Dynamic Urban Scenes with Gaussian Splatting**\
  <sub>ECCV 2024</sub> · [📄 Paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9243_ECCV_2024_paper.php)

- <a id="paper-ost2021neuralscenegraphs"></a>**Neural Scene Graphs for Dynamic Scenes**\
  <sub>CVPR 2021</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2021/html/Ost_Neural_Scene_Graphs_for_Dynamic_Scenes_CVPR_2021_paper.html)


#### Feed-forward and aerial reconstruction

- <a id="paper-liu2026aerodgs"></a>**AeroDGS: Physically Consistent Dynamic Gaussian Splatting for Single-Sequence Aerial 4D Reconstruction**\
  <sub>CVPR 2026</sub> · [📄 Paper](https://arxiv.org/abs/2602.22376v1)

- <a id="paper-li2026aerogs"></a>**AeroGS: Scale-Aware Gaussian Splatting for Pose-Free Dynamic UAV Scene Reconstruction**\
  <sub>CVPR 2026</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_AeroGS_Scale-Aware_Gaussian_Splatting_for_Pose-Free_Dynamic_UAV_Scene_Reconstruction_CVPR_2026_paper.html)

- <a id="paper-chen2026dggt"></a>**DGGT: Feedforward 4D Reconstruction of Dynamic Driving Scenes using Unposed Images**\
  <sub>CVPR 2026</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_DGGT_Feedforward_4D_Reconstruction_of_Dynamic_Driving_Scenes_using_Unposed_CVPR_2026_paper.html)

- <a id="paper-nvidia2026instantnurec"></a>**Instant NuRec: Feed-Forward 3D Gaussian Reconstruction for Driving Scene Simulation**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2607.14203v1) · [🌐 Project](https://research.nvidia.com/labs/sil/projects/instant-nurec) · [💻 Code](https://github.com/nvidia/instant-nurec)

- <a id="paper-choi2026uav4d"></a>**UAV4D: Dynamic Neural Rendering of Human-Centric UAV Imagery Using Gaussian Splatting**\
  <sub>AAAI 2026</sub> · [📄 Paper](https://ojs.aaai.org/index.php/AAAI/article/view/37333)

- <a id="paper-ren2024scube"></a>**SCube: Instant Large-Scale Scene Reconstruction using VoxSplats**\
  <sub>NeurIPS 2024</sub> · [📄 Paper](https://proceedings.nips.cc/paper_files/paper/2024/hash/b111aa30ab71255946b19b6bd4e68939-Abstract-Conference.html)


#### Surface recovery and generative completion

- <a id="paper-qian2026sat3dgen"></a>**Sat3DGen: Comprehensive Street-Level 3D Scene Generation from Single Satellite Image**\
  <sub>ICLR 2026</sub> · [📄 Paper](https://arxiv.org/abs/2605.14984) · [💻 Code](https://github.com/qianmingduowan/Sat3DGen)

- <a id="paper-zhao2025drivedreamer4d"></a>**DriveDreamer4D: World Models Are Effective Data Machines for 4D Driving Scene Representation**\
  <sub>CVPR 2025</sub> · [📄 Paper](https://arxiv.org/abs/2410.13571v3)

- <a id="paper-ni2025recondreamer"></a>**ReconDreamer: Crafting World Models for Driving Scene Reconstruction via Online Restoration**\
  <sub>CVPR 2025</sub> · [📄 Paper](https://arxiv.org/abs/2411.19548v1)

- <a id="paper-yan2025streetcrafter"></a>**StreetCrafter: Street View Synthesis with Controllable Video Diffusion Models**\
  <sub>CVPR 2025</sub> · [📄 Paper](https://arxiv.org/abs/2412.13188v3)

- <a id="paper-zhang2024hgca"></a>**Outdoor Scene Extrapolation with Hierarchical Generative Cellular Automata**\
  <sub>CVPR 2024</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Outdoor_Scene_Extrapolation_with_Hierarchical_Generative_Cellular_Automata_CVPR_2024_paper.html)

- <a id="paper-li2024sat2scene"></a>**Sat2Scene: 3D Urban Scene Generation from Satellite Images with Diffusion**\
  <sub>CVPR 2024</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Li_Sat2Scene_3D_Urban_Scene_Generation_from_Satellite_Images_with_Diffusion_CVPR_2024_paper.html)

- <a id="paper-guo2023streetsurfv1"></a>**StreetSurf: Extending Multi-View Implicit Surface Reconstruction to Street Views**\
  <sub>arXiv 2023</sub> · [📄 Paper](https://arxiv.org/abs/2306.04988v1)


#### Cross-scale observations and navigation-oriented surfaces

- <a id="paper-wang2026urbangs"></a>**Urban-GS: A Unified 3D Gaussian Splatting Framework for Compact and High-Fidelity Aerial-to-Street Reconstruction**\
  <sub>CVPR 2026</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Urban-GS_A_Unified_3D_Gaussian_Splatting_Framework_for_Compact_and_CVPR_2026_paper.pdf)

- <a id="paper-xie2025vid2sim"></a>**Vid2Sim: Realistic and Interactive Simulation from Video for Urban Navigation**\
  <sub>CVPR 2025</sub> · [📄 Paper](https://arxiv.org/abs/2501.06693) · [🌐 Project](https://metadriverse.github.io/vid2sim/)


<a id="reconstruction-properties"></a>

### 🌬️ 2.4 Recovering Simulation-Relevant Structures and Properties

Recovery extends to persistent surfaces, calibrated facility behavior, and environmental fields.

- <a id="paper-xu2025streetunveiler"></a>**3D StreetUnveiler with Semantic-aware 2DGS - a simple baseline**\
  <sub>ICLR 2025</sub> · [📄 Paper](https://arxiv.org/abs/2405.18416) · [🌐 Project](https://streetunveiler.github.io)

- <a id="paper-schnerring2025solar"></a>**A simulation environment for UAV-based real-time condition monitoring of solar tower power plants**\
  <sub>Solar Energy 2025</sub> · [📄 Paper](https://doi.org/10.1016/j.solener.2025.113803)

- <a id="paper-wu2025emiemap"></a>**EMIE-MAP: Large-Scale Road Surface Reconstruction Based on Explicit Mesh and Implicit Encoding**\
  <sub>ECCV 2024 (proceedings 2025)</sub> · [📄 Paper](https://doi.org/10.1007/978-3-031-73021-4_22)

- <a id="paper-chen2025invrgbl"></a>**InvRGB+L: Inverse Rendering of Complex Scenes with Unified Color and LiDAR Reflectance Modeling**\
  <sub>ICCV 2025</sub> · [📄 Paper](https://arxiv.org/abs/2507.17613)

- <a id="paper-achermann2024windseer"></a>**WindSeer: real-time volumetric wind prediction over complex terrain aboard a small uncrewed aerial vehicle**\
  <sub>Nature Communications 2024</sub> · [📄 Paper](https://doi.org/10.1038/s41467-024-47778-4)

[↑ Back to contents](#contents)


---

<a id="transformation"></a>

## 🛠️ 3. Transformation of Existing Environments

Modify an existing digital environment while maintaining the content and relationships required by the task.


<a id="transformation-completion"></a>

### 🧱 3.1 Geometric Completion, Local Repair, and Spatial Expansion

Missing regions are completed while preserving alignment with the surrounding environment.

- <a id="paper-balde2026editssc"></a>**EditSSC: Toward Editable Semantic Occupancy Scenes with Unconditional Diffusion Models**\
  <sub>CVPR Workshop 2026</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026W/USM3D/html/Balde_EditSSC_Toward_Editable_Semantic_Occupancy_Scenes_with_Unconditional_Diffusion_Models_CVPRW_2026_paper.html)

- <a id="paper-gao2026gscompleterv2"></a>**GSCompleter: A Distillation-Free Plugin for Metric-Aware 3D Gaussian Splatting Completion in Seconds**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2604.20155v2) · [🌐 Project](https://yuhuoo.github.io/projects/gscompleter/)

- <a id="paper-chen2025gsroadpatching"></a>**GS-RoadPatching: Inpainting Gaussians via 3D Searching and Placing for Driving Scenes**\
  <sub>SIGGRAPH Asia 2025</sub> · [📄 Paper](https://doi.org/10.1145/3757377.3763892) · [🌐 Project](https://shanzhaguoo.github.io/GS-RoadPatching/)


<a id="transformation-editing"></a>

### ✏️ 3.2 Object, Semantic, and Topological Editing

Structured scene representations expose object edits, semantic selection, and contextual integration.

- <a id="paper-deng2026gaussiandwmppv1"></a>**GaussianDWM++: Language-Grounded 3D Gaussian Driving World Model for Unified Scene Understanding, Editing, and Multi-Modal Generation**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2608.16234v1)

- <a id="paper-wang2026horizonforge"></a>**HorizonForge: Driving Scene Editing with Any Trajectories and Any Vehicles**\
  <sub>CVPR 2026</sub> · [📄 Paper](https://arxiv.org/abs/2602.21333) · [🌐 Project](https://horizonforge.github.io/)

- <a id="paper-ljungbergh2025r3d2v1"></a>**R3D2: Realistic 3D Asset Insertion via Diffusion for Autonomous Driving Simulation**\
  <sub>CVPR Workshop 2026</sub> · [📄 Paper](https://arxiv.org/abs/2506.07826v1)

- <a id="paper-park2026simsplatv2"></a>**SIMSplat: Language-Aligned 4D Gaussian Splatting for Driving Scenario Generation**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2510.02469v2)

- <a id="paper-xiong2025drivinggaussianppv1"></a>**DrivingGaussian++: Towards Realistic Reconstruction and Editable Simulation for Surrounding Dynamic Driving Scenes**\
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2508.20965v1) · [🌐 Project](https://xiong-creator.github.io/DrivingGaussian_plus.github.io)

- <a id="paper-miao2025falcongymv1"></a>**Performance-Guided Refinement for Visual Aerial Navigation using Editable Gaussian Splatting in FalconGym 2.0**\
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2510.02248v1)

- <a id="paper-wei2024chatsim"></a>**Editable Scene Simulation for Autonomous Driving via Collaborative LLM-Agents**\
  <sub>CVPR 2024</sub> · [📄 Paper](https://arxiv.org/abs/2402.05746v3) · [💻 Code](https://github.com/yifanlu0227/ChatSim)

- <a id="paper-yang2023unisim"></a>**UniSim: A Neural Closed-Loop Sensor Simulator**\
  <sub>CVPR 2023</sub> · [📄 Paper](https://arxiv.org/abs/2308.01898v1) · [🌐 Project](https://waabi.ai/research/unisim/)


<a id="transformation-properties"></a>

### 🌦️ 3.3 Transformations of Appearance, Physics, and Environmental Properties

Scene variants change illumination, weather, physical properties, or geometry-dependent environmental fields.

- <a id="paper-fiebelman2026letitsnow"></a>**Let it Snow! Animating 3D Gaussian Scenes with Dynamic Weather Effects via Physics-Guided Score Distillation**\
  <sub>CVPR 2026</sub> · [📄 Paper](https://arxiv.org/abs/2504.05296v4) · [🌐 Project](https://galfiebelman.github.io/let-it-snow/) · [💻 Code](https://github.com/galfiebelman/let-it-snow)

- <a id="paper-fan2026metegs"></a>**MeteGS: Meteorology-Guided Gaussian Splatting for Scene Rendering and Recovery in Adverse Weather Conditions**\
  <sub>AAAI 2026</sub> · [📄 Paper](https://ijcai.org/proceedings/2026/120)

- <a id="paper-chen2026musyncv1"></a>**muSync-GS: Physics-Synchronized Driving Video Synthesis for Weather and Geometric Road Hazards**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2608.04412v1)

- <a id="paper-zhou2026rovesv1"></a>**Physics-Aware 3D Gaussian Editing for Driving Scene Generation**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2605.25373v1)

- <a id="paper-qian2026weatheredit"></a>**WeatherEdit: Controllable Weather Editing with 4D Gaussian Field**\
  <sub>AAAI 2026</sub> · [📄 Paper](https://doi.org/10.1609/aaai.v40i10.37802) · [🌐 Project](https://jumponthemoon.github.io/w-edit/)

- <a id="paper-lv2026relightablev2"></a>**Zero-Shot UAV Navigation in Forests via Relightable 3D Gaussian Splatting**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2602.07101v2)

- <a id="paper-dai2025rainygs"></a>**RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting**\
  <sub>CVPR 2025</sub> · [📄 Paper](https://arxiv.org/abs/2503.21442)

- <a id="paper-zhang2024dronewisv1"></a>**DroneWiS: Automated Simulation Testing of small Unmanned Aerial System in Realistic Windy Conditions**\
  <sub>ASE Demo 2024</sub> · [📄 Paper](https://doi.org/10.1145/3691620.3695351) · [📝 Preprint](https://arxiv.org/abs/2408.16559v1)

- <a id="paper-li2023climatenerf"></a>**ClimateNeRF: Extreme Weather Synthesis in Neural Radiance Field**\
  <sub>ICCV 2023</sub> · [📄 Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Li_ClimateNeRF_Extreme_Weather_Synthesis_in_Neural_Radiance_Field_ICCV_2023_paper.html)

- <a id="paper-pun2023lightsim"></a>**Neural Lighting Simulation for Urban Scenes**\
  <sub>NeurIPS 2023</sub> · [📄 Paper](https://papers.neurips.cc/paper_files/paper/2023/hash/3d7259031023c5aa463187c4a31c95c8-Abstract-Conference.html)

- <a id="paper-rudnev2022nerfosr"></a>**NeRF for Outdoor Scene Relighting**\
  <sub>ECCV 2022</sub> · [📄 Paper](https://doi.org/10.1007/978-3-031-19787-1_35)

[↑ Back to contents](#contents)


---

<a id="hybrid"></a>

## 🤖 4. Hybrid Construction and Automated Orchestration

Hybrid pipelines connect different construction operations. Orchestration selects and executes tools, maintains construction state, and uses feedback to revise intermediate results.

- <a id="paper-kang2026simworldstudiov2"></a>**SimWorld Studio: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2605.09423v2) · [🌐 Project](https://simworld.org/simworld-studio/)

- <a id="paper-wang2026urbanworld2v3"></a>**UrbanWorld2.0: A Multimodal Agentic Framework for Reality-Aligned 3D World Generation at City-Scale**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2511.18005v3)

- <a id="paper-wang2026worldgen"></a>**WorldGen: From Text to Traversable and Interactive 3D Worlds**\
  <sub>CVPR 2026</sub> · [📄 Paper](https://arxiv.org/abs/2511.16825)

- <a id="paper-zhou2025scenex"></a>**SceneX: Procedural Controllable Large-Scale Scene Generation**\
  <sub>AAAI 2025</sub> · [📄 Paper](https://doi.org/10.1609/aaai.v39i10.33174) · [🌐 Project](https://zhouzq1.github.io/SceneX/)


Related examples include [3D-GPT](#paper-sun2023gpt3dv1) and [CityX](#paper-zhang2024cityxv1) for language-to-tool orchestration, and [DroneWiS](#paper-zhang2024dronewisv1) for geometry-dependent wind augmentation.

[↑ Back to contents](#contents)

---

<a id="resources"></a>

## 🧰 5. Supporting Resources

Platforms, scene data, assets, and benchmarks for constructing and evaluating simulation environments.


### 🏗️ Simulation Platforms

Environment execution, configurable scenes, and repeatable trials.

| Resource | Purpose | Links |
| :--- | :--- | :--- |
| **CARLA** | Scenario execution, synchronization, and replay | [📘 Documentation](https://carla.readthedocs.io/en/latest/) |
| **MetaDrive** | Procedural driving environments and repeatable scenario configuration | [📘 Documentation](https://metadrive-simulator.readthedocs.io/en/latest/) |
| **MetaUrban** | Interactive urban environments for navigation evaluation | [🌐 Project](https://metadriverse.github.io/metaurban) |

### 🗃️ Scene Data and Evaluation Inputs

Observations and scene inputs used in the reviewed experiments.

| Resource | Purpose | Links |
| :--- | :--- | :--- |
| **GoogleEarth views** | Rendered city views used to evaluate visual quality and cross-view consistency | [🌐 Project](https://haozhexie.com/project/gaussian-city) |
| **Waymo Open Dataset** | Driving observations for reconstruction, editing, and transfer experiments | [🗃️ Dataset](https://waymo.com/open/) · [📄 Paper](https://openaccess.thecvf.com/content_CVPR_2020/html/Sun_Scalability_in_Perception_for_Autonomous_Driving_Waymo_Open_Dataset_CVPR_2020_paper.html) |
| **PandaSet** | Camera and LiDAR observations for sensor fidelity and transfer evaluation | [🧰 Devkit](https://github.com/scaleapi/pandaset-devkit) · [📄 Paper](https://arxiv.org/abs/2112.12610) |
| **KITTI** | Real observations and labels for detection transfer evaluation | [🗃️ Dataset](https://www.cvlibs.net/datasets/kitti/) · [📄 Paper](https://doi.org/10.1177/0278364913491297) |
| **DL3DV-10K** | Multiview scene observations for completion and preservation evaluation | [🗃️ Dataset](https://huggingface.co/DL3DV) · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Ling_DL3DV-10K_A_Large-Scale_Scene_Dataset_for_Deep_Learning-based_3D_Vision_CVPR_2024_paper.html) |
| **Vid2Sim videos** | Monocular urban video inputs for reconstruction and navigation experiments | [🌐 Project](https://metadriverse.github.io/vid2sim/) |
| **UrbanScene3D** | Urban imagery and geometry for capture planning, reconstruction, and view synthesis | [📄 Paper](https://doi.org/10.1007/978-3-031-20074-8_6) |
| **MatrixCity** | Synthetic aerial and street views with reference buffers for controlled city-scale rendering tests | [📄 Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Li_MatrixCity_A_Large-scale_City_Dataset_for_City-scale_Neural_Rendering_and_ICCV_2023_paper.html) |
| **KITTI-360** | Urban observations with semantic and instance correspondence | [📄 Paper](https://www.cvlibs.net/datasets/kitti-360/) |
| **Oxford Spires** | Calibrated multimodal sequences and reference maps for geometry, localisation, and rendering | [📄 Paper](https://journals.sagepub.com/doi/10.1177/02783649251369905) |
| **Virtual KITTI / 2** | Cloned driving scenes and controlled variants for perception comparisons | [📄 Paper](https://www.cv-foundation.org/openaccess/content_cvpr_2016/html/Gaidon_Virtual_Worlds_as_CVPR_2016_paper.html) · [🔗 Paper (V2)](https://arxiv.org/abs/2001.10773v1) |
| **OpenStreetMap** | Geographic road structure used by map-driven construction pipelines | [📄 Paper](https://discovery.ucl.ac.uk/id/eprint/13849/) |

### 🧩 Asset Resources

Object resources compared within construction and perception pipelines.

| Resource | Purpose | Links |
| :--- | :--- | :--- |
| **LiDARsim assets** | Reconstructed objects and CAD vehicles compared in perception experiments | [📄 Paper](https://arxiv.org/abs/2006.09348) |
| **Objaverse** | Annotated reusable 3D objects for retrieval and assembly | [📄 Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Deitke_Objaverse_A_Universe_of_Annotated_3D_Objects_CVPR_2023_paper.html) |
| **GenAssets** | Generated foreground assets and fixed-layout actor replacements | [📄 Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_GenAssets_Generating_in-the-wild_3D_Assets_in_Latent_Space_CVPR_2025_paper.html) |

### 🔌 Runtime Integration

Methods that connect construction outputs to rendering, sensor operators, and simulator state.

| Resource | Purpose | Links |
| :--- | :--- | :--- |
| **UE4-NeRF** | Neural scene conversion to engine rasterization with rendering proxies and level-of-detail management | [📄 Paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/b94d8b035e2183e47afef9e2f299ba47-Abstract-Conference.html) |
| **AlignMiF** | Cross-modal geometry alignment with modality-specific details | [📄 Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Tao_AlignMiF_Geometry-Aligned_Multimodal_Implicit_Field_for_LiDAR-Camera_Joint_Synthesis_CVPR_2024_paper.html) |
| **Uni-Gaussians** | Camera rasterization and LiDAR ray tracing of a shared dynamic Gaussian scene | [📄 Paper](https://arxiv.org/abs/2503.08317v3) |
| **CARLA-GS** | CARLA-controlled actor motion transferred to StreetGaussians scene state | [📄 Paper](https://arxiv.org/abs/2607.07601v1) |

### 📊 Evaluation Frameworks

View extrapolation, world-generation control, policy learning, and scenario-based safety evaluation.

| Resource | Purpose | Links |
| :--- | :--- | :--- |
| **EUVS** | Separate interpolation from translation, rotation, and combined viewpoint extrapolation | [📄 Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Han_Extrapolated_Urban_View_Synthesis_Benchmark_ICCV_2025_paper.html) |
| **WorldScore** | Controllability, quality, and dynamics under standardized camera trajectories and semantic controls | [📄 Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Duan_WorldScore_A_Unified_Evaluation_Benchmark_for_World_Generation_ICCV_2025_paper.html) |
| **NeuroNCAP** | Scenario-based safety tests with policy actions and subsequent rendered observations | [📄 Paper](https://doi.org/10.1007/978-3-031-73404-5_10) |
| **RAD** | Policy learning in reconstructed Gaussian environments; other actors follow logged trajectories in the reviewed experiments | [📄 Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2ed3a566a0af6dcec424b988f1880ecc-Abstract-Conference.html) |

### 📏 Response References

Measurements or external model outputs used to assess environmental and vehicle responses.

| Resource | Purpose | Links |
| :--- | :--- | :--- |
| **WindSeer measurements** | Field measurements used to assess wind prediction | [📄 Paper](https://doi.org/10.1038/s41467-024-47778-4) |
| **CarSim** | Vehicle-response reference; the reviewed muSync-GS experiments use CarSim 2022.1 | [🔗 Product](https://www.carsim.com/products/carsim/) |


---

<a id="contributing"></a>

## 🤝 Contributing

Suggestions and corrections are welcome through [Issues](https://github.com/liuliuyaonuli/outdoor-sim-construction-survey/issues) or pull requests. To suggest a paper, include its title, paper link, and relevant topic.

<div align="center">

🌱 **Create** &nbsp; · &nbsp; 🧭 **Recover** &nbsp; · &nbsp; 🛠️ **Transform**

[↑ Back to top](#top)

</div>
