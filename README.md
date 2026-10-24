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

<b>211</b> Papers &nbsp; · &nbsp; <b>123</b> Repositories &nbsp; · &nbsp; <b>6</b> Research areas &nbsp; · &nbsp; <b>16</b> Topics

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
<td>18</td>
</tr>
<tr>
<td><a href="#topic-sampling-splatting">1.2 Differentiable Sampling &amp; Splatting</a></td>
<td>12</td>
</tr>
<tr>
<td rowspan="3" valign="middle"><a href="#area-alignment">2. Correspondence &amp; Image Alignment</a></td>
<td><a href="#topic-optical-flow">2.1 Optical Flow &amp; Dense Correspondence</a></td>
<td>26</td>
</tr>
<tr>
<td><a href="#topic-image-alignment">2.2 Image Registration, Stitching &amp; Stabilization</a></td>
<td>15</td>
</tr>
<tr>
<td><a href="#topic-medical-registration">2.3 Medical Registration &amp; Diffeomorphic Deformation</a></td>
<td>21</td>
</tr>
<tr>
<td rowspan="2" valign="middle"><a href="#area-video-processing">3. Video Processing &amp; Human Deformation</a></td>
<td><a href="#topic-video-restoration">3.1 Video Interpolation, Restoration &amp; Editing</a></td>
<td>21</td>
</tr>
<tr>
<td><a href="#topic-human-deformation">3.2 Animation, Motion Transfer &amp; Virtual Try-On</a></td>
<td>18</td>
</tr>
<tr>
<td rowspan="2" valign="middle"><a href="#area-video-generation">4. Video Generation &amp; Motion Control</a></td>
<td><a href="#topic-noise-warping">4.1 Noise Warping &amp; Temporal Consistency</a></td>
<td>7</td>
</tr>
<tr>
<td><a href="#topic-controlled-generation">4.2 Camera-, Trajectory- &amp; Motion-Controlled Generation</a></td>
<td>11</td>
</tr>
<tr>
<td rowspan="4" valign="middle"><a href="#area-spatial-intelligence">5. Spatial Intelligence</a></td>
<td><a href="#topic-spatial-perception">5.1 Spatial Perception, Depth &amp; 3D Reconstruction</a></td>
<td>12</td>
</tr>
<tr>
<td><a href="#topic-novel-view-synthesis">5.2 Reprojection &amp; Novel View Synthesis</a></td>
<td>16</td>
</tr>
<tr>
<td><a href="#topic-dynamic-3d">5.3 Dynamic 3D &amp; 4D Scenes</a></td>
<td>17</td>
</tr>
<tr>
<td><a href="#topic-spatial-reasoning">5.4 Spatial Reasoning &amp; Scene Memory</a></td>
<td>5</td>
</tr>
<tr>
<td rowspan="3" valign="middle"><a href="#area-world-models-agents">6. World Models &amp; Embodied Agents</a></td>
<td><a href="#topic-world-models">6.1 World Models &amp; Environment Prediction</a></td>
<td>3</td>
</tr>
<tr>
<td><a href="#topic-interactive-simulation">6.2 Interactive Environments &amp; Simulation</a></td>
<td>2</td>
</tr>
<tr>
<td><a href="#topic-embodied-agents">6.3 Embodied Agents, Planning &amp; Control</a></td>
<td>7</td>
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
> **18 papers · Newest first**

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

<a id="s003"></a>
#### Inpaint4Drag: Repurposing Inpainting Models for Drag-Based Image Editing via Bidirectional Warping (ICCV 2025)

