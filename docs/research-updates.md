# 📑 Research Additions — 2026-11-07

[← Survey reading guide](../README.md)

The supplied research report was used as a discovery list. Paper identities, dates and abstracts were checked against primary sources; linked implementations and release plans were inspected separately. No training, inference or end-to-end reproduction was performed. Metadata checks do not establish every reported experimental claim.

The principal discovery window is 2026-08-31 through 2026-11-06 by first submission. Historical omissions, methodological scope extensions and updates to manuscript-cited papers are identified separately. These additions do not change the manuscript's citation snapshot.


## Construction Methods


### OctWorld

- **OctWorld: Long-Range World-Consistent Video Generation with Octree-Based 3D Mapping**\
  <sub>ECCV 2026</sub> · [📄 Paper](https://arxiv.org/abs/2609.03919) · [🌐 Project](https://microsoft.github.io/OctWorld/) · [💻 Inference code](https://github.com/microsoft/OctWorld)

First submission: **2026-09-03** · Checked version: **v2 (2026-10-27)** · Added: **2026-11-07**.

Placement: [topic 1.4](../README.md#paper-research2026octworld).

Fuses generated RGB-D into an extensible octree TSDF memory for consistent exploration and revisits.

Persistent output: Octree TSDF map.

Scope: Rendering and spatial consistency; collision geometry and controller outcomes are not established.

Code status: `inference-released` (checked 2026-11-07).


### L3G-World

- **L3G-World: Real-Time Infinite World Generation with Latent 3D Gaussian Memory**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2610.40614) · [🌐 Project](https://cvlab-kaist.github.io/L3G-World/) · [📌 Release plan](https://github.com/cvlab-kaist/L3G-World) · <sub>⏳ Code pending</sub>

First submission: **2026-10-29** · Checked version: **v1 (2026-10-29)** · Added: **2026-11-07**.

Placement: [topic 1.4](../README.md#paper-research2026l3gworld).

Alternates video generation with updates to persistent latent Gaussian memory.

Persistent output: Latent 3D Gaussians.

Scope: Latent spatial memory does not establish exportable collision assets or physical interaction.

Code status: `planned` (checked 2026-11-07).


### Drive2Gauss

- **Drive2Gauss: FeedForward 4D Gaussian Reconstruction from Multimodal Generative Driving Videos**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2610.26585) · [💻 Code](https://github.com/zttt04/Drive2Gauss_)

First submission: **2026-10-19** · Checked version: **v1 (2026-10-19)** · Added: **2026-11-07**.

Placement: [topic 1.4](../README.md#paper-research2026drive2gauss).

Converts jointly generated driving RGB, metric depth and flow into reusable dynamic Gaussian scenes.

Persistent output: Dynamic 4D Gaussians.

Scope: Reconstruction quality is measured against generated observations; planner or physics benefits are not established.

Code status: `released` (checked 2026-11-07).


### BuildRome

- **Building Rome from a Single Image**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2610.08790) · [🌐 Project](https://build-rome.github.io/) · [💻 Inference code](https://github.com/Applied-Intuition-Open-Source/BuildRome) · [🤗 Weights](https://huggingface.co/AppliedIntuitionResearch/BuildRome)

First submission: **2026-10-06** · Checked version: **v1 (2026-10-06)** · Added: **2026-11-07**.

Placement: [topic 2.3](../README.md#paper-research2026buildrome).

Recovers complete indoor/outdoor scene meshes from a single reference image using adaptive spatial chunks.

Persistent output: Exportable triangle mesh.

Scope: Mesh export is supported; estimated scale, collision proxies and navigation structures need separate validation.

Code status: `inference-released` (checked 2026-11-07).


### DistScene

- **DistScene: Object-to-Scene Distillation for 3D Scene Generation**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2610.06960) · [🌐 Project](https://coolbeam.github.io/DistScene/) · <sub>⏳ Code pending</sub>

First submission: **2026-10-03** · Checked version: **v1 (2026-10-03)** · Added: **2026-11-07**.

Placement: [topic 2.3](../README.md#paper-research2026distscene).

Uses object-to-scene distillation and local refinement to recover compositional scenes from an image.

Persistent output: Environment and object geometry in shared coordinates.

Scope: Includes outdoor reconstruction evaluation; physically checked training compositions do not establish physical validity of outputs.

Code status: `planned` (checked 2026-11-07).


### RECAST

- **RECAST: From Log Replay to Closed-Loop Driving Simulation with View-Complete Actors**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2609.31374) · [🌐 Project](https://zijunkr.github.io/RECAST/)

First submission: **2026-09-25** · Checked version: **v1 (2026-09-25)** · Added: **2026-11-07**.

Placement: [topic 2.3](../README.md#paper-research2026recast).

Completes partially observed vehicle actors and registers them in reconstructed scenes for planner-in-the-loop simulation.

Persistent output: View-complete Gaussian actors registered in a driving scene.

Scope: Closed-loop results concern GTRS-Dense in controlled ego–actor interactions; distinct from Recast Navigation.

Code status: `unverified` (checked 2026-11-07).


### Foundation4D

- **Foundation4D: Towards a unified perception and reconstruction model for autonomous vehicles**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2610.30340) · [🌐 Project](https://research.nvidia.com/labs/sil/projects/foundation4d/) · [🗃️ Dataset](https://huggingface.co/datasets/nvidia/PhysicalAI-Autonomous-Vehicles-Foundation4D)

First submission: **2026-10-21** · Checked version: **v1 (2026-10-21)** · Added: **2026-11-07**.

Placement: [topic 2.3](../README.md#paper-research2026foundation4d).

Jointly recovers driving-scene structure and supplies geometry and actor priors to LiDAR-free NuRec.

Persistent output: Geometry, tracks, occupancy and Gaussian scenes.

Scope: Downstream reconstruction still uses GPS/IMU; training annotations use LiDAR. Data release does not establish model-code release.

Code status: `unverified` (checked 2026-11-07).


### OpenFlyScan

- **OpenFlyScan: A Quality-Guided Aerial Reconstruction System for Consumer Drones**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2609.24253) · [🌐 Project](https://openflyscan.github.io/) · [💻 Partial code](https://github.com/mistletoe235/OpenFlyScan)

First submission: **2026-09-21** · Checked version: **v1 (2026-09-21)** · Added: **2026-11-07**.

Placement: [topic 2.3](../README.md#paper-research2026openflyscan).

Predicts regional reconstruction quality and plans targeted drone reacquisition before joint reconstruction.

Persistent output: Joint aerial reconstruction from initial and additional observations.

Scope: Field acquisition and reconstruction are demonstrated; full teacher/cache training resources remain incomplete.

Code status: `partial` (checked 2026-11-07).


### SkyAnchor

- **SkyAnchor: Updating Metric-scale Aerial 3D Gaussian Scenes from Unposed Ground-View Sequences**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2609.13903)

First submission: **2026-09-12** · Checked version: **v1 (2026-09-12)** · Added: **2026-11-07**.

Placement: [topic 2.3](../README.md#paper-research2026skyanchor).

Registers later unposed ground sequences against an existing metric aerial scaffold and fuses scene updates.

Persistent output: Metric-scale aerial–ground Gaussian scene.

Scope: Requires an existing metric aerial SfM/Gaussian anchor; updates measurements of the same real place.

Code status: `unverified` (checked 2026-11-07).


### VDGS

- **VDGS: Visibility-Driven Large-Scale 3D Gaussian Splatting for Aerial Scene Reconstruction**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2609.23049)

First submission: **2026-09-19** · Checked version: **v1 (2026-09-19)** · Added: **2026-11-07**.

Placement: [topic 2.3](../README.md#paper-research2026vdgs).

Uses visibility statistics for partitioning and gradient compensation in large aerial reconstructions.

Persistent output: Partitioned aerial Gaussian scene.

Scope: Evidence concerns reconstruction quality and scalability, rather than navigation or physical interaction.

Code status: `unverified` (checked 2026-11-07).


### ReconDreamer#

- **ReconDreamer#: Self-Evolving Closed-Loop Synergy of Reconstruction and Generation for Dynamic Driving Scenes**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2611.04173)

First submission: **2026-11-03** · Checked version: **v1 (2026-11-03)** · Added: **2026-11-07**.

Placement: [topic 2.3](../README.md#paper-research2026recondreamer).

Iteratively improves generation and reconstruction with an adaptive geometry-prior ground model.

Persistent output: Dynamic driving-scene representation.

Scope: Closed loop refers to reconstruction–generation refinement, rather than a planner/controller loop. This is a separate paper ID.

Code status: `unverified` (checked 2026-11-07).


### OccSplat

- **Quo Vadis, Driving Scene Reconstruction? Occlusion-Aware Gaussian Densification**\
  <sub>CV4DC / ACCV Workshop 2026 (accepted)</sub> · [📄 Paper](https://arxiv.org/abs/2611.06273)

First submission: **2026-11-04** · Checked version: **v1 (2026-11-04)** · Added: **2026-11-07**.

Placement: [topic 2.3](../README.md#paper-research2026occsplat).

Maps unsupported occluded regions and completes them by adding persistent Gaussian primitives.

Persistent output: Gaussian primitives added to occluded regions.

Scope: Completes the 3D representation rather than only rendered pixels; inferred unseen geometry is not measurement ground truth.

Code status: `unverified` (checked 2026-11-07).


### PointForward V2

- **PointForward V2: Point-Aligned Interaction for Feedforward Driving Reconstruction**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2610.28120)

First submission: **2026-10-20** · Checked version: **v1 (2026-10-20)** · Added: **2026-11-07**.

Placement: [topic 2.3](../README.md#paper-research2026pointforwardv2).

Uses compact static and dynamic registers for point-aligned interaction across views and times.

Persistent output: Static and object-aligned dynamic scene representation.

Scope: Verified at abstract level; V2 code availability is not inherited from PointForward.

Code status: `unverified` (checked 2026-11-07).


### TerrainForge

- **TerrainForge: Physics-Grounded Road Geometry Editing for Counterfactual Autonomous Driving**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2610.02825)

First submission: **2026-10-02** · Checked version: **v2 (2026-10-11)** · Added: **2026-11-07**.

Placement: [topic 3.3](../README.md#paper-research2026terrainforge).

Propagates road-shape and friction edits through vehicle dynamics, camera viewpoint and inter-vehicle clearance.

Persistent output: Edited road geometry, friction and dependent vehicle state.

Scope: Physics is compared with CarSim in specified settings; no unrelated procedural-terrain repository is linked.

Code status: `unverified` (checked 2026-11-07).


### IGSW

- **IGSW: Multi-Weather Urban Scene Reconstruction with Intrinsic-Decoupled Gaussian Splatting**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2611.04374) · [🌐 Project](https://akaxi6.github.io/IGSW/) · [📌 Release plan](https://github.com/Akaxi6/IGSW_IntrinsicGSWeather) · <sub>⏳ Code pending</sub>

First submission: **2026-11-03** · Checked version: **v1 (2026-11-03)** · Added: **2026-11-07**.

Placement: [topic 3.3](../README.md#paper-research2026igsw).

Separates shared scene structure from weather-dependent appearance and rejects unreliable teacher regions.

Persistent output: Intrinsic-decoupled multi-weather 4D Gaussians.

Scope: Weather appearance control does not establish corresponding friction, wind or other physical-property changes.

Code status: `planned` (checked 2026-11-07).


### Drive3R

- **Drive3R: Block-wise Streaming Geometric Foundation Models for Autonomous Driving**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2610.15112) · [💻 Code](https://github.com/AutoLab-SAI-SJTU/Drive3R)

First submission: **2026-10-10** · Checked version: **v1 (2026-10-10)** · Added: **2026-11-07**.

Placement: [topic 2.2](../README.md#paper-research2026drive3r).

Streams long driving sequences through block-wise geometry estimation with confidence-aware re-anchoring.

Persistent output: World-frame points and camera poses.

Scope: A driving-specific geometric support method; not a complete simulator or physical scene package.

Code status: `released` (checked 2026-11-07).


### MCSplat

- **MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes**\
  <sub>NeurIPS 2026 (accepted)</sub> · [📄 Paper](https://arxiv.org/abs/2610.25345)

First submission: **2026-10-18** · Checked version: **v1 (2026-10-18)** · Added: **2026-11-07**.

Placement: [topic 2.3](../README.md#paper-research2026mcsplat).

Separates camera-specific appearance from canonical scene appearance to reduce geometric artifacts.

Persistent output: Multi-camera-consistent driving Gaussians.

Scope: Evidence concerns geometry and rendering consistency; simulator physics is not established.

Code status: `unverified` (checked 2026-11-07).


### LangStreet

- **LangStreet: Persistent Language Fields for Anchor-Decoded Street Gaussians**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2609.11616) · <sub>⏳ Code pending</sub>

First submission: **2026-09-10** · Checked version: **v1 (2026-09-10)** · Added: **2026-11-07**.

Placement: [topic 2.4](../README.md#paper-research2026langstreet).

Attaches stable semantic ownership to persistent street-scene anchors and decoder slots.

Persistent output: Persistent anchor/slot language fields.

Scope: A semantic-query layer for driving scenes; semantic benchmarks do not establish physical interaction.

Code status: `planned` (checked 2026-11-07).


### World from Motion

- **World from Motion: Generative Dynamic Gaussian Reconstruction from Monocular Video**\
  <sub>NeurIPS 2026 (accepted)</sub> · [📄 Paper](https://arxiv.org/abs/2607.01202) · [🌐 Project](https://research.nvidia.com/labs/amri/projects/world-from-motion/) · [💻 Partial code](https://github.com/GradientSpaces/World-from-Motion)

First submission: **2026-07-01** · Checked version: **v2 (2026-10-23)** · Added: **2026-11-07**.

Placement: [topic 2.3](../README.md#paper-research2026worldfrommotion).

Distills generated novel-view content and motion back into a persistent monocular-video reconstruction.

Persistent output: Dynamic 3D Gaussians with distilled generative completion.

Scope: Historical omission, first submitted in July. Generic 4D reconstruction includes outdoor examples; driving/UAV policy benefits are not established.

Code status: `partial` (checked 2026-11-07).


### HieraScaffold

- **HieraScaffold: Learning Compact Hierarchical Representations for Scalable 4D LiDAR Generation**\
  <sub>ICML 2026</sub> · [📄 Paper](https://proceedings.mlr.press/v306/wu26cf.html)

First submission: **unverified (formal ICML 2026 proceedings confirmed)** · Checked version: **formal proceedings** · Added: **2026-11-07**.

Placement: [topic 1.3](../README.md#paper-research2026hierascaffold).

Generates outdoor 4D LiDAR with hierarchical geometry/motion decomposition and compact neural contourlets.

Persistent output: Hierarchical static geometry and temporal motion scaffold.

Scope: Historical omission from ICML 2026; not a full physical environment. Earliest preprint date was not established.

Code status: `unverified` (checked 2026-11-07).


## Outdoor / Mixed-Scene Evaluation


### Code4Scene

- **Code4Scene: Benchmarking Coding Agents for Constructing and Editing 3D Scenes**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2609.36777) · [💻 Code](https://github.com/SimWorld-AI/Code4Scene)

First submission: **2026-09-29** · Checked version: **v1 (2026-09-29)** · Added: **2026-11-07**.

Benchmarks construction and editing of persistent Unreal scenes, including validity and preservation of non-target content.

Persistent output: Engine-native scenes and evaluation artifacts.

Scope: Includes outdoor scenes. Runtime route execution is controller-specific; external scene assets are obtained separately.

Code status: `released` (checked 2026-11-07).


### Visibility-Aware Reference

- **Visibility-Aware Reference Generation for Benchmarking Visual 3D Reconstruction in Vegetation-Rich Environments**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2611.05361) · <sub>⏳ Code pending</sub>

First submission: **2026-11-03** · Checked version: **v1 (2026-11-03)** · Added: **2026-11-07**.

Builds camera-visible geometric references from images, LiDAR and poses for vegetation-rich outdoor evaluation.

Persistent output: Visibility-filtered depth and reference point clouds.

Scope: Evaluates reference coverage and reconstruction; does not generate an interactive simulation world.

Code status: `planned` (checked 2026-11-07).


## Scoped Methodological References


### PERSIST

- **Beyond Pixel Histories: World Models with Persistent 3D State**\
  <sub>ICML 2026</sub> · [📄 Paper](https://proceedings.mlr.press/v306/garcin26a.html) · [💻 Code](https://github.com/francelico/PERSIST) · [📝 Preprint](https://arxiv.org/abs/2603.03482)

First submission: **2026-03-03** · Checked version: **v2 (2026-06-03)** · Added: **2026-11-07**.

Maintains persistent 3D world state and supports geometry-aware editing in interactive world generation.

Persistent output: Latent 3D environment, camera and renderer.

Scope: Game-world evidence in Craftium/OpenWorldCreative; retained as a scoped mechanism reference.

Code status: `released` (checked 2026-11-07).


### Puffin-World

- **Puffin-World: Scaling a Unified Multimodal Model with Native 3D World States**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2609.04196) · [🌐 Project](https://kangliao929.github.io/projects/puffin-world/) · [💻 Code](https://github.com/KangLiao929/Puffin)

First submission: **2026-09-03** · Checked version: **v1 (2026-09-03)** · Added: **2026-11-07**.

Unifies multimodal perception and generation with native 3D world-state components.

Persistent output: Camera, depth and appearance with aligned point-cloud outputs.

Scope: General mechanism with outdoor examples; a persistent global map and robot-control loop have not been established.

Code status: `released` (checked 2026-11-07).


### SceneRig

- **SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images**\
  <sub>CoRL Agentic Robotics Workshop 2026 (accepted)</sub> · [📄 Paper](https://arxiv.org/abs/2610.28585)

First submission: **2026-10-20** · Checked version: **v1 (2026-10-20)** · Added: **2026-11-07**.

Uses geometry, vision and physics tools in repeated reconstruction, editing and validation loops.

Persistent output: Editable scene assets validated inside a physics simulator.

Scope: Primarily indoor manipulation; robot-policy results do not establish outdoor applicability.

Code status: `unverified` (checked 2026-11-07).


### WEDGE

- **From Failures to Learnable Worlds: Policy-Conditioned Environment Generation for Navigation Agents**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2610.19420) · [🌐 Project](https://zhangyuejoslin.github.io/WEDGE/)

First submission: **2026-10-14** · Checked version: **v1 (2026-10-14)** · Added: **2026-11-07**.

Turns policy weaknesses into executable environment factors and targeted generation for navigation adaptation.

Persistent output: Policy-conditioned indoor layouts and object placements.

Scope: Already cited in the supplied manuscript; ProcTHOR/HM3D evidence remains explicitly indoor.

Code status: `unverified` (checked 2026-11-07).


## Evaluation and Runtime Extensions


### ScIntBench

- **ScIntBench: Physical Interaction Plausibility in 3D Scene Generation**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2610.37326) · [🌐 Project](https://scintbench.github.io/)

First submission: **2026-10-27** · Checked version: **v1 (2026-10-27)** · Added: **2026-11-07**.

Evaluates physical interaction plausibility through prescribed manipulation and post-interaction checks.

Persistent output: Interaction evaluation traces and scene-state checks.

Scope: Indoor benchmark; retained for transferable evaluation design, outside the outdoor resource count.

Code status: `unverified` (checked 2026-11-07).


### OneFixer

- **OneFixer: High-Quality and Consistent One-Step Autoregressive 3DGS Refinement for Driving Scenes**\
  <sub>arXiv 2026</sub> · [📄 Paper](https://arxiv.org/abs/2609.32175)

First submission: **2026-09-26** · Checked version: **v1 (2026-09-26)** · Added: **2026-11-07**.

Refines driving-scene renderings with one-step autoregressive diffusion and evaluates closed-loop driving.

Persistent output: Refined rendered observations; 3D write-back unverified.

Scope: Runtime observation refinement; persistence of edits in the underlying 3D state is not established.

Code status: `unverified` (checked 2026-11-07).


## Existing Record Updates

- **wang2026worldagentv1**: Official project explicitly says code coming soon.
- **zhang2026code2worlds2v1**: Source is public; frozen reference-package readiness is not a generated-environment success rate.

## Outside the Construction List

- [HorizonComposer: Spatiotemporally Consistent Driving Video Editing with Enriched Traffic Semantics](https://arxiv.org/abs/2610.28829): Video editing; persistent 3D-state write-back not established.
- [PRG-Fusion: Orchestrating Generative Priors with Reconstruction Evidence for Driving View Synthesis](https://arxiv.org/abs/2609.06948): Novel-trajectory observation synthesis; persistent 3D-state write-back not established.

[Structured records and primary-source links](../data/research-updates.json)
