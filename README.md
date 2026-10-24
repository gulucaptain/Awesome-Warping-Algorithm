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

<b>128</b> Papers &nbsp; · &nbsp; <b>87</b> Repositories &nbsp; · &nbsp; <b>6</b> Research areas &nbsp; · &nbsp; <b>16</b> Topics

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

Entries follow **research area → topic**, with papers listed newest year first within each topic. Each topic opens with a scope and paper-count block. Papers follow a consistent sequence: full paper title (venue and year), one row of resource badges followed by technique tags, and a contribution summary. Full publication histories, code provenance and limitations remain in the bilingual catalog and research guides. Horizontal rules separate methods; classical and recent work appear together without year navigation or year groups. Published work uses its representative publication year, and preprints use their preprint year; publication histories are retained. Entries combining foundational methods use the publication year of the linked representative paper. General concepts and documentation are kept in the research guide and excluded from paper listings and counts. Entries from the same year retain catalog order. Coverage ends on 2026-10-24. Descriptions are grounded in papers and author resources; the collection does not claim a unified reproduction of all methods.

Each work has one primary topic, with related tags and reading links for other directions. Extended sections distinguish spatial maps and memory, predictive world models, interactive simulators and closed-loop embodied agents. Foundational representations and prediction models are identified separately from explicit spatial warping operators. New papers must fit the stated scope of their topic.

