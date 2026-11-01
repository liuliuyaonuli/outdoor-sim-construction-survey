<a id="top"></a>

<div align="center">

# 🌍 Outdoor 3D Simulation<br>Environment Construction Survey

**Automated Construction of Outdoor 3D Simulation Environments for Autonomous Systems**

面向自主系统的室外三维仿真环境自动构建

**🚗 Autonomous Driving &nbsp; · &nbsp; 🚁 Aerial Robotics &nbsp; · &nbsp; 🌲 Outdoor Worlds**

<p>
  <kbd>📚 177 entries</kbd> &nbsp;
  <kbd>🗂️ 15 topics</kbd> &nbsp;
  <kbd>🔎 25 provisional additions</kbd>
</p>

<p>
  <a href="#synthesis">🌱 Synthesis</a> &nbsp; · &nbsp;
  <a href="#reconstruction">🧭 Reconstruction</a> &nbsp; · &nbsp;
  <a href="#transformation">🛠️ Transformation</a> &nbsp; · &nbsp;
  <a href="#contributing">🤝 Contribute</a>
</p>

</div>

---

A curated reading list for building outdoor 3D simulation environments: from creating new worlds, to recovering real places, to editing existing scenes. The organization follows the three construction tasks in our survey.

本仓库沿综述的三条主线整理研究：**新环境生成 → 真实环境重建 → 现有环境变换**。点击主题展开论文；每篇论文分行展示标题、发表信息和资源链接。

<table>
<tr>
<td width="33%" valign="top">
<h3>🌱 Synthesis</h3>
<p><strong>新环境生成 · 97 entries</strong></p>
<p>Create a new environment from rules, assets, language, or learned priors.</p>
<p><sub>Diversity + constraints</sub></p>
<a href="#synthesis">Explore synthesis →</a>
</td>
<td width="33%" valign="top">
<h3>🧭 Reconstruction</h3>
<p><strong>真实环境重建 · 38 entries</strong></p>
<p>Recover a digital counterpart of a specific real place or observed state.</p>
<p><sub>Reality correspondence</sub></p>
<a href="#reconstruction">Explore reconstruction →</a>
</td>
<td width="33%" valign="top">
<h3>🛠️ Transformation</h3>
<p><strong>现有环境变换 · 42 entries</strong></p>
<p>Edit, complete, or vary an existing digital environment.</p>
<p><sub>Change + preservation</sub></p>
<a href="#transformation">Explore transformation →</a>
</td>
</tr>
</table>

<a id="contents"></a>

## 🗂️ Explore the Collection

<details>
<summary><strong>📑 Full topic index — choose a research direction</strong></summary>