[![arXiv: 2509.04582](https://img.shields.io/badge/arXiv-2509.04582-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.04582) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2509.04582) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://visual-ai.github.io/inpaint4drag/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Visual-AI/Inpaint4Drag) [![GitHub stars](https://img.shields.io/github/stars/Visual-AI/Inpaint4Drag?style=flat-square&label=stars&color=C58A18)](https://github.com/Visual-AI/Inpaint4Drag/stargazers) [![GitHub forks](https://img.shields.io/github/forks/Visual-AI/Inpaint4Drag?style=flat-square&label=forks&color=64748B)](https://github.com/Visual-AI/Inpaint4Drag/forks) &nbsp; [`T3`](#t3) [`T9`](#t9)

Separates pixel-space bidirectional warping from inpainting to deform selected regions and fill newly exposed content.

---

<a id="s004"></a>
#### FlowDrag: 3D-aware Drag-based Image Editing with Mesh-guided Deformation Vector Flow Fields (ICML 2025)

[![arXiv: 2507.08285](https://img.shields.io/badge/arXiv-2507.08285-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.08285) &nbsp; [`T3`](#t3) [`T6`](#t6) [`T9`](#t9)

Deforms a reconstructed mesh with user handles and projects its displacement into a 2D flow field for diffusion editing.

---

<a id="a04"></a>
#### FastDrag: Manipulate Anything in One Step (NeurIPS 2024)

[![arXiv: 2405.15769](https://img.shields.io/badge/arXiv-2405.15769-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2405.15769) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://fastdrag-site.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/XuanjiaZ/FastDrag) [![GitHub stars](https://img.shields.io/github/stars/XuanjiaZ/FastDrag?style=flat-square&label=stars&color=C58A18)](https://github.com/XuanjiaZ/FastDrag/stargazers) [![GitHub forks](https://img.shields.io/github/forks/XuanjiaZ/FastDrag?style=flat-square&label=forks&color=64748B)](https://github.com/XuanjiaZ/FastDrag/forks) &nbsp; [`T2`](#t2) [`T9`](#t9)

Moves latent pixels in one step with a latent warpage function that mimics stretched material, then fills warp-induced holes with bilateral nearest-neighbor interpolation for drag editing.

---

<a id="a03"></a>
#### Rectangling panoramic images via warping (SIGGRAPH / TOG 2013)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1145/2461912.2462004) &nbsp; [`T3`](#t3)

Uses a local warp to stretch irregular stitched panoramas to a rectangle, then a line- and shape-preserving global mesh optimization to reduce distortion instead of cropping or completion.

---

<a id="p03"></a>
#### Bounded Biharmonic Weights for Real-Time Deformation (SIGGRAPH / TOG 2011)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://igl.ethz.ch/projects/bbw/bounded-biharmonic-weights-siggraph-2011-jacobson-et-al.pdf) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://igl.ethz.ch/projects/bbw/) &nbsp; [`T2`](#t2) [`T3`](#t3)

Computes shape-aware bounded biharmonic blending weights for point, bone and cage deformation handles.

---

<a id="s002"></a>
#### Green Coordinates (SIGGRAPH / TOG 2008)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.wisdom.weizmann.ac.il/~ylipman/GC/gc_techrep.pdf) &nbsp; [`T3`](#t3)

Combines cage vertices and face orientations through Green coordinates for shape-preserving space deformation.

---

<a id="a02"></a>
#### Optimized scale-and-stretch for image resizing (SIGGRAPH Asia / TOG 2008)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1145/1409060.1409071) &nbsp; [`T3`](#t3)

Optimizes per-quad scaling and stretching on a mesh warp so salient regions scale nearly uniformly while distortion spreads into less important areas for content-aware resizing.

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

<a id="s001"></a>
#### Harmonic Coordinates for Character Articulation (SIGGRAPH / TOG 2007)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.cs.jhu.edu/~misha/ReadingSeminar/Papers/Joshi07.pdf) &nbsp; [`T3`](#t3)

Uses harmonic cage weights to drive volumetric deformation with nonnegative influence and interior locality.

---

<a id="c08"></a>
#### Image deformation using moving least squares (SIGGRAPH / TOG 2006)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1145/1141911.1141920) &nbsp; [`T2`](#t2)

Schaefer and colleagues construct affine, similarity and rigid image deformations through locally weighted fitting, enabling interactive point and line controls.

---

<a id="a01"></a>
#### Mean value coordinates for closed triangular meshes (SIGGRAPH / TOG 2005)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1145/1073204.1073229) &nbsp; [`T3`](#t3)

Extends mean value coordinates to closed triangular cages, giving smooth cage-vertex weights that drive interior space deformation.

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
<summary>Related reading · 9 papers in other topics</summary>

- [Tether / Autonomous Functional Play](#s077) (2026)
- [SC-GS](#s061) (2024)
- [Unsupervised Deep Image Stitching (UDIS)](#p14) (2021)
- [Transporter Networks](#p65) (2021)
- [X2Face](#p30) (2018)
- [Deep Image Homography Estimation](#p13) (2016)
- [DynamicFusion](#p50) (2015)
- [EWA Volume Splatting](#c25) (2001)
- [Heckbert Texture Mapping & Image Warping](#a05) (1989)

</details>

[↑ Start of 1.1](#topic-geometry-editing) · [↑ Back to topic navigation](#topics)

---

<a id="topic-15"></a>
<a id="topic-sampling-splatting"></a>
### 1.2 Differentiable Sampling & Splatting

> **Scope** · Interpolation, resampling, differentiable spatial transforms, sampling kernels, adjoints and derivatives
>
> **12 papers · Newest first**

---

<a id="s079"></a>
#### Towards Progressive Multi-Frequency Representation for Image Warping (CVPR 2024)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content/CVPR2024/html/Xiao_Towards_Progressive_Multi-Frequency_Representation_for_Image_Warping_CVPR_2024_paper.html) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/junxiao01/MFR) [![GitHub stars](https://img.shields.io/github/stars/junxiao01/MFR?style=flat-square&label=stars&color=C58A18)](https://github.com/junxiao01/MFR/stargazers) [![GitHub forks](https://img.shields.io/github/forks/junxiao01/MFR?style=flat-square&label=forks&color=64748B)](https://github.com/junxiao01/MFR/forks) &nbsp; [`T7`](#t7)

Uses progressive frequency representations and learnable Gabor filters to preserve local detail during image warping.

---

<a id="n10"></a>
#### ImWIP: Open-source image warping toolbox with adjoints and derivatives (SoftwareX 2023)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1016/j.softx.2023.101524) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://imwip.readthedocs.io/en/latest/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/RendersJens/ImWIP) [![GitHub stars](https://img.shields.io/github/stars/RendersJens/ImWIP?style=flat-square&label=stars&color=C58A18)](https://github.com/RendersJens/ImWIP/stargazers) [![GitHub forks](https://img.shields.io/github/forks/RendersJens/ImWIP?style=flat-square&label=forks&color=64748B)](https://github.com/RendersJens/ImWIP/forks) &nbsp; [`T7`](#t7)

Provides differentiable image-warp operators with exact discrete adjoints and derivatives for inverse-problem optimization.

---

<a id="s006"></a>
#### Kernel Aware Resampler (CVPR 2023)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content/CVPR2023/html/Bernasconi_Kernel_Aware_Resampler_CVPR_2023_paper.html) &nbsp; [`T7`](#t7)

Conditions image resampling on spatially varying degradation that accounts for reconstruction kernels, geometric distortion and antialiasing.

---

<a id="s085"></a>
#### Learning Local Implicit Fourier Representation for Image Warping (ECCV 2022)

[![arXiv: 2207.01831](https://img.shields.io/badge/arXiv-2207.01831-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2207.01831) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/jaewon-lee-b/ltew) [![GitHub stars](https://img.shields.io/github/stars/jaewon-lee-b/ltew?style=flat-square&label=stars&color=C58A18)](https://github.com/jaewon-lee-b/ltew/stargazers) [![GitHub forks](https://img.shields.io/github/forks/jaewon-lee-b/ltew?style=flat-square&label=forks&color=64748B)](https://github.com/jaewon-lee-b/ltew/forks) &nbsp; [`T7`](#t7)

Uses local texture estimates and transformation Jacobians to predict Fourier responses for continuous image warping.

---

<a id="s086"></a>
#### SRWarp: Generalized Image Super-Resolution under Arbitrary Transformation (CVPR 2021)

[![arXiv: 2104.10325](https://img.shields.io/badge/arXiv-2104.10325-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2104.10325) &nbsp; [`T7`](#t7)

Generalizes super-resolution to arbitrary spatial transforms using multiscale features and adaptive warping.

---

<a id="c19"></a>
#### Softmax Splatting for Video Frame Interpolation (CVPR 2020)

[![arXiv: 2003.05534](https://img.shields.io/badge/arXiv-2003.05534-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2003.05534) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://sniklaus.com/softsplat) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sniklaus/softmax-splatting) [![GitHub stars](https://img.shields.io/github/stars/sniklaus/softmax-splatting?style=flat-square&label=stars&color=C58A18)](https://github.com/sniklaus/softmax-splatting/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sniklaus/softmax-splatting?style=flat-square&label=forks&color=64748B)](https://github.com/sniklaus/softmax-splatting/forks) &nbsp; [`T7`](#t7)

Niklaus and Liu use softmax weighting to resolve many-to-one conflicts in a differentiable forward warp, supporting both image and feature splatting.

---

<a id="s007"></a>
#### Linearized Multi-Sampling for Differentiable Image Transformation (ICCV 2019)

[![arXiv: 1901.07124](https://img.shields.io/badge/arXiv-1901.07124-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1901.07124) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/vcg-uvic/linearized_multisampling_release) [![GitHub stars](https://img.shields.io/github/stars/vcg-uvic/linearized_multisampling_release?style=flat-square&label=stars&color=C58A18)](https://github.com/vcg-uvic/linearized_multisampling_release/stargazers) [![GitHub forks](https://img.shields.io/github/forks/vcg-uvic/linearized_multisampling_release?style=flat-square&label=forks&color=64748B)](https://github.com/vcg-uvic/linearized_multisampling_release/forks) &nbsp; [`T7`](#t7)

Uses auxiliary neighboring samples and local linearization to improve gradients through differentiable image transformations.

---

<a id="c14"></a>
#### Deformable Convolutional Networks (ICCV 2017)

[![arXiv: 1703.06211](https://img.shields.io/badge/arXiv-1703.06211-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1703.06211) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/msracver/Deformable-ConvNets) [![GitHub stars](https://img.shields.io/github/stars/msracver/Deformable-ConvNets?style=flat-square&label=stars&color=C58A18)](https://github.com/msracver/Deformable-ConvNets/stargazers) [![GitHub forks](https://img.shields.io/github/forks/msracver/Deformable-ConvNets?style=flat-square&label=forks&color=64748B)](https://github.com/msracver/Deformable-ConvNets/forks) &nbsp; [`T8`](#t8)

Learns offsets for convolutional sampling locations, allowing features to adapt to local geometric variation.

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

<a id="a05"></a>
#### Fundamentals of Texture Mapping and Image Warping (UC Berkeley Master's Thesis 1989)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1989/5504.html) &nbsp; [`T1`](#t1) [`T7`](#t7)

Systematizes affine, bilinear and projective mappings and formulates resampling in texture mapping and image warping as reconstruction, warping, prefiltering and sampling, a classic reference for antialiased resampling.

---

<details>
<summary>Related reading · 8 papers in other topics</summary>

- [Fast Forward](#s084) (2026)
- [Infinite-Resolution Integral Noise Warping](#s043) (2025)
- [Warped Diffusion](#n17) (2024)
- [Dynamic 3D Gaussians](#p51) (2024)
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
> **26 papers · Newest first**

---

<a id="a06"></a>
#### WAFT: Warping-Alone Field Transforms for Optical Flow (ICLR 2026)

[![arXiv: 2506.21526](https://img.shields.io/badge/arXiv-2506.21526-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.21526) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/princeton-vl/WAFT) [![GitHub stars](https://img.shields.io/github/stars/princeton-vl/WAFT?style=flat-square&label=stars&color=C58A18)](https://github.com/princeton-vl/WAFT/stargazers) [![GitHub forks](https://img.shields.io/github/forks/princeton-vl/WAFT?style=flat-square&label=forks&color=64748B)](https://github.com/princeton-vl/WAFT/forks) &nbsp; [`T4`](#t4) [`T7`](#t7)

Replaces cost volumes with high-resolution feature warping, estimating flow in RAFT-style iterative updates from warped features alone with lower memory and high accuracy.

---

<a id="n20"></a>
#### MEMFOF: High-Resolution Training for Memory-Efficient Multi-Frame Optical Flow Estimation (ICCV 2025)

[![arXiv: 2506.23151](https://img.shields.io/badge/arXiv-2506.23151-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.23151) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2506.23151) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://msu-video-group.github.io/memfof/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/msu-video-group/memfof) [![GitHub stars](https://img.shields.io/github/stars/msu-video-group/memfof?style=flat-square&label=stars&color=C58A18)](https://github.com/msu-video-group/memfof/stargazers) [![GitHub forks](https://img.shields.io/github/forks/msu-video-group/memfof?style=flat-square&label=forks&color=64748B)](https://github.com/msu-video-group/memfof/forks) &nbsp; [`T4`](#t4)

Combines reduced correlation representations, multiframe estimation and high-resolution training to improve memory efficiency for native FullHD optical flow.

---

<a id="s015"></a>
#### UFM: A Simple Path towards Unified Dense Correspondence with Flow (NeurIPS 2025)

[![arXiv: 2506.09278](https://img.shields.io/badge/arXiv-2506.09278-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.09278) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2506.09278) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://uniflowmatch.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/UniFlowMatch/UFM) [![GitHub stars](https://img.shields.io/github/stars/UniFlowMatch/UFM?style=flat-square&label=stars&color=C58A18)](https://github.com/UniFlowMatch/UFM/stargazers) [![GitHub forks](https://img.shields.io/github/forks/UniFlowMatch/UFM?style=flat-square&label=forks&color=64748B)](https://github.com/UniFlowMatch/UFM/forks) &nbsp; [`T4`](#t4)

Directly regresses 2D displacement from unified covisible training pairs for optical flow and wide-baseline matching.

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

<a id="s012"></a>
#### PDC-Net+: Enhanced Probabilistic Dense Correspondence Network (TPAMI 2023)

[![arXiv: 2109.13912](https://img.shields.io/badge/arXiv-2109.13912-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2109.13912) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/PruneTruong/DenseMatching) [![GitHub stars](https://img.shields.io/github/stars/PruneTruong/DenseMatching?style=flat-square&label=stars&color=C58A18)](https://github.com/PruneTruong/DenseMatching/stargazers) [![GitHub forks](https://img.shields.io/github/forks/PruneTruong/DenseMatching?style=flat-square&label=forks&color=64748B)](https://github.com/PruneTruong/DenseMatching/forks) &nbsp; [`T4`](#t4)

Jointly predicts dense correspondences and probabilistic confidence for large-displacement and wide-baseline matching.

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

<a id="s011"></a>
#### COTR: Correspondence Transformer for Matching Across Images (ICCV 2021)

[![arXiv: 2103.14167](https://img.shields.io/badge/arXiv-2103.14167-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2103.14167) &nbsp; [`T4`](#t4)

Predicts correspondences for continuous coordinate queries with a cross-image transformer and local refinement.

---

<a id="a07"></a>
#### SMURF: Self-Teaching Multi-Frame Unsupervised RAFT with Full-Image Warping (CVPR 2021)

[![arXiv: 2105.07014](https://img.shields.io/badge/arXiv-2105.07014-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2105.07014) &nbsp; [`T4`](#t4) [`T7`](#t7)

Trains RAFT without labels using full-image warping for out-of-frame motion in the photometric loss, multi-frame self-teaching and occlusion reasoning.

---

<a id="c20"></a>
#### RAFT: Recurrent All-Pairs Field Transforms for Optical Flow (ECCV 2020)

[![arXiv: 2003.12039](https://img.shields.io/badge/arXiv-2003.12039-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2003.12039) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2003.12039) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/princeton-vl/RAFT) [![GitHub stars](https://img.shields.io/github/stars/princeton-vl/RAFT?style=flat-square&label=stars&color=C58A18)](https://github.com/princeton-vl/RAFT/stargazers) [![GitHub forks](https://img.shields.io/github/forks/princeton-vl/RAFT?style=flat-square&label=forks&color=64748B)](https://github.com/princeton-vl/RAFT/forks) &nbsp; [`T4`](#t4)

Builds all-pairs correlation volumes and updates a dense flow field recurrently, providing an influential baseline for correspondence estimation.

---

<a id="s013"></a>
#### GLU-Net: Global-Local Universal Network for Dense Flow and Correspondences (CVPR 2020)

[![arXiv: 1912.05524](https://img.shields.io/badge/arXiv-1912.05524-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1912.05524) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/PruneTruong/GLU-Net) [![GitHub stars](https://img.shields.io/github/stars/PruneTruong/GLU-Net?style=flat-square&label=stars&color=C58A18)](https://github.com/PruneTruong/GLU-Net/stargazers) [![GitHub forks](https://img.shields.io/github/forks/PruneTruong/GLU-Net?style=flat-square&label=forks&color=64748B)](https://github.com/PruneTruong/GLU-Net/forks) &nbsp; [`T4`](#t4)

Combines global and local correlations with adaptive resolution for geometric, optical-flow and semantic matching.

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

<a id="a08"></a>
#### UnFlow: Unsupervised Learning of Optical Flow with a Bidirectional Census Loss (AAAI 2018)

[![arXiv: 1711.07837](https://img.shields.io/badge/arXiv-1711.07837-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1711.07837) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/simonmeister/UnFlow) [![GitHub stars](https://img.shields.io/github/stars/simonmeister/UnFlow?style=flat-square&label=stars&color=C58A18)](https://github.com/simonmeister/UnFlow/stargazers) [![GitHub forks](https://img.shields.io/github/forks/simonmeister/UnFlow?style=flat-square&label=forks&color=64748B)](https://github.com/simonmeister/UnFlow/forks) &nbsp; [`T4`](#t4) [`T7`](#t7)

Trains FlowNet without labels using census photometric losses on forward-backward warps, forward-backward consistency and occlusion masks.

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
<summary>Related reading · 5 papers in other topics</summary>

- [SceNeRFlow](#s062) (2024)
- [OmniMotion](#a39) (2023)
- [E2FGVI](#s025) (2022)
- [Neural Scene Flow Fields (NSFF)](#p49) (2021)
- [Lucas–Kanade / Inverse Compositional](#c02) (2004)

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
> **15 papers · Newest first**

---

<a id="s018"></a>
#### PixelStitch: Structure-Preserving Pixel-Wise Bidirectional Warps for Unsupervised Image Stitching (ICCV 2025)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content/ICCV2025/html/Jin_PixelStitch_Structure-Preserving_Pixel-Wise_Bidirectional_Warps_for_Unsupervised_Image_Stitching_ICCV_2025_paper.html) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MakiseChris666/PixelStitch) [![GitHub stars](https://img.shields.io/github/stars/MakiseChris666/PixelStitch?style=flat-square&label=stars&color=C58A18)](https://github.com/MakiseChris666/PixelStitch/stargazers) [![GitHub forks](https://img.shields.io/github/forks/MakiseChris666/PixelStitch?style=flat-square&label=forks&color=64748B)](https://github.com/MakiseChris666/PixelStitch/forks) &nbsp; [`T1`](#t1) [`T4`](#t4)

Uses an intermediate projection plane and bidirectional pixel-wise residual warps to align images while preserving structure.

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

<a id="s019"></a>
#### DUT: Learning Video Stabilization by Simply Watching Unstable Videos (IEEE TIP 2022)

[![arXiv: 2011.14574](https://img.shields.io/badge/arXiv-2011.14574-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2011.14574) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Annbless/DUTCode) [![GitHub stars](https://img.shields.io/github/stars/Annbless/DUTCode?style=flat-square&label=stars&color=C58A18)](https://github.com/Annbless/DUTCode/stargazers) [![GitHub forks](https://img.shields.io/github/forks/Annbless/DUTCode?style=flat-square&label=forks&color=64748B)](https://github.com/Annbless/DUTCode/forks) &nbsp; [`T1`](#t1) [`T3`](#t3)

Learns grid trajectories and adaptive smoothing from unstable videos to drive mesh-based stabilization.

---

<a id="p14"></a>
#### Unsupervised Deep Image Stitching: Reconstructing Stitched Features to Images (IEEE TIP 2021)

[![arXiv: 2106.12859](https://img.shields.io/badge/arXiv-2106.12859-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2106.12859) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nie-lang/UnsupervisedDeepImageStitching) [![GitHub stars](https://img.shields.io/github/stars/nie-lang/UnsupervisedDeepImageStitching?style=flat-square&label=stars&color=C58A18)](https://github.com/nie-lang/UnsupervisedDeepImageStitching/stargazers) [![GitHub forks](https://img.shields.io/github/forks/nie-lang/UnsupervisedDeepImageStitching?style=flat-square&label=forks&color=64748B)](https://github.com/nie-lang/UnsupervisedDeepImageStitching/forks) &nbsp; [`T1`](#t1) [`T3`](#t3)

Learns image alignment without homography labels and reconstructs stitched images from aligned features.

---

<a id="a10"></a>
#### Content-Aware Unsupervised Deep Homography Estimation (ECCV 2020)

[![arXiv: 1909.05983](https://img.shields.io/badge/arXiv-1909.05983-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1909.05983) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/JirongZhang/DeepHomography) [![GitHub stars](https://img.shields.io/github/stars/JirongZhang/DeepHomography?style=flat-square&label=stars&color=C58A18)](https://github.com/JirongZhang/DeepHomography/stargazers) [![GitHub forks](https://img.shields.io/github/forks/JirongZhang/DeepHomography?style=flat-square&label=forks&color=64748B)](https://github.com/JirongZhang/DeepHomography/forks) &nbsp; [`T1`](#t1) [`T7`](#t7)

Compares warped images in feature space with learned content masks so moving objects and weak textures do less harm to unsupervised homography estimation.

---

<a id="a09"></a>
#### Unsupervised Deep Homography: A Fast and Robust Homography Estimation Model (IEEE RA-L 2018)

[![arXiv: 1709.03966](https://img.shields.io/badge/arXiv-1709.03966-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1709.03966) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tynguyen/unsupervisedDeepHomographyRAL2018) [![GitHub stars](https://img.shields.io/github/stars/tynguyen/unsupervisedDeepHomographyRAL2018?style=flat-square&label=stars&color=C58A18)](https://github.com/tynguyen/unsupervisedDeepHomographyRAL2018/stargazers) [![GitHub forks](https://img.shields.io/github/forks/tynguyen/unsupervisedDeepHomographyRAL2018?style=flat-square&label=forks&color=64748B)](https://github.com/tynguyen/unsupervisedDeepHomographyRAL2018/forks) &nbsp; [`T1`](#t1) [`T7`](#t7)

Uses a differentiable DLT and spatial-transformer warping of predicted homographies to train homography estimation from photometric error without labels.

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

<a id="s016"></a>
#### Shape-Preserving Half-Projective Warps for Image Stitching (CVPR 2014)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content_cvpr_2014/html/Chang_Shape-Preserving_Half-Projective_Warps_2014_CVPR_paper.html) &nbsp; [`T1`](#t1)

Transitions smoothly from projective alignment to similarity transforms to reduce distortion outside image overlaps.

---

<a id="s017"></a>
#### Parallax-tolerant Image Stitching (CVPR 2014)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content_cvpr_2014/html/Zhang_Parallax-tolerant_Image_Stitching_2014_CVPR_paper.html) &nbsp; [`T1`](#t1) [`T3`](#t3)

Combines homography, content-preserving local warps and seam selection for parallax-tolerant stitching.

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

<a id="c02"></a>
#### Lucas-Kanade 20 Years On: A Unifying Framework (IJCV 2004)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.ri.cmu.edu/pub_files/pub3/baker_simon_2004_1/baker_simon_2004_1.pdf) &nbsp; [`T1`](#t1) [`T4`](#t4)

Optimizes warp parameters using image residuals. The inverse compositional formulation reuses parts of the computation and remains a foundation of direct image alignment.

---

<details>
<summary>Related reading · 11 papers in other topics</summary>

- [HomoGen](#s028) (2025)
- [Robust Dense Matching (RoMa)](#p71) (2024)
- [Dense Kernelized Matching (DKM)](#p70) (2023)
- [PDC-Net+](#s012) (2023)
- [LoFTR](#p69) (2021)
- [COTR](#s011) (2021)
- [GLU-Net](#s013) (2020)
- [Rectangling Panoramas via Warping](#a03) (2013)
- [SIFT Flow](#p72) (2011)
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
> **21 papers · Newest first**

---

<a id="s023"></a>
#### Learning Diffeomorphism for Medical Image Registration with Time-Embedded Architectures Using Semigroup Regularization (CVPR 2026)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content/CVPR2026/html/Matinkia_Learning_Diffeomorphism_for_Medical_Image_Registration_with_Time-Embedded_Architectures_Using_CVPR_2026_paper.html) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://mattkia.github.io/SGDIR/) &nbsp; [`T5`](#t5)

Models continuous-time registration with time-embedded networks and semigroup regularization instead of explicit integration.

---

<a id="s084"></a>
#### Fast forward: Rephrasing 3D deformable image registration through density alignment and splatting (MIDL 2025 / PMLR 2026)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://proceedings.mlr.press/v301/heinrich26a.html) &nbsp; [`T5`](#t5) [`T7`](#t7)

Recasts medical registration as density alignment of forward-splatted point clouds using differentiable rasterization.

---

<a id="n14"></a>
#### uniGradICON: A Foundation Model for Medical Image Registration (MICCAI 2024)

[![arXiv: 2403.05780](https://img.shields.io/badge/arXiv-2403.05780-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2403.05780) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/uncbiag/uniGradICON) [![GitHub stars](https://img.shields.io/github/stars/uncbiag/uniGradICON?style=flat-square&label=stars&color=C58A18)](https://github.com/uncbiag/uniGradICON/stargazers) [![GitHub forks](https://img.shields.io/github/forks/uncbiag/uniGradICON?style=flat-square&label=forks&color=64748B)](https://github.com/uncbiag/uniGradICON/forks) &nbsp; [`T5`](#t5)

Moves learned registration toward a reusable model across datasets, anatomical regions and new tasks, including zero-shot use and initialization for adaptation.

---

<a id="s020"></a>
#### GradICON: Approximate Diffeomorphisms via Gradient Inverse Consistency (CVPR 2023)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content/CVPR2023/html/Tian_GradICON_Approximate_Diffeomorphisms_via_Gradient_Inverse_Consistency_CVPR_2023_paper.html) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/uncbiag/ICON) [![GitHub stars](https://img.shields.io/github/stars/uncbiag/ICON?style=flat-square&label=stars&color=C58A18)](https://github.com/uncbiag/ICON/stargazers) [![GitHub forks](https://img.shields.io/github/forks/uncbiag/ICON?style=flat-square&label=forks&color=64748B)](https://github.com/uncbiag/ICON/forks) &nbsp; [`T5`](#t5)

Regularizes the Jacobian of composed forward and reverse maps to learn smoother medical registration transforms.

---

<a id="s022"></a>
#### Fourier-Net: Fast Image Registration with Band-limited Deformation (AAAI 2023)

[![arXiv: 2211.16342](https://img.shields.io/badge/arXiv-2211.16342-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2211.16342) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/xi-jia/Fourier-Net) [![GitHub stars](https://img.shields.io/github/stars/xi-jia/Fourier-Net?style=flat-square&label=stars&color=C58A18)](https://github.com/xi-jia/Fourier-Net/stargazers) [![GitHub forks](https://img.shields.io/github/forks/xi-jia/Fourier-Net?style=flat-square&label=forks&color=64748B)](https://github.com/xi-jia/Fourier-Net/forks) &nbsp; [`T5`](#t5)

Predicts band-limited Fourier deformation coefficients and decodes them into full-resolution displacement fields.

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

<a id="s021"></a>
#### Large Deformation Diffeomorphic Image Registration with Laplacian Pyramid Networks (MICCAI 2020)

[![arXiv: 2006.16148](https://img.shields.io/badge/arXiv-2006.16148-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2006.16148) &nbsp; [`T5`](#t5)

Estimates deformations coarse to fine in a Laplacian pyramid within a diffeomorphic registration framework.

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

<a id="a14"></a>
#### Recursive Cascaded Networks for Unsupervised Medical Image Registration (ICCV 2019)

[![arXiv: 1907.12353](https://img.shields.io/badge/arXiv-1907.12353-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1907.12353) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/Recursive-Cascaded-Networks) [![GitHub stars](https://img.shields.io/github/stars/microsoft/Recursive-Cascaded-Networks?style=flat-square&label=stars&color=C58A18)](https://github.com/microsoft/Recursive-Cascaded-Networks/stargazers) [![GitHub forks](https://img.shields.io/github/forks/microsoft/Recursive-Cascaded-Networks?style=flat-square&label=forks&color=64748B)](https://github.com/microsoft/Recursive-Cascaded-Networks/forks) &nbsp; [`T5`](#t5) [`T7`](#t7)

Cascades subnetworks that each predict an incremental deformation of the previously warped image and compose the fields to handle large deformations.

---

<a id="a13"></a>
#### Unsupervised Learning for Fast Probabilistic Diffeomorphic Registration (MICCAI 2018)

[![arXiv: 1805.04605](https://img.shields.io/badge/arXiv-1805.04605-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1805.04605) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/voxelmorph/voxelmorph) [![GitHub stars](https://img.shields.io/github/stars/voxelmorph/voxelmorph?style=flat-square&label=stars&color=C58A18)](https://github.com/voxelmorph/voxelmorph/stargazers) [![GitHub forks](https://img.shields.io/github/forks/voxelmorph/voxelmorph?style=flat-square&label=forks&color=64748B)](https://github.com/voxelmorph/voxelmorph/forks) &nbsp; [`T5`](#t5) [`T7`](#t7)

Predicts a velocity-field distribution and integrates it into a diffeomorphic deformation inside the network by scaling and squaring, trained without labels through a spatial-transformer warp.

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

<a id="a12"></a>
#### A fast diffeomorphic image registration algorithm (NeuroImage 2007)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1016/j.neuroimage.2007.07.007) &nbsp; [`T5`](#t5)

Models diffeomorphisms with constant velocity fields and exponentiation while building population templates, a widely used brain registration method in SPM.

---

<a id="a11"></a>
#### A Log-Euclidean Framework for Statistics on Diffeomorphisms (MICCAI 2006)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1007/11866565_113) &nbsp; [`T5`](#t5)

Parameterizes diffeomorphisms by group exponentials of stationary velocity fields, computes them efficiently by scaling and squaring, and performs statistics in the log domain; later learned registration widely adopts this integration.

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
### 3.1 Video Interpolation, Restoration & Editing

> **Scope** · Interpolation, super-resolution, denoising, inpainting, cross-frame feature alignment, video inverse problems, and flow-guided video editing with temporal consistency
>
> **21 papers · Newest first**

---

<a id="s028"></a>
#### HomoGen: Enhanced Video Inpainting via Homography Propagation and Diffusion (CVPR 2025)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content/CVPR2025/html/Ding_HomoGen_Enhanced_Video_Inpainting_via_Homography_Propagation_and_Diffusion_CVPR_2025_paper.html) &nbsp; [`T1`](#t1) [`T9`](#t9)

Propagates context through homography registration and injects the resulting priors into video diffusion inpainting.

---

<a id="s029"></a>
#### BiM-VFI: Bidirectional Motion Field-Guided Frame Interpolation for Video with Non-uniform Motions (CVPR 2025)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content/CVPR2025/html/Seo_BiM-VFI_Bidirectional_Motion_Field-Guided_Frame_Interpolation_for_Video_with_Non-uniform_CVPR_2025_paper.html) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://kaist-viclab.github.io/BiM-VFI_site/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/KAIST-VICLab/BiM-VFI) [![GitHub stars](https://img.shields.io/github/stars/KAIST-VICLab/BiM-VFI?style=flat-square&label=stars&color=C58A18)](https://github.com/KAIST-VICLab/BiM-VFI/stargazers) [![GitHub forks](https://img.shields.io/github/forks/KAIST-VICLab/BiM-VFI?style=flat-square&label=forks&color=64748B)](https://github.com/KAIST-VICLab/BiM-VFI/forks) &nbsp; [`T4`](#t4)

Models nonuniform motion with bidirectional fields and combines flow estimation, adaptive upsampling and distillation for interpolation.

---

<a id="s027"></a>
#### Coherent Video Inpainting Using Optical Flow-Guided Efficient Diffusion (arXiv 2024)

[![arXiv: 2412.00857](https://img.shields.io/badge/arXiv-2412.00857-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2412.00857) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2412.00857) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://nevsnev.github.io/FloED/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/NevSNev/FloED-main) [![GitHub stars](https://img.shields.io/github/stars/NevSNev/FloED-main?style=flat-square&label=stars&color=C58A18)](https://github.com/NevSNev/FloED-main/stargazers) [![GitHub forks](https://img.shields.io/github/forks/NevSNev/FloED-main?style=flat-square&label=forks&color=64748B)](https://github.com/NevSNev/FloED-main/forks) &nbsp; [`T4`](#t4) [`T9`](#t9)

Guides video inpainting with completed flow and multiscale adapters, using flow-warped latent interpolation to accelerate denoising.

---

<a id="s030"></a>
#### Upscale-A-Video: Temporal-Consistent Diffusion Model for Real-World Video Super-Resolution (CVPR 2024)

[![arXiv: 2312.06640](https://img.shields.io/badge/arXiv-2312.06640-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2312.06640) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2312.06640) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://shangchenzhou.com/projects/upscale-a-video/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sczhou/Upscale-A-Video) [![GitHub stars](https://img.shields.io/github/stars/sczhou/Upscale-A-Video?style=flat-square&label=stars&color=C58A18)](https://github.com/sczhou/Upscale-A-Video/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sczhou/Upscale-A-Video?style=flat-square&label=forks&color=64748B)](https://github.com/sczhou/Upscale-A-Video/forks) &nbsp; [`T4`](#t4) [`T9`](#t9)

Combines temporal layers with global flow-guided recurrent latent propagation for diffusion-based video super-resolution.

---

<a id="s038"></a>
#### FlowVid: Taming Imperfect Optical Flows for Consistent Video-to-Video Synthesis (CVPR 2024)

[![arXiv: 2312.17681](https://img.shields.io/badge/arXiv-2312.17681-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2312.17681) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2312.17681) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://jeff-liangf.github.io/projects/flowvid/) &nbsp; [`T4`](#t4) [`T9`](#t9)

Warps an edited first frame into later frames and combines these references with spatial conditions for video editing.

---

<a id="s042"></a>
#### WAVE: Warping DDIM Inversion Features for Zero-shot Text-to-Video Editing (ECCV 2024)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9682_ECCV_2024_paper.php) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://ree1s.github.io/wave/) &nbsp; [`T4`](#t4) [`T9`](#t9)

Propagates key-frame features with flow during DDIM inversion to improve latent consistency for video editing.

---

<a id="s024"></a>
#### ProPainter: Improving Propagation and Transformer for Video Inpainting (ICCV 2023)

[![arXiv: 2309.03897](https://img.shields.io/badge/arXiv-2309.03897-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2309.03897) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2309.03897) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://shangchenzhou.com/projects/ProPainter/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sczhou/ProPainter) [![GitHub stars](https://img.shields.io/github/stars/sczhou/ProPainter?style=flat-square&label=stars&color=C58A18)](https://github.com/sczhou/ProPainter/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sczhou/ProPainter?style=flat-square&label=forks&color=64748B)](https://github.com/sczhou/ProPainter/forks) &nbsp; [`T4`](#t4) [`T8`](#t8)

Combines recurrent flow completion, image-and-feature propagation and a sparse video transformer for inpainting.

---

<a id="s040"></a>
#### LatentWarp: Consistent Diffusion Latents for Zero-Shot Video-to-Video Translation (arXiv 2023)

[![arXiv: 2311.00353](https://img.shields.io/badge/arXiv-2311.00353-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2311.00353) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2311.00353) &nbsp; [`T4`](#t4) [`T9`](#t9)

Warps diffusion latents with optical flow to constrain query tokens for consistent zero-shot video translation.

---

<a id="s041"></a>
#### Rerender A Video: Zero-Shot Text-Guided Video-to-Video Translation (SIGGRAPH Asia / TOG 2023)

[![arXiv: 2306.07954](https://img.shields.io/badge/arXiv-2306.07954-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2306.07954) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2306.07954) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://www.mmlab-ntu.com/project/rerender/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/williamyang1991/Rerender_A_Video) [![GitHub stars](https://img.shields.io/github/stars/williamyang1991/Rerender_A_Video?style=flat-square&label=stars&color=C58A18)](https://github.com/williamyang1991/Rerender_A_Video/stargazers) [![GitHub forks](https://img.shields.io/github/forks/williamyang1991/Rerender_A_Video?style=flat-square&label=forks&color=64748B)](https://github.com/williamyang1991/Rerender_A_Video/forks) &nbsp; [`T4`](#t4) [`T9`](#t9)

Constrains key-frame shape and texture with cross-frame alignment, then propagates edits through temporal matching and blending.

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

<a id="s025"></a>
#### Towards An End-to-End Framework for Flow-Guided Video Inpainting (CVPR 2022)

[![arXiv: 2204.02663](https://img.shields.io/badge/arXiv-2204.02663-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2204.02663) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2204.02663) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MCG-NKU/E2FGVI) [![GitHub stars](https://img.shields.io/github/stars/MCG-NKU/E2FGVI?style=flat-square&label=stars&color=C58A18)](https://github.com/MCG-NKU/E2FGVI/stargazers) [![GitHub forks](https://img.shields.io/github/forks/MCG-NKU/E2FGVI?style=flat-square&label=forks&color=64748B)](https://github.com/MCG-NKU/E2FGVI/forks) &nbsp; [`T4`](#t4) [`T8`](#t8)

Jointly trains flow completion, aligned feature propagation and content hallucination for end-to-end video inpainting.

---

<a id="p25"></a>
#### BasicVSR: The Search for Essential Components in Video Super-Resolution and Beyond (CVPR 2021)

[![arXiv: 2012.02181](https://img.shields.io/badge/arXiv-2012.02181-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2012.02181) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ckkelvinchan/BasicVSR-IconVSR) [![GitHub stars](https://img.shields.io/github/stars/ckkelvinchan/BasicVSR-IconVSR?style=flat-square&label=stars&color=C58A18)](https://github.com/ckkelvinchan/BasicVSR-IconVSR/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ckkelvinchan/BasicVSR-IconVSR?style=flat-square&label=forks&color=64748B)](https://github.com/ckkelvinchan/BasicVSR-IconVSR/forks) &nbsp; [`T4`](#t4)

Builds a video super-resolution baseline around bidirectional propagation, flow-based alignment, aggregation and upsampling.

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

<a id="s026"></a>
#### Deep Flow-Guided Video Inpainting (CVPR 2019)

[![arXiv: 1905.02884](https://img.shields.io/badge/arXiv-1905.02884-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1905.02884) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/1905.02884) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://nbei.github.io/video-inpainting.html) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nbei/Deep-Flow-Guided-Video-Inpainting) [![GitHub stars](https://img.shields.io/github/stars/nbei/Deep-Flow-Guided-Video-Inpainting?style=flat-square&label=stars&color=C58A18)](https://github.com/nbei/Deep-Flow-Guided-Video-Inpainting/stargazers) [![GitHub forks](https://img.shields.io/github/forks/nbei/Deep-Flow-Guided-Video-Inpainting?style=flat-square&label=forks&color=64748B)](https://github.com/nbei/Deep-Flow-Guided-Video-Inpainting/forks) &nbsp; [`T4`](#t4)

Completes spatiotemporal flow fields and propagates visible pixels along them to repair masked video regions.

---

<a id="p21"></a>
#### Super SloMo: High Quality Estimation of Multiple Intermediate Frames for Video Interpolation (CVPR 2018)

[![arXiv: 1712.00080](https://img.shields.io/badge/arXiv-1712.00080-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1712.00080) &nbsp; [`T4`](#t4)

Synthesizes intermediate frames using bidirectional flow, intermediate-flow refinement and soft visibility maps.

---

<a id="a16"></a>
#### Learning Blind Video Temporal Consistency (ECCV 2018)

[![arXiv: 1808.00449](https://img.shields.io/badge/arXiv-1808.00449-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1808.00449) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/phoenix104104/fast_blind_video_consistency) [![GitHub stars](https://img.shields.io/github/stars/phoenix104104/fast_blind_video_consistency?style=flat-square&label=stars&color=C58A18)](https://github.com/phoenix104104/fast_blind_video_consistency/stargazers) [![GitHub forks](https://img.shields.io/github/forks/phoenix104104/fast_blind_video_consistency?style=flat-square&label=forks&color=64748B)](https://github.com/phoenix104104/fast_blind_video_consistency/forks) &nbsp; [`T4`](#t4) [`T7`](#t7)

Builds short- and long-term temporal losses from flow-warped frames to learn task-agnostic video stabilization of per-frame outputs, and evaluates flicker with warping error.

---

<a id="a15"></a>
#### Video Frame Synthesis using Deep Voxel Flow (ICCV 2017)

[![arXiv: 1702.02463](https://img.shields.io/badge/arXiv-1702.02463-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1702.02463) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://liuziwei7.github.io/projects/VoxelFlow) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/liuziwei7/voxel-flow) [![GitHub stars](https://img.shields.io/github/stars/liuziwei7/voxel-flow?style=flat-square&label=stars&color=C58A18)](https://github.com/liuziwei7/voxel-flow/stargazers) [![GitHub forks](https://img.shields.io/github/forks/liuziwei7/voxel-flow?style=flat-square&label=forks&color=64748B)](https://github.com/liuziwei7/voxel-flow/forks) &nbsp; [`T4`](#t4) [`T7`](#t7)

Predicts spatiotemporal voxel flow and trilinearly samples neighboring frames for interpolation and extrapolation without flow labels.

---

<details>
<summary>Related reading · 12 papers in other topics</summary>

- [Warped Diffusion](#n17) (2024)
- [CoDeF](#a22) (2024)
- [Global Motion Aggregation (GMA)](#p11) (2021)
- [RAFT](#c20) (2020)
- [Softmax Splatting](#c19) (2020)
- [PWC-Net](#c15) (2018)
- [LiteFlowNet](#p10) (2018)
- [SDC-Net](#a41) (2018)
- [Deformable ConvNets (DCN)](#c14) (2017)
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
> **18 papers · Newest first**

---

<a id="s032"></a>
#### Learning Implicit Features with Flow-Infused Transformations for Realistic Virtual Try-On (ICCV 2025)

[![arXiv: 2412.11435](https://img.shields.io/badge/arXiv-2412.11435-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2412.11435) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2412.11435) &nbsp; [`T4`](#t4) [`T9`](#t9)

Injects dense warp flow and garment features into attention for implicit alignment guidance in diffusion try-on.

---

<a id="s033"></a>
#### FloAt: Flow Warping of Self-Attention for Clothing Animation Generation (arXiv 2024)

[![arXiv: 2411.15028](https://img.shields.io/badge/arXiv-2411.15028-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2411.15028) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2411.15028) &nbsp; [`T4`](#t4) [`T9`](#t9)

Warps previous-frame self-attention features using flow from normal maps and blends them into clothing-animation generation.

---

<a id="s036"></a>
#### D4-VTON: Dynamic Semantics Disentangling for Differential Diffusion based Virtual Try-On (ECCV 2024)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6231_ECCV_2024_paper.php) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Jerome-Young/D4-VTON) [![GitHub stars](https://img.shields.io/github/stars/Jerome-Young/D4-VTON?style=flat-square&label=stars&color=C58A18)](https://github.com/Jerome-Young/D4-VTON/stargazers) [![GitHub forks](https://img.shields.io/github/forks/Jerome-Young/D4-VTON?style=flat-square&label=forks&color=64748B)](https://github.com/Jerome-Young/D4-VTON/forks) &nbsp; [`T4`](#t4) [`T9`](#t9)

Discovers garment semantics for local-flow warping and uses differential information tracking in diffusion try-on.

---

<a id="a19"></a>
#### LivePortrait: Efficient Portrait Animation with Stitching and Retargeting Control (arXiv 2024)

[![arXiv: 2407.03168](https://img.shields.io/badge/arXiv-2407.03168-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2407.03168) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://liveportrait.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/KlingAIResearch/LivePortrait) [![GitHub stars](https://img.shields.io/github/stars/KlingAIResearch/LivePortrait?style=flat-square&label=stars&color=C58A18)](https://github.com/KlingAIResearch/LivePortrait/stargazers) [![GitHub forks](https://img.shields.io/github/forks/KlingAIResearch/LivePortrait?style=flat-square&label=forks&color=64748B)](https://github.com/KlingAIResearch/LivePortrait/forks) &nbsp; [`T8`](#t8)

Follows the implicit-keypoint framework, turning keypoint transforms into dense warping fields that drive source features, and adds stitching and retargeting modules for efficient portrait animation.

---

<a id="s031"></a>
#### Taming the Power of Diffusion Models for High-Quality Virtual Try-On with Appearance Flow (ACM MM 2023)

[![arXiv: 2308.06101](https://img.shields.io/badge/arXiv-2308.06101-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2308.06101) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2308.06101) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/bcmi/DCI-VTON-Virtual-Try-On) [![GitHub stars](https://img.shields.io/github/stars/bcmi/DCI-VTON-Virtual-Try-On?style=flat-square&label=stars&color=C58A18)](https://github.com/bcmi/DCI-VTON-Virtual-Try-On/stargazers) [![GitHub forks](https://img.shields.io/github/forks/bcmi/DCI-VTON-Virtual-Try-On?style=flat-square&label=forks&color=64748B)](https://github.com/bcmi/DCI-VTON-Virtual-Try-On/forks) &nbsp; [`T4`](#t4) [`T9`](#t9)

Explicitly warps garments with appearance flow and uses the aligned clothing to condition diffusion-based virtual try-on.

---

<a id="s035"></a>
#### GP-VTON: Towards General Purpose Virtual Try-on via Collaborative Local-Flow Global-Parsing Learning (CVPR 2023)

[![arXiv: 2303.13756](https://img.shields.io/badge/arXiv-2303.13756-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2303.13756) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2303.13756) &nbsp; [`T4`](#t4) [`T9`](#t9)

Combines local garment flows and global parsing with dynamic gradient truncation to reduce boundary-related texture distortion.

---

<a id="n03"></a>
#### Thin-Plate Spline Motion Model for Image Animation (CVPR 2022)

[![arXiv: 2203.14367](https://img.shields.io/badge/arXiv-2203.14367-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2203.14367) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2203.14367) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/yoyo-nb/Thin-Plate-Spline-Motion-Model) [![GitHub stars](https://img.shields.io/github/stars/yoyo-nb/Thin-Plate-Spline-Motion-Model?style=flat-square&label=stars&color=C58A18)](https://github.com/yoyo-nb/Thin-Plate-Spline-Motion-Model/stargazers) [![GitHub forks](https://img.shields.io/github/forks/yoyo-nb/Thin-Plate-Spline-Motion-Model?style=flat-square&label=forks&color=64748B)](https://github.com/yoyo-nb/Thin-Plate-Spline-Motion-Model/forks) &nbsp; [`T2`](#t2) [`T8`](#t8)

Extends local affine motion representations to multiple TPS transformations, using multiscale occlusion masks for feature warping in image animation.

---

<a id="s034"></a>
#### High-Resolution Virtual Try-On with Misalignment and Occlusion-Handled Conditions (ECCV 2022)

[![arXiv: 2206.14180](https://img.shields.io/badge/arXiv-2206.14180-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2206.14180) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2206.14180) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sangyun884/hr-viton) [![GitHub stars](https://img.shields.io/github/stars/sangyun884/hr-viton?style=flat-square&label=stars&color=C58A18)](https://github.com/sangyun884/hr-viton/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sangyun884/hr-viton?style=flat-square&label=forks&color=64748B)](https://github.com/sangyun884/hr-viton/forks) &nbsp; [`T4`](#t4) [`T9`](#t9)

Jointly exchanges information between garment warping and segmentation to reduce misalignment and occlusion-related texture squeezing.

---

<a id="s078"></a>
#### ClothFormer: Taming Video Virtual Try-On in All Module (CVPR 2022)

[![arXiv: 2204.12151](https://img.shields.io/badge/arXiv-2204.12151-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2204.12151) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://cloth-former.github.io) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/luxiangju-PersonAI/ClothFormer) [![GitHub stars](https://img.shields.io/github/stars/luxiangju-PersonAI/ClothFormer?style=flat-square&label=stars&color=C58A18)](https://github.com/luxiangju-PersonAI/ClothFormer/stargazers) [![GitHub forks](https://img.shields.io/github/forks/luxiangju-PersonAI/ClothFormer?style=flat-square&label=forks&color=64748B)](https://github.com/luxiangju-PersonAI/ClothFormer/forks) &nbsp; [`T4`](#t4) [`T9`](#t9)

Combines occlusion-aware garment warping, appearance-flow smoothing and a dual-stream transformer for consistent video try-on.

---

<a id="p29"></a>
#### Parser-Free Virtual Try-on via Distilling Appearance Flows (CVPR 2021)

[![arXiv: 2103.04559](https://img.shields.io/badge/arXiv-2103.04559-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2103.04559) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/geyuying/PF-AFN) [![GitHub stars](https://img.shields.io/github/stars/geyuying/PF-AFN?style=flat-square&label=stars&color=C58A18)](https://github.com/geyuying/PF-AFN/stargazers) [![GitHub forks](https://img.shields.io/github/forks/geyuying/PF-AFN?style=flat-square&label=forks&color=64748B)](https://github.com/geyuying/PF-AFN/forks) &nbsp; [`T4`](#t4) [`T9`](#t9)

Distills garment-to-person appearance flows to enable parser-free virtual try-on at inference time.

---

<a id="s037"></a>
#### One-Shot Free-View Neural Talking-Head Synthesis for Video Conferencing (CVPR 2021)

[![arXiv: 2011.15126](https://img.shields.io/badge/arXiv-2011.15126-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2011.15126) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2011.15126) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://nvlabs.github.io/face-vid2vid/) &nbsp; [`T8`](#t8)

Disentangles identity and motion keypoints to drive dense deformation and source-feature warping for talking-head synthesis.

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

<a id="a17"></a>
#### Liquid Warping GAN: A Unified Framework for Human Motion Imitation, Appearance Transfer and Novel View Synthesis (ICCV 2019)

[![arXiv: 1909.12224](https://img.shields.io/badge/arXiv-1909.12224-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1909.12224) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://svip-lab.github.io/project/impersonator) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/svip-lab/impersonator) [![GitHub stars](https://img.shields.io/github/stars/svip-lab/impersonator?style=flat-square&label=stars&color=C58A18)](https://github.com/svip-lab/impersonator/stargazers) [![GitHub forks](https://img.shields.io/github/forks/svip-lab/impersonator?style=flat-square&label=forks&color=64748B)](https://github.com/svip-lab/impersonator/forks) &nbsp; [`T6`](#t6) [`T8`](#t8)

Computes transformation flow from 3D body meshes between source and target and warps features with a liquid warping block to keep texture, identity and clothing detail.

---

<a id="a18"></a>
#### ClothFlow: A Flow-Based Model for Clothed Person Generation (ICCV 2019)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content_ICCV_2019/html/Han_ClothFlow_A_Flow-Based_Model_for_Clothed_Person_Generation_ICCV_2019_paper.html) &nbsp; [`T4`](#t4) [`T9`](#t9)

Estimates dense appearance flow in a cascade to warp garments from source to target pose for pose-guided person generation and virtual try-on.

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
<summary>Related reading · 8 papers in other topics</summary>

- [Go-with-the-Flow](#n19) (2025)
- [HumanNeRF](#a37) (2022)
- [SNARF](#a36) (2021)
- [Appearance Flow](#a34) (2016)
- [Bounded Biharmonic Weights (BBW)](#p03) (2011)
- [Green Coordinates](#s002) (2008)
- [Harmonic Coordinates](#s001) (2007)
- [Mean Value Coordinates (MVC)](#a01) (2005)

</details>

[↑ Start of 3.2](#topic-human-deformation) · [↑ Back to topic navigation](#topics)

---

<a id="area-video-generation"></a>
## 4. Video Generation & Motion Control


<a id="topic-noise-warping"></a>
### 4.1 Noise Warping & Temporal Consistency

> **Scope** · Random-field transport, noise statistics, motion-correlated noise, latent warping and noise-level temporal consistency
>
> **7 papers · Newest first**

---

<a id="a20"></a>
#### Track the Noise, Move the World: 3D-Grounded Motion-Consistent Noise for Controllable Video Generation (arXiv 2026)

[![arXiv: 2607.02798](https://img.shields.io/badge/arXiv-2607.02798-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2607.02798) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://phongnhhn.info/Unicamo/) &nbsp; [`T6`](#t6) [`T9`](#t9)

Warps reference-frame Gaussian noise along sparse 3D point tracks and uses a virtual spherical noise field for regions revealed by camera motion, jointly controlling object and camera motion.

---

<a id="s043"></a>
#### Infinite-Resolution Integral Noise Warping for Diffusion Models (ICLR 2025)

[![arXiv: 2411.01212](https://img.shields.io/badge/arXiv-2411.01212-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2411.01212) &nbsp; [`T9`](#t9)

Uses Brownian-bridge increments to compute the infinite-resolution limit of integral noise warping efficiently.

---

<a id="s044"></a>
#### On Equivariance and Fast Sampling in Video Diffusion Models Trained with Warped Noise (arXiv 2025)

[![arXiv: 2504.09789](https://img.shields.io/badge/arXiv-2504.09789-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.09789) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2504.09789) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://research.nvidia.com/labs/genair/equivdm/) &nbsp; [`T9`](#t9)

Studies how warped-noise training encourages spatial equivariance and applies it to efficient video generation and distillation.

---

<a id="n16"></a>
#### How I Warped Your Noise: a Temporally-Correlated Noise Prior for Diffusion Models (ICLR 2024)

[![arXiv: 2504.03072](https://img.shields.io/badge/arXiv-2504.03072-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.03072) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://warpyournoise.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/mskwak01/How-I-Warped-Your-Noise-Unofficial) [![GitHub stars](https://img.shields.io/github/stars/mskwak01/How-I-Warped-Your-Noise-Unofficial?style=flat-square&label=stars&color=C58A18)](https://github.com/mskwak01/How-I-Warped-Your-Noise-Unofficial/stargazers) [![GitHub forks](https://img.shields.io/github/forks/mskwak01/How-I-Warped-Your-Noise-Unofficial?style=flat-square&label=forks&color=64748B)](https://github.com/mskwak01/How-I-Warped-Your-Noise-Unofficial/forks) &nbsp; [`T7`](#t7) [`T9`](#t9)

Interprets pixel noise as integrals over a continuous white-noise field and designs transport for Gaussian statistics while retaining motion-induced temporal correlation.

---

<a id="n17"></a>
#### Warped Diffusion: Solving Video Inverse Problems with Image Diffusion Models (NeurIPS 2024)

[![arXiv: 2410.16152](https://img.shields.io/badge/arXiv-2410.16152-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2410.16152) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2410.16152) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://giannisdaras.github.io/warped_diffusion.github.io/) &nbsp; [`T9`](#t9)

Uses continuous function spaces and transformation equivariance for video inverse problems, improving temporal consistency with test-time self-equivariance guidance.

---

<a id="a22"></a>
#### CoDeF: Content Deformation Fields for Temporally Consistent Video Processing (CVPR 2024)

[![arXiv: 2308.07926](https://img.shields.io/badge/arXiv-2308.07926-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2308.07926) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://qiuyu96.github.io/CoDeF/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/qiuyu96/CoDeF) [![GitHub stars](https://img.shields.io/github/stars/qiuyu96/CoDeF?style=flat-square&label=stars&color=C58A18)](https://github.com/qiuyu96/CoDeF/stargazers) [![GitHub forks](https://img.shields.io/github/forks/qiuyu96/CoDeF?style=flat-square&label=forks&color=64748B)](https://github.com/qiuyu96/CoDeF/forks) &nbsp; [`T8`](#t8)

Represents video as a canonical content field plus per-frame temporal deformation fields, so edits on the canonical image propagate through the deformation to every frame.

---

<a id="a21"></a>
#### Text2Video-Zero: Text-to-Image Diffusion Models are Zero-Shot Video Generators (ICCV 2023)

[![arXiv: 2303.13439](https://img.shields.io/badge/arXiv-2303.13439-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2303.13439) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Picsart-AI-Research/Text2Video-Zero) [![GitHub stars](https://img.shields.io/github/stars/Picsart-AI-Research/Text2Video-Zero?style=flat-square&label=stars&color=C58A18)](https://github.com/Picsart-AI-Research/Text2Video-Zero/stargazers) [![GitHub forks](https://img.shields.io/github/forks/Picsart-AI-Research/Text2Video-Zero?style=flat-square&label=forks&color=64748B)](https://github.com/Picsart-AI-Research/Text2Video-Zero/forks) &nbsp; [`T1`](#t1) [`T9`](#t9)

Warps the first-frame latent by global translation to initialize later frames and combines this with cross-frame attention for training-free text-to-video generation.

---

<details>
<summary>Related reading · 15 papers in other topics</summary>

- [CameraNoise](#n24) (2026)
- [Go-with-the-Flow](#n19) (2025)
- [FIA-VTON](#s032) (2025)
- [CamTrol](#a24) (2025)
- [FloED](#s027) (2024)
- [Upscale-A-Video](#s030) (2024)
- [FloAt](#s033) (2024)
- [FlowVid](#s038) (2024)
- [WAVE (DDIM inversion)](#s042) (2024)
- [MotionCraft](#s046) (2024)
- [ProPainter](#s024) (2023)
- [LatentWarp](#s040) (2023)
- [Rerender A Video](#s041) (2023)
- [ClothFormer](#s078) (2022)
- [Blind Video Temporal Consistency](#a16) (2018)

</details>

[↑ Start of 4.1](#topic-noise-warping) · [↑ Back to topic navigation](#topics)

---

<a id="topic-14"></a>
<a id="topic-controlled-generation"></a>
### 4.2 Camera-, Trajectory- & Motion-Controlled Generation

> **Scope** · Camera and object-motion control, geometric guidance and history-frame alignment
>
> **11 papers · Newest first**

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

<a id="s047"></a>
#### FloVD: Optical Flow Meets Video Diffusion Model for Enhanced Camera-Controlled Video Synthesis (CVPR 2025)

[![arXiv: 2502.08244](https://img.shields.io/badge/arXiv-2502.08244-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.08244) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2502.08244) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://jinwonjoon.github.io/flovd_site/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/JinWonjoon/FloVD) [![GitHub stars](https://img.shields.io/github/stars/JinWonjoon/FloVD?style=flat-square&label=stars&color=C58A18)](https://github.com/JinWonjoon/FloVD/stargazers) [![GitHub forks](https://img.shields.io/github/forks/JinWonjoon/FloVD?style=flat-square&label=forks&color=64748B)](https://github.com/JinWonjoon/FloVD/forks) &nbsp; [`T4`](#t4) [`T9`](#t9)

Represents camera and object motion with flow, using flow generation followed by flow-conditioned video synthesis.

---

<a id="s048"></a>
#### TrajectoryCrafter: Redirecting Camera Trajectory for Monocular Videos via Diffusion Models (ICCV 2025)

[![arXiv: 2503.05638](https://img.shields.io/badge/arXiv-2503.05638-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2503.05638) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2503.05638) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://TrajectoryCrafter.github.io) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/TrajectoryCrafter/TrajectoryCrafter) [![GitHub stars](https://img.shields.io/github/stars/TrajectoryCrafter/TrajectoryCrafter?style=flat-square&label=stars&color=C58A18)](https://github.com/TrajectoryCrafter/TrajectoryCrafter/stargazers) [![GitHub forks](https://img.shields.io/github/forks/TrajectoryCrafter/TrajectoryCrafter?style=flat-square&label=forks&color=64748B)](https://github.com/TrajectoryCrafter/TrajectoryCrafter/forks) &nbsp; [`T6`](#t6) [`T9`](#t9)

Conditions diffusion on source video and target-trajectory point-cloud renders, using double reprojection for training data.

---

<a id="s049"></a>
#### Latent-Reframe: Enabling Camera Control for Video Diffusion Models without Training (ICCV 2025)

[![arXiv: 2412.06029](https://img.shields.io/badge/arXiv-2412.06029-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2412.06029) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2412.06029) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://latent-reframe.github.io) &nbsp; [`T6`](#t6) [`T9`](#t9)

Reframes video latents through time-aware point clouds and refines them with latent inpainting and harmonization.

---

<a id="a23"></a>
#### GEN3C: 3D-Informed World-Consistent Video Generation with Precise Camera Control (CVPR 2025)

[![arXiv: 2503.03751](https://img.shields.io/badge/arXiv-2503.03751-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2503.03751) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://research.nvidia.com/labs/toronto-ai/GEN3C/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nv-tlabs/GEN3C) [![GitHub stars](https://img.shields.io/github/stars/nv-tlabs/GEN3C?style=flat-square&label=stars&color=C58A18)](https://github.com/nv-tlabs/GEN3C/stargazers) [![GitHub forks](https://img.shields.io/github/forks/nv-tlabs/GEN3C?style=flat-square&label=forks&color=64748B)](https://github.com/nv-tlabs/GEN3C/forks) &nbsp; [`T6`](#t6) [`T9`](#t9)

Builds a point-cloud 3D cache from per-pixel depth, reprojects it along the user camera trajectory and conditions video diffusion on the renderings so generation focuses on unobserved regions.

---

<a id="a24"></a>
#### Training-free Camera Control for Video Generation (ICLR 2025)

[![arXiv: 2406.10126](https://img.shields.io/badge/arXiv-2406.10126-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2406.10126) &nbsp; [`T6`](#t6) [`T9`](#t9)

Rearranges image layout through explicit camera motion in 3D point-cloud space and reorganizes noisy latents accordingly as a layout prior for training-free camera control.

---

<a id="s045"></a>
#### Motion-I2V: Consistent and Controllable Image-to-Video Generation with Explicit Motion Modeling (SIGGRAPH 2024)

[![arXiv: 2401.15977](https://img.shields.io/badge/arXiv-2401.15977-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2401.15977) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2401.15977) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://xiaoyushi97.github.io/Motion-I2V/) &nbsp; [`T4`](#t4) [`T9`](#t9)

Predicts pixel trajectories and uses motion-augmented temporal attention to propagate features under sparse trajectory control.

---

<a id="s046"></a>
#### MotionCraft: Physics-Based Zero-Shot Video Generation (NeurIPS 2024)

[![arXiv: 2405.13557](https://img.shields.io/badge/arXiv-2405.13557-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2405.13557) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2405.13557) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://mezzelfo.github.io/MotionCraft/) &nbsp; [`T4`](#t4) [`T9`](#t9)

Warps diffusion noise latents with optical flow from a physics simulation for zero-shot motion control.

---

<a id="a25"></a>
#### ViewCrafter: Taming Video Diffusion Models for High-fidelity Novel View Synthesis (arXiv 2024)

[![arXiv: 2409.02048](https://img.shields.io/badge/arXiv-2409.02048-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2409.02048) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://drexubery.github.io/ViewCrafter/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Drexubery/ViewCrafter) [![GitHub stars](https://img.shields.io/github/stars/Drexubery/ViewCrafter?style=flat-square&label=stars&color=C58A18)](https://github.com/Drexubery/ViewCrafter/stargazers) [![GitHub forks](https://img.shields.io/github/forks/Drexubery/ViewCrafter?style=flat-square&label=forks&color=64748B)](https://github.com/Drexubery/ViewCrafter/forks) &nbsp; [`T6`](#t6) [`T9`](#t9)

Reprojects point clouds from sparse views to target cameras, conditions video diffusion on the renderings to complete missing regions, and iteratively extends the point cloud for wider novel views.

---

<details>
<summary>Related reading · 12 papers in other topics</summary>

- [UniCaMo / Track the Noise](#a20) (2026)
- [Inpaint4Drag](#s003) (2025)
- [FlowDrag](#s004) (2025)
- [EquiVDM / Warped-Noise Equivariance](#s044) (2025)
- [NVS-Solver](#a35) (2025)
- [How I Warped Your Noise / ∫-noise](#n16) (2024)
- [FloAt](#s033) (2024)
- [FlowVid](#s038) (2024)
- [FastDrag](#a04) (2024)
- [face-vid2vid](#s037) (2021)
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
> **12 papers · Newest first**

---

<a id="s059"></a>
#### DepthSplat: Connecting Gaussian Splatting and Depth (CVPR 2025)

[![arXiv: 2410.13862](https://img.shields.io/badge/arXiv-2410.13862-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2410.13862) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2410.13862) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://haofeixu.github.io/depthsplat/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/cvg/depthsplat) [![GitHub stars](https://img.shields.io/github/stars/cvg/depthsplat?style=flat-square&label=stars&color=C58A18)](https://github.com/cvg/depthsplat/stargazers) [![GitHub forks](https://img.shields.io/github/forks/cvg/depthsplat?style=flat-square&label=forks&color=64748B)](https://github.com/cvg/depthsplat/forks) &nbsp; [`T6`](#t6) [`T7`](#t7)

Connects multiview depth estimation and Gaussian reconstruction, using rendering supervision to improve depth representations.

---

<a id="p40"></a>
#### DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras (NeurIPS 2021)

[![arXiv: 2108.10869](https://img.shields.io/badge/arXiv-2108.10869-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2108.10869) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2108.10869) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/princeton-vl/DROID-SLAM) [![GitHub stars](https://img.shields.io/github/stars/princeton-vl/DROID-SLAM?style=flat-square&label=stars&color=C58A18)](https://github.com/princeton-vl/DROID-SLAM/stargazers) [![GitHub forks](https://img.shields.io/github/forks/princeton-vl/DROID-SLAM?style=flat-square&label=forks&color=64748B)](https://github.com/princeton-vl/DROID-SLAM/forks) &nbsp; [`T4`](#t4) [`T6`](#t6)

Jointly updates camera poses and pixelwise depth through recurrent dense bundle adjustment.

---

<a id="s051"></a>
#### Cascade Cost Volume for High-Resolution Multi-View Stereo and Stereo Matching (CVPR 2020)

[![arXiv: 1912.06378](https://img.shields.io/badge/arXiv-1912.06378-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1912.06378) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/alibaba/cascade-stereo) [![GitHub stars](https://img.shields.io/github/stars/alibaba/cascade-stereo?style=flat-square&label=stars&color=C58A18)](https://github.com/alibaba/cascade-stereo/stargazers) [![GitHub forks](https://img.shields.io/github/forks/alibaba/cascade-stereo?style=flat-square&label=forks&color=64748B)](https://github.com/alibaba/cascade-stereo/forks) &nbsp; [`T6`](#t6)

Narrows depth hypotheses across cascaded feature cost volumes for high-resolution stereo and multiview depth estimation.

---

<a id="c16"></a>
#### Digging Into Self-Supervised Monocular Depth Estimation (ICCV 2019)

[![arXiv: 1806.01260](https://img.shields.io/badge/arXiv-1806.01260-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1806.01260) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nianticlabs/monodepth2) [![GitHub stars](https://img.shields.io/github/stars/nianticlabs/monodepth2?style=flat-square&label=stars&color=C58A18)](https://github.com/nianticlabs/monodepth2/stargazers) [![GitHub forks](https://img.shields.io/github/forks/nianticlabs/monodepth2?style=flat-square&label=forks&color=64748B)](https://github.com/nianticlabs/monodepth2/forks) &nbsp; [`T6`](#t6)

Uses depth, pose and differentiable reprojection for self-supervised view reconstruction, introducing minimum reprojection loss and automasking.

---

<a id="s052"></a>
#### DPSNet: End-to-end Deep Plane Sweep Stereo (ICLR 2019)

[![arXiv: 1905.00538](https://img.shields.io/badge/arXiv-1905.00538-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1905.00538) &nbsp; [`T6`](#t6) [`T7`](#t7)

Builds feature cost volumes with differentiable plane-sweep warping, then aggregates them to regress scene depth.

---

<a id="p39"></a>
#### MVSNet: Depth Inference for Unstructured Multi-view Stereo (ECCV 2018)

[![arXiv: 1804.02505](https://img.shields.io/badge/arXiv-1804.02505-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1804.02505) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/YoYo000/MVSNet) [![GitHub stars](https://img.shields.io/github/stars/YoYo000/MVSNet?style=flat-square&label=stars&color=C58A18)](https://github.com/YoYo000/MVSNet/stargazers) [![GitHub forks](https://img.shields.io/github/forks/YoYo000/MVSNet?style=flat-square&label=forks&color=64748B)](https://github.com/YoYo000/MVSNet/forks) &nbsp; [`T6`](#t6)

Builds multiview cost volumes with differentiable homography warping to infer reference-view depth.

---

<a id="a28"></a>
#### Direct Sparse Odometry (TPAMI 2018)

[![arXiv: 1607.02565](https://img.shields.io/badge/arXiv-1607.02565-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1607.02565) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://cvg.cit.tum.de/research/vslam/dso) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/JakobEngel/dso) [![GitHub stars](https://img.shields.io/github/stars/JakobEngel/dso?style=flat-square&label=stars&color=C58A18)](https://github.com/JakobEngel/dso/stargazers) [![GitHub forks](https://img.shields.io/github/forks/JakobEngel/dso?style=flat-square&label=forks&color=64748B)](https://github.com/JakobEngel/dso/forks) &nbsp; [`T6`](#t6)

Jointly optimizes depth, poses and photometric calibration of sparse points using photometric error after reprojection warping, forming direct visual odometry.

---

<a id="p43"></a>
#### Unsupervised Learning of Depth and Ego-Motion from Video (CVPR 2017)

[![arXiv: 1704.07813](https://img.shields.io/badge/arXiv-1704.07813-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1704.07813) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/1704.07813) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tinghuiz/SfMLearner) [![GitHub stars](https://img.shields.io/github/stars/tinghuiz/SfMLearner?style=flat-square&label=stars&color=C58A18)](https://github.com/tinghuiz/SfMLearner/stargazers) [![GitHub forks](https://img.shields.io/github/forks/tinghuiz/SfMLearner?style=flat-square&label=forks&color=64748B)](https://github.com/tinghuiz/SfMLearner/forks) &nbsp; [`T6`](#t6)

Couples monocular depth and camera motion through differentiable view reconstruction and photometric supervision.

---

<a id="a30"></a>
#### Unsupervised Monocular Depth Estimation with Left-Right Consistency (CVPR 2017)

[![arXiv: 1609.03677](https://img.shields.io/badge/arXiv-1609.03677-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1609.03677) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/mrharicot/monodepth) [![GitHub stars](https://img.shields.io/github/stars/mrharicot/monodepth?style=flat-square&label=stars&color=C58A18)](https://github.com/mrharicot/monodepth/stargazers) [![GitHub forks](https://img.shields.io/github/forks/mrharicot/monodepth?style=flat-square&label=forks&color=64748B)](https://github.com/mrharicot/monodepth/forks) &nbsp; [`T6`](#t6) [`T7`](#t7)

Warps left and right views into each other by differentiable bilinear sampling and adds a left-right disparity consistency loss for monocular depth training.

---

<a id="a29"></a>
#### Unsupervised CNN for Single View Depth Estimation: Geometry to the Rescue (ECCV 2016)

[![arXiv: 1603.04992](https://img.shields.io/badge/arXiv-1603.04992-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1603.04992) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Ravi-Garg/Unsupervised_Depth_Estimation) [![GitHub stars](https://img.shields.io/github/stars/Ravi-Garg/Unsupervised_Depth_Estimation?style=flat-square&label=stars&color=C58A18)](https://github.com/Ravi-Garg/Unsupervised_Depth_Estimation/stargazers) [![GitHub forks](https://img.shields.io/github/forks/Ravi-Garg/Unsupervised_Depth_Estimation?style=flat-square&label=forks&color=64748B)](https://github.com/Ravi-Garg/Unsupervised_Depth_Estimation/forks) &nbsp; [`T6`](#t6) [`T7`](#t7)

Warps the other stereo view with predicted disparity and trains a monocular depth network from reconstruction error, an early self-supervised depth method.

---

<a id="a27"></a>
#### LSD-SLAM: Large-Scale Direct Monocular SLAM (ECCV 2014)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1007/978-3-319-10605-2_54) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tum-vision/lsd_slam) [![GitHub stars](https://img.shields.io/github/stars/tum-vision/lsd_slam?style=flat-square&label=stars&color=C58A18)](https://github.com/tum-vision/lsd_slam/stargazers) [![GitHub forks](https://img.shields.io/github/forks/tum-vision/lsd_slam?style=flat-square&label=forks&color=64748B)](https://github.com/tum-vision/lsd_slam/forks) &nbsp; [`T6`](#t6) [`T1`](#t1)

Directly estimates Sim(3) poses by minimizing photometric error of depth-warped semi-dense high-gradient pixels for large-scale monocular SLAM.

---

<a id="a26"></a>
#### DTAM: Dense tracking and mapping in real-time (ICCV 2011)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1109/ICCV.2011.6126513) &nbsp; [`T6`](#t6)

Builds per-pixel photometric cost volumes over inverse depth by warping the reference frame into many frames, and tracks the camera by whole-image alignment for real-time dense monocular mapping.

---

<details>
<summary>Related reading · 11 papers in other topics</summary>

- [UFM](#s015) (2025)
- [Robust Dense Matching (RoMa)](#p71) (2024)
- [MVSplat](#s058) (2024)
- [UniMatch: Unifying Flow, Stereo and Depth Estimation](#n09) (2023)
- [Dense Kernelized Matching (DKM)](#p70) (2023)
- [PDC-Net+](#s012) (2023)
- [Trans4Map](#s082) (2023)
- [IBRNet](#p46) (2021)
- [pixelNeRF](#p47) (2021)
- [LoFTR](#p69) (2021)
- [COTR](#s011) (2021)

</details>

[↑ Start of 5.1](#topic-spatial-perception) · [↑ Back to topic navigation](#topics)

---

<a id="topic-12"></a>
<a id="topic-novel-view-synthesis"></a>
### 5.2 Reprojection & Novel View Synthesis

> **Scope** · DIBR, cross-view warping, visibility and disocclusion completion
>
> **16 papers · Newest first**

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

<a id="a35"></a>
#### NVS-Solver: Video Diffusion Model as Zero-Shot Novel View Synthesizer (ICLR 2025)

[![arXiv: 2405.15364](https://img.shields.io/badge/arXiv-2405.15364-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2405.15364) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ZHU-Zhiyu/NVS_Solver) [![GitHub stars](https://img.shields.io/github/stars/ZHU-Zhiyu/NVS_Solver?style=flat-square&label=stars&color=C58A18)](https://github.com/ZHU-Zhiyu/NVS_Solver/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ZHU-Zhiyu/NVS_Solver?style=flat-square&label=forks&color=64748B)](https://github.com/ZHU-Zhiyu/NVS_Solver/forks) &nbsp; [`T6`](#t6) [`T9`](#t9)

Uses input views warped to target poses as scene priors and adaptively modulates the video-diffusion score during sampling for training-free novel view synthesis.

---

<a id="n15"></a>
#### GenWarp: Single Image to Novel Views with Semantic-Preserving Generative Warping (NeurIPS 2024)

[![arXiv: 2405.17251](https://img.shields.io/badge/arXiv-2405.17251-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2405.17251) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2405.17251) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://genwarp-nvs.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sony/genwarp) [![GitHub stars](https://img.shields.io/github/stars/sony/genwarp?style=flat-square&label=stars&color=C58A18)](https://github.com/sony/genwarp/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sony/genwarp?style=flat-square&label=forks&color=64748B)](https://github.com/sony/genwarp/forks) &nbsp; [`T6`](#t6) [`T9`](#t9)

Combines depth-induced coordinate information with cross-view and self-attention, learning which content to transfer and which missing regions to generate.

---

<a id="s058"></a>
#### MVSplat: Efficient 3D Gaussian Splatting from Sparse Multi-View Images (ECCV 2024)

[![arXiv: 2403.14627](https://img.shields.io/badge/arXiv-2403.14627-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2403.14627) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2403.14627) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://donydchen.github.io/mvsplat/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/donydchen/mvsplat) [![GitHub stars](https://img.shields.io/github/stars/donydchen/mvsplat?style=flat-square&label=stars&color=C58A18)](https://github.com/donydchen/mvsplat/stargazers) [![GitHub forks](https://img.shields.io/github/forks/donydchen/mvsplat?style=flat-square&label=forks&color=64748B)](https://github.com/donydchen/mvsplat/forks) &nbsp; [`T6`](#t6) [`T7`](#t7)

Uses plane-sweep feature cost volumes to predict 3D Gaussians for feed-forward novel-view rendering from sparse views.

---

<a id="s060"></a>
#### MultiDiff: Consistent Novel View Synthesis from a Single Image (CVPR 2024)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content/CVPR2024/html/Muller_MultiDiff_Consistent_Novel_View_Synthesis_from_a_Single_Image_CVPR_2024_paper.html) &nbsp; [`T6`](#t6) [`T9`](#t9)

Warps a reference image with monocular depth and jointly synthesizes target views using a video-diffusion prior.

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

<a id="s056"></a>
#### SynSin: End-to-End View Synthesis From a Single Image (CVPR 2020)

[![arXiv: 1912.08804](https://img.shields.io/badge/arXiv-1912.08804-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1912.08804) &nbsp; [`T6`](#t6) [`T7`](#t7)

Lifts image features into a point cloud, differentiably projects them to target views and refines disoccluded regions.

---

<a id="s083"></a>
#### 3D Photography Using Context-Aware Layered Depth Inpainting (CVPR 2020)

[![arXiv: 2004.04727](https://img.shields.io/badge/arXiv-2004.04727-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2004.04727) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2004.04727) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://shihmengli.github.io/3D-Photo-Inpainting/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/vt-vl-lab/3d-photo-inpainting) [![GitHub stars](https://img.shields.io/github/stars/vt-vl-lab/3d-photo-inpainting?style=flat-square&label=stars&color=C58A18)](https://github.com/vt-vl-lab/3d-photo-inpainting/stargazers) [![GitHub forks](https://img.shields.io/github/forks/vt-vl-lab/3d-photo-inpainting?style=flat-square&label=forks&color=64748B)](https://github.com/vt-vl-lab/3d-photo-inpainting/forks) &nbsp; [`T6`](#t6)

Builds a layered depth image with explicit pixel connectivity and inpaints hidden color and depth for parallax rendering.

---

<a id="p48"></a>
#### Stereo Magnification: Learning view synthesis using multiplane images (SIGGRAPH / TOG 2018)

[![arXiv: 1805.09817](https://img.shields.io/badge/arXiv-1805.09817-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1805.09817) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/1805.09817) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://tinghuiz.github.io/projects/mpi/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/google/stereo-magnification) [![GitHub stars](https://img.shields.io/github/stars/google/stereo-magnification?style=flat-square&label=stars&color=C58A18)](https://github.com/google/stereo-magnification/stargazers) [![GitHub forks](https://img.shields.io/github/forks/google/stereo-magnification?style=flat-square&label=forks&color=64748B)](https://github.com/google/stereo-magnification/forks) &nbsp; [`T6`](#t6)

Predicts multiplane images from narrow-baseline stereo and warps depth planes to synthesize wider-baseline views.

---

<a id="a34"></a>
#### View Synthesis by Appearance Flow (ECCV 2016)

[![arXiv: 1605.03557](https://img.shields.io/badge/arXiv-1605.03557-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1605.03557) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tinghuiz/appearance-flow) [![GitHub stars](https://img.shields.io/github/stars/tinghuiz/appearance-flow?style=flat-square&label=stars&color=C58A18)](https://github.com/tinghuiz/appearance-flow/stargazers) [![GitHub forks](https://img.shields.io/github/forks/tinghuiz/appearance-flow?style=flat-square&label=forks&color=64748B)](https://github.com/tinghuiz/appearance-flow/forks) &nbsp; [`T4`](#t4) [`T7`](#t7)

Predicts dense appearance flow from target to input views and bilinearly samples pixels for view synthesis; later garment-warping methods build on it.

---

<a id="c28"></a>
#### Depth-image-based rendering (DIBR), compression, and transmission for a new approach on 3D-TV (SPIE 2004)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1117/12.524762) &nbsp; [`T6`](#t6)

Synthesizes virtual views from color and depth, providing a classic route to depth reprojection, visibility reasoning and hole handling. This paper did not originate the general idea of reprojection.

---

<a id="a33"></a>
#### Layered depth images (SIGGRAPH 1998)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1145/280814.280882) &nbsp; [`T6`](#t6) [`T7`](#t7)

Stores multiple depth and color layers along each ray of one viewpoint so 3D warping can fill holes from occluded layers, with efficient splat rendering.

---

<a id="a32"></a>
#### Plenoptic modeling: an image-based rendering system (SIGGRAPH 1995)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1145/218380.218398) &nbsp; [`T6`](#t6)

Reconstructs plenoptic samples from cylindrical panoramas and synthesizes new views with disparity-based 3D image warping and an occlusion-compatible drawing order.

---

<a id="a31"></a>
#### View interpolation for image synthesis (SIGGRAPH 1993)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1145/166117.166153) &nbsp; [`T4`](#t4) [`T6`](#t6)

Interpolates precomputed pixel correspondences (morph maps) between nearby reference images to synthesize intermediate viewpoints quickly, an early image-based rendering and view-morphing work.

---

<details>
<summary>Related reading · 20 papers in other topics</summary>

- [TrajectoryCrafter](#s048) (2025)
- [Latent-Reframe](#s049) (2025)
- [DepthSplat](#s059) (2025)
- [MoSca](#s063) (2025)
- [Dynamic 3D Gaussians](#p51) (2024)
- [ViewCrafter](#a25) (2024)
- [RVT](#s075) (2023)
- [DynIBaR](#a38) (2023)
- [TiNeuVox](#p52) (2022)
- [D-NeRF](#c21) (2021)
- [Nerfies](#c22) (2021)
- [Neural Scene Flow Fields (NSFF)](#p49) (2021)
- [NR-NeRF](#s064) (2021)
- [CasMVSNet](#s051) (2020)
- [Monodepth2](#c16) (2019)
- [DPSNet](#s052) (2019)
- [MVSNet](#p39) (2018)
- [Gibson Env](#s071) (2018)
- [SfMLearner](#p43) (2017)
- [Monodepth](#a30) (2017)

</details>

[↑ Start of 5.2](#topic-novel-view-synthesis) · [↑ Back to topic navigation](#topics)

---

<a id="topic-13"></a>
<a id="topic-dynamic-3d"></a>
### 5.3 Dynamic 3D & 4D Scenes

> **Scope** · Canonical deformation, dynamic NeRF, deformable Gaussians and spatiotemporal scene representations
>
> **17 papers · Newest first**

---

<a id="s063"></a>
#### MoSca: Dynamic Gaussian Fusion from Casual Videos via 4D Motion Scaffolds (CVPR 2025)

[![arXiv: 2405.17421](https://img.shields.io/badge/arXiv-2405.17421-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2405.17421) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2405.17421) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/JiahuiLei/MoSca) [![GitHub stars](https://img.shields.io/github/stars/JiahuiLei/MoSca?style=flat-square&label=stars&color=C58A18)](https://github.com/JiahuiLei/MoSca/stargazers) [![GitHub forks](https://img.shields.io/github/forks/JiahuiLei/MoSca?style=flat-square&label=forks&color=64748B)](https://github.com/JiahuiLei/MoSca/forks) &nbsp; [`T6`](#t6) [`T8`](#t8)

Lifts video priors into a 4D motion scaffold and fuses attached Gaussians to separate appearance from deformation.

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

<a id="s061"></a>
#### SC-GS: Sparse-Controlled Gaussian Splatting for Editable Dynamic Scenes (CVPR 2024)

[![arXiv: 2312.14937](https://img.shields.io/badge/arXiv-2312.14937-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2312.14937) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2312.14937) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://yihua7.github.io/SC-GS-web/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/CVMI-Lab/SC-GS) [![GitHub stars](https://img.shields.io/github/stars/CVMI-Lab/SC-GS?style=flat-square&label=stars&color=C58A18)](https://github.com/CVMI-Lab/SC-GS/stargazers) [![GitHub forks](https://img.shields.io/github/forks/CVMI-Lab/SC-GS?style=flat-square&label=forks&color=64748B)](https://github.com/CVMI-Lab/SC-GS/forks) &nbsp; [`T8`](#t8)

Interpolates time-varying 6-DoF transforms of sparse control points to deform dense Gaussians for dynamic reconstruction and editing.

---

<a id="s062"></a>
#### SceNeRFlow: Time-Consistent Reconstruction of General Dynamic Scenes (3DV 2024)

[![arXiv: 2308.08258](https://img.shields.io/badge/arXiv-2308.08258-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2308.08258) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2308.08258) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://vcai.mpi-inf.mpg.de/projects/scenerflow/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/facebookresearch/SceNeRFlow) [![GitHub stars](https://img.shields.io/github/stars/facebookresearch/SceNeRFlow?style=flat-square&label=stars&color=C58A18)](https://github.com/facebookresearch/SceNeRFlow/stargazers) [![GitHub forks](https://img.shields.io/github/forks/facebookresearch/SceNeRFlow?style=flat-square&label=forks&color=64748B)](https://github.com/facebookresearch/SceNeRFlow/forks) &nbsp; [`T8`](#t8)

Uses backward deformation into a canonical scene to recover time-consistent correspondences over large motions.

---

<a id="a38"></a>
#### DynIBaR: Neural Dynamic Image-Based Rendering (CVPR 2023)

[![arXiv: 2211.11082](https://img.shields.io/badge/arXiv-2211.11082-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2211.11082) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://dynibar.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/google/dynibar) [![GitHub stars](https://img.shields.io/github/stars/google/dynibar?style=flat-square&label=stars&color=C58A18)](https://github.com/google/dynibar/stargazers) [![GitHub forks](https://img.shields.io/github/forks/google/dynibar?style=flat-square&label=forks&color=64748B)](https://github.com/google/dynibar/forks) &nbsp; [`T6`](#t6) [`T8`](#t8)

Uses motion trajectory fields to project samples into nearby frames and aggregate their features, with scene-motion-aware volume rendering for novel views of long dynamic videos.

---

<a id="a39"></a>
#### Tracking Everything Everywhere All at Once (ICCV 2023)

[![arXiv: 2306.05422](https://img.shields.io/badge/arXiv-2306.05422-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2306.05422) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://omnimotion.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/qianqianwang68/omnimotion) [![GitHub stars](https://img.shields.io/github/stars/qianqianwang68/omnimotion?style=flat-square&label=stars&color=C58A18)](https://github.com/qianqianwang68/omnimotion/stargazers) [![GitHub forks](https://img.shields.io/github/forks/qianqianwang68/omnimotion?style=flat-square&label=forks&color=64748B)](https://github.com/qianqianwang68/omnimotion/forks) &nbsp; [`T4`](#t4) [`T8`](#t8)

Builds invertible-network bijections between each frame and a quasi-3D canonical volume for full-length per-pixel motion that persists through occlusion.

---

<a id="p52"></a>
#### Fast Dynamic Radiance Fields with Time-Aware Neural Voxels (SIGGRAPH Asia 2022)

[![arXiv: 2205.15285](https://img.shields.io/badge/arXiv-2205.15285-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2205.15285) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://jaminfong.cn/tineuvox/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/hustvl/TiNeuVox) [![GitHub stars](https://img.shields.io/github/stars/hustvl/TiNeuVox?style=flat-square&label=stars&color=C58A18)](https://github.com/hustvl/TiNeuVox/stargazers) [![GitHub forks](https://img.shields.io/github/forks/hustvl/TiNeuVox?style=flat-square&label=forks&color=64748B)](https://github.com/hustvl/TiNeuVox/forks) &nbsp; [`T6`](#t6) [`T8`](#t8)

Combines time-aware voxel features, a compact deformation network and multi-distance interpolation for efficient dynamic radiance fields.

---

<a id="a37"></a>
#### HumanNeRF: Free-viewpoint Rendering of Moving People from Monocular Video (CVPR 2022)

[![arXiv: 2201.04127](https://img.shields.io/badge/arXiv-2201.04127-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2201.04127) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://grail.cs.washington.edu/projects/humannerf/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/chungyiweng/humannerf) [![GitHub stars](https://img.shields.io/github/stars/chungyiweng/humannerf?style=flat-square&label=stars&color=C58A18)](https://github.com/chungyiweng/humannerf/stargazers) [![GitHub forks](https://img.shields.io/github/forks/chungyiweng/humannerf?style=flat-square&label=forks&color=64748B)](https://github.com/chungyiweng/humannerf/forks) &nbsp; [`T8`](#t8)

Maps observation-space points to a canonical human radiance field with skeletal rigid motion plus a nonrigid residual for free-viewpoint rendering from monocular video.

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

<a id="s064"></a>
#### Non-Rigid Neural Radiance Fields: Reconstruction and Novel View Synthesis of a Dynamic Scene From Monocular Video (ICCV 2021)

[![arXiv: 2012.12247](https://img.shields.io/badge/arXiv-2012.12247-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2012.12247) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://vcai.mpi-inf.mpg.de/projects/nonrigid_nerf/) &nbsp; [`T8`](#t8)

Uses ray bending and rigidity constraints to separate canonical radiance from deformation in monocular dynamic reconstruction.

---

<a id="a36"></a>
#### SNARF: Differentiable Forward Skinning for Animating Non-Rigid Neural Implicit Shapes (ICCV 2021)

[![arXiv: 2104.03953](https://img.shields.io/badge/arXiv-2104.03953-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2104.03953) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://xuchen-ethz.github.io/snarf/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/xuchen-ethz/snarf) [![GitHub stars](https://img.shields.io/github/stars/xuchen-ethz/snarf?style=flat-square&label=stars&color=C58A18)](https://github.com/xuchen-ethz/snarf/stargazers) [![GitHub forks](https://img.shields.io/github/forks/xuchen-ethz/snarf?style=flat-square&label=forks&color=64748B)](https://github.com/xuchen-ethz/snarf/forks) &nbsp; [`T8`](#t8)

Learns forward skinning weights in canonical space, finds canonical correspondences of deformed points by iterative root finding, and differentiates through the implicit function theorem.

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
> **5 papers · Newest first**

---

<a id="s082"></a>
#### Trans4Map: Revisiting Holistic Bird's-Eye-View Mapping From Egocentric Images to Allocentric Semantics With Vision Transformers (WACV 2023)

[![arXiv: 2207.06205](https://img.shields.io/badge/arXiv-2207.06205-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2207.06205) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2207.06205) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/InSAI-Lab/Trans4Map) [![GitHub stars](https://img.shields.io/github/stars/InSAI-Lab/Trans4Map?style=flat-square&label=stars&color=C58A18)](https://github.com/InSAI-Lab/Trans4Map/stargazers) [![GitHub forks](https://img.shields.io/github/forks/InSAI-Lab/Trans4Map?style=flat-square&label=forks&color=64748B)](https://github.com/InSAI-Lab/Trans4Map/forks) &nbsp; [`T6`](#t6) [`T8`](#t8)

Projects transformer features from egocentric images into bidirectional allocentric memory for top-down semantic mapping.

---

<a id="p53"></a>
#### Semantic MapNet: Building Allocentric Semantic Maps and Representations from Egocentric Views (AAAI 2021)

[![arXiv: 2010.01191](https://img.shields.io/badge/arXiv-2010.01191-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2010.01191) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2010.01191) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://vincentcartillier.github.io/smnet.html) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/vincentcartillier/Semantic-MapNet) [![GitHub stars](https://img.shields.io/github/stars/vincentcartillier/Semantic-MapNet?style=flat-square&label=stars&color=C58A18)](https://github.com/vincentcartillier/Semantic-MapNet/stargazers) [![GitHub forks](https://img.shields.io/github/forks/vincentcartillier/Semantic-MapNet?style=flat-square&label=forks&color=64748B)](https://github.com/vincentcartillier/Semantic-MapNet/forks) &nbsp; [`T6`](#t6)

Projects egocentric RGB-D features into allocentric spatial memory to build semantic maps for navigation and question answering.

---

<a id="s080"></a>
#### EgoMap: Projective mapping and structured egocentric memory for Deep RL (ECML PKDD 2020)

[![arXiv: 2002.02286](https://img.shields.io/badge/arXiv-2002.02286-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2002.02286) &nbsp; [`T1`](#t1) [`T6`](#t6) [`T8`](#t8)

Inverse-projects image features into a top-down memory map and updates its coordinates with ego-motion-driven affine transforms.

---

<a id="s081"></a>
#### MapNet: An Allocentric Spatial Memory for Mapping Environments (CVPR 2018)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content_cvpr_2018/html/Henriques_MapNet_An_Allocentric_CVPR_2018_paper.html) &nbsp; [`T6`](#t6) [`T8`](#t8)

Registers RGB-D observations into learned allocentric memory using paired convolutional localization and registration operations.

---

<a id="a40"></a>
#### Cognitive Mapping and Planning for Visual Navigation (CVPR 2017)

[![arXiv: 1702.03920](https://img.shields.io/badge/arXiv-1702.03920-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1702.03920) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://sites.google.com/view/cognitive-mapping-and-planning/) &nbsp; [`T1`](#t1) [`T6`](#t6)

Differentiably warps the previous top-down belief map by egomotion before fusing the current first-person observation, learning mapping and planning jointly.

---

<details>
<summary>Related reading · 3 papers in other topics</summary>

- [Spatial Memory World Models](#s073) (2025)
- [CLIPort](#p66) (2022)
- [Active Neural SLAM](#p63) (2020)

</details>

[↑ Start of 5.4](#topic-spatial-reasoning) · [↑ Back to topic navigation](#topics)

---

<a id="area-world-models-agents"></a>
## 6. World Models & Embodied Agents


<a id="topic-world-models"></a>
### 6.1 World Models & Environment Prediction

> **Scope** · State representations, dynamics prediction, action-conditioned prediction and future rollouts
>
> **3 papers · Newest first**

---

<a id="s070"></a>
#### Stochastic Variational Video Prediction (ICLR 2018)

[![arXiv: 1710.11252](https://img.shields.io/badge/arXiv-1710.11252-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1710.11252) &nbsp; [`T7`](#t7)

Adds stochastic latents to a CDNA motion-transforming predictor to model multiple possible visual futures.

---

<a id="a41"></a>
#### SDCNet: Video Prediction Using Spatially-Displaced Convolution (ECCV 2018)

[![arXiv: 1811.00684](https://img.shields.io/badge/arXiv-1811.00684-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1811.00684) &nbsp; [`T4`](#t4) [`T7`](#t7)

Predicts a motion vector and kernel per pixel and applies the kernel at the displaced source location, combining flow-based warping and kernel synthesis for future-frame prediction.

---

<a id="s068"></a>
#### Unsupervised Learning for Physical Interaction through Video Prediction (NeurIPS 2016)

[![arXiv: 1605.07157](https://img.shields.io/badge/arXiv-1605.07157-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1605.07157) &nbsp; [`T1`](#t1) [`T7`](#t7)

Predicts pixel motion with DNA, CDNA and spatial-transformer predictors, transforming and compositing prior frames into action-conditioned futures.

---

<details>
<summary>Related reading · 3 papers in other topics</summary>

- [Spatial Memory World Models](#s073) (2025)
- [AVDC](#a43) (2024)
- [Deep Voxel Flow](#a15) (2017)

</details>

[↑ Start of 6.1](#topic-world-models) · [↑ Back to topic navigation](#topics)

---


<a id="topic-interactive-simulation"></a>
### 6.2 Interactive Environments & Simulation

> **Scope** · Interactive world generation, scene persistence, training and evaluation environments, and synthetic data
>
> **2 papers · Newest first**

---

<a id="s073"></a>
#### Video World Models with Long-term Spatial Memory (NeurIPS 2025)

[![arXiv: 2506.05284](https://img.shields.io/badge/arXiv-2506.05284-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.05284) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2506.05284) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://spmem.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/spmem/spmem) [![GitHub stars](https://img.shields.io/github/stars/spmem/spmem?style=flat-square&label=stars&color=C58A18)](https://github.com/spmem/spmem/stargazers) [![GitHub forks](https://img.shields.io/github/forks/spmem/spmem?style=flat-square&label=forks&color=64748B)](https://github.com/spmem/spmem/forks) &nbsp; [`T6`](#t6) [`T9`](#t9)

Accumulates generated frames into geometric spatial memory for camera-conditioned retrieval and rendering in persistent world generation.

---

<a id="s071"></a>
#### Gibson Env: Real-World Perception for Embodied Agents (CVPR 2018)

[![arXiv: 1808.10654](https://img.shields.io/badge/arXiv-1808.10654-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1808.10654) &nbsp; [`T6`](#t6)

Reprojects observations from scanned real spaces and uses neural rendering to support embodied perception and control in simulation.

---

<details>
<summary>Related reading · 2 papers in other topics</summary>

- [GEN3C](#a23) (2025)
- [SV2P](#s070) (2018)

</details>

[↑ Start of 6.2](#topic-interactive-simulation) · [↑ Back to topic navigation](#topics)

---


<a id="topic-embodied-agents"></a>
### 6.3 Embodied Agents, Planning & Control

> **Scope** · Visual navigation, robotic manipulation, active perception, spatial-memory-guided planning and perception–action loops
>
> **7 papers · Newest first**

---

<a id="s077"></a>
#### Autonomous Functional Play with Correspondence-Driven Trajectory Warping (ICLR 2026)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://proceedings.iclr.cc/paper_files/paper/2026/hash/b52ffc1e3ab14f7b423acbb14cdbfe8e-Abstract-Conference.html) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://tether-research.github.io) &nbsp; [`T3`](#t3) [`T4`](#t4)

Warps demonstration action trajectories through semantic keypoint correspondences and collects experience through autonomous functional play.

---

<a id="a43"></a>
#### Learning to Act from Actionless Videos through Dense Correspondences (ICLR 2024)

[![arXiv: 2310.08576](https://img.shields.io/badge/arXiv-2310.08576-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2310.08576) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://flow-diffusion.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/flow-diffusion/AVDC) [![GitHub stars](https://img.shields.io/github/stars/flow-diffusion/AVDC?style=flat-square&label=stars&color=C58A18)](https://github.com/flow-diffusion/AVDC/stargazers) [![GitHub forks](https://img.shields.io/github/forks/flow-diffusion/AVDC?style=flat-square&label=forks&color=64748B)](https://github.com/flow-diffusion/AVDC/forks) &nbsp; [`T4`](#t4) [`T6`](#t6)

Synthesizes task-execution videos, then solves object rigid transforms from dense inter-frame flow and depth to infer actions in closed form.

---

<a id="s075"></a>
#### RVT: Robotic View Transformer for 3D Object Manipulation (CoRL 2023 / PMLR 2023)

[![arXiv: 2306.14896](https://img.shields.io/badge/arXiv-2306.14896-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2306.14896) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2306.14896) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://robotic-view-transformer.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nvlabs/rvt) [![GitHub stars](https://img.shields.io/github/stars/nvlabs/rvt?style=flat-square&label=stars&color=C58A18)](https://github.com/nvlabs/rvt/stargazers) [![GitHub forks](https://img.shields.io/github/forks/nvlabs/rvt?style=flat-square&label=forks&color=64748B)](https://github.com/nvlabs/rvt/forks) &nbsp; [`T6`](#t6)

Renders RGB-D point clouds into virtual views, fuses their features and back-projects predictions into 3D robot actions.

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

<a id="a42"></a>
#### Learning from Demonstrations Through the Use of Non-rigid Registration (ISRR 2013 / Springer 2016)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1007/978-3-319-28872-7_20) &nbsp; [`T2`](#t2)

Fits a TPS non-rigid registration between demonstration and test point clouds and transfers the demonstrated trajectory through the same warp for deformable-object manipulation such as knot tying.

---

<details>
<summary>Related reading · 7 papers in other topics</summary>

- [DROID-SLAM](#p40) (2021)
- [Semantic MapNet (SMNet)](#p53) (2021)
- [EgoMap](#s080) (2020)
- [Gibson Env](#s071) (2018)
- [MapNet](#s081) (2018)
- [Cognitive Mapping and Planning (CMP)](#a40) (2017)
- [DNA / CDNA / STP](#s068) (2016)

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
| <a id="t1"></a>**T1 · Parametric geometry** | Rigid / similarity / affine / homography | [PixelStitch](#s018) · [HomoGen](#s028) · [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) · [Text2Video-Zero](#a21) · [CLIPort](#p66) · [DUT](#s019) · [Unsupervised Deep Image Stitching (UDIS)](#p14) · [Transporter Networks](#p65) · [EgoMap](#s080) · [Content-Aware Unsupervised Deep Homography](#a10) · [Unsupervised Deep Homography](#a09) · [Cognitive Mapping and Planning (CMP)](#a40) · [Deep Image Homography Estimation](#p13) · [DNA / CDNA / STP](#s068) · [SPHP](#s016) · [Parallax-tolerant Image Stitching](#s017) · [LSD-SLAM](#a27) · [Lucas–Kanade / Inverse Compositional](#c02) · [Heckbert Texture Mapping & Image Warping](#a05) |
| <a id="t2"></a>**T2 · Control points and splines** | TPS / RBF / FFD / B-splines / MLS | [WarpI2I](#n26) · [StabStitch](#n28) · [FastDrag](#a04) · [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) · [Thin-Plate Spline Motion Model for Image Animation](#n03) · [Adaptive Content Generation and Preservation (ACGPN)](#p28) · [Deep Learning Image Registration (DLIR)](#p18) · [CP-VTON](#c24) · [VITON](#p27) · [TPS Trajectory Transfer](#a42) · [Bounded Biharmonic Weights (BBW)](#p03) · [Moving Least Squares (MLS)](#c08) · [B-spline FFD Registration](#c07) · [Beier–Neely Feature-Based Morphing](#c06) · [Thin-Plate Spline (TPS) / Principal Warps](#c05) · [Free-Form Deformation (FFD)](#c04) |
| <a id="t3"></a>**T3 · Meshes and local shape preservation** | Piecewise maps / ARAP / local projective models | [Tether / Autonomous Functional Play](#s077) · [Inpaint4Drag](#s003) · [FlowDrag](#s004) · [StabStitch](#n28) · [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) · [DUT](#s019) · [Unsupervised Deep Image Stitching (UDIS)](#p14) · [MeshFlow](#p16) · [DynamicFusion](#p50) · [Parallax-tolerant Image Stitching](#s017) · [As-Projective-As-Possible (APAP) / Moving DLT](#c12) · [Bundled Camera Paths](#p15) · [Rectangling Panoramas via Warping](#a03) · [Bounded Biharmonic Weights (BBW)](#p03) · [Content-Preserving Warps for 3D Video Stabilization](#c29) · [Green Coordinates](#s002) · [Optimized Scale-and-Stretch](#a02) · [As-Rigid-As-Possible (ARAP) Surface Modeling](#c09) · [Embedded Deformation](#p02) · [Harmonic Coordinates](#s001) · [Mean Value Coordinates (MVC)](#a01) · [Laplacian Surface Editing](#p01) |
| <a id="t4"></a>**T4 · Dense correspondence and optical flow** | Dense flow / correlation volumes / global matching | [Tether / Autonomous Functional Play](#s077) · [WAFT](#a06) · [MEMFOF](#n20) · [UFM](#s015) · [PixelStitch](#s018) · [BiM-VFI](#s029) · [FIA-VTON](#s032) · [FloVD](#s047) · [SEA-RAFT](#n13) · [Robust Dense Matching (RoMa)](#p71) · [FloED](#s027) · [Upscale-A-Video](#s030) · [FloAt](#s033) · [D4-VTON](#s036) · [FlowVid](#s038) · [WAVE (DDIM inversion)](#s042) · [Motion-I2V](#s045) · [MotionCraft](#s046) · [AVDC](#a43) · [UniMatch: Unifying Flow, Stereo and Depth Estimation](#n09) · [FlowFormer++](#p12) · [Dense Kernelized Matching (DKM)](#p70) · [PDC-Net+](#s012) · [ProPainter](#s024) · [DCI-VTON](#s031) · [GP-VTON](#s035) · [LatentWarp](#s040) · [Rerender A Video](#s041) · [OmniMotion](#a39) · [GMFlow](#n01) · [FlowFormer](#n02) · [FILM: Frame Interpolation for Large Motion](#n04) · [BasicVSR++](#n07) · [RIFE](#p23) · [E2FGVI](#s025) · [HR-VITON](#s034) · [ClothFormer](#s078) · [Global Motion Aggregation (GMA)](#p11) · [BasicVSR](#p25) · [Parser-Free Appearance Flow (PF-AFN)](#p29) · [DROID-SLAM](#p40) · [Neural Scene Flow Fields (NSFF)](#p49) · [LoFTR](#p69) · [COTR](#s011) · [SMURF](#a07) · [RAFT](#c20) · [GLU-Net](#s013) · [Depth-Aware Interpolation (DAIN)](#p22) · [EDVR](#p24) · [Task-Oriented Flow (TOFlow)](#p26) · [Deep Flow-Guided Video Inpainting](#s026) · [ClothFlow](#a18) · [PWC-Net](#c15) · [LiteFlowNet](#p10) · [Super SloMo](#p21) · [UnFlow](#a08) · [Blind Video Temporal Consistency](#a16) · [SDC-Net](#a41) · [FlowNet 2.0](#p08) · [SPyNet](#p09) · [Deep Voxel Flow](#a15) · [MeshFlow](#p16) · [Appearance Flow](#a34) · [FlowNet](#p07) · [SIFT Flow](#p72) · [Lucas–Kanade / Inverse Compositional](#c02) · [Brox et al. Variational Optical Flow](#c27) · [View Interpolation](#a31) · [Horn–Schunck](#c03) |
| <a id="t5"></a>**T5 · Invertible deformation and registration** | Velocity fields / diffeomorphisms / inverse consistency | [SGDIR](#s023) · [Fast Forward](#s084) · [uniGradICON](#n14) · [GradICON](#s020) · [Fourier-Net](#s022) · [TransMorph](#n05) · [SynthMorph](#n06) · [ICON](#p20) · [Symmetric Diffeomorphic Registration (SYMNet)](#p19) · [LapIRN](#s021) · [VoxelMorph](#c18) · [Deep Learning Image Registration (DLIR)](#p18) · [Recursive Cascaded Networks](#a14) · [Probabilistic Diffeomorphic VoxelMorph](#a13) · [Diffeomorphic Demons](#c11) · [SyN: Symmetric Diffeomorphic Registration](#c10) · [DARTEL](#a12) · [Log-Euclidean Diffeomorphisms](#a11) · [LDDMM / Geodesic Flows of Diffeomorphisms](#c26) · [B-spline FFD Registration](#c07) · [Demons Registration](#p17) |
| <a id="t6"></a>**T6 · Depth and 3D reprojection** | Depth / camera pose / projection / visibility | [CameraNoise](#n24) · [Warp-as-History](#n27) · [UniCaMo / Track the Noise](#a20) · [WAVE: Warp-Based View Guidance](#n22) · [SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion](#n23) · [FlowDrag](#s004) · [TrajectoryCrafter](#s048) · [Latent-Reframe](#s049) · [DepthSplat](#s059) · [MoSca](#s063) · [Spatial Memory World Models](#s073) · [GEN3C](#a23) · [CamTrol](#a24) · [NVS-Solver](#a35) · [GenWarp](#n15) · [Dynamic 3D Gaussians](#p51) · [MVSplat](#s058) · [MultiDiff](#s060) · [ViewCrafter](#a25) · [AVDC](#a43) · [UniMatch: Unifying Flow, Stereo and Depth Estimation](#n09) · [RVT](#s075) · [Trans4Map](#s082) · [DynIBaR](#a38) · [TiNeuVox](#p52) · [DROID-SLAM](#p40) · [IBRNet](#p46) · [pixelNeRF](#p47) · [Neural Scene Flow Fields (NSFF)](#p49) · [Semantic MapNet (SMNet)](#p53) · [Active Neural SLAM](#p63) · [CasMVSNet](#s051) · [SynSin](#s056) · [EgoMap](#s080) · [3D Photography](#s083) · [Monodepth2](#c16) · [Depth-Aware Interpolation (DAIN)](#p22) · [DPSNet](#s052) · [Liquid Warping GAN](#a17) · [MVSNet](#p39) · [Stereo Magnification / Multiplane Images](#p48) · [Gibson Env](#s071) · [MapNet](#s081) · [Direct Sparse Odometry (DSO)](#a28) · [SfMLearner](#p43) · [Monodepth](#a30) · [Cognitive Mapping and Planning (CMP)](#a40) · [Garg et al. Self-Supervised Depth](#a29) · [DynamicFusion](#p50) · [LSD-SLAM](#a27) · [DTAM](#a26) · [Depth-Image-Based Rendering (DIBR)](#c28) · [Layered Depth Images (LDI)](#a33) · [Plenoptic Modeling](#a32) · [View Interpolation](#a31) |
| <a id="t7"></a>**T7 · Differentiable sampling and splatting** | Interpolation / footprints / aggregation / adjoints | [Fast Forward](#s084) · [WAFT](#a06) · [LookingGlass / Laplacian Pyramid Warping (LPW)](#n21) · [SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion](#n23) · [DepthSplat](#s059) · [How I Warped Your Noise / ∫-noise](#n16) · [Dynamic 3D Gaussians](#p51) · [MVSplat](#s058) · [Multi-Frequency Representation (MFR)](#s079) · [ImWIP](#n10) · [Kernel Aware Resampler](#s006) · [Local Texture Estimator for Warping (LTEW)](#s085) · [IBRNet](#p46) · [SRWarp](#s086) · [SMURF](#a07) · [Softmax Splatting](#c19) · [SynSin](#s056) · [Content-Aware Unsupervised Deep Homography](#a10) · [Depth-Aware Interpolation (DAIN)](#p22) · [Linearized Multi-Sampling](#s007) · [DPSNet](#s052) · [Recursive Cascaded Networks](#a14) · [SV2P](#s070) · [UnFlow](#a08) · [Unsupervised Deep Homography](#a09) · [Probabilistic Diffeomorphic VoxelMorph](#a13) · [Blind Video Temporal Consistency](#a16) · [SDC-Net](#a41) · [Deep Voxel Flow](#a15) · [Monodepth](#a30) · [DNA / CDNA / STP](#s068) · [Garg et al. Self-Supervised Depth](#a29) · [Appearance Flow](#a34) · [Spatial Transformer Networks (STN)](#c13) · [EWA Volume Splatting](#c25) · [Surface Splatting](#p04) · [Layered Depth Images (LDI)](#a33) · [Heckbert Texture Mapping & Image Warping](#a05) |
| <a id="t8"></a>**T8 · Learned feature and 3D deformation** | Offsets / local affine motion / canonical fields | [MoSca](#s063) · [Deformable 3D Gaussians](#n11) · [4D Gaussian Splatting for Real-Time Dynamic Scene Rendering](#n12) · [Dynamic 3D Gaussians](#p51) · [SC-GS](#s061) · [SceNeRFlow](#s062) · [LivePortrait](#a19) · [CoDeF](#a22) · [ProPainter](#s024) · [Trans4Map](#s082) · [DynIBaR](#a38) · [OmniMotion](#a39) · [Thin-Plate Spline Motion Model for Image Animation](#n03) · [FILM: Frame Interpolation for Large Motion](#n04) · [BasicVSR++](#n07) · [TiNeuVox](#p52) · [CLIPort](#p66) · [E2FGVI](#s025) · [HumanNeRF](#a37) · [D-NeRF](#c21) · [Nerfies](#c22) · [HyperNeRF](#c23) · [Neural Scene Flow Fields (NSFF)](#p49) · [Transporter Networks](#p65) · [face-vid2vid](#s037) · [NR-NeRF](#s064) · [SNARF](#a36) · [EgoMap](#s080) · [First Order Motion Model (FOMM)](#c17) · [EDVR](#p24) · [Liquid Warping GAN](#a17) · [X2Face](#p30) · [MapNet](#s081) · [Deformable ConvNets (DCN)](#c14) · [DynamicFusion](#p50) |
| <a id="t9"></a>**T9 · Generative, frequency and stochastic warping** | Geometry–generation fusion / noise transport / frequency handling | [CameraNoise](#n24) · [WarpI2I](#n26) · [Warp-as-History](#n27) · [UniCaMo / Track the Noise](#a20) · [Go-with-the-Flow](#n19) · [LookingGlass / Laplacian Pyramid Warping (LPW)](#n21) · [WAVE: Warp-Based View Guidance](#n22) · [SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion](#n23) · [Inpaint4Drag](#s003) · [FlowDrag](#s004) · [HomoGen](#s028) · [FIA-VTON](#s032) · [Infinite-Resolution Integral Noise Warping](#s043) · [EquiVDM / Warped-Noise Equivariance](#s044) · [FloVD](#s047) · [TrajectoryCrafter](#s048) · [Latent-Reframe](#s049) · [Spatial Memory World Models](#s073) · [GEN3C](#a23) · [CamTrol](#a24) · [NVS-Solver](#a35) · [GenWarp](#n15) · [How I Warped Your Noise / ∫-noise](#n16) · [Warped Diffusion](#n17) · [FloED](#s027) · [Upscale-A-Video](#s030) · [FloAt](#s033) · [D4-VTON](#s036) · [FlowVid](#s038) · [WAVE (DDIM inversion)](#s042) · [Motion-I2V](#s045) · [MotionCraft](#s046) · [MultiDiff](#s060) · [FastDrag](#a04) · [ViewCrafter](#a25) · [DCI-VTON](#s031) · [GP-VTON](#s035) · [LatentWarp](#s040) · [Rerender A Video](#s041) · [Text2Video-Zero](#a21) · [HR-VITON](#s034) · [ClothFormer](#s078) · [Parser-Free Appearance Flow (PF-AFN)](#p29) · [Adaptive Content Generation and Preservation (ACGPN)](#p28) · [First Order Motion Model (FOMM)](#c17) · [ClothFlow](#a18) · [CP-VTON](#c24) · [VITON](#p27) · [X2Face](#p30) |

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
| Systematic search across all topics | [Queries, relevance decisions and version checks](docs/SYSTEMATIC_SEARCH.md) |

<a id="contributing"></a>
## 🤝 Contributing

Suggestions, corrections and verified links are welcome through [Issues](https://github.com/gulucaptain/Awesome-Warping-Algorithm/issues) and [Pull Requests](https://github.com/gulucaptain/Awesome-Warping-Algorithm/pulls).

Please include the **paper title, publication year/status, Paper, Project, GitHub, technique family, primary topic and related topic tags**. Leave unavailable links empty, and distinguish author implementations, third-party reimplementations and shared frameworks.

Edit [the bilingual catalog](data/catalog.json) and run `python3 scripts/build_readme.py` to update both READMEs. Counts and indexes use the same data; check consistency with `python3 scripts/build_readme.py --check`. Set each work's unique home with `primary_topic`; `topics` contains that home and related directions. When adding papers to a reserved topic, set its `reserved` flag to `false`. Prioritize topic fit, verified publication records and established impact. Citation snapshots must name the provider, matched record and query date; do not add preprint and publication counts together. See the [curation audit](docs/EXPANSION_AUDIT.md) for this expansion.

For systematic additions, discover candidates across tasks, spatial mechanisms and transformed representations before exact-title verification. Keep query logs, exclusion reasons and version relationships; identify explicit warping, correspondence estimation, flow conditioning and spatial memory separately. See the [systematic search record](docs/SYSTEMATIC_SEARCH.md). General documentation is excluded from paper counts, and preprints are not counted again when a formal version appears.

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
