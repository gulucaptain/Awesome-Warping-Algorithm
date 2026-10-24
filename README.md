<!-- Generated from data/catalog.json by scripts/build_readme.py. -->
<a id="top"></a>

<div align="center">

<img src="assets/warping-banner-v2.png" alt="Luminous coordinate grids deform into a continuous three-dimensional flow surface" width="100%">

# Awesome Warping Algorithms

*A curated atlas of spatial warping.*

**English** · [简体中文](README.zh-CN.md)

<p align="justify">
Warping maps pixels, features, and noise across space and time, providing a foundation for image alignment, 3D reconstruction, and controllable generation. This repository connects classical methods with recent advances, organizing papers and implementations into six research areas and their topics to help researchers navigate the field, compare approaches, and build on existing work.
</p>

<b>57</b> Papers &nbsp; · &nbsp; <b>37</b> Repositories &nbsp; · &nbsp; <b>6</b> Research areas &nbsp; · &nbsp; <b>16</b> Topics

</div>

---

<a id="start"></a>
## 🧭 Start here

| Your interest | Suggested reading |
| --- | --- |
| **Warping fundamentals** | [TPS](#c05) → [MLS](#c08) → [STN](#c13) → [Softmax Splatting](#c19) |
| **Motion and video alignment** | [PWC-Net](#c15) → [RAFT](#c20) → [GMFlow](#n01) → [SEA-RAFT](#n13) → [MEMFOF](#n20) |
| **Dynamic 3D deformation** | [D-NeRF](#c21) → [Nerfies](#c22) → [Deformable 3D Gaussians](#n11) → [4D-GS](#n12) |
| **Diffusion and motion control** | [∫-noise](#n16) → [Go-with-the-Flow](#n19) → [CameraNoise](#n24) · [GenWarp](#n15) → [SplatDiff](#n23) |

<details>
<summary><b>Scope and publication dates</b></summary>

The collection focuses on **spatial warping** in computer vision, graphics and medical imaging. It distinguishes transformation models, correspondence estimators, resampling operators and application pipelines. Time-series DTW and GPU execution warps are outside its scope.

Entries follow **research area → topic**, with papers listed newest year first within each topic. Each topic opens with a scope and paper-count block. Papers follow a consistent sequence: full paper title (venue and year), one row of resource badges followed by technique tags, and a contribution summary. Full publication histories, code provenance and limitations remain in the bilingual catalog and research guides. Horizontal rules separate methods; classical and recent work appear together without year navigation or year groups. Published work uses its representative publication year, and preprints use their preprint year; publication histories are retained. Entries combining foundational methods use the publication year of the linked representative paper. Undated foundations appear last within their topic. Entries from the same year retain catalog order. Coverage ends on 2026-10-24. Descriptions are grounded in papers and author resources; the collection does not claim a unified reproduction of all methods.

Each work has one primary topic, with related tags and reading links for other directions. Spatial reasoning, world models, interactive simulation and embodied agents are reserved for future work directly connected to warping.

[Definitions, mapping conventions and evidence policy →](docs/RESEARCH_GUIDE.md#scope)

</details>

<a id="topics"></a>
## 🗂️ Topic navigation

6 research areas and 16 topics, including 4 reserved topics. Counts include primary entries only; related reading is not counted twice.

<table>
<thead>
<tr><th align="left">Research area</th><th align="left">Topic</th><th align="left">Primary entries / status</th></tr>
</thead>
<tbody>
<tr>
<td rowspan="2" valign="middle"><a href="#area-foundations">1. Warping Foundations &amp; Operators</a></td>
<td><a href="#topic-geometry-editing">1.1 Geometric Transformations &amp; Deformation Editing</a></td>
<td>8</td>
</tr>
<tr>
<td><a href="#topic-sampling-splatting">1.2 Differentiable Sampling &amp; Splatting</a></td>
<td>3</td>
</tr>
<tr>
<td rowspan="3" valign="middle"><a href="#area-alignment">2. Correspondence &amp; Image Alignment</a></td>
<td><a href="#topic-optical-flow">2.1 Optical Flow &amp; Dense Correspondence</a></td>
<td>10</td>
</tr>
<tr>
<td><a href="#topic-image-alignment">2.2 Image Registration, Stitching &amp; Stabilization</a></td>
<td>5</td>
</tr>
<tr>
<td><a href="#topic-medical-registration">2.3 Medical Registration &amp; Diffeomorphic Deformation</a></td>
<td>8</td>
</tr>
<tr>
<td rowspan="2" valign="middle"><a href="#area-video-processing">3. Video Processing &amp; Human Deformation</a></td>
<td><a href="#topic-video-restoration">3.1 Video Interpolation &amp; Restoration</a></td>
<td>5</td>
</tr>
<tr>
<td><a href="#topic-human-deformation">3.2 Animation, Motion Transfer &amp; Virtual Try-On</a></td>
<td>4</td>
</tr>
<tr>
<td rowspan="2" valign="middle"><a href="#area-video-generation">4. Video Generation &amp; Motion Control</a></td>
<td><a href="#topic-noise-warping">4.1 Noise Warping &amp; Temporal Consistency</a></td>
<td>1</td>
</tr>
<tr>
<td><a href="#topic-controlled-generation">4.2 Camera-, Trajectory- &amp; Motion-Controlled Generation</a></td>
<td>3</td>
</tr>
<tr>
<td rowspan="4" valign="middle"><a href="#area-spatial-intelligence">5. Spatial Intelligence</a></td>
<td><a href="#topic-spatial-perception">5.1 Spatial Perception, Depth &amp; 3D Reconstruction</a></td>
<td>1</td>
</tr>
<tr>
<td><a href="#topic-novel-view-synthesis">5.2 Reprojection &amp; Novel View Synthesis</a></td>
<td>4</td>
</tr>
<tr>
<td><a href="#topic-dynamic-3d">5.3 Dynamic 3D &amp; 4D Scenes</a></td>
<td>5</td>
</tr>
<tr>
<td><a href="#topic-spatial-reasoning">5.4 Spatial Reasoning &amp; Scene Memory</a></td>
<td>Reserved</td>
</tr>
<tr>
<td rowspan="3" valign="middle"><a href="#area-world-models-agents">6. World Models &amp; Embodied Agents</a></td>
<td><a href="#topic-world-models">6.1 World Models &amp; Environment Prediction</a></td>
<td>Reserved</td>
</tr>
<tr>
<td><a href="#topic-interactive-simulation">6.2 Interactive Environments &amp; Simulation</a></td>
<td>Reserved</td>
</tr>
<tr>
<td><a href="#topic-embodied-agents">6.3 Embodied Agents, Planning &amp; Control</a></td>
<td>Reserved</td>
</tr>
</tbody>
</table>

<a id="area-foundations"></a>
## 1. Warping Foundations & Operators

<a id="topic-08"></a>
<a id="topic-16"></a>
<a id="topic-geometry-editing"></a>
### 1.1 Geometric Transformations & Deformation Editing

> **Scope** · Parametric transforms, TPS, FFD, MLS, ARAP, morphing, frequency-aware deformation and warp–unwarp
>
> **8 papers · Newest first**

---

<a id="n26"></a>
#### WarpI2I: Image Warping for Image-to-Image Translation (ECCV 2026)

[![arXiv: 2606.31018](https://img.shields.io/badge/arXiv-2606.31018-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.31018) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2606.31018) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://shenzheng2000.github.io/WarpI2I.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ShenZheng2000/WarpI2I) [![GitHub stars](https://img.shields.io/github/stars/ShenZheng2000/WarpI2I?style=flat-square&label=stars&color=C58A18)](https://github.com/ShenZheng2000/WarpI2I/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ShenZheng2000/WarpI2I?style=flat-square&label=forks&color=64748B)](https://github.com/ShenZheng2000/WarpI2I/forks) &nbsp; [`T2`](#t2) [`T9`](#t9)

Uses a saliency-guided warp before encoding to allocate more spatial representation to salient regions, then unwarps the output to improve structural preservation in compact latent models.

---

<a id="n21"></a>
#### LookingGlass: Generative Anamorphoses via Laplacian Pyramid Warping (CVPR 2025)

[![arXiv: 2504.08902](https://img.shields.io/badge/arXiv-2504.08902-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.08902) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2504.08902) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://lookingglass-lpw.github.io/) &nbsp; [`T7`](#t7) [`T9`](#t9)

Uses Laplacian pyramids for frequency-aware image warping and view aggregation, enabling multiview generative anamorphoses.

---

<a id="c09"></a>
#### As-Rigid-As-Possible Surface Modeling (SGP 2007)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://igl.ethz.ch/projects/ARAP/arap_web.pdf) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://igl.ethz.ch/projects/ARAP/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/libigl/libigl) [![GitHub stars](https://img.shields.io/github/stars/libigl/libigl?style=flat-square&label=stars&color=C58A18)](https://github.com/libigl/libigl/stargazers) [![GitHub forks](https://img.shields.io/github/forks/libigl/libigl?style=flat-square&label=forks&color=64748B)](https://github.com/libigl/libigl/forks) &nbsp; [`T3`](#t3)

Sorkine and Alexa preserve local shape through an as-rigid-as-possible energy, establishing a widely used approach to detail-preserving mesh editing.

---

<a id="c08"></a>
#### Image deformation using moving least squares (SIGGRAPH / TOG 2006)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1145/1141911.1141920) &nbsp; [`T2`](#t2)

Schaefer and colleagues construct affine, similarity and rigid image deformations through locally weighted fitting, enabling interactive point and line controls.

---

<a id="c06"></a>
#### Feature-Based Image Metamorphosis (SIGGRAPH 1992)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://wcours.gel.ulaval.ca/GIF4105/old/h20/tps/tp3/beierneely92.pdf) &nbsp; [`T2`](#t2)

Uses corresponding feature-line pairs to control an inverse warp, then blends image colors to produce morphing effects.

---

<a id="c05"></a>
#### Principal warps: thin-plate splines and the decomposition of deformations (TPAMI 1989)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1109/34.24792) &nbsp; [`T2`](#t2)

Bookstein uses thin-plate splines for landmark-based deformation analysis, defining smooth nonrigid maps through bending energy. The underlying mathematics of TPS predates this paper.

---

<a id="c04"></a>
#### Free-Form Deformation of Solid Geometric Models (SIGGRAPH 1986)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.cse.iitd.ac.in/~jatin/minor_p/papers/sederberg.pdf) &nbsp; [`T2`](#t2)

Sederberg and Parry deform geometric objects through a control lattice and Bernstein polynomials, establishing a foundation for volumetric free-form deformation.

---

<a id="c01"></a>
#### Rigid / Similarity / Affine / Homography (Foundational models)

[![Reference: Read](https://img.shields.io/badge/Reference-Read-2563EB?style=flat-square)](https://docs.opencv.org/4.x/d9/dab/tutorial_homography.html) &nbsp; [`T1`](#t1)

Global rigid, similarity, affine and projective maps provide compact coordinate transformations. A homography models a plane or a change of view under pure rotation about a fixed optical center.

---

<details>
<summary>Related reading · 1 papers in other topics</summary>

- [EWA Volume Splatting](#c25) (2001)

</details>

[↑ Start of 1.1](#topic-geometry-editing) · [↑ Back to topic navigation](#topics)

---

<a id="topic-15"></a>
<a id="topic-sampling-splatting"></a>
### 1.2 Differentiable Sampling & Splatting

> **Scope** · Interpolation, resampling, differentiable spatial transforms, sampling kernels, adjoints and derivatives
>
> **3 papers · Newest first**

---

<a id="n10"></a>
#### ImWIP: Open-source image warping toolbox with adjoints and derivatives (SoftwareX 2023)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1016/j.softx.2023.101524) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://imwip.readthedocs.io/en/latest/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/RendersJens/ImWIP) [![GitHub stars](https://img.shields.io/github/stars/RendersJens/ImWIP?style=flat-square&label=stars&color=C58A18)](https://github.com/RendersJens/ImWIP/stargazers) [![GitHub forks](https://img.shields.io/github/forks/RendersJens/ImWIP?style=flat-square&label=forks&color=64748B)](https://github.com/RendersJens/ImWIP/forks) &nbsp; [`T7`](#t7)

Provides differentiable image-warp operators with exact discrete adjoints and derivatives for inverse-problem optimization.

---

<a id="c13"></a>
#### Spatial Transformer Networks (NeurIPS 2015)

[![arXiv: 1506.02025](https://img.shields.io/badge/arXiv-1506.02025-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1506.02025) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/1506.02025) &nbsp; [`T7`](#t7)

Jointly trains transformation prediction, grid generation and differentiable sampling, making spatial transformation a learnable neural-network module.

---

<a id="c25"></a>
#### EWA Volume Splatting (IEEE Visualization 2001)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://dash.harvard.edu/bitstream/handle/1/4138240/Zwicker_EWA.pdf) &nbsp; [`T7`](#t7)

Uses elliptical weighted-average kernels for projected reconstruction and low-pass filtering, providing a classic reference for splat footprints and antialiasing.

---

<details>
<summary>Related reading · 2 papers in other topics</summary>

- [Warped Diffusion](#n17) (2024)
- [B-spline FFD Registration](#c07) (1999)

</details>

[↑ Start of 1.2](#topic-sampling-splatting) · [↑ Back to topic navigation](#topics)

---

<a id="area-alignment"></a>
## 2. Correspondence & Image Alignment

<a id="topic-05"></a>
<a id="topic-optical-flow"></a>
### 2.1 Optical Flow & Dense Correspondence

> **Scope** · Motion estimation, correlation volumes, global matching and multiframe correspondence
>
> **10 papers · Newest first**

---

<a id="n20"></a>
#### MEMFOF: High-Resolution Training for Memory-Efficient Multi-Frame Optical Flow Estimation (ICCV 2025)

[![arXiv: 2506.23151](https://img.shields.io/badge/arXiv-2506.23151-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.23151) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2506.23151) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://msu-video-group.github.io/memfof/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/msu-video-group/memfof) [![GitHub stars](https://img.shields.io/github/stars/msu-video-group/memfof?style=flat-square&label=stars&color=C58A18)](https://github.com/msu-video-group/memfof/stargazers) [![GitHub forks](https://img.shields.io/github/forks/msu-video-group/memfof?style=flat-square&label=forks&color=64748B)](https://github.com/msu-video-group/memfof/forks) &nbsp; [`T4`](#t4)

Combines reduced correlation representations, multiframe estimation and high-resolution training to improve memory efficiency for native FullHD optical flow.

---

<a id="n13"></a>
#### SEA-RAFT: Simple, Efficient, Accurate RAFT for Optical Flow (ECCV 2024)

[![arXiv: 2405.14793](https://img.shields.io/badge/arXiv-2405.14793-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2405.14793) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2405.14793) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/princeton-vl/SEA-RAFT) [![GitHub stars](https://img.shields.io/github/stars/princeton-vl/SEA-RAFT?style=flat-square&label=stars&color=C58A18)](https://github.com/princeton-vl/SEA-RAFT/stargazers) [![GitHub forks](https://img.shields.io/github/forks/princeton-vl/SEA-RAFT?style=flat-square&label=forks&color=64748B)](https://github.com/princeton-vl/SEA-RAFT/forks) &nbsp; [`T4`](#t4)

Improves RAFT's efficiency and accuracy through initial-flow regression, a mixture-of-Laplace loss and rigid-motion pretraining.

---

<a id="n09"></a>
#### Unifying Flow, Stereo and Depth Estimation (TPAMI 2023)

[![arXiv: 2211.05783](https://img.shields.io/badge/arXiv-2211.05783-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2211.05783) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2211.05783) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://haofeixu.github.io/unimatch/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/autonomousvision/unimatch) [![GitHub stars](https://img.shields.io/github/stars/autonomousvision/unimatch?style=flat-square&label=stars&color=C58A18)](https://github.com/autonomousvision/unimatch/stargazers) [![GitHub forks](https://img.shields.io/github/forks/autonomousvision/unimatch?style=flat-square&label=forks&color=64748B)](https://github.com/autonomousvision/unimatch/forks) &nbsp; [`T4`](#t4) [`T6`](#t6)

Unifies optical flow, stereo disparity and depth from posed views as dense correspondence-matching problems.

---

<a id="n01"></a>
#### GMFlow: Learning Optical Flow via Global Matching (CVPR 2022)

[![arXiv: 2111.13680](https://img.shields.io/badge/arXiv-2111.13680-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2111.13680) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2111.13680) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/haofeixu/gmflow) [![GitHub stars](https://img.shields.io/github/stars/haofeixu/gmflow?style=flat-square&label=stars&color=C58A18)](https://github.com/haofeixu/gmflow/stargazers) [![GitHub forks](https://img.shields.io/github/forks/haofeixu/gmflow?style=flat-square&label=forks&color=64748B)](https://github.com/haofeixu/gmflow/forks) &nbsp; [`T4`](#t4)

Uses Transformer-enhanced cross-image features and global matching to estimate flow with less reliance on long sequences of iterative refinement.

---

<a id="n02"></a>
#### FlowFormer: A Transformer Architecture for Optical Flow (ECCV 2022)

[![arXiv: 2203.16194](https://img.shields.io/badge/arXiv-2203.16194-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2203.16194) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://drinkingcoder.github.io/publication/flowformer/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/drinkingcoder/FlowFormer-Official) [![GitHub stars](https://img.shields.io/github/stars/drinkingcoder/FlowFormer-Official?style=flat-square&label=stars&color=C58A18)](https://github.com/drinkingcoder/FlowFormer-Official/stargazers) [![GitHub forks](https://img.shields.io/github/forks/drinkingcoder/FlowFormer-Official?style=flat-square&label=forks&color=64748B)](https://github.com/drinkingcoder/FlowFormer-Official/forks) &nbsp; [`T4`](#t4)

Encodes a 4D cost volume with Transformers and recurrently decodes motion updates.

---

<a id="c20"></a>
#### RAFT: Recurrent All-Pairs Field Transforms for Optical Flow (ECCV 2020)

[![arXiv: 2003.12039](https://img.shields.io/badge/arXiv-2003.12039-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2003.12039) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2003.12039) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/princeton-vl/RAFT) [![GitHub stars](https://img.shields.io/github/stars/princeton-vl/RAFT?style=flat-square&label=stars&color=C58A18)](https://github.com/princeton-vl/RAFT/stargazers) [![GitHub forks](https://img.shields.io/github/forks/princeton-vl/RAFT?style=flat-square&label=forks&color=64748B)](https://github.com/princeton-vl/RAFT/forks) &nbsp; [`T4`](#t4)

Builds all-pairs correlation volumes and updates a dense flow field recurrently, providing an influential baseline for correspondence estimation.

---

<a id="c15"></a>
#### PWC-Net: CNNs for Optical Flow Using Pyramid, Warping, and Cost Volume (CVPR 2018)

[![arXiv: 1709.02371](https://img.shields.io/badge/arXiv-1709.02371-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1709.02371) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/NVlabs/PWC-Net) [![GitHub stars](https://img.shields.io/github/stars/NVlabs/PWC-Net?style=flat-square&label=stars&color=C58A18)](https://github.com/NVlabs/PWC-Net/stargazers) [![GitHub forks](https://img.shields.io/github/forks/NVlabs/PWC-Net?style=flat-square&label=forks&color=64748B)](https://github.com/NVlabs/PWC-Net/forks) &nbsp; [`T4`](#t4)

Combines feature pyramids, feature warping and cost volumes to learn residual motion from coarse to fine.

---

<a id="c02"></a>
#### Lucas-Kanade 20 Years On: A Unifying Framework (IJCV 2004)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.ri.cmu.edu/pub_files/pub3/baker_simon_2004_1/baker_simon_2004_1.pdf) &nbsp; [`T1`](#t1) [`T4`](#t4)

Optimizes warp parameters using image residuals. The inverse compositional formulation reuses parts of the computation and remains a foundation of direct image alignment.

---

<a id="c27"></a>
#### High Accuracy Optical Flow Estimation Based on a Theory for Warping (ECCV 2004)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.mia.uni-saarland.de/Publications/brox-eccv04-of.pdf) &nbsp; [`T4`](#t4)

Combines brightness and gradient constancy with edge-preserving regularization, and gives a theoretical interpretation of coarse-to-fine warping in the numerical solver.

---

<a id="c03"></a>
#### Determining optical flow (Artificial Intelligence 1981)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1016/0004-3702(81)90024-2) &nbsp; [`T4`](#t4)

Combines brightness constancy with a global smoothness regularizer, establishing a classical variational formulation of dense optical flow.

[↑ Start of 2.1](#topic-optical-flow) · [↑ Back to topic navigation](#topics)

---

<a id="topic-01"></a>
<a id="topic-03"></a>
<a id="topic-04"></a>
<a id="topic-image-alignment"></a>
### 2.2 Image Registration, Stitching & Stabilization

> **Scope** · Image alignment, panoramic stitching, parallax handling and temporal stabilization
>
> **5 papers · Newest first**

---

<a id="n25"></a>
#### DMAligner: Enhancing Image Alignment via Diffusion Model Based View Synthesis (CVPR 2026)

[![arXiv: 2602.23022](https://img.shields.io/badge/arXiv-2602.23022-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.23022) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://boomluo02.github.io/DMAligner/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/boomluo02/DMAligner) [![GitHub stars](https://img.shields.io/github/stars/boomluo02/DMAligner?style=flat-square&label=stars&color=C58A18)](https://github.com/boomluo02/DMAligner/stargazers) [![GitHub forks](https://img.shields.io/github/forks/boomluo02/DMAligner?style=flat-square&label=forks&color=64748B)](https://github.com/boomluo02/DMAligner/forks) &nbsp; [`T9`](#t9)

Recasts image alignment as diffusion-based view synthesis, using dynamics-aware training to address occlusion and illumination variation.

---

<a id="n28"></a>
#### Eliminating Warping Shakes for Unsupervised Online Video Stitching (ECCV 2024)

[![arXiv: 2403.06378](https://img.shields.io/badge/arXiv-2403.06378-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2403.06378) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2403.06378) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nie-lang/StabStitch) [![GitHub stars](https://img.shields.io/github/stars/nie-lang/StabStitch?style=flat-square&label=stars&color=C58A18)](https://github.com/nie-lang/StabStitch/stargazers) [![GitHub forks](https://img.shields.io/github/forks/nie-lang/StabStitch?style=flat-square&label=forks&color=64748B)](https://github.com/nie-lang/StabStitch/forks) &nbsp; [`T2`](#t2) [`T3`](#t3)

Unifies video stitching and stabilization in an unsupervised online framework, constraining spatial alignment and temporal stability to suppress warping shake.

---

<a id="n08"></a>
#### Parallax-Tolerant Unsupervised Deep Image Stitching (ICCV 2023)

[![arXiv: 2302.08207](https://img.shields.io/badge/arXiv-2302.08207-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2302.08207) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2302.08207) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nie-lang/UDIS2) [![GitHub stars](https://img.shields.io/github/stars/nie-lang/UDIS2?style=flat-square&label=stars&color=C58A18)](https://github.com/nie-lang/UDIS2/stargazers) [![GitHub forks](https://img.shields.io/github/forks/nie-lang/UDIS2?style=flat-square&label=forks&color=64748B)](https://github.com/nie-lang/UDIS2/forks) &nbsp; [`T1`](#t1) [`T2`](#t2) [`T3`](#t3)

Combines global homography with local TPS, jointly considering overlap alignment, non-overlap shape preservation and seam composition.

---

<a id="c12"></a>
#### As-Projective-As-Possible Image Stitching with Moving DLT (CVPR 2013)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content_cvpr_2013/papers/Zaragoza_As-Projective-As-Possible_Image_Stitching_2013_CVPR_paper.pdf) &nbsp; [`T3`](#t3)

Zaragoza and colleagues allow local departures from a global projective map through Moving DLT, accommodating parallax and nonplanarity in image stitching.

---

<a id="c29"></a>
#### Content-Preserving Warps for 3D Video Stabilization (SIGGRAPH / TOG 2009)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://pages.cs.wisc.edu/~fliu/papers/siggraph09.pdf) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://web.cecs.pdx.edu/~fliu/project/3dstab.htm) &nbsp; [`T3`](#t3)

Combines reconstructed 3D camera motion with content-preserving mesh warps to stabilize video while balancing alignment and salient-region shape.

---

<details>
<summary>Related reading · 4 papers in other topics</summary>

- [Lucas–Kanade / Inverse Compositional](#c02) (2004)
- [B-spline FFD Registration](#c07) (1999)
- [Thin-Plate Spline (TPS) / Principal Warps](#c05) (1989)
- [Rigid / Similarity / Affine / Homography](#c01) (Foundational models (undated))

</details>

[↑ Start of 2.2](#topic-image-alignment) · [↑ Back to topic navigation](#topics)

---

<a id="topic-02"></a>
<a id="topic-medical-registration"></a>
### 2.3 Medical Registration & Diffeomorphic Deformation

> **Scope** · Cross-modal registration, diffeomorphisms, topology preservation and inverse consistency
>
> **8 papers · Newest first**

---

<a id="n14"></a>
#### uniGradICON: A Foundation Model for Medical Image Registration (MICCAI 2024)

[![arXiv: 2403.05780](https://img.shields.io/badge/arXiv-2403.05780-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2403.05780) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/uncbiag/uniGradICON) [![GitHub stars](https://img.shields.io/github/stars/uncbiag/uniGradICON?style=flat-square&label=stars&color=C58A18)](https://github.com/uncbiag/uniGradICON/stargazers) [![GitHub forks](https://img.shields.io/github/forks/uncbiag/uniGradICON?style=flat-square&label=forks&color=64748B)](https://github.com/uncbiag/uniGradICON/forks) &nbsp; [`T5`](#t5)

Moves learned registration toward a reusable model across datasets, anatomical regions and new tasks, including zero-shot use and initialization for adaptation.

---

<a id="n05"></a>
#### TransMorph: Transformer for unsupervised medical image registration (Medical Image Analysis 2022)

[![arXiv: 2111.10480](https://img.shields.io/badge/arXiv-2111.10480-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2111.10480) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration) [![GitHub stars](https://img.shields.io/github/stars/junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration?style=flat-square&label=stars&color=C58A18)](https://github.com/junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration/stargazers) [![GitHub forks](https://img.shields.io/github/forks/junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration?style=flat-square&label=forks&color=64748B)](https://github.com/junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration/forks) &nbsp; [`T5`](#t5)

Uses a hybrid Transformer–ConvNet architecture to model long-range relationships in volumetric medical registration.

---

<a id="n06"></a>
#### SynthMorph: learning contrast-invariant registration without acquired images (IEEE TMI 2022)

[![arXiv: 2004.10282](https://img.shields.io/badge/arXiv-2004.10282-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2004.10282) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2004.10282) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://w3id.org/synthmorph) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/voxelmorph/voxelmorph) [![GitHub stars](https://img.shields.io/github/stars/voxelmorph/voxelmorph?style=flat-square&label=stars&color=C58A18)](https://github.com/voxelmorph/voxelmorph/stargazers) [![GitHub forks](https://img.shields.io/github/forks/voxelmorph/voxelmorph?style=flat-square&label=forks&color=64748B)](https://github.com/voxelmorph/voxelmorph/forks) &nbsp; [`T5`](#t5)

Trains with synthetic label maps and diverse image appearances to improve deformable registration across MRI contrasts.

---

<a id="c18"></a>
#### VoxelMorph: A Learning Framework for Deformable Medical Image Registration (IEEE TMI 2019)

[![arXiv: 1809.05231](https://img.shields.io/badge/arXiv-1809.05231-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1809.05231) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://voxelmorph.csail.mit.edu/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/voxelmorph/voxelmorph) [![GitHub stars](https://img.shields.io/github/stars/voxelmorph/voxelmorph?style=flat-square&label=stars&color=C58A18)](https://github.com/voxelmorph/voxelmorph/stargazers) [![GitHub forks](https://img.shields.io/github/forks/voxelmorph/voxelmorph?style=flat-square&label=forks&color=64748B)](https://github.com/voxelmorph/voxelmorph/forks) &nbsp; [`T5`](#t5)

Amortizes pairwise optimization into a network that predicts deformation fields, trained with differentiable warping and image-similarity objectives.

---

<a id="c11"></a>
#### Diffeomorphic demons: Efficient non-parametric image registration (NeuroImage 2009)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1016/j.neuroimage.2008.10.040) &nbsp; [`T5`](#t5)

Introduces diffeomorphic updates within the Demons framework, combining efficient nonparametric registration with smooth, invertible deformation models.

---

<a id="c10"></a>
#### Symmetric Diffeomorphic Image Registration with Cross-Correlation: Evaluating Automated Labeling of Elderly and Neurodegenerative Brain (Medical Image Analysis 2008)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2276735/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ANTsX/ANTs) [![GitHub stars](https://img.shields.io/github/stars/ANTsX/ANTs?style=flat-square&label=stars&color=C58A18)](https://github.com/ANTsX/ANTs/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ANTsX/ANTs?style=flat-square&label=forks&color=64748B)](https://github.com/ANTsX/ANTs/forks) &nbsp; [`T5`](#t5)

Uses symmetric diffeomorphic registration with cross-correlation for anatomical alignment; SyN is a representative method in ANTs.

---

<a id="c26"></a>
#### Computing Large Deformation Metric Mappings via Geodesic Flows of Diffeomorphisms (IJCV 2005)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.cs.jhu.edu/~misha/ReadingSeminar/Papers/Beg05.pdf) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://www.cis.jhu.edu/software/lddmm-volume/index.php) &nbsp; [`T5`](#t5)

Beg and colleagues construct large diffeomorphic deformations through smooth velocity fields and geodesic flows, forming a foundation of computational anatomy.

---

<a id="c07"></a>
#### Nonrigid registration using free-form deformations: application to breast MR images (IEEE TMI 1999)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1109/42.796284) &nbsp; [`T2`](#t2) [`T5`](#t5)

Rueckert and colleagues combine global affine alignment with local B-spline free-form deformation for nonrigid breast MR registration.

[↑ Start of 2.3](#topic-medical-registration) · [↑ Back to topic navigation](#topics)

---

<a id="area-video-processing"></a>
## 3. Video Processing & Human Deformation

<a id="topic-06"></a>
<a id="topic-07"></a>
<a id="topic-video-restoration"></a>
### 3.1 Video Interpolation & Restoration

> **Scope** · Interpolation, super-resolution, denoising, inpainting, cross-frame feature alignment and video inverse problems
>
> **5 papers · Newest first**

---

<a id="n17"></a>
#### Warped Diffusion: Solving Video Inverse Problems with Image Diffusion Models (NeurIPS 2024)

[![arXiv: 2410.16152](https://img.shields.io/badge/arXiv-2410.16152-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2410.16152) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2410.16152) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://giannisdaras.github.io/warped_diffusion.github.io/) &nbsp; [`T9`](#t9)

Uses continuous function spaces and transformation equivariance for video inverse problems, improving temporal consistency with test-time self-equivariance guidance.

---

<a id="n04"></a>
#### FILM: Frame Interpolation for Large Motion (ECCV 2022)

[![arXiv: 2202.04901](https://img.shields.io/badge/arXiv-2202.04901-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2202.04901) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2202.04901) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://film-net.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/google-research/frame-interpolation) [![GitHub stars](https://img.shields.io/github/stars/google-research/frame-interpolation?style=flat-square&label=stars&color=C58A18)](https://github.com/google-research/frame-interpolation/stargazers) [![GitHub forks](https://img.shields.io/github/forks/google-research/frame-interpolation?style=flat-square&label=forks&color=64748B)](https://github.com/google-research/frame-interpolation/forks) &nbsp; [`T4`](#t4) [`T8`](#t8)

Shares feature extraction and motion estimation across scales to improve large-motion frame interpolation using training from image frames alone.

---

<a id="n07"></a>
#### BasicVSR++: Improving Video Super-Resolution with Enhanced Propagation and Alignment (CVPR 2022)

[![arXiv: 2104.13371](https://img.shields.io/badge/arXiv-2104.13371-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2104.13371) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2104.13371) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ckkelvinchan/BasicVSR_PlusPlus) [![GitHub stars](https://img.shields.io/github/stars/ckkelvinchan/BasicVSR_PlusPlus?style=flat-square&label=stars&color=C58A18)](https://github.com/ckkelvinchan/BasicVSR_PlusPlus/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ckkelvinchan/BasicVSR_PlusPlus?style=flat-square&label=forks&color=64748B)](https://github.com/ckkelvinchan/BasicVSR_PlusPlus/forks) &nbsp; [`T4`](#t4) [`T8`](#t8)

Combines second-order propagation with flow-guided deformable alignment to integrate optical-flow priors and adaptive feature sampling for video restoration.

---

<a id="c19"></a>
#### Softmax Splatting for Video Frame Interpolation (CVPR 2020)

[![arXiv: 2003.05534](https://img.shields.io/badge/arXiv-2003.05534-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2003.05534) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://sniklaus.com/softsplat) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sniklaus/softmax-splatting) [![GitHub stars](https://img.shields.io/github/stars/sniklaus/softmax-splatting?style=flat-square&label=stars&color=C58A18)](https://github.com/sniklaus/softmax-splatting/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sniklaus/softmax-splatting?style=flat-square&label=forks&color=64748B)](https://github.com/sniklaus/softmax-splatting/forks) &nbsp; [`T7`](#t7)

Niklaus and Liu use softmax weighting to resolve many-to-one conflicts in a differentiable forward warp, supporting both image and feature splatting.

---

<a id="c14"></a>
#### Deformable Convolutional Networks (ICCV 2017)

[![arXiv: 1703.06211](https://img.shields.io/badge/arXiv-1703.06211-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1703.06211) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/msracver/Deformable-ConvNets) [![GitHub stars](https://img.shields.io/github/stars/msracver/Deformable-ConvNets?style=flat-square&label=stars&color=C58A18)](https://github.com/msracver/Deformable-ConvNets/stargazers) [![GitHub forks](https://img.shields.io/github/forks/msracver/Deformable-ConvNets?style=flat-square&label=forks&color=64748B)](https://github.com/msracver/Deformable-ConvNets/forks) &nbsp; [`T8`](#t8)

Learns offsets for convolutional sampling locations, allowing features to adapt to local geometric variation.

---

<details>
<summary>Related reading · 2 papers in other topics</summary>

- [RAFT](#c20) (2020)
- [PWC-Net](#c15) (2018)

</details>

[↑ Start of 3.1](#topic-video-restoration) · [↑ Back to topic navigation](#topics)

---

<a id="topic-09"></a>
<a id="topic-10"></a>
<a id="topic-human-deformation"></a>
### 3.2 Animation, Motion Transfer & Virtual Try-On

> **Scope** · Animation, appearance preservation, pose transfer and garment alignment
>
> **4 papers · Newest first**

---

<a id="n18"></a>
#### StableVITON: Learning Semantic Correspondence with Latent Diffusion Model for Virtual Try-On (CVPR 2024)

[![arXiv: 2312.01725](https://img.shields.io/badge/arXiv-2312.01725-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2312.01725) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2312.01725) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/rlawjdghek/StableVITON) [![GitHub stars](https://img.shields.io/github/stars/rlawjdghek/StableVITON?style=flat-square&label=stars&color=C58A18)](https://github.com/rlawjdghek/StableVITON/stargazers) [![GitHub forks](https://img.shields.io/github/forks/rlawjdghek/StableVITON?style=flat-square&label=forks&color=64748B)](https://github.com/rlawjdghek/StableVITON/forks) &nbsp; [`T9`](#t9)

Learns semantic garment-to-person correspondence inside a latent diffusion model, using attention for implicit alignment and detail transfer.

---

<a id="n03"></a>
#### Thin-Plate Spline Motion Model for Image Animation (CVPR 2022)

[![arXiv: 2203.14367](https://img.shields.io/badge/arXiv-2203.14367-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2203.14367) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2203.14367) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/yoyo-nb/Thin-Plate-Spline-Motion-Model) [![GitHub stars](https://img.shields.io/github/stars/yoyo-nb/Thin-Plate-Spline-Motion-Model?style=flat-square&label=stars&color=C58A18)](https://github.com/yoyo-nb/Thin-Plate-Spline-Motion-Model/stargazers) [![GitHub forks](https://img.shields.io/github/forks/yoyo-nb/Thin-Plate-Spline-Motion-Model?style=flat-square&label=forks&color=64748B)](https://github.com/yoyo-nb/Thin-Plate-Spline-Motion-Model/forks) &nbsp; [`T2`](#t2) [`T8`](#t8)

Extends local affine motion representations to multiple TPS transformations, using multiscale occlusion masks for feature warping in image animation.

---

<a id="c17"></a>
#### First Order Motion Model for Image Animation (NeurIPS 2019)

[![arXiv: 2003.00196](https://img.shields.io/badge/arXiv-2003.00196-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2003.00196) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2003.00196) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://aliaksandrsiarohin.github.io/first-order-model-website/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AliaksandrSiarohin/first-order-model) [![GitHub stars](https://img.shields.io/github/stars/AliaksandrSiarohin/first-order-model?style=flat-square&label=stars&color=C58A18)](https://github.com/AliaksandrSiarohin/first-order-model/stargazers) [![GitHub forks](https://img.shields.io/github/forks/AliaksandrSiarohin/first-order-model?style=flat-square&label=forks&color=64748B)](https://github.com/AliaksandrSiarohin/first-order-model/forks) &nbsp; [`T8`](#t8) [`T9`](#t9)

Learns keypoints and local first-order affine motion to construct dense feature warps and occlusion maps for image animation.

---

<a id="c24"></a>
#### Toward Characteristic-Preserving Image-based Virtual Try-On Network (ECCV 2018)

[![arXiv: 1807.07688](https://img.shields.io/badge/arXiv-1807.07688-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1807.07688) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/1807.07688) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sergeywong/cp-vton) [![GitHub stars](https://img.shields.io/github/stars/sergeywong/cp-vton?style=flat-square&label=stars&color=C58A18)](https://github.com/sergeywong/cp-vton/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sergeywong/cp-vton?style=flat-square&label=forks&color=64748B)](https://github.com/sergeywong/cp-vton/forks) &nbsp; [`T2`](#t2) [`T9`](#t9)

Learns a TPS with a geometric matching module to align an in-shop garment with a person, then learns a composition mask.

---

<details>
<summary>Related reading · 1 papers in other topics</summary>

- [Go-with-the-Flow](#n19) (2025)

</details>

[↑ Start of 3.2](#topic-human-deformation) · [↑ Back to topic navigation](#topics)

---

<a id="area-video-generation"></a>
## 4. Video Generation & Motion Control


<a id="topic-noise-warping"></a>
### 4.1 Noise Warping & Temporal Consistency

> **Scope** · Random-field transport, noise statistics, motion-correlated noise and temporal consistency
>
> **1 papers · Newest first**

---

<a id="n16"></a>
#### How I Warped Your Noise: a Temporally-Correlated Noise Prior for Diffusion Models (ICLR 2024)

[![arXiv: 2504.03072](https://img.shields.io/badge/arXiv-2504.03072-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.03072) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://warpyournoise.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/mskwak01/How-I-Warped-Your-Noise-Unofficial) [![GitHub stars](https://img.shields.io/github/stars/mskwak01/How-I-Warped-Your-Noise-Unofficial?style=flat-square&label=stars&color=C58A18)](https://github.com/mskwak01/How-I-Warped-Your-Noise-Unofficial/stargazers) [![GitHub forks](https://img.shields.io/github/forks/mskwak01/How-I-Warped-Your-Noise-Unofficial?style=flat-square&label=forks&color=64748B)](https://github.com/mskwak01/How-I-Warped-Your-Noise-Unofficial/forks) &nbsp; [`T7`](#t7) [`T9`](#t9)

Interprets pixel noise as integrals over a continuous white-noise field and designs transport for Gaussian statistics while retaining motion-induced temporal correlation.

---

<details>
<summary>Related reading · 2 papers in other topics</summary>

- [CameraNoise](#n24) (2026)
- [Go-with-the-Flow](#n19) (2025)

</details>

[↑ Start of 4.1](#topic-noise-warping) · [↑ Back to topic navigation](#topics)

---

<a id="topic-14"></a>
<a id="topic-controlled-generation"></a>
### 4.2 Camera-, Trajectory- & Motion-Controlled Generation

> **Scope** · Camera and object-motion control, geometric guidance and history-frame alignment
>
> **3 papers · Newest first**

---

<a id="n24"></a>
#### CameraNoise: Enabling Faithful Camera Control in Video Diffusion through Geometry-Flow-Guided Noise Warping (ICML 2026)

[![arXiv: 2605.30774](https://img.shields.io/badge/arXiv-2605.30774-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.30774) [![Hugging Face: Model](https://img.shields.io/badge/Hugging%20Face-Model-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/gulucaptain/CameraNoise-I2V) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://gulucaptain.github.io/CameraNoise/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/gulucaptain/CameraNoise) [![GitHub stars](https://img.shields.io/github/stars/gulucaptain/CameraNoise?style=flat-square&label=stars&color=C58A18)](https://github.com/gulucaptain/CameraNoise/stargazers) [![GitHub forks](https://img.shields.io/github/forks/gulucaptain/CameraNoise?style=flat-square&label=forks&color=64748B)](https://github.com/gulucaptain/CameraNoise/forks) &nbsp; [`T6`](#t6) [`T9`](#t9)

Uses geometry-guided reprojection flow and noise warping to encode camera motion into temporally correlated noise, while preserving the Gaussian prior and trajectory control.

---

<a id="n27"></a>
#### Warp-as-History: Generalizable Camera-Controlled Video Generation from One Training Video (arXiv 2026)

[![arXiv: 2605.15182](https://img.shields.io/badge/arXiv-2605.15182-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.15182) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2605.15182) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://yyfz.github.io/warp-as-history/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/yyfz/Warp-as-History) [![GitHub stars](https://img.shields.io/github/stars/yyfz/Warp-as-History?style=flat-square&label=stars&color=C58A18)](https://github.com/yyfz/Warp-as-History/stargazers) [![GitHub forks](https://img.shields.io/github/forks/yyfz/Warp-as-History?style=flat-square&label=forks&color=64748B)](https://github.com/yyfz/Warp-as-History/forks) &nbsp; [`T6`](#t6) [`T9`](#t9)

Turns camera-induced warps into pseudo-history aligned with target positions, selecting valid tokens to use a frozen model's visual-history pathway; also explores single-video LoRA adaptation.

---

<a id="n19"></a>
#### Go-with-the-Flow: Motion-Controllable Video Diffusion Models Using Real-Time Warped Noise (CVPR 2025)

[![arXiv: 2501.08331](https://img.shields.io/badge/arXiv-2501.08331-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2501.08331) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2501.08331) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://eyeline-labs.github.io/Go-with-the-Flow/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Eyeline-Labs/Go-with-the-Flow) [![GitHub stars](https://img.shields.io/github/stars/Eyeline-Labs/Go-with-the-Flow?style=flat-square&label=stars&color=C58A18)](https://github.com/Eyeline-Labs/Go-with-the-Flow/stargazers) [![GitHub forks](https://img.shields.io/github/forks/Eyeline-Labs/Go-with-the-Flow?style=flat-square&label=forks&color=64748B)](https://github.com/Eyeline-Labs/Go-with-the-Flow/forks) &nbsp; [`T9`](#t9)

Efficiently constructs warped noise and adapts video diffusion models to use it as a motion prior for motion transfer and camera or object control.

---

<details>
<summary>Related reading · 3 papers in other topics</summary>

- [How I Warped Your Noise / ∫-noise](#n16) (2024)
- [RAFT](#c20) (2020)
- [Softmax Splatting](#c19) (2020)

</details>

[↑ Start of 4.2](#topic-controlled-generation) · [↑ Back to topic navigation](#topics)

---

<a id="area-spatial-intelligence"></a>
## 5. Spatial Intelligence

<a id="topic-11"></a>
<a id="topic-spatial-perception"></a>
### 5.1 Spatial Perception, Depth & 3D Reconstruction

> **Scope** · Depth, stereo, multiview geometry, camera pose and scene reconstruction
>
> **1 papers · Newest first**

---

<a id="c16"></a>
#### Digging Into Self-Supervised Monocular Depth Estimation (ICCV 2019)

[![arXiv: 1806.01260](https://img.shields.io/badge/arXiv-1806.01260-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1806.01260) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nianticlabs/monodepth2) [![GitHub stars](https://img.shields.io/github/stars/nianticlabs/monodepth2?style=flat-square&label=stars&color=C58A18)](https://github.com/nianticlabs/monodepth2/stargazers) [![GitHub forks](https://img.shields.io/github/forks/nianticlabs/monodepth2?style=flat-square&label=forks&color=64748B)](https://github.com/nianticlabs/monodepth2/forks) &nbsp; [`T6`](#t6)

Uses depth, pose and differentiable reprojection for self-supervised view reconstruction, introducing minimum reprojection loss and automasking.

---

<details>
<summary>Related reading · 2 papers in other topics</summary>

- [UniMatch: Unifying Flow, Stereo and Depth Estimation](#n09) (2023)
- [Rigid / Similarity / Affine / Homography](#c01) (Foundational models (undated))

</details>

[↑ Start of 5.1](#topic-spatial-perception) · [↑ Back to topic navigation](#topics)

---

<a id="topic-12"></a>
<a id="topic-novel-view-synthesis"></a>
### 5.2 Reprojection & Novel View Synthesis

> **Scope** · DIBR, cross-view warping, visibility and disocclusion completion
>
> **4 papers · Newest first**

---

<a id="n22"></a>
#### WAVE: Warp-Based View Guidance for Consistent Novel View Synthesis Using a Single Image (ICCV 2025)

[![arXiv: 2506.23518](https://img.shields.io/badge/arXiv-2506.23518-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.23518) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/jwoo-park0/WAVE) [![GitHub stars](https://img.shields.io/github/stars/jwoo-park0/WAVE?style=flat-square&label=stars&color=C58A18)](https://github.com/jwoo-park0/WAVE/stargazers) [![GitHub forks](https://img.shields.io/github/forks/jwoo-park0/WAVE?style=flat-square&label=forks&color=64748B)](https://github.com/jwoo-park0/WAVE/forks) &nbsp; [`T6`](#t6) [`T9`](#t9)

Uses view warping to guide adaptive attention and noise reinitialization, improving single-image novel-view consistency without additional training.

---

<a id="n23"></a>
#### High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion (SIGGRAPH 2025)

[![arXiv: 2502.12752](https://img.shields.io/badge/arXiv-2502.12752-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.12752) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2502.12752) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://studios.disneyresearch.com/2025/07/16/splatdiff/) &nbsp; [`T6`](#t6) [`T7`](#t7) [`T9`](#t9)

Uses pixel splatting to constrain target views and combines aligned synthesis with a texture bridge to balance geometric consistency and texture fidelity.

---

<a id="n15"></a>
#### GenWarp: Single Image to Novel Views with Semantic-Preserving Generative Warping (NeurIPS 2024)

[![arXiv: 2405.17251](https://img.shields.io/badge/arXiv-2405.17251-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2405.17251) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2405.17251) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://genwarp-nvs.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sony/genwarp) [![GitHub stars](https://img.shields.io/github/stars/sony/genwarp?style=flat-square&label=stars&color=C58A18)](https://github.com/sony/genwarp/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sony/genwarp?style=flat-square&label=forks&color=64748B)](https://github.com/sony/genwarp/forks) &nbsp; [`T6`](#t6) [`T9`](#t9)

Combines depth-induced coordinate information with cross-view and self-attention, learning which content to transfer and which missing regions to generate.

---

<a id="c28"></a>
#### Depth-image-based rendering (DIBR), compression, and transmission for a new approach on 3D-TV (SPIE 2004)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1117/12.524762) &nbsp; [`T6`](#t6)

Synthesizes virtual views from color and depth, providing a classic route to depth reprojection, visibility reasoning and hole handling. This paper did not originate the general idea of reprojection.

---

<details>
<summary>Related reading · 3 papers in other topics</summary>

- [D-NeRF](#c21) (2021)
- [Nerfies](#c22) (2021)
- [Monodepth2](#c16) (2019)

</details>

[↑ Start of 5.2](#topic-novel-view-synthesis) · [↑ Back to topic navigation](#topics)

---

<a id="topic-13"></a>
<a id="topic-dynamic-3d"></a>
### 5.3 Dynamic 3D & 4D Scenes

> **Scope** · Canonical deformation, dynamic NeRF, deformable Gaussians and spatiotemporal scene representations
>
> **5 papers · Newest first**

---

<a id="n11"></a>
#### Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction (CVPR 2024)

[![arXiv: 2309.13101](https://img.shields.io/badge/arXiv-2309.13101-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2309.13101) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2309.13101) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://ingra14m.github.io/Deformable-Gaussians/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ingra14m/Deformable-3D-Gaussians) [![GitHub stars](https://img.shields.io/github/stars/ingra14m/Deformable-3D-Gaussians?style=flat-square&label=stars&color=C58A18)](https://github.com/ingra14m/Deformable-3D-Gaussians/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ingra14m/Deformable-3D-Gaussians?style=flat-square&label=forks&color=64748B)](https://github.com/ingra14m/Deformable-3D-Gaussians/forks) &nbsp; [`T8`](#t8)

Learns a deformation field over canonical Gaussians, combining dynamic reconstruction with fast splatting-based rendering.

---

<a id="n12"></a>
#### 4D Gaussian Splatting for Real-Time Dynamic Scene Rendering (CVPR 2024)

[![arXiv: 2310.08528](https://img.shields.io/badge/arXiv-2310.08528-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2310.08528) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2310.08528) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://guanjunwu.github.io/4dgs/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/hustvl/4DGaussians) [![GitHub stars](https://img.shields.io/github/stars/hustvl/4DGaussians?style=flat-square&label=stars&color=C58A18)](https://github.com/hustvl/4DGaussians/stargazers) [![GitHub forks](https://img.shields.io/github/forks/hustvl/4DGaussians?style=flat-square&label=forks&color=64748B)](https://github.com/hustvl/4DGaussians/forks) &nbsp; [`T8`](#t8)

Combines spatiotemporal features with Gaussian deformation to improve training, storage and rendering efficiency for dynamic scenes.

---

<a id="c21"></a>
#### D-NeRF: Neural Radiance Fields for Dynamic Scenes (CVPR 2021)

[![arXiv: 2011.13961](https://img.shields.io/badge/arXiv-2011.13961-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2011.13961) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://www.albertpumarola.com/research/D-NeRF/index.html) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/albertpumarola/D-NeRF) [![GitHub stars](https://img.shields.io/github/stars/albertpumarola/D-NeRF?style=flat-square&label=stars&color=C58A18)](https://github.com/albertpumarola/D-NeRF/stargazers) [![GitHub forks](https://img.shields.io/github/forks/albertpumarola/D-NeRF?style=flat-square&label=forks&color=64748B)](https://github.com/albertpumarola/D-NeRF/forks) &nbsp; [`T8`](#t8)

Learns time-conditioned deformation that maps dynamic-scene coordinates into a canonical radiance field.

---

<a id="c22"></a>
#### Nerfies: Deformable Neural Radiance Fields (ICCV 2021)

[![arXiv: 2011.12948](https://img.shields.io/badge/arXiv-2011.12948-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2011.12948) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2011.12948) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://nerfies.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/google/nerfies) [![GitHub stars](https://img.shields.io/github/stars/google/nerfies?style=flat-square&label=stars&color=C58A18)](https://github.com/google/nerfies/stargazers) [![GitHub forks](https://img.shields.io/github/forks/google/nerfies?style=flat-square&label=forks&color=64748B)](https://github.com/google/nerfies/forks) &nbsp; [`T8`](#t8)

Combines continuous 3D deformation, elastic regularization and coarse-to-fine optimization to reconstruct casually captured nonrigid scenes.

---

<a id="c23"></a>
#### HyperNeRF: A Higher-Dimensional Representation for Topologically Varying Neural Radiance Fields (SIGGRAPH Asia / TOG 2021)

[![arXiv: 2106.13228](https://img.shields.io/badge/arXiv-2106.13228-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2106.13228) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://hypernerf.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/google/hypernerf) [![GitHub stars](https://img.shields.io/github/stars/google/hypernerf?style=flat-square&label=stars&color=C58A18)](https://github.com/google/hypernerf/stargazers) [![GitHub forks](https://img.shields.io/github/forks/google/hypernerf?style=flat-square&label=forks&color=64748B)](https://github.com/google/hypernerf/forks) &nbsp; [`T8`](#t8)

Lifts the representation into a higher-dimensional space and uses slices to model topology changes beyond ordinary continuous 3D warps.

[↑ Start of 5.3](#topic-dynamic-3d) · [↑ Back to topic navigation](#topics)

---


<a id="topic-spatial-reasoning"></a>
### 5.4 Spatial Reasoning & Scene Memory

> **Scope** · Spatial relationships, cross-view understanding, persistent maps and spatial memory
>
> **Reserved · No papers collected yet**

---

**Reserved:** No papers collected yet. Future entries should directly connect to spatial correspondence, reprojection, deformation, noise transport or spatiotemporal alignment.

[↑ Start of 5.4](#topic-spatial-reasoning) · [↑ Back to topic navigation](#topics)

---

<a id="area-world-models-agents"></a>
## 6. World Models & Embodied Agents


<a id="topic-world-models"></a>
### 6.1 World Models & Environment Prediction

> **Scope** · State representations, dynamics prediction, action-conditioned prediction and future rollouts
>
> **Reserved · No papers collected yet**

---

**Reserved:** No papers collected yet. Future entries should directly connect to spatial correspondence, reprojection, deformation, noise transport or spatiotemporal alignment.

[↑ Start of 6.1](#topic-world-models) · [↑ Back to topic navigation](#topics)

---


<a id="topic-interactive-simulation"></a>
### 6.2 Interactive Environments & Simulation

> **Scope** · Interactive world generation, scene persistence, training and evaluation environments, and synthetic data
>
> **Reserved · No papers collected yet**

---

**Reserved:** No papers collected yet. Future entries should directly connect to spatial correspondence, reprojection, deformation, noise transport or spatiotemporal alignment.

[↑ Start of 6.2](#topic-interactive-simulation) · [↑ Back to topic navigation](#topics)

---


<a id="topic-embodied-agents"></a>
### 6.3 Embodied Agents, Planning & Control

> **Scope** · Visual navigation, robotic manipulation, active perception, spatial-memory-guided planning and perception–action loops
>
> **Reserved · No papers collected yet**

---

**Reserved:** No papers collected yet. Future entries should directly connect to spatial correspondence, reprojection, deformation, noise transport or spatiotemporal alignment.

[↑ Start of 6.3](#topic-embodied-agents) · [↑ Back to topic navigation](#topics)

---


<a id="technology"></a>
## 🧩 Technique cross-index

Methods can belong to multiple families. Follow a method name to its primary entry; `T1–T9` tags link back to this map. Works are listed newest year first.

<details>
<summary><b>Browse all 9 technique families</b></summary>

| Technique family | Core representation | Works |
| --- | --- | --- |
| <a id="t1"></a>**T1 · Parametric geometry** | Rigid / similarity / affine / homography | [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) · [Lucas–Kanade / Inverse Compositional](#c02) · [Rigid / Similarity / Affine / Homography](#c01) |
| <a id="t2"></a>**T2 · Control points and splines** | TPS / RBF / FFD / B-splines / MLS | [WarpI2I](#n26) · [StabStitch](#n28) · [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) · [Thin-Plate Spline Motion Model for Image Animation](#n03) · [CP-VTON](#c24) · [Moving Least Squares (MLS)](#c08) · [B-spline FFD Registration](#c07) · [Beier–Neely Feature-Based Morphing](#c06) · [Thin-Plate Spline (TPS) / Principal Warps](#c05) · [Free-Form Deformation (FFD)](#c04) |
| <a id="t3"></a>**T3 · Meshes and local shape preservation** | Piecewise maps / ARAP / local projective models | [StabStitch](#n28) · [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) · [As-Projective-As-Possible (APAP) / Moving DLT](#c12) · [Content-Preserving Warps for 3D Video Stabilization](#c29) · [As-Rigid-As-Possible (ARAP) Surface Modeling](#c09) |
| <a id="t4"></a>**T4 · Dense correspondence and optical flow** | Dense flow / correlation volumes / global matching | [MEMFOF](#n20) · [SEA-RAFT](#n13) · [UniMatch: Unifying Flow, Stereo and Depth Estimation](#n09) · [GMFlow](#n01) · [FlowFormer](#n02) · [FILM: Frame Interpolation for Large Motion](#n04) · [BasicVSR++](#n07) · [RAFT](#c20) · [PWC-Net](#c15) · [Lucas–Kanade / Inverse Compositional](#c02) · [Brox et al. Variational Optical Flow](#c27) · [Horn–Schunck](#c03) |
| <a id="t5"></a>**T5 · Invertible deformation and registration** | Velocity fields / diffeomorphisms / inverse consistency | [uniGradICON](#n14) · [TransMorph](#n05) · [SynthMorph](#n06) · [VoxelMorph](#c18) · [Diffeomorphic Demons](#c11) · [SyN: Symmetric Diffeomorphic Registration](#c10) · [LDDMM / Geodesic Flows of Diffeomorphisms](#c26) · [B-spline FFD Registration](#c07) |
| <a id="t6"></a>**T6 · Depth and 3D reprojection** | Depth / camera pose / projection / visibility | [CameraNoise](#n24) · [Warp-as-History](#n27) · [WAVE: Warp-Based View Guidance](#n22) · [SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion](#n23) · [GenWarp](#n15) · [UniMatch: Unifying Flow, Stereo and Depth Estimation](#n09) · [Monodepth2](#c16) · [Depth-Image-Based Rendering (DIBR)](#c28) |
| <a id="t7"></a>**T7 · Differentiable sampling and splatting** | Interpolation / footprints / aggregation / adjoints | [LookingGlass / Laplacian Pyramid Warping (LPW)](#n21) · [SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion](#n23) · [How I Warped Your Noise / ∫-noise](#n16) · [ImWIP](#n10) · [Softmax Splatting](#c19) · [Spatial Transformer Networks (STN)](#c13) · [EWA Volume Splatting](#c25) |
| <a id="t8"></a>**T8 · Learned feature and 3D deformation** | Offsets / local affine motion / canonical fields | [Deformable 3D Gaussians](#n11) · [4D Gaussian Splatting for Real-Time Dynamic Scene Rendering](#n12) · [Thin-Plate Spline Motion Model for Image Animation](#n03) · [FILM: Frame Interpolation for Large Motion](#n04) · [BasicVSR++](#n07) · [D-NeRF](#c21) · [Nerfies](#c22) · [HyperNeRF](#c23) · [First Order Motion Model (FOMM)](#c17) · [Deformable ConvNets (DCN)](#c14) |
| <a id="t9"></a>**T9 · Generative, frequency and stochastic warping** | Geometry–generation fusion / noise transport / frequency handling | [CameraNoise](#n24) · [DMAligner](#n25) · [WarpI2I](#n26) · [Warp-as-History](#n27) · [Go-with-the-Flow](#n19) · [LookingGlass / Laplacian Pyramid Warping (LPW)](#n21) · [WAVE: Warp-Based View Guidance](#n22) · [SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion](#n23) · [GenWarp](#n15) · [How I Warped Your Noise / ∫-noise](#n16) · [Warped Diffusion](#n17) · [StableVITON](#n18) · [First Order Motion Model (FOMM)](#c17) · [CP-VTON](#c24) |

</details>

<a id="resources"></a>
## 🛠️ Evaluation and implementation resources

| Resource | Entry point |
| --- | --- |
| Metrics and comparison principles | [Evaluation guidance](docs/RESEARCH_GUIDE.md#evaluation) |
| Image transforms, differentiable sampling and deformation tools | [Tools and starting points](docs/RESEARCH_GUIDE.md#practice) |
| Datasets and benchmarks | To be added; contributions should specify the task, data version, metrics and evaluation protocol |

<a id="guide"></a>
## 📖 Reading guide

| Explore further | Resource |
| --- | --- |
| Definitions and mapping conventions | [Forward / backward warping and the three layers](docs/RESEARCH_GUIDE.md#scope) |
| Research trends and open problems | [What changed, and what remains difficult](docs/RESEARCH_GUIDE.md#trends) |
| Noise-warping statistics | [Why ordinary interpolation changes Gaussian noise](docs/RESEARCH_GUIDE.md#noise) |
| Implementation and method selection | [Tools and practical starting points](docs/RESEARCH_GUIDE.md#practice) |
| Extended research notes | [Detailed Chinese guide](docs/RESEARCH_GUIDE.zh-CN.md) |

<a id="contributing"></a>
## 🤝 Contributing

Suggestions, corrections and verified links are welcome through [Issues](https://github.com/gulucaptain/Awesome-Warping-Algorithm/issues) and [Pull Requests](https://github.com/gulucaptain/Awesome-Warping-Algorithm/pulls).

Please include the **paper title, publication year/status, Paper, Project, GitHub, technique family, primary topic and related topic tags**. Leave unavailable links empty, and distinguish author implementations, third-party reimplementations and shared frameworks.

Edit [the bilingual catalog](data/catalog.json) and run `python3 scripts/build_readme.py` to update both READMEs. Counts and indexes use the same data; check consistency with `python3 scripts/build_readme.py --check`. Set each work's unique home with `primary_topic`; `topics` contains that home and related directions. When adding papers to a reserved topic, set its `reserved` flag to `false`.

<details>
<summary>Design references and acknowledgments</summary>

The text-free banner was generated with GPT-Image. The layout uses GitHub-native Markdown. Navigation and resource organization were informed by these collections and templates; their paper descriptions and images were not copied:

- [Awesome Diffusion Models in Medical Imaging](https://github.com/amirhossein-kz/Awesome-Diffusion-Models-in-Medical-Imaging)
- [Awesome Diffusion Models](https://github.com/diff-usion/Awesome-Diffusion-Models)
- [Awesome Diffusion Categorized](https://github.com/wangkai930418/awesome-diffusion-categorized)
- [Awesome list guidelines](https://github.com/sindresorhus/awesome/blob/main/awesome.md)
- [Best README Template](https://github.com/othneildrew/Best-README-Template)
- [Shields.io](https://shields.io/) and [Simple Icons](https://simpleicons.org/): branded resource badges
- [Hugging Face brand assets](https://huggingface.co/brand): brand reference

Brand marks identify linked services and do not imply endorsement.

</details>

<div align="center">

**[↑ Back to top](#top)**

<sub>Map coordinates. Preserve structure. Explore motion.</sub>

</div>