[Definitions, mapping conventions and evidence policy →](docs/RESEARCH_GUIDE.md#scope)

</details>

<a id="topics"></a>
## 🗂️ Topic navigation

6 research areas and 16 topics. Counts include primary paper entries only; related reading is not counted twice.

<table>
<thead>
<tr><th align="left">Research area</th><th align="left">Topic</th><th align="left">Primary entries / status</th></tr>
</thead>
<tbody>
<tr>
<td rowspan="2" valign="middle"><a href="#area-foundations">1. Warping Foundations &amp; Operators</a></td>
<td><a href="#topic-geometry-editing">1.1 Geometric Transformations &amp; Deformation Editing</a></td>
<td>10</td>
</tr>
<tr>
<td><a href="#topic-sampling-splatting">1.2 Differentiable Sampling &amp; Splatting</a></td>
<td>6</td>
</tr>
<tr>
<td rowspan="3" valign="middle"><a href="#area-alignment">2. Correspondence &amp; Image Alignment</a></td>
<td><a href="#topic-optical-flow">2.1 Optical Flow &amp; Dense Correspondence</a></td>
<td>20</td>
</tr>
<tr>
<td><a href="#topic-image-alignment">2.2 Image Registration, Stitching &amp; Stabilization</a></td>
<td>9</td>
</tr>
<tr>
<td><a href="#topic-medical-registration">2.3 Medical Registration &amp; Diffeomorphic Deformation</a></td>
<td>12</td>
</tr>
<tr>
<td rowspan="2" valign="middle"><a href="#area-video-processing">3. Video Processing &amp; Human Deformation</a></td>
<td><a href="#topic-video-restoration">3.1 Video Interpolation &amp; Restoration</a></td>
<td>11</td>
</tr>
<tr>
<td><a href="#topic-human-deformation">3.2 Animation, Motion Transfer &amp; Virtual Try-On</a></td>
<td>8</td>
</tr>
<tr>
<td rowspan="2" valign="middle"><a href="#area-video-generation">4. Video Generation &amp; Motion Control</a></td>
<td><a href="#topic-noise-warping">4.1 Noise Warping &amp; Temporal Consistency</a></td>
<td>4</td>
</tr>
<tr>
<td><a href="#topic-controlled-generation">4.2 Camera-, Trajectory- &amp; Motion-Controlled Generation</a></td>
<td>7</td>
</tr>
<tr>
<td rowspan="4" valign="middle"><a href="#area-spatial-intelligence">5. Spatial Intelligence</a></td>
<td><a href="#topic-spatial-perception">5.1 Spatial Perception, Depth &amp; 3D Reconstruction</a></td>
<td>7</td>
</tr>
<tr>
<td><a href="#topic-novel-view-synthesis">5.2 Reprojection &amp; Novel View Synthesis</a></td>
<td>9</td>
</tr>
<tr>
<td><a href="#topic-dynamic-3d">5.3 Dynamic 3D &amp; 4D Scenes</a></td>
<td>9</td>
</tr>
<tr>
<td><a href="#topic-spatial-reasoning">5.4 Spatial Reasoning &amp; Scene Memory</a></td>
<td>4</td>
</tr>
<tr>
<td rowspan="3" valign="middle"><a href="#area-world-models-agents">6. World Models &amp; Embodied Agents</a></td>
<td><a href="#topic-world-models">6.1 World Models &amp; Environment Prediction</a></td>
<td>5</td>
</tr>
<tr>
<td><a href="#topic-interactive-simulation">6.2 Interactive Environments &amp; Simulation</a></td>
<td>3</td>
</tr>
<tr>
<td><a href="#topic-embodied-agents">6.3 Embodied Agents, Planning &amp; Control</a></td>
<td>4</td>
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
> **10 papers · Newest first**

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

<a id="p03"></a>
#### Bounded Biharmonic Weights for Real-Time Deformation (SIGGRAPH / TOG 2011)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://igl.ethz.ch/projects/bbw/bounded-biharmonic-weights-siggraph-2011-jacobson-et-al.pdf) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://igl.ethz.ch/projects/bbw/) &nbsp; [`T2`](#t2) [`T3`](#t3)

Computes shape-aware bounded biharmonic blending weights for point, bone and cage deformation handles.

---

<a id="c09"></a>
#### As-Rigid-As-Possible Surface Modeling (SGP 2007)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://igl.ethz.ch/projects/ARAP/arap_web.pdf) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://igl.ethz.ch/projects/ARAP/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/libigl/libigl) [![GitHub stars](https://img.shields.io/github/stars/libigl/libigl?style=flat-square&label=stars&color=C58A18)](https://github.com/libigl/libigl/stargazers) [![GitHub forks](https://img.shields.io/github/forks/libigl/libigl?style=flat-square&label=forks&color=64748B)](https://github.com/libigl/libigl/forks) &nbsp; [`T3`](#t3)

Sorkine and Alexa preserve local shape through an as-rigid-as-possible energy, establishing a widely used approach to detail-preserving mesh editing.

---

<a id="p02"></a>
#### Embedded Deformation for Shape Manipulation (SIGGRAPH / TOG 2007)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://cgl.ethz.ch/~sumnerb/research/embdef/Sumner2007EDF.pdf) &nbsp; [`T3`](#t3)

Blends local affine transforms on a sparse deformation graph to manipulate complex shapes.

---

<a id="c08"></a>
#### Image deformation using moving least squares (SIGGRAPH / TOG 2006)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1145/1141911.1141920) &nbsp; [`T2`](#t2)

Schaefer and colleagues construct affine, similarity and rigid image deformations through locally weighted fitting, enabling interactive point and line controls.

---

<a id="p01"></a>
#### Laplacian Surface Editing (SGP 2004)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://diglib.eg.org/items/ee43c2c6-4956-4ff0-9db1-c946306a5b99) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://igl.ethz.ch/projects/Laplacian-mesh-processing/Laplacian-mesh-editing/) &nbsp; [`T3`](#t3)

Uses local Laplacian coordinates and handle constraints for detail-preserving mesh editing.

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

<details>
<summary>Related reading · 7 papers in other topics</summary>

- [Unsupervised Deep Image Stitching (UDIS)](#p14) (2021)
- [Transporter Networks](#p65) (2021)
- [Neural 3D Mesh Renderer](#p05) (2018)
- [X2Face](#p30) (2018)
- [Deep Image Homography Estimation](#p13) (2016)
- [DynamicFusion](#p50) (2015)
- [EWA Volume Splatting](#c25) (2001)

</details>

[↑ Start of 1.1](#topic-geometry-editing) · [↑ Back to topic navigation](#topics)

---

<a id="topic-15"></a>
<a id="topic-sampling-splatting"></a>
### 1.2 Differentiable Sampling & Splatting

> **Scope** · Interpolation, resampling, differentiable spatial transforms, sampling kernels, adjoints and derivatives
>
> **6 papers · Newest first**

---

<a id="n10"></a>
#### ImWIP: Open-source image warping toolbox with adjoints and derivatives (SoftwareX 2023)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1016/j.softx.2023.101524) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://imwip.readthedocs.io/en/latest/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/RendersJens/ImWIP) [![GitHub stars](https://img.shields.io/github/stars/RendersJens/ImWIP?style=flat-square&label=stars&color=C58A18)](https://github.com/RendersJens/ImWIP/stargazers) [![GitHub forks](https://img.shields.io/github/forks/RendersJens/ImWIP?style=flat-square&label=forks&color=64748B)](https://github.com/RendersJens/ImWIP/forks) &nbsp; [`T7`](#t7)

Provides differentiable image-warp operators with exact discrete adjoints and derivatives for inverse-problem optimization.

---

<a id="p06"></a>
#### Soft Rasterizer: A Differentiable Renderer for Image-based 3D Reasoning (ICCV 2019)

[![arXiv: 1904.01786](https://img.shields.io/badge/arXiv-1904.01786-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1904.01786) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ShichenLiu/SoftRas) [![GitHub stars](https://img.shields.io/github/stars/ShichenLiu/SoftRas?style=flat-square&label=stars&color=C58A18)](https://github.com/ShichenLiu/SoftRas/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ShichenLiu/SoftRas?style=flat-square&label=forks&color=64748B)](https://github.com/ShichenLiu/SoftRas/forks) &nbsp; [`T7`](#t7)

Uses probabilistic coverage and soft aggregation to differentiate image formation with respect to mesh geometry.

---

<a id="p05"></a>
#### Neural 3D Mesh Renderer (CVPR 2018)

[![arXiv: 1711.07566](https://img.shields.io/badge/arXiv-1711.07566-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1711.07566) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/hiroharu-kato/neural_renderer) [![GitHub stars](https://img.shields.io/github/stars/hiroharu-kato/neural_renderer?style=flat-square&label=stars&color=C58A18)](https://github.com/hiroharu-kato/neural_renderer/stargazers) [![GitHub forks](https://img.shields.io/github/forks/hiroharu-kato/neural_renderer?style=flat-square&label=forks&color=64748B)](https://github.com/hiroharu-kato/neural_renderer/forks) &nbsp; [`T7`](#t7)

Approximates rasterization gradients so image losses can optimize mesh geometry and camera parameters.

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

<a id="p04"></a>
#### Surface Splatting (SIGGRAPH 2001)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.cs.umd.edu/~zwicker/publications/SurfaceSplatting-SIG01.pdf) &nbsp; [`T7`](#t7)

Extends screen-space EWA filtering to irregular surface samples for antialiased point-based rendering.

---

<details>
<summary>Related reading · 7 papers in other topics</summary>

- [Warped Diffusion](#n17) (2024)
- [Dynamic 3D Gaussians](#p51) (2024)
- [3D Gaussian Splatting (3DGS)](#p45) (2023)
- [Deep Learning Image Registration (DLIR)](#p18) (2019)
- [Depth-Aware Interpolation (DAIN)](#p22) (2019)
- [Stereo Magnification / Multiplane Images](#p48) (2018)
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
> **20 papers · Newest first**

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

<a id="p71"></a>
#### RoMa: Robust Dense Feature Matching (CVPR 2024)

[![arXiv: 2305.15404](https://img.shields.io/badge/arXiv-2305.15404-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2305.15404) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2305.15404) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Parskatt/RoMa) [![GitHub stars](https://img.shields.io/github/stars/Parskatt/RoMa?style=flat-square&label=stars&color=C58A18)](https://github.com/Parskatt/RoMa/stargazers) [![GitHub forks](https://img.shields.io/github/forks/Parskatt/RoMa?style=flat-square&label=forks&color=64748B)](https://github.com/Parskatt/RoMa/forks) &nbsp; [`T4`](#t4)

Combines frozen foundation features, local convolutional features and a match decoder for robust dense coordinate mappings.

---

<a id="n09"></a>
#### Unifying Flow, Stereo and Depth Estimation (TPAMI 2023)

[![arXiv: 2211.05783](https://img.shields.io/badge/arXiv-2211.05783-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2211.05783) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2211.05783) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://haofeixu.github.io/unimatch/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/autonomousvision/unimatch) [![GitHub stars](https://img.shields.io/github/stars/autonomousvision/unimatch?style=flat-square&label=stars&color=C58A18)](https://github.com/autonomousvision/unimatch/stargazers) [![GitHub forks](https://img.shields.io/github/forks/autonomousvision/unimatch?style=flat-square&label=forks&color=64748B)](https://github.com/autonomousvision/unimatch/forks) &nbsp; [`T4`](#t4) [`T6`](#t6)

Unifies optical flow, stereo disparity and depth from posed views as dense correspondence-matching problems.

---

<a id="p12"></a>
#### FlowFormer++: Masked Cost Volume Autoencoding for Pretraining Optical Flow Estimation (CVPR 2023)

[![arXiv: 2303.01237](https://img.shields.io/badge/arXiv-2303.01237-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2303.01237) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/XiaoyuShi97/FlowFormerPlusPlus) [![GitHub stars](https://img.shields.io/github/stars/XiaoyuShi97/FlowFormerPlusPlus?style=flat-square&label=stars&color=C58A18)](https://github.com/XiaoyuShi97/FlowFormerPlusPlus/stargazers) [![GitHub forks](https://img.shields.io/github/forks/XiaoyuShi97/FlowFormerPlusPlus?style=flat-square&label=forks&color=64748B)](https://github.com/XiaoyuShi97/FlowFormerPlusPlus/forks) &nbsp; [`T4`](#t4)

Pretrains correspondence representations with masked cost-volume autoencoding for optical-flow estimation.

---

<a id="p70"></a>
#### DKM: Dense Kernelized Feature Matching for Geometry Estimation (CVPR 2023)

[![arXiv: 2202.00667](https://img.shields.io/badge/arXiv-2202.00667-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2202.00667) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2202.00667) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://parskatt.github.io/DKM/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Parskatt/DKM) [![GitHub stars](https://img.shields.io/github/stars/Parskatt/DKM?style=flat-square&label=stars&color=C58A18)](https://github.com/Parskatt/DKM/stargazers) [![GitHub forks](https://img.shields.io/github/forks/Parskatt/DKM?style=flat-square&label=forks&color=64748B)](https://github.com/Parskatt/DKM/forks) &nbsp; [`T4`](#t4)

Combines global kernelized regression with local refinement to estimate dense matches and confidence for geometric estimation.

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

<a id="p11"></a>
#### Learning to Estimate Hidden Motions with Global Motion Aggregation (ICCV 2021)

[![arXiv: 2104.02409](https://img.shields.io/badge/arXiv-2104.02409-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2104.02409) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2104.02409) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/zacjiang/GMA) [![GitHub stars](https://img.shields.io/github/stars/zacjiang/GMA?style=flat-square&label=stars&color=C58A18)](https://github.com/zacjiang/GMA/stargazers) [![GitHub forks](https://img.shields.io/github/forks/zacjiang/GMA?style=flat-square&label=forks&color=64748B)](https://github.com/zacjiang/GMA/forks) &nbsp; [`T4`](#t4)

Aggregates global motion information to improve flow estimates in occluded regions.

---

<a id="p69"></a>
#### LoFTR: Detector-Free Local Feature Matching with Transformers (CVPR 2021)

[![arXiv: 2104.00680](https://img.shields.io/badge/arXiv-2104.00680-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2104.00680) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2104.00680) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://zju3dv.github.io/loftr/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/zju3dv/LoFTR) [![GitHub stars](https://img.shields.io/github/stars/zju3dv/LoFTR?style=flat-square&label=stars&color=C58A18)](https://github.com/zju3dv/LoFTR/stargazers) [![GitHub forks](https://img.shields.io/github/forks/zju3dv/LoFTR?style=flat-square&label=forks&color=64748B)](https://github.com/zju3dv/LoFTR/forks) &nbsp; [`T4`](#t4)

Uses pair-conditioned Transformer features and coarse-to-fine refinement for detector-free image correspondence.

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

<a id="p10"></a>
#### LiteFlowNet: A Lightweight Convolutional Neural Network for Optical Flow Estimation (CVPR 2018)

[![arXiv: 1805.07036](https://img.shields.io/badge/arXiv-1805.07036-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1805.07036) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/twhui/LiteFlowNet) [![GitHub stars](https://img.shields.io/github/stars/twhui/LiteFlowNet?style=flat-square&label=stars&color=C58A18)](https://github.com/twhui/LiteFlowNet/stargazers) [![GitHub forks](https://img.shields.io/github/forks/twhui/LiteFlowNet?style=flat-square&label=forks&color=64748B)](https://github.com/twhui/LiteFlowNet/forks) &nbsp; [`T4`](#t4)

Combines pyramidal features, feature warping, matching and local regularization in a compact flow network.

---

<a id="p08"></a>
#### FlowNet 2.0: Evolution of Optical Flow Estimation with Deep Networks (CVPR 2017)

[![arXiv: 1612.01925](https://img.shields.io/badge/arXiv-1612.01925-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1612.01925) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/1612.01925) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/lmb-freiburg/flownet2) [![GitHub stars](https://img.shields.io/github/stars/lmb-freiburg/flownet2?style=flat-square&label=stars&color=C58A18)](https://github.com/lmb-freiburg/flownet2/stargazers) [![GitHub forks](https://img.shields.io/github/forks/lmb-freiburg/flownet2?style=flat-square&label=forks&color=64748B)](https://github.com/lmb-freiburg/flownet2/forks) &nbsp; [`T4`](#t4)

Stacks flow networks with intermediate image warping and a dedicated small-displacement branch.

---

<a id="p09"></a>
#### Optical Flow Estimation using a Spatial Pyramid Network (CVPR 2017)

[![arXiv: 1611.00850](https://img.shields.io/badge/arXiv-1611.00850-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1611.00850) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/anuragranj/spynet) [![GitHub stars](https://img.shields.io/github/stars/anuragranj/spynet?style=flat-square&label=stars&color=C58A18)](https://github.com/anuragranj/spynet/stargazers) [![GitHub forks](https://img.shields.io/github/forks/anuragranj/spynet?style=flat-square&label=forks&color=64748B)](https://github.com/anuragranj/spynet/forks) &nbsp; [`T4`](#t4)

Combines a spatial pyramid with compact residual-flow networks and coarse-to-fine warping.

---

<a id="p07"></a>
#### FlowNet: Learning Optical Flow with Convolutional Networks (ICCV 2015)

[![arXiv: 1504.06852](https://img.shields.io/badge/arXiv-1504.06852-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1504.06852) &nbsp; [`T4`](#t4)

Introduces convolutional optical-flow estimation with correlation features and synthetic Flying Chairs training data.

---

<a id="p72"></a>
#### SIFT Flow: Dense Correspondence across Scenes and its Applications (TPAMI 2011)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://people.csail.mit.edu/celiu/SIFTflow/) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://people.csail.mit.edu/celiu/SIFTflow/) &nbsp; [`T4`](#t4)

Optimizes discontinuity-preserving matching over dense SIFT descriptors to align images across different scenes and appearances.

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

---

<details>
<summary>Related reading · 2 papers in other topics</summary>

- [MASt3R](#p42) (2024)
- [Neural Scene Flow Fields (NSFF)](#p49) (2021)

</details>

[↑ Start of 2.1](#topic-optical-flow) · [↑ Back to topic navigation](#topics)

---

<a id="topic-01"></a>
<a id="topic-03"></a>
<a id="topic-04"></a>
<a id="topic-image-alignment"></a>
### 2.2 Image Registration, Stitching & Stabilization

> **Scope** · Image alignment, panoramic stitching, parallax handling and temporal stabilization
>
> **9 papers · Newest first**

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

<a id="p14"></a>
#### Unsupervised Deep Image Stitching: Reconstructing Stitched Features to Images (IEEE TIP 2021)

[![arXiv: 2106.12859](https://img.shields.io/badge/arXiv-2106.12859-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2106.12859) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nie-lang/UnsupervisedDeepImageStitching) [![GitHub stars](https://img.shields.io/github/stars/nie-lang/UnsupervisedDeepImageStitching?style=flat-square&label=stars&color=C58A18)](https://github.com/nie-lang/UnsupervisedDeepImageStitching/stargazers) [![GitHub forks](https://img.shields.io/github/forks/nie-lang/UnsupervisedDeepImageStitching?style=flat-square&label=forks&color=64748B)](https://github.com/nie-lang/UnsupervisedDeepImageStitching/forks) &nbsp; [`T1`](#t1) [`T3`](#t3)

Learns image alignment without homography labels and reconstructs stitched images from aligned features.

---

<a id="p13"></a>
#### Deep Image Homography Estimation (arXiv 2016)

[![arXiv: 1606.03798](https://img.shields.io/badge/arXiv-1606.03798-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1606.03798) &nbsp; [`T1`](#t1)

Predicts a four-point homography directly from image pairs for learned planar alignment.

---

<a id="p16"></a>
#### MeshFlow: Minimum Latency Online Video Stabilization (ECCV 2016)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1007/978-3-319-46466-4_48) &nbsp; [`T3`](#t3) [`T4`](#t4)

Propagates feature motions to mesh vertices and smooths vertex trajectories for online video stabilization.

---

<a id="c12"></a>
#### As-Projective-As-Possible Image Stitching with Moving DLT (CVPR 2013)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content_cvpr_2013/papers/Zaragoza_As-Projective-As-Possible_Image_Stitching_2013_CVPR_paper.pdf) &nbsp; [`T3`](#t3)

Zaragoza and colleagues allow local departures from a global projective map through Moving DLT, accommodating parallax and nonplanarity in image stitching.

---

<a id="p15"></a>
#### Bundled Camera Paths for Video Stabilization (SIGGRAPH / TOG 2013)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/Stabilization_SIGGRAPH13.pdf) &nbsp; [`T3`](#t3)

Stabilizes video by optimizing spatially varying mesh-based camera paths over space and time.

---

<a id="c29"></a>
#### Content-Preserving Warps for 3D Video Stabilization (SIGGRAPH / TOG 2009)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://pages.cs.wisc.edu/~fliu/papers/siggraph09.pdf) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://web.cecs.pdx.edu/~fliu/project/3dstab.htm) &nbsp; [`T3`](#t3)

Combines reconstructed 3D camera motion with content-preserving mesh warps to stabilize video while balancing alignment and salient-region shape.

---

<details>
<summary>Related reading · 8 papers in other topics</summary>

- [Robust Dense Matching (RoMa)](#p71) (2024)
- [Dense Kernelized Matching (DKM)](#p70) (2023)
- [LoFTR](#p69) (2021)
- [COLMAP / Structure-from-Motion Revisited](#p38) (2016)
- [SIFT Flow](#p72) (2011)
- [Lucas–Kanade / Inverse Compositional](#c02) (2004)
- [B-spline FFD Registration](#c07) (1999)
- [Thin-Plate Spline (TPS) / Principal Warps](#c05) (1989)

</details>

[↑ Start of 2.2](#topic-image-alignment) · [↑ Back to topic navigation](#topics)

---

<a id="topic-02"></a>
<a id="topic-medical-registration"></a>
### 2.3 Medical Registration & Diffeomorphic Deformation

> **Scope** · Cross-modal registration, diffeomorphisms, topology preservation and inverse consistency
>
> **12 papers · Newest first**

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

<a id="p20"></a>
#### ICON: Learning Regular Maps Through Inverse Consistency (ICCV 2021)

[![arXiv: 2105.04459](https://img.shields.io/badge/arXiv-2105.04459-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2105.04459) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/uncbiag/ICON) [![GitHub stars](https://img.shields.io/github/stars/uncbiag/ICON?style=flat-square&label=stars&color=C58A18)](https://github.com/uncbiag/ICON/stargazers) [![GitHub forks](https://img.shields.io/github/forks/uncbiag/ICON?style=flat-square&label=forks&color=64748B)](https://github.com/uncbiag/ICON/forks) &nbsp; [`T5`](#t5)

Uses inverse consistency and randomized off-grid interpolation to regularize learned spatial registration maps.

---

<a id="p19"></a>
#### Fast Symmetric Diffeomorphic Image Registration with Convolutional Neural Networks (CVPR 2020)

[![arXiv: 2003.09514](https://img.shields.io/badge/arXiv-2003.09514-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2003.09514) &nbsp; [`T5`](#t5)

Learns forward and inverse transforms jointly in a symmetric diffeomorphic registration framework.

---

<a id="c18"></a>
#### VoxelMorph: A Learning Framework for Deformable Medical Image Registration (IEEE TMI 2019)

[![arXiv: 1809.05231](https://img.shields.io/badge/arXiv-1809.05231-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1809.05231) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://voxelmorph.csail.mit.edu/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/voxelmorph/voxelmorph) [![GitHub stars](https://img.shields.io/github/stars/voxelmorph/voxelmorph?style=flat-square&label=stars&color=C58A18)](https://github.com/voxelmorph/voxelmorph/stargazers) [![GitHub forks](https://img.shields.io/github/forks/voxelmorph/voxelmorph?style=flat-square&label=forks&color=64748B)](https://github.com/voxelmorph/voxelmorph/forks) &nbsp; [`T5`](#t5)

Amortizes pairwise optimization into a network that predicts deformation fields, trained with differentiable warping and image-similarity objectives.

---

<a id="p18"></a>
#### A deep learning framework for unsupervised affine and deformable image registration (Medical Image Analysis 2019)

[![arXiv: 1809.06130](https://img.shields.io/badge/arXiv-1809.06130-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1809.06130) &nbsp; [`T2`](#t2) [`T5`](#t5)

Combines affine and deformable networks in an unsupervised image-similarity-based registration framework.

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

---

<a id="p17"></a>
#### Image matching as a diffusion process: an analogy with Maxwell's demons (Medical Image Analysis 1998)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1016/s1361-8415(98)80022-4) &nbsp; [`T5`](#t5)

Formulates dense image-matching updates through a diffusion analogy for deformable medical registration.

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
> **11 papers · Newest first**

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

<a id="p23"></a>
#### Real-Time Intermediate Flow Estimation for Video Frame Interpolation (ECCV 2022)

[![arXiv: 2011.06294](https://img.shields.io/badge/arXiv-2011.06294-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2011.06294) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2011.06294) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/megvii-research/ECCV2022-RIFE) [![GitHub stars](https://img.shields.io/github/stars/megvii-research/ECCV2022-RIFE?style=flat-square&label=stars&color=C58A18)](https://github.com/megvii-research/ECCV2022-RIFE/stargazers) [![GitHub forks](https://img.shields.io/github/forks/megvii-research/ECCV2022-RIFE?style=flat-square&label=forks&color=64748B)](https://github.com/megvii-research/ECCV2022-RIFE/forks) &nbsp; [`T4`](#t4)

Directly estimates intermediate optical flow with privileged distillation and temporal encoding for efficient frame interpolation.

---

<a id="p25"></a>
#### BasicVSR: The Search for Essential Components in Video Super-Resolution and Beyond (CVPR 2021)

[![arXiv: 2012.02181](https://img.shields.io/badge/arXiv-2012.02181-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2012.02181) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ckkelvinchan/BasicVSR-IconVSR) [![GitHub stars](https://img.shields.io/github/stars/ckkelvinchan/BasicVSR-IconVSR?style=flat-square&label=stars&color=C58A18)](https://github.com/ckkelvinchan/BasicVSR-IconVSR/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ckkelvinchan/BasicVSR-IconVSR?style=flat-square&label=forks&color=64748B)](https://github.com/ckkelvinchan/BasicVSR-IconVSR/forks) &nbsp; [`T4`](#t4)

Builds a video super-resolution baseline around bidirectional propagation, flow-based alignment, aggregation and upsampling.

---

<a id="c19"></a>
#### Softmax Splatting for Video Frame Interpolation (CVPR 2020)

[![arXiv: 2003.05534](https://img.shields.io/badge/arXiv-2003.05534-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2003.05534) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://sniklaus.com/softsplat) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sniklaus/softmax-splatting) [![GitHub stars](https://img.shields.io/github/stars/sniklaus/softmax-splatting?style=flat-square&label=stars&color=C58A18)](https://github.com/sniklaus/softmax-splatting/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sniklaus/softmax-splatting?style=flat-square&label=forks&color=64748B)](https://github.com/sniklaus/softmax-splatting/forks) &nbsp; [`T7`](#t7)

Niklaus and Liu use softmax weighting to resolve many-to-one conflicts in a differentiable forward warp, supporting both image and feature splatting.

---

<a id="p22"></a>
#### Depth-Aware Video Frame Interpolation (CVPR 2019)

[![arXiv: 1904.00830](https://img.shields.io/badge/arXiv-1904.00830-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1904.00830) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/baowenbo/DAIN) [![GitHub stars](https://img.shields.io/github/stars/baowenbo/DAIN?style=flat-square&label=stars&color=C58A18)](https://github.com/baowenbo/DAIN/stargazers) [![GitHub forks](https://img.shields.io/github/forks/baowenbo/DAIN?style=flat-square&label=forks&color=64748B)](https://github.com/baowenbo/DAIN/forks) &nbsp; [`T4`](#t4) [`T6`](#t6) [`T7`](#t7)

Uses depth-aware flow projection and warped contextual features to handle occlusions during frame interpolation.

---

<a id="p24"></a>
#### EDVR: Video Restoration with Enhanced Deformable Convolutional Networks (CVPR Workshops 2019)

[![arXiv: 1905.02716](https://img.shields.io/badge/arXiv-1905.02716-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1905.02716) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/xinntao/EDVR) [![GitHub stars](https://img.shields.io/github/stars/xinntao/EDVR?style=flat-square&label=stars&color=C58A18)](https://github.com/xinntao/EDVR/stargazers) [![GitHub forks](https://img.shields.io/github/forks/xinntao/EDVR?style=flat-square&label=forks&color=64748B)](https://github.com/xinntao/EDVR/forks) &nbsp; [`T4`](#t4) [`T8`](#t8)

Combines pyramid-cascading deformable alignment with temporal-spatial attention for video restoration.

---

<a id="p26"></a>
#### Video Enhancement with Task-Oriented Flow (IJCV 2019)

[![arXiv: 1711.09078](https://img.shields.io/badge/arXiv-1711.09078-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1711.09078) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/1711.09078) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/anchen1011/toflow) [![GitHub stars](https://img.shields.io/github/stars/anchen1011/toflow?style=flat-square&label=stars&color=C58A18)](https://github.com/anchen1011/toflow/stargazers) [![GitHub forks](https://img.shields.io/github/forks/anchen1011/toflow?style=flat-square&label=forks&color=64748B)](https://github.com/anchen1011/toflow/forks) &nbsp; [`T4`](#t4)

Jointly learns task-oriented motion and video processing so alignment serves interpolation, denoising and super-resolution.

---

<a id="p21"></a>
#### Super SloMo: High Quality Estimation of Multiple Intermediate Frames for Video Interpolation (CVPR 2018)

[![arXiv: 1712.00080](https://img.shields.io/badge/arXiv-1712.00080-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1712.00080) &nbsp; [`T4`](#t4)

Synthesizes intermediate frames using bidirectional flow, intermediate-flow refinement and soft visibility maps.

---

<a id="c14"></a>
#### Deformable Convolutional Networks (ICCV 2017)

[![arXiv: 1703.06211](https://img.shields.io/badge/arXiv-1703.06211-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1703.06211) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/msracver/Deformable-ConvNets) [![GitHub stars](https://img.shields.io/github/stars/msracver/Deformable-ConvNets?style=flat-square&label=stars&color=C58A18)](https://github.com/msracver/Deformable-ConvNets/stargazers) [![GitHub forks](https://img.shields.io/github/forks/msracver/Deformable-ConvNets?style=flat-square&label=forks&color=64748B)](https://github.com/msracver/Deformable-ConvNets/forks) &nbsp; [`T8`](#t8)

Learns offsets for convolutional sampling locations, allowing features to adapt to local geometric variation.

---

<details>
<summary>Related reading · 7 papers in other topics</summary>

- [Global Motion Aggregation (GMA)](#p11) (2021)
- [RAFT](#c20) (2020)
- [PWC-Net](#c15) (2018)
- [LiteFlowNet](#p10) (2018)
- [FlowNet 2.0](#p08) (2017)
- [SPyNet](#p09) (2017)
- [FlowNet](#p07) (2015)

</details>

[↑ Start of 3.1](#topic-video-restoration) · [↑ Back to topic navigation](#topics)

---

<a id="topic-09"></a>
<a id="topic-10"></a>
<a id="topic-human-deformation"></a>
### 3.2 Animation, Motion Transfer & Virtual Try-On

> **Scope** · Animation, appearance preservation, pose transfer and garment alignment
>
> **8 papers · Newest first**

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

<a id="p29"></a>
#### Parser-Free Virtual Try-on via Distilling Appearance Flows (CVPR 2021)

[![arXiv: 2103.04559](https://img.shields.io/badge/arXiv-2103.04559-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2103.04559) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/geyuying/PF-AFN) [![GitHub stars](https://img.shields.io/github/stars/geyuying/PF-AFN?style=flat-square&label=stars&color=C58A18)](https://github.com/geyuying/PF-AFN/stargazers) [![GitHub forks](https://img.shields.io/github/forks/geyuying/PF-AFN?style=flat-square&label=forks&color=64748B)](https://github.com/geyuying/PF-AFN/forks) &nbsp; [`T4`](#t4) [`T9`](#t9)

Distills garment-to-person appearance flows to enable parser-free virtual try-on at inference time.

---

<a id="p28"></a>
#### Towards Photo-Realistic Virtual Try-On by Adaptively Generating-Preserving Image Content (CVPR 2020)

[![arXiv: 2003.05863](https://img.shields.io/badge/arXiv-2003.05863-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2003.05863) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2003.05863) &nbsp; [`T2`](#t2) [`T9`](#t9)

Uses predicted semantic layouts, garment warping and adaptive content generation or preservation for virtual try-on.

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

<a id="p27"></a>
#### VITON: An Image-based Virtual Try-on Network (CVPR 2018)

[![arXiv: 1711.08447](https://img.shields.io/badge/arXiv-1711.08447-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1711.08447) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/xthan/VITON) [![GitHub stars](https://img.shields.io/github/stars/xthan/VITON?style=flat-square&label=stars&color=C58A18)](https://github.com/xthan/VITON/stargazers) [![GitHub forks](https://img.shields.io/github/forks/xthan/VITON?style=flat-square&label=forks&color=64748B)](https://github.com/xthan/VITON/forks) &nbsp; [`T2`](#t2) [`T9`](#t9)

Combines coarse-to-fine synthesis, garment deformation and blending for image-based virtual try-on.

---

<a id="p30"></a>
#### X2Face: A network for controlling face generation using images, audio, and pose codes (ECCV 2018)

[![arXiv: 1807.10550](https://img.shields.io/badge/arXiv-1807.10550-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1807.10550) &nbsp; [`T8`](#t8) [`T9`](#t9)

Learns a face embedding and a driving sampling field for image-, pose- or audio-controlled face generation.

---

<details>
<summary>Related reading · 2 papers in other topics</summary>

- [Go-with-the-Flow](#n19) (2025)
- [Bounded Biharmonic Weights (BBW)](#p03) (2011)

</details>

[↑ Start of 3.2](#topic-human-deformation) · [↑ Back to topic navigation](#topics)

---

<a id="area-video-generation"></a>
## 4. Video Generation & Motion Control


<a id="topic-noise-warping"></a>
### 4.1 Noise Warping & Temporal Consistency

> **Scope** · Random-field transport, noise statistics, motion-correlated noise and temporal consistency
>
> **4 papers · Newest first**

---

<a id="n16"></a>
#### How I Warped Your Noise: a Temporally-Correlated Noise Prior for Diffusion Models (ICLR 2024)

[![arXiv: 2504.03072](https://img.shields.io/badge/arXiv-2504.03072-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.03072) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://warpyournoise.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/mskwak01/How-I-Warped-Your-Noise-Unofficial) [![GitHub stars](https://img.shields.io/github/stars/mskwak01/How-I-Warped-Your-Noise-Unofficial?style=flat-square&label=stars&color=C58A18)](https://github.com/mskwak01/How-I-Warped-Your-Noise-Unofficial/stargazers) [![GitHub forks](https://img.shields.io/github/forks/mskwak01/How-I-Warped-Your-Noise-Unofficial?style=flat-square&label=forks&color=64748B)](https://github.com/mskwak01/How-I-Warped-Your-Noise-Unofficial/forks) &nbsp; [`T7`](#t7) [`T9`](#t9)

Interprets pixel noise as integrals over a continuous white-noise field and designs transport for Gaussian statistics while retaining motion-induced temporal correlation.

---

<a id="p32"></a>
#### FreeNoise: Tuning-Free Longer Video Diffusion via Noise Rescheduling (ICLR 2024)

[![arXiv: 2310.15169](https://img.shields.io/badge/arXiv-2310.15169-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2310.15169) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2310.15169) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AILab-CVC/FreeNoise) [![GitHub stars](https://img.shields.io/github/stars/AILab-CVC/FreeNoise?style=flat-square&label=stars&color=C58A18)](https://github.com/AILab-CVC/FreeNoise/stargazers) [![GitHub forks](https://img.shields.io/github/forks/AILab-CVC/FreeNoise?style=flat-square&label=forks&color=64748B)](https://github.com/AILab-CVC/FreeNoise/forks) &nbsp; [`T9`](#t9)

Reschedules initial noise and uses windowed temporal attention to extend pretrained video diffusion to longer sequences.

---

<a id="p33"></a>
#### ConsistI2V: Enhancing Visual Consistency for Image-to-Video Generation (TMLR 2024)

[![arXiv: 2402.04324](https://img.shields.io/badge/arXiv-2402.04324-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2402.04324) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2402.04324) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/TIGER-AI-Lab/ConsistI2V) [![GitHub stars](https://img.shields.io/github/stars/TIGER-AI-Lab/ConsistI2V?style=flat-square&label=stars&color=C58A18)](https://github.com/TIGER-AI-Lab/ConsistI2V/stargazers) [![GitHub forks](https://img.shields.io/github/forks/TIGER-AI-Lab/ConsistI2V?style=flat-square&label=forks&color=64748B)](https://github.com/TIGER-AI-Lab/ConsistI2V/forks) &nbsp; [`T9`](#t9)

Combines first-frame spatiotemporal attention with low-frequency noise initialization for consistent image-to-video generation.

---

<a id="p31"></a>
#### Preserve Your Own Correlation: A Noise Prior for Video Diffusion Models (ICCV 2023)

[![arXiv: 2305.10474](https://img.shields.io/badge/arXiv-2305.10474-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2305.10474) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2305.10474) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://research.nvidia.com/labs/dir/pyoco/) &nbsp; [`T9`](#t9)

Adapts image diffusion to video with mixed and progressive temporally correlated noise priors.

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
> **7 papers · Newest first**

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

<a id="p34"></a>
#### MotionCtrl: A Unified and Flexible Motion Controller for Video Generation (SIGGRAPH 2024)

[![arXiv: 2312.03641](https://img.shields.io/badge/arXiv-2312.03641-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2312.03641) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2312.03641) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/TencentARC/MotionCtrl) [![GitHub stars](https://img.shields.io/github/stars/TencentARC/MotionCtrl?style=flat-square&label=stars&color=C58A18)](https://github.com/TencentARC/MotionCtrl/stargazers) [![GitHub forks](https://img.shields.io/github/forks/TencentARC/MotionCtrl?style=flat-square&label=forks&color=64748B)](https://github.com/TencentARC/MotionCtrl/forks) &nbsp; [`T6`](#t6) [`T9`](#t9)

Uses camera poses and object trajectories to control camera and object motions independently in video generation.

---

<a id="p35"></a>
#### CameraCtrl: Enabling Camera Control for Text-to-Video Generation (ECCV 2024)

[![arXiv: 2404.02101](https://img.shields.io/badge/arXiv-2404.02101-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2404.02101) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2404.02101) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://hehao13.github.io/projects-CameraCtrl/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/hehao13/CameraCtrl) [![GitHub stars](https://img.shields.io/github/stars/hehao13/CameraCtrl?style=flat-square&label=stars&color=C58A18)](https://github.com/hehao13/CameraCtrl/stargazers) [![GitHub forks](https://img.shields.io/github/forks/hehao13/CameraCtrl?style=flat-square&label=forks&color=64748B)](https://github.com/hehao13/CameraCtrl/forks) &nbsp; [`T6`](#t6) [`T9`](#t9)

Encodes camera trajectories in a plug-in module for camera-pose-controlled text-to-video generation.

---

<a id="p37"></a>
#### DragAnything: Motion Control for Anything using Entity Representation (ECCV 2024)

[![arXiv: 2403.07420](https://img.shields.io/badge/arXiv-2403.07420-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2403.07420) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2403.07420) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/showlab/DragAnything) [![GitHub stars](https://img.shields.io/github/stars/showlab/DragAnything?style=flat-square&label=stars&color=C58A18)](https://github.com/showlab/DragAnything/stargazers) [![GitHub forks](https://img.shields.io/github/forks/showlab/DragAnything?style=flat-square&label=forks&color=64748B)](https://github.com/showlab/DragAnything/forks) &nbsp; [`T4`](#t4) [`T9`](#t9)

Connects user trajectories to entity representations for multi-object and background motion control.

---

<a id="p36"></a>
#### DragNUWA: Fine-grained Control in Video Generation by Integrating Text, Image, and Trajectory (arXiv 2023)

[![arXiv: 2308.08089](https://img.shields.io/badge/arXiv-2308.08089-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2308.08089) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2308.08089) &nbsp; [`T4`](#t4) [`T9`](#t9)

Combines text, image and sampled trajectories for fine-grained motion control in open-domain video generation.

---

<details>
<summary>Related reading · 4 papers in other topics</summary>

- [How I Warped Your Noise / ∫-noise](#n16) (2024)
- [ConsistI2V](#p33) (2024)
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
> **7 papers · Newest first**

---

<a id="p41"></a>
#### DUSt3R: Geometric 3D Vision Made Easy (CVPR 2024)

[![arXiv: 2312.14132](https://img.shields.io/badge/arXiv-2312.14132-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2312.14132) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2312.14132) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/naver/dust3r) [![GitHub stars](https://img.shields.io/github/stars/naver/dust3r?style=flat-square&label=stars&color=C58A18)](https://github.com/naver/dust3r/stargazers) [![GitHub forks](https://img.shields.io/github/forks/naver/dust3r?style=flat-square&label=forks&color=64748B)](https://github.com/naver/dust3r/forks) &nbsp; [`T6`](#t6)

Regresses pairwise pointmaps and globally aligns them for uncalibrated multiview 3D reconstruction.

---

<a id="p42"></a>
#### Grounding Image Matching in 3D with MASt3R (ECCV 2024)

[![arXiv: 2406.09756](https://img.shields.io/badge/arXiv-2406.09756-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2406.09756) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2406.09756) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/naver/mast3r) [![GitHub stars](https://img.shields.io/github/stars/naver/mast3r?style=flat-square&label=stars&color=C58A18)](https://github.com/naver/mast3r/stargazers) [![GitHub forks](https://img.shields.io/github/forks/naver/mast3r?style=flat-square&label=forks&color=64748B)](https://github.com/naver/mast3r/forks) &nbsp; [`T4`](#t4) [`T6`](#t6)

Adds local descriptors and efficient matching to DUSt3R pointmaps to ground image correspondences in 3D.

---

<a id="p40"></a>
#### DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras (NeurIPS 2021)

[![arXiv: 2108.10869](https://img.shields.io/badge/arXiv-2108.10869-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2108.10869) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2108.10869) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/princeton-vl/DROID-SLAM) [![GitHub stars](https://img.shields.io/github/stars/princeton-vl/DROID-SLAM?style=flat-square&label=stars&color=C58A18)](https://github.com/princeton-vl/DROID-SLAM/stargazers) [![GitHub forks](https://img.shields.io/github/forks/princeton-vl/DROID-SLAM?style=flat-square&label=forks&color=64748B)](https://github.com/princeton-vl/DROID-SLAM/forks) &nbsp; [`T4`](#t4) [`T6`](#t6)

Jointly updates camera poses and pixelwise depth through recurrent dense bundle adjustment.

---

<a id="c16"></a>
#### Digging Into Self-Supervised Monocular Depth Estimation (ICCV 2019)

[![arXiv: 1806.01260](https://img.shields.io/badge/arXiv-1806.01260-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1806.01260) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nianticlabs/monodepth2) [![GitHub stars](https://img.shields.io/github/stars/nianticlabs/monodepth2?style=flat-square&label=stars&color=C58A18)](https://github.com/nianticlabs/monodepth2/stargazers) [![GitHub forks](https://img.shields.io/github/forks/nianticlabs/monodepth2?style=flat-square&label=forks&color=64748B)](https://github.com/nianticlabs/monodepth2/forks) &nbsp; [`T6`](#t6)

Uses depth, pose and differentiable reprojection for self-supervised view reconstruction, introducing minimum reprojection loss and automasking.

---

<a id="p39"></a>
#### MVSNet: Depth Inference for Unstructured Multi-view Stereo (ECCV 2018)

[![arXiv: 1804.02505](https://img.shields.io/badge/arXiv-1804.02505-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1804.02505) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/YoYo000/MVSNet) [![GitHub stars](https://img.shields.io/github/stars/YoYo000/MVSNet?style=flat-square&label=stars&color=C58A18)](https://github.com/YoYo000/MVSNet/stargazers) [![GitHub forks](https://img.shields.io/github/forks/YoYo000/MVSNet?style=flat-square&label=forks&color=64748B)](https://github.com/YoYo000/MVSNet/forks) &nbsp; [`T6`](#t6)

Builds multiview cost volumes with differentiable homography warping to infer reference-view depth.

---

<a id="p43"></a>
#### Unsupervised Learning of Depth and Ego-Motion from Video (CVPR 2017)

[![arXiv: 1704.07813](https://img.shields.io/badge/arXiv-1704.07813-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1704.07813) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/1704.07813) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tinghuiz/SfMLearner) [![GitHub stars](https://img.shields.io/github/stars/tinghuiz/SfMLearner?style=flat-square&label=stars&color=C58A18)](https://github.com/tinghuiz/SfMLearner/stargazers) [![GitHub forks](https://img.shields.io/github/forks/tinghuiz/SfMLearner?style=flat-square&label=forks&color=64748B)](https://github.com/tinghuiz/SfMLearner/forks) &nbsp; [`T6`](#t6)

Couples monocular depth and camera motion through differentiable view reconstruction and photometric supervision.

---

<a id="p38"></a>
#### Structure-from-Motion Revisited (CVPR 2016)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content_cvpr_2016/html/Schonberger_Structure-From-Motion_Revisited_CVPR_2016_paper.html) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://colmap.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/colmap/colmap) [![GitHub stars](https://img.shields.io/github/stars/colmap/colmap?style=flat-square&label=stars&color=C58A18)](https://github.com/colmap/colmap/stargazers) [![GitHub forks](https://img.shields.io/github/forks/colmap/colmap?style=flat-square&label=forks&color=64748B)](https://github.com/colmap/colmap/forks) &nbsp; [`T1`](#t1) [`T6`](#t6)

Improves incremental structure-from-motion to recover camera poses and sparse geometry from unordered images.

---

<details>
<summary>Related reading · 7 papers in other topics</summary>

- [Robust Dense Matching (RoMa)](#p71) (2024)
- [UniMatch: Unifying Flow, Stereo and Depth Estimation](#n09) (2023)
- [ConceptFusion](#p55) (2023)
- [Dense Kernelized Matching (DKM)](#p70) (2023)
- [IBRNet](#p46) (2021)
- [pixelNeRF](#p47) (2021)
- [LoFTR](#p69) (2021)

</details>

[↑ Start of 5.1](#topic-spatial-perception) · [↑ Back to topic navigation](#topics)

---

<a id="topic-12"></a>
<a id="topic-novel-view-synthesis"></a>
### 5.2 Reprojection & Novel View Synthesis

> **Scope** · DIBR, cross-view warping, visibility and disocclusion completion
>
> **9 papers · Newest first**

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

<a id="p45"></a>
#### 3D Gaussian Splatting for Real-Time Radiance Field Rendering (SIGGRAPH / TOG 2023)

[![arXiv: 2308.04079](https://img.shields.io/badge/arXiv-2308.04079-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2308.04079) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2308.04079) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/graphdeco-inria/gaussian-splatting) [![GitHub stars](https://img.shields.io/github/stars/graphdeco-inria/gaussian-splatting?style=flat-square&label=stars&color=C58A18)](https://github.com/graphdeco-inria/gaussian-splatting/stargazers) [![GitHub forks](https://img.shields.io/github/forks/graphdeco-inria/gaussian-splatting?style=flat-square&label=forks&color=64748B)](https://github.com/graphdeco-inria/gaussian-splatting/forks) &nbsp; [`T6`](#t6) [`T7`](#t7)

Optimizes anisotropic 3D Gaussians and their density with visibility-aware splatting for efficient novel-view rendering.

---

<a id="p46"></a>
#### IBRNet: Learning Multi-View Image-Based Rendering (CVPR 2021)

[![arXiv: 2102.13090](https://img.shields.io/badge/arXiv-2102.13090-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2102.13090) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/googleinterns/IBRNet) [![GitHub stars](https://img.shields.io/github/stars/googleinterns/IBRNet?style=flat-square&label=stars&color=C58A18)](https://github.com/googleinterns/IBRNet/stargazers) [![GitHub forks](https://img.shields.io/github/forks/googleinterns/IBRNet?style=flat-square&label=forks&color=64748B)](https://github.com/googleinterns/IBRNet/forks) &nbsp; [`T6`](#t6) [`T7`](#t7)

Aggregates projected source-view features along rays for generalizable image-based novel-view rendering.

---

<a id="p47"></a>
#### pixelNeRF: Neural Radiance Fields from One or Few Images (CVPR 2021)

[![arXiv: 2012.02190](https://img.shields.io/badge/arXiv-2012.02190-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2012.02190) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2012.02190) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sxyu/pixel-nerf) [![GitHub stars](https://img.shields.io/github/stars/sxyu/pixel-nerf?style=flat-square&label=stars&color=C58A18)](https://github.com/sxyu/pixel-nerf/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sxyu/pixel-nerf?style=flat-square&label=forks&color=64748B)](https://github.com/sxyu/pixel-nerf/forks) &nbsp; [`T6`](#t6)

Conditions radiance fields on image features sampled by projecting 3D points into one or a few source images.

---

<a id="p44"></a>
#### NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis (ECCV 2020)

[![arXiv: 2003.08934](https://img.shields.io/badge/arXiv-2003.08934-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2003.08934) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2003.08934) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://www.matthewtancik.com/nerf) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/bmild/nerf) [![GitHub stars](https://img.shields.io/github/stars/bmild/nerf?style=flat-square&label=stars&color=C58A18)](https://github.com/bmild/nerf/stargazers) [![GitHub forks](https://img.shields.io/github/forks/bmild/nerf?style=flat-square&label=forks&color=64748B)](https://github.com/bmild/nerf/forks) &nbsp; [`T6`](#t6)

Represents scenes with a continuous radiance field optimized through differentiable volume rendering.

---

<a id="p48"></a>
#### Stereo Magnification: Learning view synthesis using multiplane images (SIGGRAPH / TOG 2018)

[![arXiv: 1805.09817](https://img.shields.io/badge/arXiv-1805.09817-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1805.09817) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/1805.09817) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://tinghuiz.github.io/projects/mpi/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/google/stereo-magnification) [![GitHub stars](https://img.shields.io/github/stars/google/stereo-magnification?style=flat-square&label=stars&color=C58A18)](https://github.com/google/stereo-magnification/stargazers) [![GitHub forks](https://img.shields.io/github/forks/google/stereo-magnification?style=flat-square&label=forks&color=64748B)](https://github.com/google/stereo-magnification/forks) &nbsp; [`T6`](#t6)

Predicts multiplane images from narrow-baseline stereo and warps depth planes to synthesize wider-baseline views.

---

<a id="c28"></a>
#### Depth-image-based rendering (DIBR), compression, and transmission for a new approach on 3D-TV (SPIE 2004)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1117/12.524762) &nbsp; [`T6`](#t6)

Synthesizes virtual views from color and depth, providing a classic route to depth reprojection, visibility reasoning and hole handling. This paper did not originate the general idea of reprojection.

---

<details>
<summary>Related reading · 9 papers in other topics</summary>

- [Dynamic 3D Gaussians](#p51) (2024)
- [TiNeuVox](#p52) (2022)
- [D-NeRF](#c21) (2021)
- [Nerfies](#c22) (2021)
- [Neural Scene Flow Fields (NSFF)](#p49) (2021)
- [Monodepth2](#c16) (2019)
- [Soft Rasterizer (SoftRas)](#p06) (2019)
- [MVSNet](#p39) (2018)
- [SfMLearner](#p43) (2017)

</details>

[↑ Start of 5.2](#topic-novel-view-synthesis) · [↑ Back to topic navigation](#topics)

---

<a id="topic-13"></a>
<a id="topic-dynamic-3d"></a>
### 5.3 Dynamic 3D & 4D Scenes

> **Scope** · Canonical deformation, dynamic NeRF, deformable Gaussians and spatiotemporal scene representations
>
> **9 papers · Newest first**

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

<a id="p51"></a>
#### Dynamic 3D Gaussians: Tracking by Persistent Dynamic View Synthesis (3DV 2024)

[![arXiv: 2308.09713](https://img.shields.io/badge/arXiv-2308.09713-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2308.09713) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2308.09713) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://dynamic3dgaussians.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/JonathonLuiten/Dynamic3DGaussians) [![GitHub stars](https://img.shields.io/github/stars/JonathonLuiten/Dynamic3DGaussians?style=flat-square&label=stars&color=C58A18)](https://github.com/JonathonLuiten/Dynamic3DGaussians/stargazers) [![GitHub forks](https://img.shields.io/github/forks/JonathonLuiten/Dynamic3DGaussians?style=flat-square&label=forks&color=64748B)](https://github.com/JonathonLuiten/Dynamic3DGaussians/forks) &nbsp; [`T6`](#t6) [`T7`](#t7) [`T8`](#t8)

Uses persistent moving Gaussians and local rigidity constraints for dynamic view synthesis and dense tracking.

---

<a id="p52"></a>
#### Fast Dynamic Radiance Fields with Time-Aware Neural Voxels (SIGGRAPH Asia 2022)

[![arXiv: 2205.15285](https://img.shields.io/badge/arXiv-2205.15285-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2205.15285) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://jaminfong.cn/tineuvox/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/hustvl/TiNeuVox) [![GitHub stars](https://img.shields.io/github/stars/hustvl/TiNeuVox?style=flat-square&label=stars&color=C58A18)](https://github.com/hustvl/TiNeuVox/stargazers) [![GitHub forks](https://img.shields.io/github/forks/hustvl/TiNeuVox?style=flat-square&label=forks&color=64748B)](https://github.com/hustvl/TiNeuVox/forks) &nbsp; [`T6`](#t6) [`T8`](#t8)

Combines time-aware voxel features, a compact deformation network and multi-distance interpolation for efficient dynamic radiance fields.

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

---

<a id="p49"></a>
#### Neural Scene Flow Fields for Space-Time View Synthesis of Dynamic Scenes (CVPR 2021)

[![arXiv: 2011.13084](https://img.shields.io/badge/arXiv-2011.13084-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2011.13084) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://www.cs.cornell.edu/~zl548/NSFF/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/zhengqili/Neural-Scene-Flow-Fields) [![GitHub stars](https://img.shields.io/github/stars/zhengqili/Neural-Scene-Flow-Fields?style=flat-square&label=stars&color=C58A18)](https://github.com/zhengqili/Neural-Scene-Flow-Fields/stargazers) [![GitHub forks](https://img.shields.io/github/forks/zhengqili/Neural-Scene-Flow-Fields?style=flat-square&label=forks&color=64748B)](https://github.com/zhengqili/Neural-Scene-Flow-Fields/forks) &nbsp; [`T4`](#t4) [`T6`](#t6) [`T8`](#t8)

Jointly models appearance, geometry and 3D scene flow for space-time view synthesis from monocular video.

---

<a id="p50"></a>
#### DynamicFusion: Reconstruction and Tracking of Non-rigid Scenes in Real-Time (CVPR 2015)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content_cvpr_2015/html/Newcombe_DynamicFusion_Reconstruction_and_2015_CVPR_paper.html) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://grail.cs.washington.edu/projects/dynamicfusion/) &nbsp; [`T3`](#t3) [`T6`](#t6) [`T8`](#t8)

Fuses RGB-D observations in canonical space while estimating a nonrigid field that warps geometry into the live frame.

---

<details>
<summary>Related reading · 1 papers in other topics</summary>

- [Embedded Deformation](#p02) (2007)

</details>

[↑ Start of 5.3](#topic-dynamic-3d) · [↑ Back to topic navigation](#topics)

---


<a id="topic-spatial-reasoning"></a>
### 5.4 Spatial Reasoning & Scene Memory

> **Scope** · Spatial relationships, cross-view understanding, persistent maps and spatial memory
>
> **4 papers · Newest first**

---

<a id="p56"></a>
#### ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning (ICRA 2024)

[![arXiv: 2309.16650](https://img.shields.io/badge/arXiv-2309.16650-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2309.16650) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2309.16650) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://concept-graphs.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/concept-graphs/concept-graphs) [![GitHub stars](https://img.shields.io/github/stars/concept-graphs/concept-graphs?style=flat-square&label=stars&color=C58A18)](https://github.com/concept-graphs/concept-graphs/stargazers) [![GitHub forks](https://img.shields.io/github/forks/concept-graphs/concept-graphs?style=flat-square&label=forks&color=64748B)](https://github.com/concept-graphs/concept-graphs/forks) &nbsp; [`T6`](#t6)

Builds open-vocabulary 3D scene graphs through multiview association for spatial reasoning and planning.

---

<a id="p54"></a>
#### Visual Language Maps for Robot Navigation (ICRA 2023)

[![arXiv: 2210.05714](https://img.shields.io/badge/arXiv-2210.05714-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2210.05714) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2210.05714) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://vlmaps.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/vlmaps/vlmaps) [![GitHub stars](https://img.shields.io/github/stars/vlmaps/vlmaps?style=flat-square&label=stars&color=C58A18)](https://github.com/vlmaps/vlmaps/stargazers) [![GitHub forks](https://img.shields.io/github/forks/vlmaps/vlmaps?style=flat-square&label=forks&color=64748B)](https://github.com/vlmaps/vlmaps/forks) &nbsp; [`T6`](#t6)

Fuses vision-language features into 3D maps for open-vocabulary localization and spatially specified navigation goals.

---

<a id="p55"></a>
#### ConceptFusion: Open-set Multimodal 3D Mapping (RSS 2023)

[![arXiv: 2302.07241](https://img.shields.io/badge/arXiv-2302.07241-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2302.07241) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://concept-fusion.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/concept-fusion/concept-fusion) [![GitHub stars](https://img.shields.io/github/stars/concept-fusion/concept-fusion?style=flat-square&label=stars&color=C58A18)](https://github.com/concept-fusion/concept-fusion/stargazers) [![GitHub forks](https://img.shields.io/github/forks/concept-fusion/concept-fusion?style=flat-square&label=forks&color=64748B)](https://github.com/concept-fusion/concept-fusion/forks) &nbsp; [`T6`](#t6)

Fuses pixel-aligned open-set features into 3D maps that support language, image and audio queries.

---

<a id="p53"></a>
#### Semantic MapNet: Building Allocentric Semantic Maps and Representations from Egocentric Views (AAAI 2021)

[![arXiv: 2010.01191](https://img.shields.io/badge/arXiv-2010.01191-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2010.01191) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2010.01191) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://vincentcartillier.github.io/smnet.html) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/vincentcartillier/Semantic-MapNet) [![GitHub stars](https://img.shields.io/github/stars/vincentcartillier/Semantic-MapNet?style=flat-square&label=stars&color=C58A18)](https://github.com/vincentcartillier/Semantic-MapNet/stargazers) [![GitHub forks](https://img.shields.io/github/forks/vincentcartillier/Semantic-MapNet?style=flat-square&label=forks&color=64748B)](https://github.com/vincentcartillier/Semantic-MapNet/forks) &nbsp; [`T6`](#t6)

Projects egocentric RGB-D features into allocentric spatial memory to build semantic maps for navigation and question answering.

---

<details>
<summary>Related reading · 3 papers in other topics</summary>

- [CLIPort](#p66) (2022)
- [Active Neural SLAM](#p63) (2020)
- [Goal-Oriented Semantic Exploration (SemExp)](#p64) (2020)

</details>

[↑ Start of 5.4](#topic-spatial-reasoning) · [↑ Back to topic navigation](#topics)

---

<a id="area-world-models-agents"></a>
## 6. World Models & Embodied Agents


<a id="topic-world-models"></a>
### 6.1 World Models & Environment Prediction

> **Scope** · State representations, dynamics prediction, action-conditioned prediction and future rollouts
>
> **5 papers · Newest first**

---

<a id="p68"></a>
#### Mastering diverse control tasks through world models (Nature 2025)

[![arXiv: 2301.04104](https://img.shields.io/badge/arXiv-2301.04104-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2301.04104) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2301.04104) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://danijar.com/project/dreamerv3/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/danijar/dreamerv3) [![GitHub stars](https://img.shields.io/github/stars/danijar/dreamerv3?style=flat-square&label=stars&color=C58A18)](https://github.com/danijar/dreamerv3/stargazers) [![GitHub forks](https://img.shields.io/github/forks/danijar/dreamerv3?style=flat-square&label=forks&color=64748B)](https://github.com/danijar/dreamerv3/forks) &nbsp; [`T9`](#t9)

Learns environment dynamics, rewards and continuation, then trains policies on imagined latent trajectories with cross-domain stabilization.

---

<a id="p59"></a>
#### Driving into the Future: Multiview Visual Forecasting and Planning with World Model for Autonomous Driving (CVPR 2024)

[![arXiv: 2311.17918](https://img.shields.io/badge/arXiv-2311.17918-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2311.17918) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2311.17918) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://drive-wm.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/BraveGroup/Drive-WM) [![GitHub stars](https://img.shields.io/github/stars/BraveGroup/Drive-WM?style=flat-square&label=stars&color=C58A18)](https://github.com/BraveGroup/Drive-WM/stargazers) [![GitHub forks](https://img.shields.io/github/forks/BraveGroup/Drive-WM?style=flat-square&label=forks&color=64748B)](https://github.com/BraveGroup/Drive-WM/forks) &nbsp; [`T6`](#t6) [`T9`](#t9)

Forecasts action-conditioned multiview driving futures and evaluates candidate trajectories with image-based rewards.

---

<a id="p62"></a>
#### Diffusion for World Modeling: Visual Details Matter in Atari (NeurIPS 2024)

[![arXiv: 2405.12399](https://img.shields.io/badge/arXiv-2405.12399-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2405.12399) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2405.12399) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://diamond-wm.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/eloialonso/diamond) [![GitHub stars](https://img.shields.io/github/stars/eloialonso/diamond?style=flat-square&label=stars&color=C58A18)](https://github.com/eloialonso/diamond/stargazers) [![GitHub forks](https://img.shields.io/github/forks/eloialonso/diamond?style=flat-square&label=forks&color=64748B)](https://github.com/eloialonso/diamond/forks) &nbsp; [`T9`](#t9)

Uses a pixel-space diffusion world model to predict visual dynamics and train policies through imagination.

---

<a id="p58"></a>
#### GAIA-1: A Generative World Model for Autonomous Driving (arXiv 2023)

[![arXiv: 2309.17080](https://img.shields.io/badge/arXiv-2309.17080-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2309.17080) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2309.17080) &nbsp; [`T9`](#t9)

Models video, text and actions as token sequences to generate action-conditioned future driving scenarios.

---

<a id="p67"></a>
#### Learning Latent Dynamics for Planning from Pixels (ICML 2019)

[![arXiv: 1811.04551](https://img.shields.io/badge/arXiv-1811.04551-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1811.04551) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/1811.04551) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://planetrl.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/google-research/planet) [![GitHub stars](https://img.shields.io/github/stars/google-research/planet?style=flat-square&label=stars&color=C58A18)](https://github.com/google-research/planet/stargazers) [![GitHub forks](https://img.shields.io/github/forks/google-research/planet?style=flat-square&label=forks&color=64748B)](https://github.com/google-research/planet/forks) &nbsp; [`T9`](#t9)

Learns deterministic-stochastic latent dynamics from pixels and searches action sequences through multistep prediction.

---

<details>
<summary>Related reading · 3 papers in other topics</summary>

- [GameNGen](#p61) (2025)
- [UniSim](#p57) (2024)
- [Genie](#p60) (2024)

</details>

[↑ Start of 6.1](#topic-world-models) · [↑ Back to topic navigation](#topics)

---


<a id="topic-interactive-simulation"></a>
### 6.2 Interactive Environments & Simulation

> **Scope** · Interactive world generation, scene persistence, training and evaluation environments, and synthetic data
>
> **3 papers · Newest first**

---

<a id="p61"></a>
#### Diffusion Models Are Real-Time Game Engines (ICLR 2025)

[![arXiv: 2408.14837](https://img.shields.io/badge/arXiv-2408.14837-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2408.14837) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2408.14837) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://gamengen.github.io/) &nbsp; [`T9`](#t9)

Conditions diffusion on frame histories and actions, with noise augmentation, to simulate interactive DOOM gameplay.

---

<a id="p57"></a>
#### Learning Interactive Real-World Simulators (ICLR 2024)

[![arXiv: 2310.06114](https://img.shields.io/badge/arXiv-2310.06114-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2310.06114) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2310.06114) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://universal-simulator.github.io/unisim/) &nbsp; [`T9`](#t9)

Learns an action-conditioned visual simulator from heterogeneous data for interactive experience generation and agent training.

---

<a id="p60"></a>
#### Genie: Generative Interactive Environments (ICML 2024)

[![arXiv: 2402.15391](https://img.shields.io/badge/arXiv-2402.15391-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2402.15391) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2402.15391) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://sites.google.com/view/genie-2024/) &nbsp; [`T9`](#t9)

Learns latent actions and spatiotemporal dynamics from unlabeled video to generate frame-by-frame interactive environments.

---

<details>
<summary>Related reading · 2 papers in other topics</summary>

- [Drive-WM](#p59) (2024)
- [DIAMOND](#p62) (2024)

</details>

[↑ Start of 6.2](#topic-interactive-simulation) · [↑ Back to topic navigation](#topics)

---


<a id="topic-embodied-agents"></a>
### 6.3 Embodied Agents, Planning & Control

> **Scope** · Visual navigation, robotic manipulation, active perception, spatial-memory-guided planning and perception–action loops
>
> **4 papers · Newest first**

---

<a id="p66"></a>
#### CLIPort: What and Where Pathways for Robotic Manipulation (CoRL 2021 / PMLR 2022)

[![arXiv: 2109.12098](https://img.shields.io/badge/arXiv-2109.12098-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2109.12098) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2109.12098) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://cliport.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/cliport/cliport) [![GitHub stars](https://img.shields.io/github/stars/cliport/cliport?style=flat-square&label=stars&color=C58A18)](https://github.com/cliport/cliport/stargazers) [![GitHub forks](https://img.shields.io/github/forks/cliport/cliport?style=flat-square&label=forks&color=64748B)](https://github.com/cliport/cliport/forks) &nbsp; [`T1`](#t1) [`T8`](#t8)

Combines CLIP semantics with Transporter spatial correspondence for language-conditioned pick-and-place manipulation.

---

<a id="p65"></a>
#### Transporter Networks: Rearranging the Visual World for Robotic Manipulation (CoRL 2020 / PMLR 2021)

[![arXiv: 2010.14406](https://img.shields.io/badge/arXiv-2010.14406-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2010.14406) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2010.14406) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://transporternets.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/google-research/ravens) [![GitHub stars](https://img.shields.io/github/stars/google-research/ravens?style=flat-square&label=stars&color=C58A18)](https://github.com/google-research/ravens/stargazers) [![GitHub forks](https://img.shields.io/github/forks/google-research/ravens?style=flat-square&label=forks&color=64748B)](https://github.com/google-research/ravens/forks) &nbsp; [`T1`](#t1) [`T8`](#t8)

Translates and rotates visual features and correlates them to infer pick-and-place displacements for robotic manipulation.

---

<a id="p63"></a>
#### Learning To Explore Using Active Neural SLAM (ICLR 2020)

[![arXiv: 2004.05155](https://img.shields.io/badge/arXiv-2004.05155-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2004.05155) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2004.05155) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/devendrachaplot/Neural-SLAM) [![GitHub stars](https://img.shields.io/github/stars/devendrachaplot/Neural-SLAM?style=flat-square&label=stars&color=C58A18)](https://github.com/devendrachaplot/Neural-SLAM/stargazers) [![GitHub forks](https://img.shields.io/github/forks/devendrachaplot/Neural-SLAM?style=flat-square&label=forks&color=64748B)](https://github.com/devendrachaplot/Neural-SLAM/forks) &nbsp; [`T6`](#t6)

Combines learned spatial mapping, global exploration and local planning for active embodied exploration.

---

<a id="p64"></a>
#### Object Goal Navigation using Goal-Oriented Semantic Exploration (NeurIPS 2020)

[![arXiv: 2007.00643](https://img.shields.io/badge/arXiv-2007.00643-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2007.00643) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/devendrachaplot/Object-Goal-Navigation) [![GitHub stars](https://img.shields.io/github/stars/devendrachaplot/Object-Goal-Navigation?style=flat-square&label=stars&color=C58A18)](https://github.com/devendrachaplot/Object-Goal-Navigation/stargazers) [![GitHub forks](https://img.shields.io/github/forks/devendrachaplot/Object-Goal-Navigation?style=flat-square&label=forks&color=64748B)](https://github.com/devendrachaplot/Object-Goal-Navigation/forks) &nbsp; [`T6`](#t6)

Builds episodic semantic maps and uses goal-dependent spatial priors for object-goal navigation in unseen environments.

---

<details>
<summary>Related reading · 8 papers in other topics</summary>

- [DreamerV3](#p68) (2025)
- [ConceptGraphs](#p56) (2024)
- [UniSim](#p57) (2024)
- [Visual Language Maps (VLMaps)](#p54) (2023)
- [ConceptFusion](#p55) (2023)
- [DROID-SLAM](#p40) (2021)
- [Semantic MapNet (SMNet)](#p53) (2021)
- [PlaNet](#p67) (2019)

</details>

[↑ Start of 6.3](#topic-embodied-agents) · [↑ Back to topic navigation](#topics)

---


<a id="technology"></a>
## 🧩 Technique cross-index

Methods can belong to multiple families. Follow a method name to its primary entry; `T1–T9` tags link back to this map. Works are listed newest year first.

<details>
<summary><b>Browse all 9 technique families</b></summary>

| Technique family | Core representation | Works |
| --- | --- | --- |
| <a id="t1"></a>**T1 · Parametric geometry** | Rigid / similarity / affine / homography | [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) · [CLIPort](#p66) · [Unsupervised Deep Image Stitching (UDIS)](#p14) · [Transporter Networks](#p65) · [Deep Image Homography Estimation](#p13) · [COLMAP / Structure-from-Motion Revisited](#p38) · [Lucas–Kanade / Inverse Compositional](#c02) |
| <a id="t2"></a>**T2 · Control points and splines** | TPS / RBF / FFD / B-splines / MLS | [WarpI2I](#n26) · [StabStitch](#n28) · [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) · [Thin-Plate Spline Motion Model for Image Animation](#n03) · [Adaptive Content Generation and Preservation (ACGPN)](#p28) · [Deep Learning Image Registration (DLIR)](#p18) · [CP-VTON](#c24) · [VITON](#p27) · [Bounded Biharmonic Weights (BBW)](#p03) · [Moving Least Squares (MLS)](#c08) · [B-spline FFD Registration](#c07) · [Beier–Neely Feature-Based Morphing](#c06) · [Thin-Plate Spline (TPS) / Principal Warps](#c05) · [Free-Form Deformation (FFD)](#c04) |
| <a id="t3"></a>**T3 · Meshes and local shape preservation** | Piecewise maps / ARAP / local projective models | [StabStitch](#n28) · [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) · [Unsupervised Deep Image Stitching (UDIS)](#p14) · [MeshFlow](#p16) · [DynamicFusion](#p50) · [As-Projective-As-Possible (APAP) / Moving DLT](#c12) · [Bundled Camera Paths](#p15) · [Bounded Biharmonic Weights (BBW)](#p03) · [Content-Preserving Warps for 3D Video Stabilization](#c29) · [As-Rigid-As-Possible (ARAP) Surface Modeling](#c09) · [Embedded Deformation](#p02) · [Laplacian Surface Editing](#p01) |
| <a id="t4"></a>**T4 · Dense correspondence and optical flow** | Dense flow / correlation volumes / global matching | [MEMFOF](#n20) · [SEA-RAFT](#n13) · [DragAnything](#p37) · [MASt3R](#p42) · [Robust Dense Matching (RoMa)](#p71) · [UniMatch: Unifying Flow, Stereo and Depth Estimation](#n09) · [FlowFormer++](#p12) · [DragNUWA](#p36) · [Dense Kernelized Matching (DKM)](#p70) · [GMFlow](#n01) · [FlowFormer](#n02) · [FILM: Frame Interpolation for Large Motion](#n04) · [BasicVSR++](#n07) · [RIFE](#p23) · [Global Motion Aggregation (GMA)](#p11) · [BasicVSR](#p25) · [Parser-Free Appearance Flow (PF-AFN)](#p29) · [DROID-SLAM](#p40) · [Neural Scene Flow Fields (NSFF)](#p49) · [LoFTR](#p69) · [RAFT](#c20) · [Depth-Aware Interpolation (DAIN)](#p22) · [EDVR](#p24) · [Task-Oriented Flow (TOFlow)](#p26) · [PWC-Net](#c15) · [LiteFlowNet](#p10) · [Super SloMo](#p21) · [FlowNet 2.0](#p08) · [SPyNet](#p09) · [MeshFlow](#p16) · [FlowNet](#p07) · [SIFT Flow](#p72) · [Lucas–Kanade / Inverse Compositional](#c02) · [Brox et al. Variational Optical Flow](#c27) · [Horn–Schunck](#c03) |
| <a id="t5"></a>**T5 · Invertible deformation and registration** | Velocity fields / diffeomorphisms / inverse consistency | [uniGradICON](#n14) · [TransMorph](#n05) · [SynthMorph](#n06) · [ICON](#p20) · [Symmetric Diffeomorphic Registration (SYMNet)](#p19) · [VoxelMorph](#c18) · [Deep Learning Image Registration (DLIR)](#p18) · [Diffeomorphic Demons](#c11) · [SyN: Symmetric Diffeomorphic Registration](#c10) · [LDDMM / Geodesic Flows of Diffeomorphisms](#c26) · [B-spline FFD Registration](#c07) · [Demons Registration](#p17) |
| <a id="t6"></a>**T6 · Depth and 3D reprojection** | Depth / camera pose / projection / visibility | [CameraNoise](#n24) · [Warp-as-History](#n27) · [WAVE: Warp-Based View Guidance](#n22) · [SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion](#n23) · [GenWarp](#n15) · [MotionCtrl](#p34) · [CameraCtrl](#p35) · [DUSt3R](#p41) · [MASt3R](#p42) · [Dynamic 3D Gaussians](#p51) · [ConceptGraphs](#p56) · [Drive-WM](#p59) · [UniMatch: Unifying Flow, Stereo and Depth Estimation](#n09) · [3D Gaussian Splatting (3DGS)](#p45) · [Visual Language Maps (VLMaps)](#p54) · [ConceptFusion](#p55) · [TiNeuVox](#p52) · [DROID-SLAM](#p40) · [IBRNet](#p46) · [pixelNeRF](#p47) · [Neural Scene Flow Fields (NSFF)](#p49) · [Semantic MapNet (SMNet)](#p53) · [NeRF](#p44) · [Active Neural SLAM](#p63) · [Goal-Oriented Semantic Exploration (SemExp)](#p64) · [Monodepth2](#c16) · [Depth-Aware Interpolation (DAIN)](#p22) · [MVSNet](#p39) · [Stereo Magnification / Multiplane Images](#p48) · [SfMLearner](#p43) · [COLMAP / Structure-from-Motion Revisited](#p38) · [DynamicFusion](#p50) · [Depth-Image-Based Rendering (DIBR)](#c28) |
| <a id="t7"></a>**T7 · Differentiable sampling and splatting** | Interpolation / footprints / aggregation / adjoints | [LookingGlass / Laplacian Pyramid Warping (LPW)](#n21) · [SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion](#n23) · [How I Warped Your Noise / ∫-noise](#n16) · [Dynamic 3D Gaussians](#p51) · [ImWIP](#n10) · [3D Gaussian Splatting (3DGS)](#p45) · [IBRNet](#p46) · [Softmax Splatting](#c19) · [Soft Rasterizer (SoftRas)](#p06) · [Depth-Aware Interpolation (DAIN)](#p22) · [Neural 3D Mesh Renderer](#p05) · [Spatial Transformer Networks (STN)](#c13) · [EWA Volume Splatting](#c25) · [Surface Splatting](#p04) |
| <a id="t8"></a>**T8 · Learned feature and 3D deformation** | Offsets / local affine motion / canonical fields | [Deformable 3D Gaussians](#n11) · [4D Gaussian Splatting for Real-Time Dynamic Scene Rendering](#n12) · [Dynamic 3D Gaussians](#p51) · [Thin-Plate Spline Motion Model for Image Animation](#n03) · [FILM: Frame Interpolation for Large Motion](#n04) · [BasicVSR++](#n07) · [TiNeuVox](#p52) · [CLIPort](#p66) · [D-NeRF](#c21) · [Nerfies](#c22) · [HyperNeRF](#c23) · [Neural Scene Flow Fields (NSFF)](#p49) · [Transporter Networks](#p65) · [First Order Motion Model (FOMM)](#c17) · [EDVR](#p24) · [X2Face](#p30) · [Deformable ConvNets (DCN)](#c14) · [DynamicFusion](#p50) |
| <a id="t9"></a>**T9 · Generative, frequency and stochastic warping** | Geometry–generation fusion / noise transport / frequency handling | [CameraNoise](#n24) · [DMAligner](#n25) · [WarpI2I](#n26) · [Warp-as-History](#n27) · [Go-with-the-Flow](#n19) · [LookingGlass / Laplacian Pyramid Warping (LPW)](#n21) · [WAVE: Warp-Based View Guidance](#n22) · [SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion](#n23) · [GameNGen](#p61) · [DreamerV3](#p68) · [GenWarp](#n15) · [How I Warped Your Noise / ∫-noise](#n16) · [Warped Diffusion](#n17) · [StableVITON](#n18) · [FreeNoise](#p32) · [ConsistI2V](#p33) · [MotionCtrl](#p34) · [CameraCtrl](#p35) · [DragAnything](#p37) · [UniSim](#p57) · [Drive-WM](#p59) · [Genie](#p60) · [DIAMOND](#p62) · [Preserve Your Own Correlation (PYoCo)](#p31) · [DragNUWA](#p36) · [GAIA-1](#p58) · [Parser-Free Appearance Flow (PF-AFN)](#p29) · [Adaptive Content Generation and Preservation (ACGPN)](#p28) · [First Order Motion Model (FOMM)](#c17) · [PlaNet](#p67) · [CP-VTON](#c24) · [VITON](#p27) · [X2Face](#p30) |

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
| Selection evidence and citation snapshots | [2026-10-24 expansion audit](docs/EXPANSION_AUDIT.md) |

<a id="contributing"></a>
## 🤝 Contributing

Suggestions, corrections and verified links are welcome through [Issues](https://github.com/gulucaptain/Awesome-Warping-Algorithm/issues) and [Pull Requests](https://github.com/gulucaptain/Awesome-Warping-Algorithm/pulls).

Please include the **paper title, publication year/status, Paper, Project, GitHub, technique family, primary topic and related topic tags**. Leave unavailable links empty, and distinguish author implementations, third-party reimplementations and shared frameworks.

Edit [the bilingual catalog](data/catalog.json) and run `python3 scripts/build_readme.py` to update both READMEs. Counts and indexes use the same data; check consistency with `python3 scripts/build_readme.py --check`. Set each work's unique home with `primary_topic`; `topics` contains that home and related directions. When adding papers to a reserved topic, set its `reserved` flag to `false`. Prioritize topic fit, verified publication records and established impact. Citation snapshots must name the provider, matched record and query date; do not add preprint and publication counts together. See the [curation audit](docs/EXPANSION_AUDIT.md) for this expansion.

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