- [🌱 **1. Synthesis of New Environments**](#synthesis)
  - [🌳 1.1 Procedural Landscapes, Maps, and Simulation Platforms](#synthesis-procedural) · 18 entries
  - [🤖 1.2 Language-Driven and Agentic World Construction](#synthesis-agentic) · 18 entries
  - [🌐 1.3 Learned Outdoor and Driving World Generation](#synthesis-learned) · 18 entries
  - [🚦 1.4 Traffic Scenarios, Synthetic Data, and Task Generation](#synthesis-scenarios) · 17 entries
  - [🌬️ 1.5 Synthetic Wind Fields and Aerial Simulation](#synthesis-wind) · 4 entries
  - [🛋️ 1.6 Related Indoor and Manipulation Scene Synthesis](#synthesis-indoor) · 22 entries

- [🧭 **2. Reconstruction of Real Environments**](#reconstruction)
  - [🚗 2.1 Driving Scene Reconstruction and Neural Simulation](#reconstruction-driving) · 20 entries
  - [🚁 2.2 Real-to-Sim for Navigation, Locomotion, and Flight](#reconstruction-robotics) · 6 entries
  - [🗺️ 2.3 Geospatial, Facility, and Environmental State Reconstruction](#reconstruction-geospatial) · 6 entries
  - [🧩 2.4 Related Indoor, Asset, and Navigability Reconstruction](#reconstruction-related) · 6 entries

- [🛠️ **3. Transformation of Existing Environments**](#transformation)
  - [🧱 3.1 Scene Completion, Inpainting, and Geometric Refinement](#transformation-completion) · 7 entries
  - [✏️ 3.2 Object Editing, Agentic Authoring, and Editable Simulation](#transformation-editing) · 14 entries
  - [🌦️ 3.3 Weather, Lighting, and Environmental Appearance Editing](#transformation-weather) · 11 entries
  - [🌬️ 3.4 Wind Field Adaptation and Sensor Domain Transformation](#transformation-state) · 5 entries
  - [🎭 3.5 Related Actor, Interaction, and Road Graph Transformation](#transformation-related) · 5 entries

- [🔎 Boundary candidates](#boundary-candidates)
- [📝 Collection notes](#collection-notes)
- [🤝 Contributing](#contributing)

</details>

<a id="about-the-survey"></a>

### 📖 How to Read

**📄 Paper** · **💻 Code** · **🌐 Project** · **🗃️ Dataset**

Entries are grouped by topic, then by year, newest first. **†** identifies the 25 provisional additions from the October 2026 supplement. Scope labels identify related indoor, asset, scenario/data, wind, road graph, and video-output work. Resource types are shown separately; a missing link has not yet been established for the collection.

<details>
<summary>📊 Coverage and classification notes</summary>

| Construction task | Existing | Provisional † | Total |
| :--- | ---: | ---: | ---: |
| 🌱 Synthesis | 86 | 11 | **97** |
| 🧭 Reconstruction | 29 | 9 | **38** |
| 🛠️ Transformation | 37 | 5 | **42** |
| **📚 All three tasks** | **152** | **25** | **177** |

Classification follows the main construction objective and its reference relationship: **conditions and constraints** for synthesis, **a specific real target** for reconstruction, and **the input scene plus requested changes and preserved content** for transformation. Hybrid systems appear once under their recorded primary task.

The counts describe registered entries, including related methods and provisional additions. Seven boundary candidates are listed separately. Provisional entries still require review of their task assignment and inclusion.

</details>


---

<a id="synthesis"></a>

## 🌱 1. Synthesis of New Environments

Create new environmental content and spatial structure through procedural rules, asset composition, language-guided programs, or learned priors.

**📚 97 entries** &nbsp;·&nbsp; [↑ Back to collection index](#contents)

<a id="synthesis-procedural"></a>

### 🌳 1.1 Procedural Landscapes, Maps, and Simulation Platforms

<details open>
<summary><strong>📚 Browse 18 entries</strong> · 1998–2026</summary>


#### 2026

- **3D Environment Generation from Sparse Inputs for Automated Driving Function Development** <sup>†</sup><br>
  <sub>Vehicles 2026</sub> · [📄 Paper](https://www.preprints.org/manuscript/202601.0011)

- **AirNavigation: Let UAV Navigation Tell Its Own Story**<br>
  <sub>AAAI Demo 2026</sub> · [📄 Paper](https://ojs.aaai.org/index.php/AAAI/article/view/42356) · [💻 Code](https://github.com/1e12Leon/AirNavigation)

- **An Efficient Simulation Scene Generation Method Based on Extracted Road Network Topology and Large Language Models**<br>
  <sub>Future Transportation 2026</sub> · [📄 Paper](https://doi.org/10.3390/futuretransp6020081)

- **LandCraft: Designing the Structured 3D Landscapes via Text Guidance**<br>
  <sub>AAAI 2026</sub> · [📄 Paper](https://ojs.aaai.org/index.php/AAAI/article/view/37686)

- **LLM-Driven 3D Scene Generation of Agricultural Simulation Environments** <sup>†</sup><br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2602.11706)

- **RoadWeaver: Large-Scale Lane-Level HD Map Generation from Scratch for Autonomous Driving Simulation**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2608.11580)


#### 2025

- **FlightForge: Advancing UAV Research Through Procedural Generation with High-Fidelity Simulation and Integrated Autonomy**<br>
  <sub>ICRA 2025</sub> · [📄 Paper](https://arxiv.org/abs/2502.05038)

- **InfiniteDiffusion: Bridging Learned Fidelity and Procedural Utility for Open-World Terrain Generation** <sup>†</sup><br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2512.08309)

- **MESA: Text-Driven Terrain Generation Using Latent Diffusion and Global Copernicus Data** <sup>†</sup><br>
  <sub>CVPR MORSE Workshop 2025</sub> · [📄 Paper](https://arxiv.org/abs/2504.07210) · [💻 Code](https://github.com/PaulBorneP/MESA)

- **Towards Autonomous Micromobility through Scalable Urban Simulation**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2505.00690) · [🌐 Project](https://metadriverse.github.io/urban-sim/)


#### 2024

- **Digital-PV: A digital twin-based platform for autonomous aerial monitoring of large-scale photovoltaic power plants**<br>
  <sub>Energy Conversion and Management 2024</sub> · [📄 Paper](https://doi.org/10.1016/j.enconman.2024.118963)

- **MetaUrban: An Embodied AI Simulation Platform for Urban Micromobility**<br>
  <sub>Technical report 2024</sub> · [📄 Paper](https://arxiv.org/abs/2407.08725) · [🌐 Project](https://metadriverse.github.io/metaurban)


#### 2022

- **Procedural Generation and Rendering of Realistic, Navigable Forest Environments: An Open-Source Tool**<br>
  <sub>arXiv 2022</sub> · [📄 Paper](https://arxiv.org/abs/2208.01471) · [💻 Code](https://github.com/callumnewlands/ForestGenerator)


#### 2020

- **AirSim Drone Racing Lab**<br>
  <sub>PMLR 2020</sub> · [📄 Paper](https://proceedings.mlr.press/v123/madaan20a.html) · [💻 Code](https://github.com/microsoft/AirSim-NeurIPS2019-Drone-Racing)


#### 2013

- **Terrain Generation Using Procedural Models Based on Hydrology**<br>
  <sub>ACM TOG 2013</sub> · [📄 Paper](https://doi.org/10.1145/2461912.2461996)


#### 2006

- **Procedural Modeling of Buildings**<br>
  <sub>SIGGRAPH 2006</sub> · [📄 Paper](https://doi.org/10.1145/1179352.1141931) · <sub>🧩 Asset</sub>


#### 2001

- **Procedural Modeling of Cities**<br>
  <sub>SIGGRAPH 2001</sub> · [📄 Paper](https://doi.org/10.1145/383259.383292)


#### 1998

- **Realistic Modeling and Rendering of Plant Ecosystems**<br>
  <sub>SIGGRAPH 1998</sub> · [📄 Paper](https://doi.org/10.1145/280814.280898)


</details>


<a id="synthesis-agentic"></a>

### 🤖 1.2 Language-Driven and Agentic World Construction

<details>
<summary><strong>📚 Browse 18 entries</strong> · 2023–2026</summary>


#### 2026

- **AutoUE: Automated Generation of 3D Games in Unreal Engine via Multi-Agent Systems**<br>
  <sub>Findings of ACL 2026</sub> · [📄 Paper](https://aclanthology.org/2026.findings-acl.111/)

- **Imagine a City: CityGenAgent for Procedural 3D City Generation**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2602.05362)

- **MAGIC: Transition-Aware Generation of Navigable Multi-Scene Game Worlds with Large Language Models**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2607.11594) · [💻 Code](https://github.com/sereneee1201/MAGIC/)

- **PhyScensis: Physics-Augmented LLM Agents for Complex Physical Scene Arrangement**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2602.14968) · <sub>🛋️ Related indoor</sub>

- **Scenethesis: Combining Language and Visual Priors for 3D Scene Generation**<br>
  <sub>ICLR 2026</sub> · [📄 Paper](https://openreview.net/forum?id=SzhezVoaNB) · [🌐 Project](https://research.nvidia.com/labs/dir/scenethesis/) · <sub>🏘️ Indoor / outdoor</sub>

- **SIMWORLD STUDIO: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2605.09423) · [🌐 Project](https://simworld.org/simworld-studio/) · <sub>🛋️ Related indoor</sub>

- **WorldClaw: Agentic 3D Open-World Generation at Scale** <sup>†</sup><br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2608.05248) · [🌐 Project](https://tencent-hunyuan.github.io/Hunyuan3D-WorldClaw)


#### 2025

- **3D-GENERALIST: Vision-Language-Action Models for Crafting 3D Worlds**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2507.06484) · <sub>🏘️ Indoor / outdoor</sub>

- **HOLODECK 2.0: Vision-Language-Guided 3D World Generation with Editing**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2508.05899) · <sub>🏘️ Indoor / outdoor</sub>

- **LatticeWorld: A Multimodal Large Language Model-Empowered Framework for Interactive Complex World Generation** <sup>†</sup><br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2509.05263)

- **MajutsuCity: Language-Driven Aesthetic-Adaptive City Generation with Controllable 3D Assets and Layouts**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2511.20415) · [🌐 Project](https://longhz140516.github.io/MajutsuCity/)

- **SCENEWEAVER: All-in-One 3D Scene Synthesis with an Extensible and Self-Reflective Agent**<br>
  <sub>NeurIPS 2025</sub> · [📄 Paper](https://arxiv.org/abs/2509.20414) · [🌐 Project](https://scene-weaver.github.io/) · <sub>🛋️ Related indoor</sub>

- **SceneX: Procedural Controllable Large-Scale Scene Generation**<br>
  <sub>AAAI 2025</sub> · [📄 Paper](https://arxiv.org/abs/2403.15698) · [🌐 Project](https://zhouzq1.github.io/SceneX/)

- **UnrealLLM: Towards Highly Controllable and Interactable 3D Scene Generation by LLM-powered Procedural Content Generation** <sup>†</sup><br>
  <sub>Findings of ACL 2025</sub> · [📄 Paper](https://aclanthology.org/2025.findings-acl.994/)

- **WorldCraft: Photo-Realistic 3D World Creation and Customization via LLM Agents**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2502.15601) · <sub>🏘️ Indoor / outdoor</sub>

- **Yo’City: Personalized and Boundless 3D Realistic City Scene Generation via Self-Critic Expansion**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2511.18734)


#### 2024

- **CityX: Controllable Procedural Content Generation for Unbounded 3D Cities**<br>
  <sub>arXiv 2024</sub> · [📄 Paper](https://arxiv.org/abs/2407.17572)


#### 2023

- **3D-GPT: Procedural 3D Modeling with Large Language Models**<br>
  <sub>arXiv 2023</sub> · [📄 Paper](https://arxiv.org/abs/2310.12945) · [🌐 Project](https://chuny1.github.io/3DGPT/3dgpt.html) · <sub>🏘️ Indoor / outdoor</sub>


</details>


<a id="synthesis-learned"></a>

### 🌐 1.3 Learned Outdoor and Driving World Generation

<details>
<summary><strong>📚 Browse 18 entries</strong> · 2025–2026</summary>


#### 2026

- **AeroScene: Progressive Scene Synthesis for Aerial Robotics**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2603.23224)

- **HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2604.14268) · [💻 Code](https://github.com/Tencent-Hunyuan/HY-World-2.0)

- **SCENEFOUNDRY: Generating Interactive Infinite 3D Worlds**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2601.05810) · <sub>🛋️ Related indoor</sub>

- **WorldFlow3D: Flowing Through 3D Distributions for Unbounded World Generation**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2603.29089) · [🌐 Project](https://light.princeton.edu/worldflow3d) · <sub>🏘️ Indoor / outdoor</sub>


#### 2025

- **Controllable 3D Outdoor Scene Generation via Scene Graphs** <sup>†</sup><br>
  <sub>ICCV 2025</sub> · [📄 Paper](https://arxiv.org/abs/2503.07152) · [💻 Code](https://github.com/yuhengliu02/control-3d-scene)

- **DRIVEARENA: A Closed-Loop Generative Simulation Platform for Autonomous Driving**<br>
  <sub>ICCV 2025</sub> · [📄 Paper](https://arxiv.org/abs/2408.00415) · [🌐 Project](https://pjlab-adg.github.io/DriveArena/)

- **EmbodiedGen: Towards a Generative 3D World Engine for Embodied Intelligence**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2506.10600) · <sub>🛋️ Related indoor</sub> · <sub>🧩 Asset</sub>

- **Generative Gaussian Splatting for Unbounded 3D City Generation**<br>
  <sub>CVPR 2025</sub> · [📄 Paper](https://arxiv.org/abs/2406.06526) · [🌐 Project](https://haozhexie.com/project/gaussian-city)

- **HiScene: Creating Hierarchical 3D Scenes with Isometric View Generation**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2504.13072) · [🌐 Project](https://zju3dv.github.io/hiscene/) · <sub>🛋️ Related indoor</sub>

- **HunyuanWorld 1.0: Generating Immersive, Explorable, and Interactive 3D Worlds from Words or Pixels**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2507.21809) · [💻 Code](https://github.com/Tencent-Hunyuan/HunyuanWorld-1.0) · <sub>🏘️ Indoor / outdoor</sub>

- **InfiniCube: Unbounded and Controllable Dynamic 3D Driving Scene Generation with World-Guided Video Models**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2412.03934) · [🌐 Project](https://research.nvidia.com/labs/toronto-ai/infinicube/)

- **Large Scene Generation with Cube-Absorb Discrete Diffusion**<br>
  <sub>ICCV 2025</sub> · [📄 Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Hu_Large_Scene_Generation_with_Cube-Absorb_Discrete_Diffusion_ICCV_2025_paper.html)

- **NuiScene: Exploring Efficient Generation of Unbounded Outdoor Scenes** <sup>†</sup><br>
  <sub>ICCV 2025</sub> · [📄 Paper](https://arxiv.org/abs/2503.16375) · [🗃️ Dataset](https://github.com/3dlg-hcvc/NuiScene43-Dataset)

- **Steerable Scene Generation with Post Training and Inference-Time Search**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2505.04831) · [🌐 Project](https://steerable-scene-generation.github.io/) · <sub>🛋️ Related indoor</sub>

- **UniScene: Unified Occupancy-centric Driving Scene Generation** <sup>†</sup><br>
  <sub>CVPR 2025</sub> · [📄 Paper](https://arxiv.org/abs/2412.05435)

- **WonderWorld: Interactive 3D Scene Generation from a Single Image**<br>
  <sub>CVPR 2025</sub> · [📄 Paper](https://arxiv.org/abs/2406.09394) · [🌐 Project](https://kovenyu.com/WonderWorld/) · <sub>🏘️ Indoor / outdoor</sub>

- **WorldGen: From Text to Traversable and Interactive 3D Worlds**<br>
  <sub>Technical report 2025</sub> · [📄 Paper](https://arxiv.org/abs/2511.16825) · <sub>🏘️ Indoor / outdoor</sub>

- **X-Scene: Large-Scale Driving Scene Generation with High Fidelity and Flexible Controllability** <sup>†</sup><br>
  <sub>NeurIPS 2025</sub> · [📄 Paper](https://arxiv.org/abs/2506.13558)


</details>


<a id="synthesis-scenarios"></a>

### 🚦 1.4 Traffic Scenarios, Synthetic Data, and Task Generation

<details>
<summary><strong>📚 Browse 17 entries</strong> · 2019–2025</summary>


#### 2025

- **DriveGen: Towards Infinite Diverse Traffic Scenarios with Large Models**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2503.05808) · <sub>🚦 Scenario / data</sub>

- **Generating Traffic Scenarios via In-Context Learning to Learn Better Motion Planner**<br>
  <sub>AAAI 2025</sub> · [📄 Paper](https://arxiv.org/abs/2412.18086) · [🌐 Project](https://ezharjan.github.io/AutoSceneGen) · <sub>🚦 Scenario / data</sub>

- **LMM-Enhanced Safety-Critical Scenario Generation for Autonomous Driving System Testing from Non-Accident Traffic Videos**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2406.10857) · <sub>🚦 Scenario / data</sub>

- **Text2Scenario: Text-Driven Scenario Generation for Autonomous Driving Test**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2503.02911) · [🌐 Project](https://caixxuan.github.io/Text2Scenario.GitHub.io/) · <sub>🚦 Scenario / data</sub>


#### 2024

- **ChatScene: Knowledge-Enabled Safety-Critical Scenario Generation for Autonomous Vehicles**<br>
  <sub>CVPR 2024</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_ChatScene_Knowledge-Enabled_Safety-Critical_Scenario_Generation_for_Autonomous_Vehicles_CVPR_2024_paper.html) · [💻 Code](https://github.com/javyduck/ChatScene) · <sub>🚦 Scenario / data</sub>

- **ChatSUMO: Large Language Model for Automating Traffic Scenario Generation in Simulation of Urban MObility**<br>
  <sub>arXiv 2024</sub> · [📄 Paper](https://arxiv.org/abs/2409.09040) · <sub>🚦 Scenario / data</sub>

- **Environment Curriculum Generation via Large Language Models**<br>
  <sub>arXiv 2024</sub> · [📄 Paper](https://arxiv.org/abs/2411.01775) · [🌐 Project](https://eureka-research.github.io/eurekaverse/) · <sub>🚦 Scenario / data</sub>

- **Generating Out-Of-Distribution Scenarios Using Language Models**<br>
  <sub>arXiv 2024</sub> · [📄 Paper](https://arxiv.org/abs/2411.16554) · <sub>🚦 Scenario / data</sub>

- **LeGEND: A Top-Down Approach to Scenario Generation of Autonomous Driving Systems Assisted by Large Language Models**<br>
  <sub>arXiv 2024</sub> · [📄 Paper](https://arxiv.org/abs/2409.10066) · <sub>🚦 Scenario / data</sub>

- **Realistic Corner Case Generation for Autonomous Vehicles with Multimodal Large Language Model**<br>
  <sub>arXiv 2024</sub> · [📄 Paper](https://arxiv.org/abs/2412.00243) · <sub>🚦 Scenario / data</sub>

- **SceneDiffuser: Efficient and Controllable Driving Simulation Initialization and Rollout**<br>
  <sub>NeurIPS 2024</sub> · [📄 Paper](https://arxiv.org/abs/2412.12129) · <sub>🚦 Scenario / data</sub>

- **SoVAR: Building Generalizable Scenarios from Accident Reports for Autonomous Driving Testing**<br>
  <sub>ASE 2024</sub> · [📄 Paper](https://arxiv.org/abs/2409.08081) · [💻 Code](https://github.com/meng2180/SoVAR) · <sub>🚦 Scenario / data</sub>

- **Traffic Scene Generation from Natural Language Description for Autonomous Vehicles with Large Language Model**<br>
  <sub>arXiv 2024</sub> · [📄 Paper](https://arxiv.org/abs/2409.09575) · [🌐 Project](https://basiclab.github.io/TTSG) · <sub>🚦 Scenario / data</sub>


#### 2023

- **Language Conditioned Traffic Generation**<br>
  <sub>arXiv 2023</sub> · [📄 Paper](https://arxiv.org/abs/2307.07947) · [🌐 Project](https://ariostgx.github.io/lctgen) · <sub>🚦 Scenario / data</sub>

- **TARGET: Traffic Rule-Based Test Generation for Autonomous Driving via Validated LLM-Guided Knowledge Extraction**<br>
  <sub>arXiv 2023</sub> · [📄 Paper](https://arxiv.org/abs/2305.06018) · <sub>🚦 Scenario / data</sub>


#### 2020

- **Meta-Sim2: Unsupervised Learning of Scene Structure for Synthetic Data Generation**<br>
  <sub>ECCV 2020</sub> · [📄 Paper](https://arxiv.org/abs/2008.09092) · [🌐 Project](https://nv-tlabs.github.io/meta-sim-structure/) · <sub>🚦 Scenario / data</sub>


#### 2019

- **Meta-Sim: Learning to Generate Synthetic Datasets**<br>
  <sub>CVPR 2019</sub> · [📄 Paper](https://arxiv.org/abs/1904.11621) · <sub>🚦 Scenario / data</sub>


</details>


<a id="synthesis-wind"></a>

### 🌬️ 1.5 Synthetic Wind Fields and Aerial Simulation

<details>
<summary><strong>📚 Browse 4 entries</strong> · 2019–2026</summary>


#### 2026

- **A Simulation Platform for Flapping-Wing Vehicles**<br>
  <sub>Manuscript 2026</sub> · [📄 Paper](https://arxiv.org/abs/2606.02370) · <sub>🌬️ Wind</sub>

- **Physics Informed Reconstruction of Four-Dimensional Atmospheric Wind Fields Using Multi-UAS Swarm Observations in a Synthetic Turbulent Environment**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2601.22111) · <sub>🌬️ Wind</sub>


#### 2025

- **Urban Wind Field Effects on the Flight Dynamics of Fixed-Wing Drones**<br>
  <sub>Drones 2025</sub> · [📄 Paper](https://doi.org/10.3390/drones9050362) · <sub>🌬️ Wind</sub>


#### 2019

- **Quad-rotor Flight Simulation in Realistic Atmospheric Conditions**<br>
  <sub>arXiv 2019</sub> · [📄 Paper](https://arxiv.org/abs/1902.01465) · <sub>🌬️ Wind</sub>


</details>


<a id="synthesis-indoor"></a>

### 🛋️ 1.6 Related Indoor and Manipulation Scene Synthesis

<details>
<summary><strong>📚 Browse 22 entries</strong> · 2021–2026</summary>


#### 2026

- **MANSION: Multi-floor lANguage-to-3D Scene generatIOn for loNg-horizon Tasks**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2603.11554) · <sub>🛋️ Related indoor</sub>

- **MolmoSpaces: A Large-Scale Open Ecosystem for Robot Navigation and Manipulation**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2602.11337) · [💻 Code](https://github.com/allenai/molmospaces) · <sub>🛋️ Related indoor</sub>

- **SAGE: Scalable Agentic 3D Scene Generation for Embodied AI**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2602.10116) · <sub>🛋️ Related indoor</sub>

- **SceneCode: Executable World Programs for Editable Indoor Scenes with Articulated Objects**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2605.19587) · [🌐 Project](https://scene-code.github.io/) · <sub>🛋️ Related indoor</sub>

- **SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes**<br>
  <sub>ICML 2026</sub> · [📄 Paper](https://arxiv.org/abs/2602.09153) · [🌐 Project](https://scenesmith.github.io/) · <sub>🛋️ Related indoor</sub>


#### 2025

- **ArtiScene: Language-Driven Artistic 3D Scene Generation Through Image Intermediary**<br>
  <sub>CVPR 2025</sub> · [📄 Paper](https://arxiv.org/abs/2506.00742) · [🌐 Project](https://research.nvidia.com/labs/dir/artiscene/) · <sub>🛋️ Related indoor</sub>

- **DynScene: Scalable Generation of Dynamic Robotic Manipulation Scenes for Embodied AI**<br>
  <sub>CVPR 2025</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Lee_DynScene_Scalable_Generation_of_Dynamic_Robotic_Manipulation_Scenes_for_Embodied_CVPR_2025_paper.html) · <sub>🛋️ Related indoor</sub>

- **EmbodiedScene: Towards Automated Generation of Diverse and Realistic Scenes for Embodied AI**<br>
  <sub>Manuscript 2025</sub> · [🌐 Project](https://embodiedscene1.github.io/embodied.scene/) · <sub>🛋️ Related indoor</sub>

- **MarketGen: A Scalable Simulation Platform with Auto-Generated Embodied Supermarket Environments**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2511.21161) · [🌐 Project](https://xuhu0529.github.io/MarketGen) · <sub>🛋️ Related indoor</sub>

- **MesaTask: Towards Task-Driven Tabletop Scene Generation via 3D Spatial Reasoning**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2509.22281) · <sub>🛋️ Related indoor</sub>

- **PAT3D: Physics-Augmented Text-to-3D Scene Generation**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2511.21978) · <sub>🛋️ Related indoor</sub>

- **TabletopGen: Tabletop Scene Generation and Interactive Simulation for Robotic Manipulation**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2512.01204) · [🌐 Project](https://d-robotics-ai-lab.github.io/TabletopGen.project/) · <sub>🛋️ Related indoor</sub>


#### 2024

- **Gen2Sim: Scaling up Robot Learning in Simulation with Generative Models**<br>
  <sub>ICRA 2024</sub> · [📄 Paper](https://arxiv.org/abs/2310.18308) · [🌐 Project](https://gen2sim.github.io/) · <sub>🛋️ Related indoor</sub>

- **GenSim2: Scaling Robot Data Generation with Multi-modal and Reasoning LLMs**<br>
  <sub>arXiv 2024</sub> · [📄 Paper](https://arxiv.org/abs/2410.03645) · [🌐 Project](https://gensim2.github.io/) · <sub>🛋️ Related indoor</sub>

- **HOLODECK: Language Guided Generation of 3D Embodied AI Environments**<br>
  <sub>CVPR 2024</sub> · [📄 Paper](https://arxiv.org/abs/2312.09067) · <sub>🛋️ Related indoor</sub>

- **I-Design: Personalized LLM Interior Designer**<br>
  <sub>arXiv 2024</sub> · [📄 Paper](https://arxiv.org/abs/2404.02838) · [🌐 Project](https://atcelen.github.io/I-Design/) · <sub>🛋️ Related indoor</sub>

- **InfiniteWorld: A Unified Scalable Simulation Framework for General Visual-Language Robot Interaction**<br>
  <sub>arXiv 2024</sub> · [📄 Paper](https://arxiv.org/abs/2412.05789) · [💻 Code](https://github.com/pzhren/InfiniteWorld) · <sub>🛋️ Related indoor</sub>

- **PHYSCENE: Physically Interactable 3D Scene Synthesis for Embodied AI**<br>
  <sub>arXiv 2024</sub> · [📄 Paper](https://arxiv.org/abs/2404.09465) · [🌐 Project](https://physcene.github.io) · <sub>🛋️ Related indoor</sub>

- **RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation**<br>
  <sub>ICML 2024</sub> · [📄 Paper](https://arxiv.org/abs/2311.01455) · [🌐 Project](https://robogen-ai.github.io/) · <sub>🛋️ Related indoor</sub>

- **SceneCraft: An LLM Agent for Synthesizing 3D Scene as Blender Code**<br>
  <sub>arXiv 2024</sub> · [📄 Paper](https://arxiv.org/abs/2403.01248) · <sub>🛋️ Related indoor</sub>


#### 2022

- **ProcTHOR: Large-Scale Embodied AI Using Procedural Generation**<br>
  <sub>NeurIPS 2022</sub> · [📄 Paper](https://arxiv.org/abs/2206.06994) · <sub>🛋️ Related indoor</sub>


#### 2021

- **LUMINOUS: Indoor Scene Generation for Embodied AI Challenges**<br>
  <sub>NeurIPS Workshop 2021</sub> · [📄 Paper](https://arxiv.org/abs/2111.05527) · <sub>🛋️ Related indoor</sub>


</details>


---

<a id="reconstruction"></a>

## 🧭 2. Reconstruction of Real Environments

Recover a specific real environment from maps, imagery, scans, or other observations, including geometry, appearance, dynamics, and local environmental states.

**📚 38 entries** &nbsp;·&nbsp; [↑ Back to collection index](#contents)

<a id="reconstruction-driving"></a>

### 🚗 2.1 Driving Scene Reconstruction and Neural Simulation

<details open>
<summary><strong>📚 Browse 20 entries</strong> · 2020–2026</summary>


#### 2026

- **Cam2Sim: Neural Scenario Reconstruction for Closed-Loop Autonomous Driving Simulation**<br>
  <sub>ASE 2026</sub> · [📄 Paper](https://arxiv.org/abs/2607.04770)

- **HybridWorldSim: A Scalable and Controllable High-fidelity Simulator for Autonomous Driving**<br>
  <sub>ACM MM 2026</sub> · [📄 Paper](https://arxiv.org/abs/2511.22187)

- **Instant NuRec: Feed-Forward 3D Gaussian Reconstruction for Driving Scene Simulation**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2607.14203) · [🌐 Project](https://research.nvidia.com/labs/sil/projects/instant-nurec) · [💻 Code](https://github.com/nvidia/instant-nurec)

- **Nighttime Autonomous Driving Scene Reconstruction with Physically-Based Gaussian Splatting** <sup>†</sup><br>
  <sub>ICRA 2026</sub> · [📄 Paper](https://arxiv.org/abs/2602.13549)

- **NimbusGS: Unified 3D Scene Reconstruction under Hybrid Weather** <sup>†</sup><br>
  <sub>CVPR 2026</sub> · [📄 Paper](https://arxiv.org/abs/2603.27228)

- **ReconDrive: Fast Feed-Forward 4D Gaussian Splatting for Autonomous Driving Scene Reconstruction** <sup>†</sup><br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2603.07552)

- **UniGaussian: Driving Scene Reconstruction from Multiple Camera Models via Unified Gaussian Representations** <sup>†</sup><br>
  <sub>3DV 2026</sub> · [📄 Paper](https://arxiv.org/abs/2411.15355)

- **Urban-GS: A Unified 3D Gaussian Splatting Framework for Compact and High-Fidelity Aerial-to-Street Reconstruction**<br>
  <sub>CVPR 2026</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Urban-GS_A_Unified_3D_Gaussian_Splatting_Framework_for_Compact_and_CVPR_2026_paper.pdf)


#### 2025

- **3D StreetUnveiler with Semantic-Aware 2DGS - A Simple Baseline**<br>
  <sub>ICLR 2025</sub> · [📄 Paper](https://arxiv.org/abs/2405.18416) · [🌐 Project](https://streetunveiler.github.io)

- **DrivingRecon: Large 4D Gaussian Reconstruction Model For Autonomous Driving** <sup>†</sup><br>
  <sub>NeurIPS 2025</sub> · [📄 Paper](https://arxiv.org/abs/2412.09043) · [💻 Code](https://github.com/EnVision-Research/DriveRecon)

- **DrivingSphere: Building a High-Fidelity 4D World for Closed-Loop Simulation**<br>
  <sub>CVPR 2025</sub> · [📄 Paper](https://arxiv.org/abs/2411.11252)

- **RealEngine: Simulating Autonomous Driving in Realistic Context**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2505.16902) · [💻 Code](https://github.com/fudan-zvg/RealEngine)

- **ReconDreamer++: Harmonizing Generative and Reconstructive Models for Driving Scene Representation** <sup>†</sup><br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2503.18438)

- **ReconDreamer: Crafting World Models for Driving Scene Reconstruction via Online Restoration** <sup>†</sup><br>
  <sub>CVPR 2025</sub> · [📄 Paper](https://arxiv.org/abs/2411.19548)

- **SplatAD: Real-Time Lidar and Camera Rendering with 3D Gaussian Splatting for Autonomous Driving** <sup>†</sup><br>
  <sub>CVPR 2025</sub> · [📄 Paper](https://arxiv.org/abs/2411.16816) · [💻 Code](https://github.com/carlinds/splatad)

- **WeatherGS: 3D Scene Reconstruction in Adverse Weather Conditions via Gaussian Splatting** <sup>†</sup><br>
  <sub>ICRA 2025</sub> · [📄 Paper](https://arxiv.org/abs/2412.18862) · [💻 Code](https://github.com/Jumponthemoon/WeatherGS)


#### 2024

- **HUGSIM: A Real-Time, Photo-Realistic and Closed-Loop Simulator for Autonomous Driving**<br>
  <sub>arXiv 2024</sub> · [📄 Paper](https://arxiv.org/abs/2412.01718) · [🌐 Project](https://xdimlab.github.io/HUGSIM)

- **ReSimAD: Zero-Shot 3D Domain Transfer for Autonomous Driving with Source Reconstruction and Target Simulation**<br>
  <sub>arXiv 2024</sub> · [📄 Paper](https://arxiv.org/abs/2309.05527) · [💻 Code](https://github.com/PJLab-ADG/3DTrans)


#### 2023

- **NeuRAD: Neural Rendering for Autonomous Driving**<br>
  <sub>arXiv 2023</sub> · [📄 Paper](https://arxiv.org/abs/2311.15260)


#### 2020

- **LiDARsim: Realistic LiDAR Simulation by Leveraging the Real World**<br>
  <sub>arXiv 2020</sub> · [📄 Paper](https://arxiv.org/abs/2006.09348)


</details>


<a id="reconstruction-robotics"></a>

### 🚁 2.2 Real-to-Sim for Navigation, Locomotion, and Flight

<details>
<summary><strong>📚 Browse 6 entries</strong> · 2024–2026</summary>


#### 2026

- **NavGSim: High-Fidelity Gaussian Splatting Simulator for Large-Scale Navigation**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2603.15186) · [💻 Code](https://github.com/2003jiahang/NavGSim) · <sub>🛋️ Related indoor</sub>


#### 2025

- **GaussGym: An Open-Source Real-to-Sim Framework for Learning Locomotion from Pixels**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2510.15352) · [🌐 Project](https://escontrela.me/gauss_gym/) · <sub>🛋️ Related indoor</sub>

- **SOUS VIDE: Cooking Visual Drone Navigation Policies in a Gaussian Splatting Vacuum**<br>
  <sub>IEEE RA-L 2025</sub> · [📄 Paper](https://arxiv.org/abs/2412.16346) · [🌐 Project](https://stanfordmsl.github.io/SousVide/)

- **Vid2Sim: Realistic and Interactive Simulation from Video for Urban Navigation**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2501.06693) · [🌐 Project](https://metadriverse.github.io/vid2sim/)

- **VR-Robo: A Real-to-Sim-to-Real Framework for Visual Robot Navigation and Locomotion**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2502.01536) · <sub>🛋️ Related indoor</sub>


#### 2024

- **Gaussian Splatting to Real World Flight Navigation Transfer with Liquid Networks**<br>
  <sub>arXiv 2024</sub> · [📄 Paper](https://arxiv.org/abs/2406.15149)


</details>


<a id="reconstruction-geospatial"></a>

### 🗺️ 2.3 Geospatial, Facility, and Environmental State Reconstruction

<details>
<summary><strong>📚 Browse 6 entries</strong> · 2024–2026</summary>


#### 2026

- **Sat3DGen: Comprehensive Street-Level 3D Scene Generation from Single Satellite Image**<br>
  <sub>ICLR 2026</sub> · [📄 Paper](https://arxiv.org/abs/2605.14984) · [💻 Code](https://github.com/qianmingduowan/Sat3DGen)

- **Semi-Automated Generation of Realistic Simulation Environments from Geospatial Data for Agricultural Robot Navigation**<br>
  <sub>Computer Modeling in Engineering 2026</sub> · [📄 Paper](https://doi.org/10.32604/cmes.2026.080739)


#### 2025

- **A Simulation Environment for UAV-based Real-time Condition Monitoring of Solar Tower Power Plants**<br>
  <sub>Solar Energy 2025</sub> · [📄 Paper](https://doi.org/10.1016/j.solener.2025.113803)

- **Elevation Aware 2D/3D Co-simulation Framework for Large-scale Traffic Flow and High-fidelity Vehicle Dynamics**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2512.11249)

- **Open-Source vs. Commercial Photogrammetry: Comparing Accuracy and Efficiency of OpenDroneMap and Agisoft Metashape**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://doi.org/10.5194/isprs-archives-XLVIII-1-W4-2025-65-2025)


#### 2024

- **WindSeer: real-time volumetric wind prediction over complex terrain aboard a small uncrewed aerial vehicle**<br>
  <sub>Nature Communications 2024</sub> · [📄 Paper](https://doi.org/10.1038/s41467-024-47778-4) · <sub>🌬️ Wind</sub>


</details>


<a id="reconstruction-related"></a>

### 🧩 2.4 Related Indoor, Asset, and Navigability Reconstruction

<details>
<summary><strong>📚 Browse 6 entries</strong> · 2025–2026</summary>


#### 2026

- **SE(2) Navigation Mesh**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2607.01454) · <sub>🛋️ Related indoor</sub>

- **SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2606.28276) · [🌐 Project](https://research.nvidia.com/labs/gear/simfoundry/) · <sub>🛋️ Related indoor</sub>


#### 2025

- **EA3D: Online Open-World 3D Object Extraction from Streaming Videos**<br>
  <sub>NeurIPS 2025</sub> · [📄 Paper](https://arxiv.org/abs/2510.25146) · [💻 Code](https://github.com/VDIGPKU/EA3D) · <sub>🛋️ Related indoor</sub> · <sub>🧩 Asset</sub>

- **MetaScenes: Automated Replica Creation for Real-World 3D Scans**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2505.02388) · [🌐 Project](https://meta-scenes.github.io/) · <sub>🛋️ Related indoor</sub>

- **RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2504.13059) · [🌐 Project](https://robotwin-benchmark.github.io) · <sub>🛋️ Related indoor</sub> · <sub>🧩 Asset</sub>

- **Zero-shot Inexact CAD Model Alignment from a Single Image**<br>
  <sub>ICCV 2025</sub> · [📄 Paper](https://arxiv.org/abs/2507.03292) · [🌐 Project](https://zerocad9d.github.io/) · [💻 Code](https://github.com/pattaramaneea/ZeroCAD) · <sub>🛋️ Related indoor</sub> · <sub>🧩 Asset</sub>


</details>


---

<a id="transformation"></a>

## 🛠️ 3. Transformation of Existing Environments

Modify an existing digital environment while preserving the scene content, spatial relationships, or runtime properties required by the task.

**📚 42 entries** &nbsp;·&nbsp; [↑ Back to collection index](#contents)

<a id="transformation-completion"></a>

### 🧱 3.1 Scene Completion, Inpainting, and Geometric Refinement

<details open>
<summary><strong>📚 Browse 7 entries</strong> · 2024–2026</summary>


#### 2026

- **GSCompleter: A Distillation-Free Plugin for Metric-Aware 3D Gaussian Splatting Completion in Seconds**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2604.20155) · [🌐 Project](https://yuhuoo.github.io/projects/gscompleter/)


#### 2025

- **AuraFusion360: Augmented Unseen Region Alignment for Reference-based 360° Unbounded Scene Inpainting** <sup>†</sup><br>
  <sub>CVPR 2025</sub> · [📄 Paper](https://arxiv.org/abs/2502.05176)

- **GS-RoadPatching: Inpainting Gaussians via 3D Searching and Placing for Driving Scenes**<br>
  <sub>ACM SAP 2025</sub> · [📄 Paper](https://arxiv.org/abs/2509.19937) · [🌐 Project](https://shanzhaguoo.github.io/GS-RoadPatching/)

- **IMFine: 3D Inpainting via Geometry-guided Multi-view Refinement** <sup>†</sup><br>
  <sub>CVPR 2025</sub> · [📄 Paper](https://arxiv.org/abs/2503.04501) · [🌐 Project](https://xinxinzuo2353.github.io/imfine/)

- **InstaInpaint: Instant 3D-Scene Inpainting with Masked Large Reconstruction Model** <sup>†</sup><br>
  <sub>NeurIPS 2025</sub> · [📄 Paper](https://arxiv.org/abs/2506.10980)

- **SplatFill: 3D Scene Inpainting via Depth-Guided Gaussian Splatting** <sup>†</sup><br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2509.07809)


#### 2024

- **ARCHITECT: Generating Vivid and Interactive 3D Scenes with Hierarchical 2D Inpainting**<br>
  <sub>NeurIPS 2024</sub> · [📄 Paper](https://arxiv.org/abs/2411.09823) · [🌐 Project](https://wangyian-me.github.io/Architect/) · <sub>🛋️ Related indoor</sub>


</details>


<a id="transformation-editing"></a>

### ✏️ 3.2 Object Editing, Agentic Authoring, and Editable Simulation

<details>
<summary><strong>📚 Browse 14 entries</strong> · 2023–2026</summary>


#### 2026

- **CARLA-GS: Decoupling Representation, Reasoning, and Physics Simulation for Autonomous Driving Corner-Case Synthesis**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2607.07601)

- **DecoupleGS: Interactive 3D Gaussian Splatting for End-to-End Autonomous Driving Testing**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2608.01761)

- **HorizonForge: Driving Scene Editing with Any Trajectories and Any Vehicles** <sup>†</sup><br>
  <sub>CVPR 2026</sub> · [📄 Paper](https://arxiv.org/abs/2602.21333) · [🌐 Project](https://horizonforge.github.io/)

- **MUSE: Agentic 3D Scene Authoring via Memory-Grounded Incremental Requirement Satisfaction**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2606.14168) · [🌐 Project](https://xujay111.github.io/muse_githubio/) · <sub>🛋️ Related indoor</sub>

- **Physics-Aware 3D Gaussian Editing for Driving Scene Generation**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2605.25373)

- **Real2Sim: A Physics-driven and Editable Gaussian Splatting Framework for Autonomous Driving Scenes**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2605.13591)

- **SIMSplat: Language-Aligned 4D Gaussian Splatting for Driving Scenario Generation**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2510.02469)

- **When Digital Twins Meet Large Language Models: Realistic, Interactive, and Editable Simulation for Autonomous Driving**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2507.00319) · [🌐 Project](https://autodrive-ecosystem.github.io)


#### 2025

- **DrivingGaussian++: Towards Realistic Reconstruction and Editable Simulation for Surrounding Dynamic Driving Scenes**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2508.20965) · [🌐 Project](https://xiong-creator.github.io/DrivingGaussian_plus.github.io)

- **Performance-Guided Refinement for Visual Aerial Navigation using Editable Gaussian Splatting in FalconGym 2.0**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2510.02248)

- **R3D2: Realistic 3D Asset Insertion via Diffusion for Autonomous Driving Simulation**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2506.07826) · <sub>🧩 Asset</sub>


#### 2024

- **Editable Scene Simulation for Autonomous Driving via Collaborative LLM-Agents**<br>
  <sub>arXiv 2024</sub> · [📄 Paper](https://arxiv.org/abs/2402.05746) · [💻 Code](https://github.com/yifanlu0227/ChatSim)

- **Language-Driven Physics-Based Scene Synthesis and Editing via Feature Splatting**<br>
  <sub>ECCV 2024</sub> · [📄 Paper](https://arxiv.org/abs/2404.01223) · [🌐 Project](https://feature-splatting.github.io/) · [💻 Code](https://github.com/vuer-ai/feature-splatting-inria) · <sub>🛋️ Related indoor</sub>


#### 2023

- **UniSim: A Neural Closed-Loop Sensor Simulator**<br>
  <sub>CVPR 2023</sub> · [📄 Paper](https://www.datocms-assets.com/163962/1755204775-unisim-paper.pdf) · [🌐 Project](https://waabi.ai/research/unisim/)


</details>


<a id="transformation-weather"></a>

### 🌦️ 3.3 Weather, Lighting, and Environmental Appearance Editing

<details>
<summary><strong>📚 Browse 11 entries</strong> · 2023–2026</summary>


#### 2026

- **AutoWeather4D: Autonomous Driving Video Weather Conversion via G-Buffer Dual-Pass Editing**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2603.26546) · [🌐 Project](https://lty2226262.github.io/autoweather4d) · <sub>🎞️ Video output</sub>

- **GSRAIN: Physically Calibrated High-/Low-Frequency Rainfall Synthesis for 3D Gaussian Driving Scenes**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2608.02177)

- **Let it Snow! Animating 3D Gaussian Scenes with Dynamic Weather Effects via Physics-Guided Score Distillation**<br>
  <sub>CVPR 2026</sub> · [📄 Paper](https://arxiv.org/abs/2504.05296) · [🌐 Project](https://galfiebelman.github.io/let-it-snow/) · [💻 Code](https://github.com/galfiebelman/let-it-snow)

- **muSync-GS: Physics-Synchronized Driving Video Synthesis for Weather and Geometric Road Hazards**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2608.04412)

- **RealityBridge: Bridging Editable 3D Gaussian Splatting Driving Simulations and Real-World Videos**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2606.16278) · <sub>🎞️ Video output</sub>

- **WeatherCity: Urban Scene Reconstruction with Controllable Multi-Weather Transformation**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2602.22096)

- **WeatherEdit: Controllable Weather Editing with 4D Gaussian Field**<br>
  <sub>AAAI 2026</sub> · [📄 Paper](https://doi.org/10.1609/aaai.v40i10.37802) · [🌐 Project](https://jumponthemoon.github.io/w-edit/)

- **WILDFIREGS: Physics-Based Wildfire Simulation in Large-Scale Semantics-Enriched Gaussian Splatting Forest Scenes**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2608.11100)

- **Zero-Shot UAV Navigation in Forests via Relightable 3D Gaussian Splatting**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2602.07101)


#### 2025

- **RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting**<br>
  <sub>CVPR 2025</sub> · [📄 Paper](https://arxiv.org/abs/2503.21442)


#### 2023

- **ClimateNeRF: Extreme Weather Synthesis in Neural Radiance Field**<br>
  <sub>ICCV 2023</sub> · [📄 Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Li_ClimateNeRF_Extreme_Weather_Synthesis_in_Neural_Radiance_Field_ICCV_2023_paper.html)


</details>


<a id="transformation-state"></a>

### 🌬️ 3.4 Wind Field Adaptation and Sensor Domain Transformation

<details>
<summary><strong>📚 Browse 5 entries</strong> · 2024–2026</summary>


#### 2026

- **Integrating Fourier Neural Operators into High-Fidelity Helicopter Flight Simulation for Real-Time Urban Wind Prediction**<br>
  <sub>AAAI / IAAI 2026</sub> · [📄 Paper](https://ojs.aaai.org/index.php/AAAI/article/view/41461) · <sub>🌬️ Wind</sub>

- **WindINR: Latent-State INR for Fast Local Wind Query and Correction in Complex Terrain**<br>
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2605.09511) · <sub>🌬️ Wind</sub>


#### 2025

- **Efficient Coupling of Urban Wind Fields and Drone Flight Dynamics Using Convolutional Autoencoders**<br>
  <sub>Drones 2025</sub> · [📄 Paper](https://doi.org/10.3390/drones9110802) · <sub>🌬️ Wind</sub>


#### 2024

- **DroneWiS: Automated Simulation Testing of small Unmanned Aerial Systems in Realistic Windy Conditions**<br>
  <sub>ASE 2024</sub> · [📄 Paper](https://arxiv.org/abs/2408.16559) · <sub>🌬️ Wind</sub>

- **LiT: Unifying LiDAR “Languages” with LiDAR Translator**<br>
  <sub>NeurIPS 2024</sub> · [📄 Paper](https://yxlao.github.io/lit/lit_paper.pdf) · [🌐 Project](https://yxlao.github.io/lit/) · [💻 Code](https://github.com/yxlao/lit) · <sub>📡 Sensor</sub>


</details>


<a id="transformation-related"></a>

### 🎭 3.5 Related Actor, Interaction, and Road Graph Transformation

<details>
<summary><strong>📚 Browse 5 entries</strong> · 2024–2026</summary>


#### 2026

- **Perceptual 3D Simulation With Physical World Modeling**<br>
  <sub>CVPR 2026</sub> · [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Lee_Perceptual_3D_Simulation_With_Physical_World_Modeling_CVPR_2026_paper.html)


#### 2025

- **RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation**<br>
  <sub>arXiv 2025</sub> · [📄 Paper](https://arxiv.org/abs/2506.18088) · [🌐 Project](https://robotwin-platform.github.io) · <sub>🛋️ Related indoor</sub>

- **SIMS: Simulating Stylized Human-Scene Interactions with Retrieval-Augmented Script Generation**<br>
  <sub>ICCV 2025</sub> · [📄 Paper](https://arxiv.org/abs/2411.19921) · [🌐 Project](https://wenjiawang0312.github.io/projects/sims/) · <sub>🛋️ Related indoor</sub> · <sub>🚦 Scenario / data</sub>

- **TraSculptor: Visual Analytics for Enhanced Decision-Making in Road Traffic Planning**<br>
  <sub>IEEE TVCG 2025</sub> · [📄 Paper](https://doi.org/10.1109/TVCG.2025.3532498) · [💻 Code](https://github.com/akihaisland/TraSculptor) · <sub>🛣️ Road graph</sub>


#### 2024

- **Promptable Closed-Loop Traffic Simulation**<br>
  <sub>arXiv 2024</sub> · [📄 Paper](https://arxiv.org/abs/2409.05863) · <sub>🚦 Scenario / data</sub>


</details>


---

<a id="boundary-candidates"></a>

## 🔎 Boundary Candidates

These records need further decisions about the construction task, output scope, or eligibility. They are excluded from the 177 task entries above.

<details>
<summary><strong>🔍 Review 7 boundary candidates</strong></summary>

- **Gen3R: 3D Scene Generation Meets Feed-Forward Reconstruction**<br>
  [📄 Paper](https://arxiv.org/abs/2601.04090) · <sub>Suggested task: Synthesis（暂定）</sub>

- **SceneFrom3D: Geometry-Conditioned Outdoor 3D Scene Generation via View Scheduling with Object-Level Control**<br>
  [📄 Paper](https://arxiv.org/abs/2607.04540) · <sub>Suggested task: Synthesis / Transformation（待判）</sub>

- **InfiniVerse: Occupancy Guided Unbounded Scene Generation for Autonomous Driving**<br>
  [📄 Paper](https://arxiv.org/abs/2606.31109) · <sub>Suggested task: Synthesis（局部/部分状态）</sub>

- **ReconDreamer-RL: Enhancing Reinforcement Learning via Diffusion-based Scene Reconstruction**<br>
  [📄 Paper](https://arxiv.org/abs/2508.08170) · <sub>Suggested task: Reconstruction / Bridge（暂定）</sub>

- **SceneDirector: Bridging Explicit Geometry and Generative Priors for Unified Driving Scene Editing**<br>
  [📄 Paper](https://openreview.net/forum?id=0dNGyQnDo2) · <sub>Suggested task: Transformation（题录线索）</sub>

- **SceneGen: Single-Image 3D Scene Generation in One Feedforward Pass**<br>
  [📄 Paper](https://arxiv.org/abs/2508.15769) · <sub>Suggested task: Reconstruction / Synthesis（待判）</sub>

- **SceneLM: 3D-Aware Language Models for Editable 3D Scene Synthesis**<br>
  [📄 Paper](https://aclanthology.org/2026.findings-acl.2116/) · <sub>Suggested task: Reconstruction（建议；待全文编码）</sub>


</details>

---

<a id="collection-notes"></a>

## 📝 Collection Notes

<details>
<summary><strong>Sources, publication metadata, and machine-readable records</strong></summary>

This initial collection merges two existing literature inventories: `论文三分类汇总.md` and `论文三分类汇总_增补2025-2026遗漏文献_20261011.md`. Duplicate PDF versions and records excluded from the three tasks are not repeated. The supplement supplies 25 provisional additions, seven boundary candidates, and four bibliographic updates for AutoUE, Scenethesis, WeatherEdit, and R3D2.

Publication labels primarily follow those inventories. Selected records were cross-checked against publisher or author pages during repository preparation. Formal publication years and first preprint years can differ; a newer arXiv version is not treated as a new study. This is an initial organization of the supplied collection, rather than an exhaustive update through the repository preparation date.

Paper identifiers and resource links were recovered from the inventories, local paper headers, publisher records, and author project pages. Linked resources have not all been tested for availability or reproducibility. EmbodiedScene currently has a project link only because its project page contains placeholder paper and code targets.

Machine-readable records, including original inventory IDs and source publication status, are available in [data/papers.json](data/papers.json). The separate review queue is in [data/candidates.json](data/candidates.json). The manuscript and paper PDFs are not included in this resource collection.

</details>

<a id="contributing"></a>

## 🤝 Contributing

Suggestions and corrections are welcome through [Issues](https://github.com/liuliuyaonuli/outdoor-sim-construction-survey/issues) or pull requests. For a paper addition, please include:

- Full title, publication venue or preprint status, and year.
- A stable paper URL and any author-maintained code or project links.
- The proposed construction task and a brief reason based on the main output.
- Any scope limits, such as indoor-only evaluation, single-asset output, actor-only scenarios, or video-only results.

Please distinguish a code release from a project page, and a preliminary candidate from a verified inclusion.

<a id="acknowledgments"></a>

## 💐 Acknowledgments

The repository layout is inspired by [Awesome-Self-Evolving-Agents](https://github.com/ANative-Lab/Awesome-Self-Evolving-Agents). The taxonomy and paper selection follow this survey's literature inventories. Credit for the linked research and software belongs to the respective authors.

<div align="center">

🌱 **Create** &nbsp; · &nbsp; 🧭 **Recover** &nbsp; · &nbsp; 🛠️ **Transform**

[↑ Back to top](#top)

</div>
