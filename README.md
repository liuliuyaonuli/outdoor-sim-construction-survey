# Outdoor Simulation Environment Construction Survey

A curated reading list for **Automated Construction of Outdoor 3D Simulation Environments for Autonomous Systems**.

**面向自主系统的室外三维仿真环境自动构建｜论文与开源资源汇总**

This repository collects research on constructing outdoor 3D environments for autonomous driving, aerial robotics, and other autonomous systems. The collection follows three construction tasks: **synthesis**, **reconstruction**, and **transformation**. It also includes related indoor methods, scenario generation, and environmental state modeling from the source collection, with their scope indicated below.

本仓库围绕“新环境生成、真实环境重建、现有环境变换”整理已有论文，并提供论文、代码与项目链接。室内场景、单资产、交通情景和风场等相关工作保留范围标记，方便按研究需要查阅。

## Contents

- [About the survey](#about-the-survey)
- [1. Synthesis of New Environments](#synthesis)
  - [1.1 Procedural landscapes, maps, and simulation platforms](#synthesis-procedural)
  - [1.2 Language-driven and agentic world construction](#synthesis-agentic)
  - [1.3 Learned outdoor and driving world generation](#synthesis-learned)
  - [1.4 Traffic scenarios, synthetic data, and task generation](#synthesis-scenarios)
  - [1.5 Synthetic wind fields and aerial simulation](#synthesis-wind)
  - [1.6 Related indoor and manipulation scene synthesis](#synthesis-indoor)
- [2. Reconstruction of Real Environments](#reconstruction)
  - [2.1 Driving scene reconstruction and neural simulation](#reconstruction-driving)
  - [2.2 Real-to-sim for navigation, locomotion, and flight](#reconstruction-robotics)
  - [2.3 Geospatial, facility, and environmental state reconstruction](#reconstruction-geospatial)
  - [2.4 Related indoor, asset, and navigability reconstruction](#reconstruction-related)
- [3. Transformation of Existing Environments](#transformation)
  - [3.1 Scene completion, inpainting, and geometric refinement](#transformation-completion)
  - [3.2 Object editing, agentic authoring, and editable simulation](#transformation-editing)
  - [3.3 Weather, lighting, and environmental appearance editing](#transformation-weather)
  - [3.4 Wind field adaptation and sensor domain transformation](#transformation-state)
  - [3.5 Related actor, interaction, and road graph transformation](#transformation-related)
- [Boundary candidates](#boundary-candidates)
- [Collection notes](#collection-notes)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## About the Survey

The taxonomy is based on the main construction objective and its reference relationship:

| Task | Construction objective | Main reference |
| --- | --- | --- |
| **Synthesis / 新环境生成** | Create a new environment instance from rules, assets, language, maps, or learned priors. | Conditions and constraints, without requiring correspondence to one specific real location. |
| **Reconstruction / 真实环境重建** | Recover the geometry, appearance, structure, semantics, or environmental state of a real target. | A specific real object, place, or observed state. |
| **Transformation / 现有环境变换** | Edit, complete, extend, or vary an existing digital environment. | The input environment, the requested changes, and the content that must be preserved. |

Hybrid systems are listed once according to the primary task recorded in the source collection; secondary reconstruction, generation, or editing operations do not create duplicate entries.

| Collection | Existing entries | Provisional additions | Total |
| --- | ---: | ---: | ---: |
| Synthesis | 86 | 11 | **97** |
| Reconstruction | 29 | 9 | **38** |
| Transformation | 37 | 5 | **42** |
| **Total** | **152** | **25** | **177** |

**Reading the list.** Entries are ordered by year, newest first within each subsection. **†** marks a provisional addition from the October 2026 supplement; its task assignment and inclusion remain subject to review. Scope tags distinguish related indoor, asset, scenario/data, wind, road graph, and video-output work. **Paper**, **Code**, **Project**, and **Dataset** links identify different resource types. A missing link means it has not yet been established for this collection.

The counts describe registered entries, including related methods and provisional additions; they are not counts of fully verified core outdoor methods. Seven additional boundary candidates are listed separately.

<a id="synthesis"></a>

## 1. Synthesis of New Environments

Create new environmental content and spatial structure through procedural rules, asset composition, language-guided programs, or learned priors.

<a id="synthesis-procedural"></a>

### 1.1 Procedural Landscapes, Maps, and Simulation Platforms

- (Vehicles 2026) **3D Environment Generation from Sparse Inputs for Automated Driving Function Development** **†**. [Paper](https://www.preprints.org/manuscript/202601.0011)
- (AAAI Demo 2026) **AirNavigation: Let UAV Navigation Tell Its Own Story**. [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/42356) · [Code](https://github.com/1e12Leon/AirNavigation)
- (Future Transportation 2026) **An Efficient Simulation Scene Generation Method Based on Extracted Road Network Topology and Large Language Models**. [Paper](https://doi.org/10.3390/futuretransp6020081)
- (AAAI 2026) **LandCraft: Designing the Structured 3D Landscapes via Text Guidance**. [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/37686)
- (arXiv 2026) **LLM-Driven 3D Scene Generation of Agricultural Simulation Environments** **†**. [Paper](https://arxiv.org/abs/2602.11706)
- (arXiv 2026) **RoadWeaver: Large-Scale Lane-Level HD Map Generation from Scratch for Autonomous Driving Simulation**. [Paper](https://arxiv.org/abs/2608.11580)
- (ICRA 2025) **FlightForge: Advancing UAV Research Through Procedural Generation with High-Fidelity Simulation and Integrated Autonomy**. [Paper](https://arxiv.org/abs/2502.05038)
- (arXiv 2025) **InfiniteDiffusion: Bridging Learned Fidelity and Procedural Utility for Open-World Terrain Generation** **†**. [Paper](https://arxiv.org/abs/2512.08309)
- (CVPR MORSE Workshop 2025) **MESA: Text-Driven Terrain Generation Using Latent Diffusion and Global Copernicus Data** **†**. [Paper](https://arxiv.org/abs/2504.07210) · [Code](https://github.com/PaulBorneP/MESA)
- (arXiv 2025) **Towards Autonomous Micromobility through Scalable Urban Simulation**. [Paper](https://arxiv.org/abs/2505.00690) · [Project](https://metadriverse.github.io/urban-sim/)
- (Energy Conversion and Management 2024) **Digital-PV: A digital twin-based platform for autonomous aerial monitoring of large-scale photovoltaic power plants**. [Paper](https://doi.org/10.1016/j.enconman.2024.118963)
- (Technical report 2024) **MetaUrban: An Embodied AI Simulation Platform for Urban Micromobility**. [Paper](https://arxiv.org/abs/2407.08725) · [Project](https://metadriverse.github.io/metaurban)
- (arXiv 2022) **Procedural Generation and Rendering of Realistic, Navigable Forest Environments: An Open-Source Tool**. [Paper](https://arxiv.org/abs/2208.01471) · [Code](https://github.com/callumnewlands/ForestGenerator)
- (PMLR 2020) **AirSim Drone Racing Lab**. [Paper](https://proceedings.mlr.press/v123/madaan20a.html) · [Code](https://github.com/microsoft/AirSim-NeurIPS2019-Drone-Racing)
- (ACM TOG 2013) **Terrain Generation Using Procedural Models Based on Hydrology**. [Paper](https://doi.org/10.1145/2461912.2461996)
- (SIGGRAPH 2006) **Procedural Modeling of Buildings**. [Paper](https://doi.org/10.1145/1179352.1141931) `Asset`
- (SIGGRAPH 2001) **Procedural Modeling of Cities**. [Paper](https://doi.org/10.1145/383259.383292)
- (SIGGRAPH 1998) **Realistic Modeling and Rendering of Plant Ecosystems**. [Paper](https://doi.org/10.1145/280814.280898)

<a id="synthesis-agentic"></a>

### 1.2 Language-Driven and Agentic World Construction

- (Findings of ACL 2026) **AutoUE: Automated Generation of 3D Games in Unreal Engine via Multi-Agent Systems**. [Paper](https://aclanthology.org/2026.findings-acl.111/)
- (arXiv 2026) **Imagine a City: CityGenAgent for Procedural 3D City Generation**. [Paper](https://arxiv.org/abs/2602.05362)
- (arXiv 2026) **MAGIC: Transition-Aware Generation of Navigable Multi-Scene Game Worlds with Large Language Models**. [Paper](https://arxiv.org/abs/2607.11594) · [Code](https://github.com/sereneee1201/MAGIC/)
- (arXiv 2026) **PhyScensis: Physics-Augmented LLM Agents for Complex Physical Scene Arrangement**. [Paper](https://arxiv.org/abs/2602.14968) `Related indoor`
- (ICLR 2026) **Scenethesis: Combining Language and Visual Priors for 3D Scene Generation**. [Paper](https://openreview.net/forum?id=SzhezVoaNB) · [Project](https://research.nvidia.com/labs/dir/scenethesis/) `Indoor / outdoor`
- (arXiv 2026) **SIMWORLD STUDIO: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning**. [Paper](https://arxiv.org/abs/2605.09423) · [Project](https://simworld.org/simworld-studio/) `Related indoor`
- (arXiv 2026) **WorldClaw: Agentic 3D Open-World Generation at Scale** **†**. [Paper](https://arxiv.org/abs/2608.05248) · [Project](https://tencent-hunyuan.github.io/Hunyuan3D-WorldClaw)
- (arXiv 2025) **3D-GENERALIST: Vision-Language-Action Models for Crafting 3D Worlds**. [Paper](https://arxiv.org/abs/2507.06484) `Indoor / outdoor`
- (arXiv 2025) **HOLODECK 2.0: Vision-Language-Guided 3D World Generation with Editing**. [Paper](https://arxiv.org/abs/2508.05899) `Indoor / outdoor`
- (arXiv 2025) **LatticeWorld: A Multimodal Large Language Model-Empowered Framework for Interactive Complex World Generation** **†**. [Paper](https://arxiv.org/abs/2509.05263)
- (arXiv 2025) **MajutsuCity: Language-Driven Aesthetic-Adaptive City Generation with Controllable 3D Assets and Layouts**. [Paper](https://arxiv.org/abs/2511.20415) · [Project](https://longhz140516.github.io/MajutsuCity/)
- (NeurIPS 2025) **SCENEWEAVER: All-in-One 3D Scene Synthesis with an Extensible and Self-Reflective Agent**. [Paper](https://arxiv.org/abs/2509.20414) · [Project](https://scene-weaver.github.io/) `Related indoor`
- (AAAI 2025) **SceneX: Procedural Controllable Large-Scale Scene Generation**. [Paper](https://arxiv.org/abs/2403.15698) · [Project](https://zhouzq1.github.io/SceneX/)
- (Findings of ACL 2025) **UnrealLLM: Towards Highly Controllable and Interactable 3D Scene Generation by LLM-powered Procedural Content Generation** **†**. [Paper](https://aclanthology.org/2025.findings-acl.994/)
- (arXiv 2025) **WorldCraft: Photo-Realistic 3D World Creation and Customization via LLM Agents**. [Paper](https://arxiv.org/abs/2502.15601) `Indoor / outdoor`
- (arXiv 2025) **Yo’City: Personalized and Boundless 3D Realistic City Scene Generation via Self-Critic Expansion**. [Paper](https://arxiv.org/abs/2511.18734)
- (arXiv 2024) **CityX: Controllable Procedural Content Generation for Unbounded 3D Cities**. [Paper](https://arxiv.org/abs/2407.17572)
- (arXiv 2023) **3D-GPT: Procedural 3D Modeling with Large Language Models**. [Paper](https://arxiv.org/abs/2310.12945) · [Project](https://chuny1.github.io/3DGPT/3dgpt.html) `Indoor / outdoor`

<a id="synthesis-learned"></a>

### 1.3 Learned Outdoor and Driving World Generation

- (arXiv 2026) **AeroScene: Progressive Scene Synthesis for Aerial Robotics**. [Paper](https://arxiv.org/abs/2603.23224)
- (arXiv 2026) **HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds**. [Paper](https://arxiv.org/abs/2604.14268) · [Code](https://github.com/Tencent-Hunyuan/HY-World-2.0)
- (arXiv 2026) **SCENEFOUNDRY: Generating Interactive Infinite 3D Worlds**. [Paper](https://arxiv.org/abs/2601.05810) `Related indoor`
- (arXiv 2026) **WorldFlow3D: Flowing Through 3D Distributions for Unbounded World Generation**. [Paper](https://arxiv.org/abs/2603.29089) · [Project](https://light.princeton.edu/worldflow3d) `Indoor / outdoor`
- (ICCV 2025) **Controllable 3D Outdoor Scene Generation via Scene Graphs** **†**. [Paper](https://arxiv.org/abs/2503.07152) · [Code](https://github.com/yuhengliu02/control-3d-scene)
- (ICCV 2025) **DRIVEARENA: A Closed-Loop Generative Simulation Platform for Autonomous Driving**. [Paper](https://arxiv.org/abs/2408.00415) · [Project](https://pjlab-adg.github.io/DriveArena/)
- (arXiv 2025) **EmbodiedGen: Towards a Generative 3D World Engine for Embodied Intelligence**. [Paper](https://arxiv.org/abs/2506.10600) `Related indoor` `Asset`
- (CVPR 2025) **Generative Gaussian Splatting for Unbounded 3D City Generation**. [Paper](https://arxiv.org/abs/2406.06526) · [Project](https://haozhexie.com/project/gaussian-city)
- (arXiv 2025) **HiScene: Creating Hierarchical 3D Scenes with Isometric View Generation**. [Paper](https://arxiv.org/abs/2504.13072) · [Project](https://zju3dv.github.io/hiscene/) `Related indoor`
- (arXiv 2025) **HunyuanWorld 1.0: Generating Immersive, Explorable, and Interactive 3D Worlds from Words or Pixels**. [Paper](https://arxiv.org/abs/2507.21809) · [Code](https://github.com/Tencent-Hunyuan/HunyuanWorld-1.0) `Indoor / outdoor`
- (arXiv 2025) **InfiniCube: Unbounded and Controllable Dynamic 3D Driving Scene Generation with World-Guided Video Models**. [Paper](https://arxiv.org/abs/2412.03934) · [Project](https://research.nvidia.com/labs/toronto-ai/infinicube/)
- (ICCV 2025) **Large Scene Generation with Cube-Absorb Discrete Diffusion**. [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Hu_Large_Scene_Generation_with_Cube-Absorb_Discrete_Diffusion_ICCV_2025_paper.html)
- (ICCV 2025) **NuiScene: Exploring Efficient Generation of Unbounded Outdoor Scenes** **†**. [Paper](https://arxiv.org/abs/2503.16375) · [Dataset](https://github.com/3dlg-hcvc/NuiScene43-Dataset)
- (arXiv 2025) **Steerable Scene Generation with Post Training and Inference-Time Search**. [Paper](https://arxiv.org/abs/2505.04831) · [Project](https://steerable-scene-generation.github.io/) `Related indoor`
- (CVPR 2025) **UniScene: Unified Occupancy-centric Driving Scene Generation** **†**. [Paper](https://arxiv.org/abs/2412.05435)
- (CVPR 2025) **WonderWorld: Interactive 3D Scene Generation from a Single Image**. [Paper](https://arxiv.org/abs/2406.09394) · [Project](https://kovenyu.com/WonderWorld/) `Indoor / outdoor`
- (Technical report 2025) **WorldGen: From Text to Traversable and Interactive 3D Worlds**. [Paper](https://arxiv.org/abs/2511.16825) `Indoor / outdoor`
- (NeurIPS 2025) **X-Scene: Large-Scale Driving Scene Generation with High Fidelity and Flexible Controllability** **†**. [Paper](https://arxiv.org/abs/2506.13558)

<a id="synthesis-scenarios"></a>

### 1.4 Traffic Scenarios, Synthetic Data, and Task Generation

- (arXiv 2025) **DriveGen: Towards Infinite Diverse Traffic Scenarios with Large Models**. [Paper](https://arxiv.org/abs/2503.05808) `Scenario / data`
- (AAAI 2025) **Generating Traffic Scenarios via In-Context Learning to Learn Better Motion Planner**. [Paper](https://arxiv.org/abs/2412.18086) · [Project](https://ezharjan.github.io/AutoSceneGen) `Scenario / data`
- (arXiv 2025) **LMM-Enhanced Safety-Critical Scenario Generation for Autonomous Driving System Testing from Non-Accident Traffic Videos**. [Paper](https://arxiv.org/abs/2406.10857) `Scenario / data`
- (arXiv 2025) **Text2Scenario: Text-Driven Scenario Generation for Autonomous Driving Test**. [Paper](https://arxiv.org/abs/2503.02911) · [Project](https://caixxuan.github.io/Text2Scenario.GitHub.io/) `Scenario / data`
- (CVPR 2024) **ChatScene: Knowledge-Enabled Safety-Critical Scenario Generation for Autonomous Vehicles**. [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_ChatScene_Knowledge-Enabled_Safety-Critical_Scenario_Generation_for_Autonomous_Vehicles_CVPR_2024_paper.html) · [Code](https://github.com/javyduck/ChatScene) `Scenario / data`
- (arXiv 2024) **ChatSUMO: Large Language Model for Automating Traffic Scenario Generation in Simulation of Urban MObility**. [Paper](https://arxiv.org/abs/2409.09040) `Scenario / data`
- (arXiv 2024) **Environment Curriculum Generation via Large Language Models**. [Paper](https://arxiv.org/abs/2411.01775) · [Project](https://eureka-research.github.io/eurekaverse/) `Scenario / data`
- (arXiv 2024) **Generating Out-Of-Distribution Scenarios Using Language Models**. [Paper](https://arxiv.org/abs/2411.16554) `Scenario / data`
- (arXiv 2024) **LeGEND: A Top-Down Approach to Scenario Generation of Autonomous Driving Systems Assisted by Large Language Models**. [Paper](https://arxiv.org/abs/2409.10066) `Scenario / data`
- (arXiv 2024) **Realistic Corner Case Generation for Autonomous Vehicles with Multimodal Large Language Model**. [Paper](https://arxiv.org/abs/2412.00243) `Scenario / data`
- (NeurIPS 2024) **SceneDiffuser: Efficient and Controllable Driving Simulation Initialization and Rollout**. [Paper](https://arxiv.org/abs/2412.12129) `Scenario / data`
- (ASE 2024) **SoVAR: Building Generalizable Scenarios from Accident Reports for Autonomous Driving Testing**. [Paper](https://arxiv.org/abs/2409.08081) · [Code](https://github.com/meng2180/SoVAR) `Scenario / data`
- (arXiv 2024) **Traffic Scene Generation from Natural Language Description for Autonomous Vehicles with Large Language Model**. [Paper](https://arxiv.org/abs/2409.09575) · [Project](https://basiclab.github.io/TTSG) `Scenario / data`
- (arXiv 2023) **Language Conditioned Traffic Generation**. [Paper](https://arxiv.org/abs/2307.07947) · [Project](https://ariostgx.github.io/lctgen) `Scenario / data`
- (arXiv 2023) **TARGET: Traffic Rule-Based Test Generation for Autonomous Driving via Validated LLM-Guided Knowledge Extraction**. [Paper](https://arxiv.org/abs/2305.06018) `Scenario / data`
- (ECCV 2020) **Meta-Sim2: Unsupervised Learning of Scene Structure for Synthetic Data Generation**. [Paper](https://arxiv.org/abs/2008.09092) · [Project](https://nv-tlabs.github.io/meta-sim-structure/) `Scenario / data`
- (CVPR 2019) **Meta-Sim: Learning to Generate Synthetic Datasets**. [Paper](https://arxiv.org/abs/1904.11621) `Scenario / data`

<a id="synthesis-wind"></a>

### 1.5 Synthetic Wind Fields and Aerial Simulation

- (Manuscript 2026) **A Simulation Platform for Flapping-Wing Vehicles**. [Paper](https://arxiv.org/abs/2606.02370) `Wind`
- (arXiv 2026) **Physics Informed Reconstruction of Four-Dimensional Atmospheric Wind Fields Using Multi-UAS Swarm Observations in a Synthetic Turbulent Environment**. [Paper](https://arxiv.org/abs/2601.22111) `Wind`
- (Drones 2025) **Urban Wind Field Effects on the Flight Dynamics of Fixed-Wing Drones**. [Paper](https://doi.org/10.3390/drones9050362) `Wind`
- (arXiv 2019) **Quad-rotor Flight Simulation in Realistic Atmospheric Conditions**. [Paper](https://arxiv.org/abs/1902.01465) `Wind`

<a id="synthesis-indoor"></a>

### 1.6 Related Indoor and Manipulation Scene Synthesis

- (arXiv 2026) **MANSION: Multi-floor lANguage-to-3D Scene generatIOn for loNg-horizon Tasks**. [Paper](https://arxiv.org/abs/2603.11554) `Related indoor`
- (arXiv 2026) **MolmoSpaces: A Large-Scale Open Ecosystem for Robot Navigation and Manipulation**. [Paper](https://arxiv.org/abs/2602.11337) · [Code](https://github.com/allenai/molmospaces) `Related indoor`
- (arXiv 2026) **SAGE: Scalable Agentic 3D Scene Generation for Embodied AI**. [Paper](https://arxiv.org/abs/2602.10116) `Related indoor`
- (arXiv 2026) **SceneCode: Executable World Programs for Editable Indoor Scenes with Articulated Objects**. [Paper](https://arxiv.org/abs/2605.19587) · [Project](https://scene-code.github.io/) `Related indoor`
- (ICML 2026) **SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes**. [Paper](https://arxiv.org/abs/2602.09153) · [Project](https://scenesmith.github.io/) `Related indoor`
- (CVPR 2025) **ArtiScene: Language-Driven Artistic 3D Scene Generation Through Image Intermediary**. [Paper](https://arxiv.org/abs/2506.00742) · [Project](https://research.nvidia.com/labs/dir/artiscene/) `Related indoor`
- (CVPR 2025) **DynScene: Scalable Generation of Dynamic Robotic Manipulation Scenes for Embodied AI**. [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Lee_DynScene_Scalable_Generation_of_Dynamic_Robotic_Manipulation_Scenes_for_Embodied_CVPR_2025_paper.html) `Related indoor`
- (Manuscript 2025) **EmbodiedScene: Towards Automated Generation of Diverse and Realistic Scenes for Embodied AI**. [Project](https://embodiedscene1.github.io/embodied.scene/) `Related indoor`
- (arXiv 2025) **MarketGen: A Scalable Simulation Platform with Auto-Generated Embodied Supermarket Environments**. [Paper](https://arxiv.org/abs/2511.21161) · [Project](https://xuhu0529.github.io/MarketGen) `Related indoor`
- (arXiv 2025) **MesaTask: Towards Task-Driven Tabletop Scene Generation via 3D Spatial Reasoning**. [Paper](https://arxiv.org/abs/2509.22281) `Related indoor`
- (arXiv 2025) **PAT3D: Physics-Augmented Text-to-3D Scene Generation**. [Paper](https://arxiv.org/abs/2511.21978) `Related indoor`
- (arXiv 2025) **TabletopGen: Tabletop Scene Generation and Interactive Simulation for Robotic Manipulation**. [Paper](https://arxiv.org/abs/2512.01204) · [Project](https://d-robotics-ai-lab.github.io/TabletopGen.project/) `Related indoor`
- (ICRA 2024) **Gen2Sim: Scaling up Robot Learning in Simulation with Generative Models**. [Paper](https://arxiv.org/abs/2310.18308) · [Project](https://gen2sim.github.io/) `Related indoor`
- (arXiv 2024) **GenSim2: Scaling Robot Data Generation with Multi-modal and Reasoning LLMs**. [Paper](https://arxiv.org/abs/2410.03645) · [Project](https://gensim2.github.io/) `Related indoor`
- (CVPR 2024) **HOLODECK: Language Guided Generation of 3D Embodied AI Environments**. [Paper](https://arxiv.org/abs/2312.09067) `Related indoor`
- (arXiv 2024) **I-Design: Personalized LLM Interior Designer**. [Paper](https://arxiv.org/abs/2404.02838) · [Project](https://atcelen.github.io/I-Design/) `Related indoor`
- (arXiv 2024) **InfiniteWorld: A Unified Scalable Simulation Framework for General Visual-Language Robot Interaction**. [Paper](https://arxiv.org/abs/2412.05789) · [Code](https://github.com/pzhren/InfiniteWorld) `Related indoor`
- (arXiv 2024) **PHYSCENE: Physically Interactable 3D Scene Synthesis for Embodied AI**. [Paper](https://arxiv.org/abs/2404.09465) · [Project](https://physcene.github.io) `Related indoor`
- (ICML 2024) **RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation**. [Paper](https://arxiv.org/abs/2311.01455) · [Project](https://robogen-ai.github.io/) `Related indoor`
- (arXiv 2024) **SceneCraft: An LLM Agent for Synthesizing 3D Scene as Blender Code**. [Paper](https://arxiv.org/abs/2403.01248) `Related indoor`
- (NeurIPS 2022) **ProcTHOR: Large-Scale Embodied AI Using Procedural Generation**. [Paper](https://arxiv.org/abs/2206.06994) `Related indoor`
- (NeurIPS Workshop 2021) **LUMINOUS: Indoor Scene Generation for Embodied AI Challenges**. [Paper](https://arxiv.org/abs/2111.05527) `Related indoor`

<a id="reconstruction"></a>

## 2. Reconstruction of Real Environments

Recover a specific real environment from maps, imagery, scans, or other observations, including geometry, appearance, dynamics, and local environmental states.

<a id="reconstruction-driving"></a>

### 2.1 Driving Scene Reconstruction and Neural Simulation

- (ASE 2026) **Cam2Sim: Neural Scenario Reconstruction for Closed-Loop Autonomous Driving Simulation**. [Paper](https://arxiv.org/abs/2607.04770)
- (ACM MM 2026) **HybridWorldSim: A Scalable and Controllable High-fidelity Simulator for Autonomous Driving**. [Paper](https://arxiv.org/abs/2511.22187)
- (arXiv 2026) **Instant NuRec: Feed-Forward 3D Gaussian Reconstruction for Driving Scene Simulation**. [Paper](https://arxiv.org/abs/2607.14203) · [Project](https://research.nvidia.com/labs/sil/projects/instant-nurec) · [Code](https://github.com/nvidia/instant-nurec)
- (ICRA 2026) **Nighttime Autonomous Driving Scene Reconstruction with Physically-Based Gaussian Splatting** **†**. [Paper](https://arxiv.org/abs/2602.13549)
- (CVPR 2026) **NimbusGS: Unified 3D Scene Reconstruction under Hybrid Weather** **†**. [Paper](https://arxiv.org/abs/2603.27228)
- (arXiv 2026) **ReconDrive: Fast Feed-Forward 4D Gaussian Splatting for Autonomous Driving Scene Reconstruction** **†**. [Paper](https://arxiv.org/abs/2603.07552)
- (3DV 2026) **UniGaussian: Driving Scene Reconstruction from Multiple Camera Models via Unified Gaussian Representations** **†**. [Paper](https://arxiv.org/abs/2411.15355)
- (CVPR 2026) **Urban-GS: A Unified 3D Gaussian Splatting Framework for Compact and High-Fidelity Aerial-to-Street Reconstruction**. [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Urban-GS_A_Unified_3D_Gaussian_Splatting_Framework_for_Compact_and_CVPR_2026_paper.pdf)
- (ICLR 2025) **3D StreetUnveiler with Semantic-Aware 2DGS - A Simple Baseline**. [Paper](https://arxiv.org/abs/2405.18416) · [Project](https://streetunveiler.github.io)
- (NeurIPS 2025) **DrivingRecon: Large 4D Gaussian Reconstruction Model For Autonomous Driving** **†**. [Paper](https://arxiv.org/abs/2412.09043) · [Code](https://github.com/EnVision-Research/DriveRecon)
- (CVPR 2025) **DrivingSphere: Building a High-Fidelity 4D World for Closed-Loop Simulation**. [Paper](https://arxiv.org/abs/2411.11252)
- (arXiv 2025) **RealEngine: Simulating Autonomous Driving in Realistic Context**. [Paper](https://arxiv.org/abs/2505.16902) · [Code](https://github.com/fudan-zvg/RealEngine)
- (arXiv 2025) **ReconDreamer++: Harmonizing Generative and Reconstructive Models for Driving Scene Representation** **†**. [Paper](https://arxiv.org/abs/2503.18438)
- (CVPR 2025) **ReconDreamer: Crafting World Models for Driving Scene Reconstruction via Online Restoration** **†**. [Paper](https://arxiv.org/abs/2411.19548)
- (CVPR 2025) **SplatAD: Real-Time Lidar and Camera Rendering with 3D Gaussian Splatting for Autonomous Driving** **†**. [Paper](https://arxiv.org/abs/2411.16816) · [Code](https://github.com/carlinds/splatad)
- (ICRA 2025) **WeatherGS: 3D Scene Reconstruction in Adverse Weather Conditions via Gaussian Splatting** **†**. [Paper](https://arxiv.org/abs/2412.18862) · [Code](https://github.com/Jumponthemoon/WeatherGS)
- (arXiv 2024) **HUGSIM: A Real-Time, Photo-Realistic and Closed-Loop Simulator for Autonomous Driving**. [Paper](https://arxiv.org/abs/2412.01718) · [Project](https://xdimlab.github.io/HUGSIM)
- (arXiv 2024) **ReSimAD: Zero-Shot 3D Domain Transfer for Autonomous Driving with Source Reconstruction and Target Simulation**. [Paper](https://arxiv.org/abs/2309.05527) · [Code](https://github.com/PJLab-ADG/3DTrans)
- (arXiv 2023) **NeuRAD: Neural Rendering for Autonomous Driving**. [Paper](https://arxiv.org/abs/2311.15260)
- (arXiv 2020) **LiDARsim: Realistic LiDAR Simulation by Leveraging the Real World**. [Paper](https://arxiv.org/abs/2006.09348)

<a id="reconstruction-robotics"></a>

### 2.2 Real-to-Sim for Navigation, Locomotion, and Flight

- (arXiv 2026) **NavGSim: High-Fidelity Gaussian Splatting Simulator for Large-Scale Navigation**. [Paper](https://arxiv.org/abs/2603.15186) · [Code](https://github.com/2003jiahang/NavGSim) `Related indoor`
- (arXiv 2025) **GaussGym: An Open-Source Real-to-Sim Framework for Learning Locomotion from Pixels**. [Paper](https://arxiv.org/abs/2510.15352) · [Project](https://escontrela.me/gauss_gym/) `Related indoor`
- (IEEE RA-L 2025) **SOUS VIDE: Cooking Visual Drone Navigation Policies in a Gaussian Splatting Vacuum**. [Paper](https://arxiv.org/abs/2412.16346) · [Project](https://stanfordmsl.github.io/SousVide/)
- (arXiv 2025) **Vid2Sim: Realistic and Interactive Simulation from Video for Urban Navigation**. [Paper](https://arxiv.org/abs/2501.06693) · [Project](https://metadriverse.github.io/vid2sim/)
- (arXiv 2025) **VR-Robo: A Real-to-Sim-to-Real Framework for Visual Robot Navigation and Locomotion**. [Paper](https://arxiv.org/abs/2502.01536) `Related indoor`
- (arXiv 2024) **Gaussian Splatting to Real World Flight Navigation Transfer with Liquid Networks**. [Paper](https://arxiv.org/abs/2406.15149)

<a id="reconstruction-geospatial"></a>

### 2.3 Geospatial, Facility, and Environmental State Reconstruction

- (ICLR 2026) **Sat3DGen: Comprehensive Street-Level 3D Scene Generation from Single Satellite Image**. [Paper](https://arxiv.org/abs/2605.14984) · [Code](https://github.com/qianmingduowan/Sat3DGen)
- (Computer Modeling in Engineering 2026) **Semi-Automated Generation of Realistic Simulation Environments from Geospatial Data for Agricultural Robot Navigation**. [Paper](https://doi.org/10.32604/cmes.2026.080739)
- (Solar Energy 2025) **A Simulation Environment for UAV-based Real-time Condition Monitoring of Solar Tower Power Plants**. [Paper](https://doi.org/10.1016/j.solener.2025.113803)
- (arXiv 2025) **Elevation Aware 2D/3D Co-simulation Framework for Large-scale Traffic Flow and High-fidelity Vehicle Dynamics**. [Paper](https://arxiv.org/abs/2512.11249)
- (arXiv 2025) **Open-Source vs. Commercial Photogrammetry: Comparing Accuracy and Efficiency of OpenDroneMap and Agisoft Metashape**. [Paper](https://doi.org/10.5194/isprs-archives-XLVIII-1-W4-2025-65-2025)
- (Nature Communications 2024) **WindSeer: real-time volumetric wind prediction over complex terrain aboard a small uncrewed aerial vehicle**. [Paper](https://doi.org/10.1038/s41467-024-47778-4) `Wind`

<a id="reconstruction-related"></a>

### 2.4 Related Indoor, Asset, and Navigability Reconstruction

- (arXiv 2026) **SE(2) Navigation Mesh**. [Paper](https://arxiv.org/abs/2607.01454) `Related indoor`
- (arXiv 2026) **SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation**. [Paper](https://arxiv.org/abs/2606.28276) · [Project](https://research.nvidia.com/labs/gear/simfoundry/) `Related indoor`
- (NeurIPS 2025) **EA3D: Online Open-World 3D Object Extraction from Streaming Videos**. [Paper](https://arxiv.org/abs/2510.25146) · [Code](https://github.com/VDIGPKU/EA3D) `Related indoor` `Asset`
- (arXiv 2025) **MetaScenes: Automated Replica Creation for Real-World 3D Scans**. [Paper](https://arxiv.org/abs/2505.02388) · [Project](https://meta-scenes.github.io/) `Related indoor`
- (arXiv 2025) **RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins**. [Paper](https://arxiv.org/abs/2504.13059) · [Project](https://robotwin-benchmark.github.io) `Related indoor` `Asset`
- (ICCV 2025) **Zero-shot Inexact CAD Model Alignment from a Single Image**. [Paper](https://arxiv.org/abs/2507.03292) · [Project](https://zerocad9d.github.io/) · [Code](https://github.com/pattaramaneea/ZeroCAD) `Related indoor` `Asset`

<a id="transformation"></a>

## 3. Transformation of Existing Environments

Modify an existing digital environment while preserving the scene content, spatial relationships, or runtime properties required by the task.

<a id="transformation-completion"></a>

### 3.1 Scene Completion, Inpainting, and Geometric Refinement

- (arXiv 2026) **GSCompleter: A Distillation-Free Plugin for Metric-Aware 3D Gaussian Splatting Completion in Seconds**. [Paper](https://arxiv.org/abs/2604.20155) · [Project](https://yuhuoo.github.io/projects/gscompleter/)
- (CVPR 2025) **AuraFusion360: Augmented Unseen Region Alignment for Reference-based 360° Unbounded Scene Inpainting** **†**. [Paper](https://arxiv.org/abs/2502.05176)
- (ACM SAP 2025) **GS-RoadPatching: Inpainting Gaussians via 3D Searching and Placing for Driving Scenes**. [Paper](https://arxiv.org/abs/2509.19937) · [Project](https://shanzhaguoo.github.io/GS-RoadPatching/)
- (CVPR 2025) **IMFine: 3D Inpainting via Geometry-guided Multi-view Refinement** **†**. [Paper](https://arxiv.org/abs/2503.04501) · [Project](https://xinxinzuo2353.github.io/imfine/)
- (NeurIPS 2025) **InstaInpaint: Instant 3D-Scene Inpainting with Masked Large Reconstruction Model** **†**. [Paper](https://arxiv.org/abs/2506.10980)
- (arXiv 2025) **SplatFill: 3D Scene Inpainting via Depth-Guided Gaussian Splatting** **†**. [Paper](https://arxiv.org/abs/2509.07809)
- (NeurIPS 2024) **ARCHITECT: Generating Vivid and Interactive 3D Scenes with Hierarchical 2D Inpainting**. [Paper](https://arxiv.org/abs/2411.09823) · [Project](https://wangyian-me.github.io/Architect/) `Related indoor`

<a id="transformation-editing"></a>

### 3.2 Object Editing, Agentic Authoring, and Editable Simulation

- (arXiv 2026) **CARLA-GS: Decoupling Representation, Reasoning, and Physics Simulation for Autonomous Driving Corner-Case Synthesis**. [Paper](https://arxiv.org/abs/2607.07601)
- (arXiv 2026) **DecoupleGS: Interactive 3D Gaussian Splatting for End-to-End Autonomous Driving Testing**. [Paper](https://arxiv.org/abs/2608.01761)
- (CVPR 2026) **HorizonForge: Driving Scene Editing with Any Trajectories and Any Vehicles** **†**. [Paper](https://arxiv.org/abs/2602.21333) · [Project](https://horizonforge.github.io/)
- (arXiv 2026) **MUSE: Agentic 3D Scene Authoring via Memory-Grounded Incremental Requirement Satisfaction**. [Paper](https://arxiv.org/abs/2606.14168) · [Project](https://xujay111.github.io/muse_githubio/) `Related indoor`
- (arXiv 2026) **Physics-Aware 3D Gaussian Editing for Driving Scene Generation**. [Paper](https://arxiv.org/abs/2605.25373)
- (arXiv 2026) **Real2Sim: A Physics-driven and Editable Gaussian Splatting Framework for Autonomous Driving Scenes**. [Paper](https://arxiv.org/abs/2605.13591)
- (arXiv 2026) **SIMSplat: Language-Aligned 4D Gaussian Splatting for Driving Scenario Generation**. [Paper](https://arxiv.org/abs/2510.02469)
- (arXiv 2026) **When Digital Twins Meet Large Language Models: Realistic, Interactive, and Editable Simulation for Autonomous Driving**. [Paper](https://arxiv.org/abs/2507.00319) · [Project](https://autodrive-ecosystem.github.io)
- (arXiv 2025) **DrivingGaussian++: Towards Realistic Reconstruction and Editable Simulation for Surrounding Dynamic Driving Scenes**. [Paper](https://arxiv.org/abs/2508.20965) · [Project](https://xiong-creator.github.io/DrivingGaussian_plus.github.io)
- (arXiv 2025) **Performance-Guided Refinement for Visual Aerial Navigation using Editable Gaussian Splatting in FalconGym 2.0**. [Paper](https://arxiv.org/abs/2510.02248)
- (arXiv 2025) **R3D2: Realistic 3D Asset Insertion via Diffusion for Autonomous Driving Simulation**. [Paper](https://arxiv.org/abs/2506.07826) `Asset`
- (arXiv 2024) **Editable Scene Simulation for Autonomous Driving via Collaborative LLM-Agents**. [Paper](https://arxiv.org/abs/2402.05746) · [Code](https://github.com/yifanlu0227/ChatSim)
- (ECCV 2024) **Language-Driven Physics-Based Scene Synthesis and Editing via Feature Splatting**. [Paper](https://arxiv.org/abs/2404.01223) · [Project](https://feature-splatting.github.io/) · [Code](https://github.com/vuer-ai/feature-splatting-inria) `Related indoor`
- (CVPR 2023) **UniSim: A Neural Closed-Loop Sensor Simulator**. [Paper](https://www.datocms-assets.com/163962/1755204775-unisim-paper.pdf) · [Project](https://waabi.ai/research/unisim/)

<a id="transformation-weather"></a>

### 3.3 Weather, Lighting, and Environmental Appearance Editing

- (arXiv 2026) **AutoWeather4D: Autonomous Driving Video Weather Conversion via G-Buffer Dual-Pass Editing**. [Paper](https://arxiv.org/abs/2603.26546) · [Project](https://lty2226262.github.io/autoweather4d) `Video output`
- (arXiv 2026) **GSRAIN: Physically Calibrated High-/Low-Frequency Rainfall Synthesis for 3D Gaussian Driving Scenes**. [Paper](https://arxiv.org/abs/2608.02177)
- (CVPR 2026) **Let it Snow! Animating 3D Gaussian Scenes with Dynamic Weather Effects via Physics-Guided Score Distillation**. [Paper](https://arxiv.org/abs/2504.05296) · [Project](https://galfiebelman.github.io/let-it-snow/) · [Code](https://github.com/galfiebelman/let-it-snow)
- (arXiv 2026) **muSync-GS: Physics-Synchronized Driving Video Synthesis for Weather and Geometric Road Hazards**. [Paper](https://arxiv.org/abs/2608.04412)
- (arXiv 2026) **RealityBridge: Bridging Editable 3D Gaussian Splatting Driving Simulations and Real-World Videos**. [Paper](https://arxiv.org/abs/2606.16278) `Video output`
- (arXiv 2026) **WeatherCity: Urban Scene Reconstruction with Controllable Multi-Weather Transformation**. [Paper](https://arxiv.org/abs/2602.22096)
- (AAAI 2026) **WeatherEdit: Controllable Weather Editing with 4D Gaussian Field**. [Paper](https://doi.org/10.1609/aaai.v40i10.37802) · [Project](https://jumponthemoon.github.io/w-edit/)
- (arXiv 2026) **WILDFIREGS: Physics-Based Wildfire Simulation in Large-Scale Semantics-Enriched Gaussian Splatting Forest Scenes**. [Paper](https://arxiv.org/abs/2608.11100)
- (arXiv 2026) **Zero-Shot UAV Navigation in Forests via Relightable 3D Gaussian Splatting**. [Paper](https://arxiv.org/abs/2602.07101)
- (CVPR 2025) **RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting**. [Paper](https://arxiv.org/abs/2503.21442)
- (ICCV 2023) **ClimateNeRF: Extreme Weather Synthesis in Neural Radiance Field**. [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Li_ClimateNeRF_Extreme_Weather_Synthesis_in_Neural_Radiance_Field_ICCV_2023_paper.html)

<a id="transformation-state"></a>

### 3.4 Wind Field Adaptation and Sensor Domain Transformation

- (AAAI / IAAI 2026) **Integrating Fourier Neural Operators into High-Fidelity Helicopter Flight Simulation for Real-Time Urban Wind Prediction**. [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/41461) `Wind`
- (arXiv 2026) **WindINR: Latent-State INR for Fast Local Wind Query and Correction in Complex Terrain**. [Paper](https://arxiv.org/abs/2605.09511) `Wind`
- (Drones 2025) **Efficient Coupling of Urban Wind Fields and Drone Flight Dynamics Using Convolutional Autoencoders**. [Paper](https://doi.org/10.3390/drones9110802) `Wind`
- (ASE 2024) **DroneWiS: Automated Simulation Testing of small Unmanned Aerial Systems in Realistic Windy Conditions**. [Paper](https://arxiv.org/abs/2408.16559) `Wind`
- (NeurIPS 2024) **LiT: Unifying LiDAR “Languages” with LiDAR Translator**. [Paper](https://yxlao.github.io/lit/lit_paper.pdf) · [Project](https://yxlao.github.io/lit/) · [Code](https://github.com/yxlao/lit) `Sensor`

<a id="transformation-related"></a>

### 3.5 Related Actor, Interaction, and Road Graph Transformation

- (CVPR 2026) **Perceptual 3D Simulation With Physical World Modeling**. [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Lee_Perceptual_3D_Simulation_With_Physical_World_Modeling_CVPR_2026_paper.html)
- (arXiv 2025) **RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation**. [Paper](https://arxiv.org/abs/2506.18088) · [Project](https://robotwin-platform.github.io) `Related indoor`
- (ICCV 2025) **SIMS: Simulating Stylized Human-Scene Interactions with Retrieval-Augmented Script Generation**. [Paper](https://arxiv.org/abs/2411.19921) · [Project](https://wenjiawang0312.github.io/projects/sims/) `Related indoor` `Scenario / data`
- (IEEE TVCG 2025) **TraSculptor: Visual Analytics for Enhanced Decision-Making in Road Traffic Planning**. [Paper](https://doi.org/10.1109/TVCG.2025.3532498) · [Code](https://github.com/akihaisland/TraSculptor) `Road graph`
- (arXiv 2024) **Promptable Closed-Loop Traffic Simulation**. [Paper](https://arxiv.org/abs/2409.05863) `Scenario / data`

## Boundary Candidates

These seven records need additional decisions about the main construction task, output scope, or eligibility. They are excluded from the 177 task entries above. Suggested tasks follow the source supplement and remain provisional.

<details>
<summary>Show 7 candidates requiring further review</summary>

- **Gen3R: 3D Scene Generation Meets Feed-Forward Reconstruction**. [Paper](https://arxiv.org/abs/2601.04090) — Suggested task: Synthesis（暂定）.
- **SceneFrom3D: Geometry-Conditioned Outdoor 3D Scene Generation via View Scheduling with Object-Level Control**. [Paper](https://arxiv.org/abs/2607.04540) — Suggested task: Synthesis / Transformation（待判）.
- **InfiniVerse: Occupancy Guided Unbounded Scene Generation for Autonomous Driving**. [Paper](https://arxiv.org/abs/2606.31109) — Suggested task: Synthesis（局部/部分状态）.
- **ReconDreamer-RL: Enhancing Reinforcement Learning via Diffusion-based Scene Reconstruction**. [Paper](https://arxiv.org/abs/2508.08170) — Suggested task: Reconstruction / Bridge（暂定）.
- **SceneDirector: Bridging Explicit Geometry and Generative Priors for Unified Driving Scene Editing**. [Paper](https://openreview.net/forum?id=0dNGyQnDo2) — Suggested task: Transformation（题录线索）.
- **SceneGen: Single-Image 3D Scene Generation in One Feedforward Pass**. [Paper](https://arxiv.org/abs/2508.15769) — Suggested task: Reconstruction / Synthesis（待判）.
- **SceneLM: 3D-Aware Language Models for Editable 3D Scene Synthesis**. [Paper](https://aclanthology.org/2026.findings-acl.2116/) — Suggested task: Reconstruction（建议；待全文编码）.

</details>

## Collection Notes

This initial collection merges two existing literature inventories: `论文三分类汇总.md` and `论文三分类汇总_增补2025-2026遗漏文献_20261011.md`. Duplicate PDF versions and records excluded from the three tasks are not repeated. The supplement supplies 25 provisional additions, seven boundary candidates, and four bibliographic updates for AutoUE, Scenethesis, WeatherEdit, and R3D2.

Publication labels primarily follow those inventories. Selected records were cross-checked against publisher or author pages during repository preparation. Formal publication years and first preprint years can differ; a newer arXiv version is not treated as a new study. This is an initial organization of the supplied collection, rather than an exhaustive update through the repository preparation date.

Paper identifiers and resource links were recovered from the inventories, local paper headers, publisher records, and author project pages. Linked resources have not all been tested for availability or reproducibility. EmbodiedScene currently has a project link only because its project page contains placeholder paper and code targets.

Machine-readable records, including original inventory IDs and source publication status, are available in [data/papers.json](data/papers.json). The separate review queue is in [data/candidates.json](data/candidates.json). The manuscript and paper PDFs are not included in this resource collection.

## Contributing

Suggestions and corrections are welcome through [Issues](https://github.com/liuliuyaonuli/outdoor-sim-construction-survey/issues) or pull requests. For a paper addition, please include:

- Full title, publication venue or preprint status, and year.
- A stable paper URL and any author-maintained code or project links.
- The proposed construction task and a brief reason based on the main output.
- Any scope limits, such as indoor-only evaluation, single-asset output, actor-only scenarios, or video-only results.

Please distinguish a code release from a project page, and a preliminary candidate from a verified inclusion.

## Acknowledgments

The repository layout is inspired by [Awesome-Self-Evolving-Agents](https://github.com/ANative-Lab/Awesome-Self-Evolving-Agents). The taxonomy and paper selection follow this survey's literature inventories. Credit for the linked research and software belongs to the respective authors.
