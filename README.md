<!-- Generated from data/catalog.json by scripts/build_readme.py. -->
<a id="top"></a>

<div align="center">

<img src="assets/warping-banner-v2.png" alt="Luminous coordinate grids deform into a continuous three-dimensional flow surface" width="100%">

# Awesome Warping Algorithms

*A curated atlas of spatial warping.*

**English** · [简体中文](README.zh-CN.md)

<p align="justify">
Warping maps pixels, features, and noise across space and time, providing a foundation for image alignment, 3D reconstruction, and controllable generation. This repository connects classical methods with recent advances, organizing papers and implementations by technique and application to help researchers navigate the field, compare approaches, and build on existing work.
</p>

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

Classics cover work before 2022. The 2022–2026 section uses representative formal publication years and retains earlier preprint dates. Coverage ends on 2026-10-24. Descriptions are grounded in papers and author resources; the collection does not claim a unified reproduction of all methods.

[Definitions, mapping conventions and evidence policy →](docs/RESEARCH_GUIDE.md#scope)

</details>

<a id="technology"></a>
## 🧩 Technique map

Methods can belong to multiple families. Follow a method name to its entry; `T1–T9` tags link back to this map.

<details>
<summary><b>Browse all 9 technique families</b></summary>

| Technique family | Core representation | Works |
| --- | --- | --- |
| <a id="t1"></a>**T1 · Parametric geometry** | Rigid / similarity / affine / homography | [Rigid / Similarity / Affine / Homography](#c01) · [Lucas–Kanade / Inverse Compositional](#c02) · [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) |
| <a id="t2"></a>**T2 · Control points and splines** | TPS / RBF / FFD / B-splines / MLS | [Free-Form Deformation (FFD)](#c04) · [Thin-Plate Spline (TPS) / Principal Warps](#c05) · [Beier–Neely Feature-Based Morphing](#c06) · [B-spline FFD Registration](#c07) · [Moving Least Squares (MLS)](#c08) · [CP-VTON](#c24) · [Thin-Plate Spline Motion Model for Image Animation](#n03) · [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) · [StabStitch](#n28) · [WarpI2I](#n26) |
| <a id="t3"></a>**T3 · Meshes and local shape preservation** | Piecewise maps / ARAP / local projective models | [As-Rigid-As-Possible (ARAP) Surface Modeling](#c09) · [Content-Preserving Warps for 3D Video Stabilization](#c29) · [As-Projective-As-Possible (APAP) / Moving DLT](#c12) · [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) · [StabStitch](#n28) |
| <a id="t4"></a>**T4 · Dense correspondence and optical flow** | Dense flow / correlation volumes / global matching | [Lucas–Kanade / Inverse Compositional](#c02) · [Horn–Schunck](#c03) · [Brox et al. Variational Optical Flow](#c27) · [PWC-Net](#c15) · [RAFT](#c20) · [GMFlow](#n01) · [FlowFormer](#n02) · [FILM: Frame Interpolation for Large Motion](#n04) · [BasicVSR++](#n07) · [UniMatch: Unifying Flow, Stereo and Depth Estimation](#n09) · [SEA-RAFT](#n13) · [MEMFOF](#n20) |
| <a id="t5"></a>**T5 · Invertible deformation and registration** | Velocity fields / diffeomorphisms / inverse consistency | [B-spline FFD Registration](#c07) · [LDDMM / Geodesic Flows of Diffeomorphisms](#c26) · [SyN: Symmetric Diffeomorphic Registration](#c10) · [Diffeomorphic Demons](#c11) · [VoxelMorph](#c18) · [TransMorph](#n05) · [SynthMorph](#n06) · [uniGradICON](#n14) |
| <a id="t6"></a>**T6 · Depth and 3D reprojection** | Depth / camera pose / projection / visibility | [Depth-Image-Based Rendering (DIBR)](#c28) · [Monodepth2](#c16) · [UniMatch: Unifying Flow, Stereo and Depth Estimation](#n09) · [GenWarp](#n15) · [WAVE: Warp-Based View Guidance](#n22) · [SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion](#n23) · [CameraNoise](#n24) · [Warp-as-History](#n27) |
| <a id="t7"></a>**T7 · Differentiable sampling and splatting** | Interpolation / footprints / aggregation / adjoints | [EWA Volume Splatting](#c25) · [Spatial Transformer Networks (STN)](#c13) · [Softmax Splatting](#c19) · [ImWIP](#n10) · [How I Warped Your Noise / ∫-noise](#n16) · [LookingGlass / Laplacian Pyramid Warping (LPW)](#n21) · [SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion](#n23) |
| <a id="t8"></a>**T8 · Learned feature and 3D deformation** | Offsets / local affine motion / canonical fields | [Deformable ConvNets (DCN)](#c14) · [First Order Motion Model (FOMM)](#c17) · [D-NeRF](#c21) · [Nerfies](#c22) · [HyperNeRF](#c23) · [Thin-Plate Spline Motion Model for Image Animation](#n03) · [FILM: Frame Interpolation for Large Motion](#n04) · [BasicVSR++](#n07) · [Deformable 3D Gaussians](#n11) · [4D Gaussian Splatting for Real-Time Dynamic Scene Rendering](#n12) |
| <a id="t9"></a>**T9 · Generative, frequency and stochastic warping** | Geometry–generation fusion / noise transport / frequency handling | [CP-VTON](#c24) · [First Order Motion Model (FOMM)](#c17) · [GenWarp](#n15) · [How I Warped Your Noise / ∫-noise](#n16) · [Warped Diffusion](#n17) · [StableVITON](#n18) · [Go-with-the-Flow](#n19) · [LookingGlass / Laplacian Pyramid Warping (LPW)](#n21) · [WAVE: Warp-Based View Guidance](#n22) · [SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion](#n23) · [CameraNoise](#n24) · [DMAligner](#n25) · [WarpI2I](#n26) · [Warp-as-History](#n27) |

</details>

<a id="topics"></a>
## 🗂️ Topic index

<details>
<summary><b>Browse all 16 application areas</b></summary>

| Topic | Core question | Works |
| --- | --- | --- |
| <a id="topic-01"></a>**Registration** | Spatially align images | [Rigid / Similarity / Affine / Homography](#c01) · [Lucas–Kanade / Inverse Compositional](#c02) · [Thin-Plate Spline (TPS) / Principal Warps](#c05) · [B-spline FFD Registration](#c07) · [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) · [DMAligner](#n25) |
| <a id="topic-02"></a>**Medical imaging** | Align 3D anatomy across scans, contrasts or subjects | [LDDMM / Geodesic Flows of Diffeomorphisms](#c26) · [SyN: Symmetric Diffeomorphic Registration](#c10) · [Diffeomorphic Demons](#c11) · [VoxelMorph](#c18) · [TransMorph](#n05) · [SynthMorph](#n06) · [uniGradICON](#n14) |
| <a id="topic-03"></a>**Stitching** | Align overlap while preserving non-overlap geometry | [Rigid / Similarity / Affine / Homography](#c01) · [As-Projective-As-Possible (APAP) / Moving DLT](#c12) · [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) |
| <a id="topic-04"></a>**Stabilization** | Suppress camera shake and temporal warp instability | [Content-Preserving Warps for 3D Video Stabilization](#c29) · [StabStitch](#n28) |
| <a id="topic-05"></a>**Optical flow** | Estimate dense correspondence for downstream warping | [Lucas–Kanade / Inverse Compositional](#c02) · [Horn–Schunck](#c03) · [Brox et al. Variational Optical Flow](#c27) · [PWC-Net](#c15) · [RAFT](#c20) · [GMFlow](#n01) · [FlowFormer](#n02) · [UniMatch: Unifying Flow, Stereo and Depth Estimation](#n09) · [SEA-RAFT](#n13) · [MEMFOF](#n20) |
| <a id="topic-06"></a>**Frame interpolation** | Synthesize intermediate frames with occlusion handling | [Softmax Splatting](#c19) · [FILM: Frame Interpolation for Large Motion](#n04) |
| <a id="topic-07"></a>**Video restoration** | Align and fuse information across frames | [Deformable ConvNets (DCN)](#c14) · [PWC-Net](#c15) · [RAFT](#c20) · [BasicVSR++](#n07) · [Warped Diffusion](#n17) |
| <a id="topic-08"></a>**Image editing** | Control local shape using points, lines or meshes | [Free-Form Deformation (FFD)](#c04) · [Thin-Plate Spline (TPS) / Principal Warps](#c05) · [Beier–Neely Feature-Based Morphing](#c06) · [Moving Least Squares (MLS)](#c08) · [As-Rigid-As-Possible (ARAP) Surface Modeling](#c09) · [LookingGlass / Laplacian Pyramid Warping (LPW)](#n21) · [WarpI2I](#n26) |
| <a id="topic-09"></a>**Animation** | Transfer motion while preserving source appearance | [First Order Motion Model (FOMM)](#c17) · [Thin-Plate Spline Motion Model for Image Animation](#n03) · [Go-with-the-Flow](#n19) |
| <a id="topic-10"></a>**Virtual try-on** | Align garments to people while retaining clothing detail | [CP-VTON](#c24) · [StableVITON](#n18) |
| <a id="topic-11"></a>**Multi-view geometry** | Establish correspondence under geometric constraints | [Rigid / Similarity / Affine / Homography](#c01) · [Monodepth2](#c16) · [UniMatch: Unifying Flow, Stereo and Depth Estimation](#n09) |
| <a id="topic-12"></a>**Novel view synthesis** | Reproject visible content and generate disoccluded regions | [Depth-Image-Based Rendering (DIBR)](#c28) · [Monodepth2](#c16) · [D-NeRF](#c21) · [Nerfies](#c22) · [GenWarp](#n15) · [WAVE: Warp-Based View Guidance](#n22) · [SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion](#n23) |
| <a id="topic-13"></a>**Dynamic 3D / 4D** | Map time-varying scenes to canonical representations | [D-NeRF](#c21) · [Nerfies](#c22) · [HyperNeRF](#c23) · [Deformable 3D Gaussians](#n11) · [4D Gaussian Splatting for Real-Time Dynamic Scene Rendering](#n12) |
| <a id="topic-14"></a>**Video diffusion** | Convey motion or geometry to a video generator | [Softmax Splatting](#c19) · [RAFT](#c20) · [How I Warped Your Noise / ∫-noise](#n16) · [Go-with-the-Flow](#n19) · [CameraNoise](#n24) · [Warp-as-History](#n27) |
| <a id="topic-15"></a>**Inverse problems** | Include motion operators in measurement models and optimization | [B-spline FFD Registration](#c07) · [Spatial Transformer Networks (STN)](#c13) · [ImWIP](#n10) · [Warped Diffusion](#n17) |
| <a id="topic-16"></a>**Anamorphosis** | Produce different interpretations under optical transformations | [Beier–Neely Feature-Based Morphing](#c06) · [EWA Volume Splatting](#c25) · [LookingGlass / Laplacian Pyramid Warping (LPW)](#n21) |

</details>

<a id="recent"></a>
## 🚀 Recent developments · 2022–2026

**[2026](#year-2026)** · **[2025](#year-2025)** · **[2024](#year-2024)** · **[2023](#year-2023)** · **[2022](#year-2022)**

Newest years first. Each entry includes sources, technique tags and a short contribution; expand its notes for limitations and publication history.

<a id="year-2026"></a>
### 2026 · 4 works

<a id="n24"></a>
#### CameraNoise: Enabling Faithful Camera Control in Video Diffusion through Geometry-Flow-Guided Noise Warping (ICML 2026)

[`T6`](#t6) [`T9`](#t9)

[![arXiv: 2605.30774](https://img.shields.io/badge/arXiv-2605.30774-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.30774) [![Hugging Face: Model](https://img.shields.io/badge/Hugging%20Face-Model-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/gulucaptain/CameraNoise-I2V) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://gulucaptain.github.io/CameraNoise/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/gulucaptain/CameraNoise) [![GitHub stars](https://img.shields.io/github/stars/gulucaptain/CameraNoise?style=flat-square&label=stars&color=C58A18)](https://github.com/gulucaptain/CameraNoise/stargazers) [![GitHub forks](https://img.shields.io/github/forks/gulucaptain/CameraNoise?style=flat-square&label=forks&color=64748B)](https://github.com/gulucaptain/CameraNoise/forks)

Uses geometry-guided reprojection flow and noise warping to encode camera motion into temporally correlated noise, while preserving the Gaussian prior and trajectory control.

<sub>Author implementation · <a href="https://github.com/gulucaptain/CameraNoise">gulucaptain/CameraNoise</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** ICML 2026 · formal PMLR publication

Depends on scene geometry and motion estimates; the results do not imply exact control of arbitrary nonrigid motion.

[Publication / primary source](https://proceedings.mlr.press/v306/zhao26l.html)

</details>

---

<a id="n25"></a>
#### DMAligner: Enhancing Image Alignment via Diffusion Model Based View Synthesis (CVPR 2026)

[`T9`](#t9)

[![arXiv: 2602.23022](https://img.shields.io/badge/arXiv-2602.23022-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.23022) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://boomluo02.github.io/DMAligner/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/boomluo02/DMAligner) [![GitHub stars](https://img.shields.io/github/stars/boomluo02/DMAligner?style=flat-square&label=stars&color=C58A18)](https://github.com/boomluo02/DMAligner/stargazers) [![GitHub forks](https://img.shields.io/github/forks/boomluo02/DMAligner?style=flat-square&label=forks&color=64748B)](https://github.com/boomluo02/DMAligner/forks)

Recasts image alignment as diffusion-based view synthesis, using dynamics-aware training to address occlusion and illumination variation.

<sub>Author implementation · <a href="https://github.com/boomluo02/DMAligner">boomluo02/DMAligner</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** 2026 · arXiv v2 reports CVPR 2026 acceptance

A generative alternative to some uses of explicit flow warping; visually aligned synthesis is not equivalent to recovering true pixel correspondence.

</details>

---

<a id="n26"></a>
#### WarpI2I: Image Warping for Image-to-Image Translation (ECCV 2026)

[`T2`](#t2) [`T9`](#t9)

[![arXiv: 2606.31018](https://img.shields.io/badge/arXiv-2606.31018-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.31018) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2606.31018) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://shenzheng2000.github.io/WarpI2I.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ShenZheng2000/WarpI2I) [![GitHub stars](https://img.shields.io/github/stars/ShenZheng2000/WarpI2I?style=flat-square&label=stars&color=C58A18)](https://github.com/ShenZheng2000/WarpI2I/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ShenZheng2000/WarpI2I?style=flat-square&label=forks&color=64748B)](https://github.com/ShenZheng2000/WarpI2I/forks)

Uses a saliency-guided warp before encoding to allocate more spatial representation to salient regions, then unwarps the output to improve structural preservation in compact latent models.

<sub>Author implementation · <a href="https://github.com/ShenZheng2000/WarpI2I">ShenZheng2000/WarpI2I</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** 2026 · arXiv lists ECCV 2026

Uses warping to allocate representation capacity rather than primarily to estimate motion; inverse mapping remains subject to resampling error.

</details>

---

<a id="n27"></a>
#### Warp-as-History: Generalizable Camera-Controlled Video Generation from One Training Video (arXiv 2026)

[`T6`](#t6) [`T9`](#t9)

[![arXiv: 2605.15182](https://img.shields.io/badge/arXiv-2605.15182-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.15182) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2605.15182) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://yyfz.github.io/warp-as-history/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/yyfz/Warp-as-History) [![GitHub stars](https://img.shields.io/github/stars/yyfz/Warp-as-History?style=flat-square&label=stars&color=C58A18)](https://github.com/yyfz/Warp-as-History/stargazers) [![GitHub forks](https://img.shields.io/github/forks/yyfz/Warp-as-History?style=flat-square&label=forks&color=64748B)](https://github.com/yyfz/Warp-as-History/forks)

Turns camera-induced warps into pseudo-history aligned with target positions, selecting valid tokens to use a frozen model's visual-history pathway; also explores single-video LoRA adaptation.

<sub>Author implementation · <a href="https://github.com/yyfz/Warp-as-History">yyfz/Warp-as-History</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** 2026 preprint

Listed as a public preprint at this update; control should be validated across datasets and camera trajectories.

</details>

[↑ Back to years](#recent)

---

<a id="year-2025"></a>
### 2025 · 5 works

<a id="n19"></a>
#### Go-with-the-Flow: Motion-Controllable Video Diffusion Models Using Real-Time Warped Noise (CVPR 2025)

[`T9`](#t9)

[![arXiv: 2501.08331](https://img.shields.io/badge/arXiv-2501.08331-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2501.08331) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2501.08331) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://eyeline-labs.github.io/Go-with-the-Flow/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Eyeline-Labs/Go-with-the-Flow) [![GitHub stars](https://img.shields.io/github/stars/Eyeline-Labs/Go-with-the-Flow?style=flat-square&label=stars&color=C58A18)](https://github.com/Eyeline-Labs/Go-with-the-Flow/stargazers) [![GitHub forks](https://img.shields.io/github/forks/Eyeline-Labs/Go-with-the-Flow?style=flat-square&label=forks&color=64748B)](https://github.com/Eyeline-Labs/Go-with-the-Flow/forks)

Efficiently constructs warped noise and adapts video diffusion models to use it as a motion prior for motion transfer and camera or object control.

<sub>Author implementation · <a href="https://github.com/Eyeline-Labs/Go-with-the-Flow">Eyeline-Labs/Go-with-the-Flow</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** CVPR 2025

Requires the corresponding model adaptation; an arbitrary pretrained model does not necessarily support the same control mechanism.

</details>

---

<a id="n20"></a>
#### MEMFOF: High-Resolution Training for Memory-Efficient Multi-Frame Optical Flow Estimation (ICCV 2025)

[`T4`](#t4)

[![arXiv: 2506.23151](https://img.shields.io/badge/arXiv-2506.23151-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.23151) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2506.23151) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://msu-video-group.github.io/memfof/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/msu-video-group/memfof) [![GitHub stars](https://img.shields.io/github/stars/msu-video-group/memfof?style=flat-square&label=stars&color=C58A18)](https://github.com/msu-video-group/memfof/stargazers) [![GitHub forks](https://img.shields.io/github/forks/msu-video-group/memfof?style=flat-square&label=forks&color=64748B)](https://github.com/msu-video-group/memfof/forks)

Combines reduced correlation representations, multiframe estimation and high-resolution training to improve memory efficiency for native FullHD optical flow.

<sub>Author implementation · <a href="https://github.com/msu-video-group/memfof">msu-video-group/memfof</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** ICCV 2025

Not a new sampling kernel; resource figures should be reproduced under the authors' resolution, precision and hardware settings.

</details>

---

<a id="n21"></a>
#### LookingGlass: Generative Anamorphoses via Laplacian Pyramid Warping (CVPR 2025)

[`T7`](#t7) [`T9`](#t9)

[![arXiv: 2504.08902](https://img.shields.io/badge/arXiv-2504.08902-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.08902) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2504.08902) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://lookingglass-lpw.github.io/) ![GitHub: Unverified](https://img.shields.io/badge/GitHub-Unverified-89939E?style=flat-square&logo=github&logoColor=white)

Uses Laplacian pyramids for frequency-aware image warping and view aggregation, enabling multiview generative anamorphoses.

<details>
<summary>Limitations and notes</summary>

**Publication history:** CVPR 2025

Targets detail preservation and synchronization across transformed views, not a direct guarantee of random-noise statistics.

</details>

---

<a id="n22"></a>
#### WAVE: Warp-Based View Guidance for Consistent Novel View Synthesis Using a Single Image (ICCV 2025)

[`T6`](#t6) [`T9`](#t9)

[![arXiv: 2506.23518](https://img.shields.io/badge/arXiv-2506.23518-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.23518) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/jwoo-park0/WAVE) [![GitHub stars](https://img.shields.io/github/stars/jwoo-park0/WAVE?style=flat-square&label=stars&color=C58A18)](https://github.com/jwoo-park0/WAVE/stargazers) [![GitHub forks](https://img.shields.io/github/forks/jwoo-park0/WAVE?style=flat-square&label=forks&color=64748B)](https://github.com/jwoo-park0/WAVE/forks)

Uses view warping to guide adaptive attention and noise reinitialization, improving single-image novel-view consistency without additional training.

<sub>Author implementation · <a href="https://github.com/jwoo-park0/WAVE">jwoo-park0/WAVE</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** ICCV 2025

Depends on the base novel-view model and geometric estimates. Distinguish it from other WAVE papers. The authors' original project URL returned 404 during verification and is omitted.

[Publication / primary source](https://openaccess.thecvf.com/content/ICCV2025/html/Park_WAVE_Warp-Based_View_Guidance_for_Consistent_Novel_View_Synthesis_Using_ICCV_2025_paper.html)

</details>

---

<a id="n23"></a>
#### High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion (SIGGRAPH 2025)

[`T6`](#t6) [`T7`](#t7) [`T9`](#t9)

[![arXiv: 2502.12752](https://img.shields.io/badge/arXiv-2502.12752-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.12752) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2502.12752) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://studios.disneyresearch.com/2025/07/16/splatdiff/) ![GitHub: Unverified](https://img.shields.io/badge/GitHub-Unverified-89939E?style=flat-square&logo=github&logoColor=white)

Uses pixel splatting to constrain target views and combines aligned synthesis with a texture bridge to balance geometric consistency and texture fidelity.

<details>
<summary>Limitations and notes</summary>

**Publication history:** SIGGRAPH 2025

Depth and splatting errors can propagate; the faithfulness of generated detail requires separate verification.

</details>

[↑ Back to years](#recent)

---

<a id="year-2024"></a>
### 2024 · 9 works

<a id="n11"></a>
#### Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction (CVPR 2024)

[`T8`](#t8)

[![arXiv: 2309.13101](https://img.shields.io/badge/arXiv-2309.13101-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2309.13101) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2309.13101) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://ingra14m.github.io/Deformable-Gaussians/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ingra14m/Deformable-3D-Gaussians) [![GitHub stars](https://img.shields.io/github/stars/ingra14m/Deformable-3D-Gaussians?style=flat-square&label=stars&color=C58A18)](https://github.com/ingra14m/Deformable-3D-Gaussians/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ingra14m/Deformable-3D-Gaussians?style=flat-square&label=forks&color=64748B)](https://github.com/ingra14m/Deformable-3D-Gaussians/forks)

Learns a deformation field over canonical Gaussians, combining dynamic reconstruction with fast splatting-based rendering.

<sub>Author implementation · <a href="https://github.com/ingra14m/Deformable-3D-Gaussians">ingra14m/Deformable-3D-Gaussians</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** CVPR 2024 · preprint 2023

Deforms 3D parameters before rendering rather than simply interpolating a 2D image; requires per-scene optimization.

</details>

---

<a id="n12"></a>
#### 4D Gaussian Splatting for Real-Time Dynamic Scene Rendering (CVPR 2024)

[`T8`](#t8)

[![arXiv: 2310.08528](https://img.shields.io/badge/arXiv-2310.08528-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2310.08528) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2310.08528) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://guanjunwu.github.io/4dgs/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/hustvl/4DGaussians) [![GitHub stars](https://img.shields.io/github/stars/hustvl/4DGaussians?style=flat-square&label=stars&color=C58A18)](https://github.com/hustvl/4DGaussians/stargazers) [![GitHub forks](https://img.shields.io/github/forks/hustvl/4DGaussians?style=flat-square&label=forks&color=64748B)](https://github.com/hustvl/4DGaussians/forks)

Combines spatiotemporal features with Gaussian deformation to improve training, storage and rendering efficiency for dynamic scenes.

<sub>Author implementation · <a href="https://github.com/hustvl/4DGaussians">hustvl/4DGaussians</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** CVPR 2024 · preprint 2023

This entry specifically refers to the 4D-GS method by Wu and colleagues, not every method named 4D Gaussian Splatting.

</details>

---

<a id="n28"></a>
#### Eliminating Warping Shakes for Unsupervised Online Video Stitching (ECCV 2024)

[`T2`](#t2) [`T3`](#t3)

[![arXiv: 2403.06378](https://img.shields.io/badge/arXiv-2403.06378-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2403.06378) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2403.06378) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nie-lang/StabStitch) [![GitHub stars](https://img.shields.io/github/stars/nie-lang/StabStitch?style=flat-square&label=stars&color=C58A18)](https://github.com/nie-lang/StabStitch/stargazers) [![GitHub forks](https://img.shields.io/github/forks/nie-lang/StabStitch?style=flat-square&label=forks&color=64748B)](https://github.com/nie-lang/StabStitch/forks)

Unifies video stitching and stabilization in an unsupervised online framework, constraining spatial alignment and temporal stability to suppress warping shake.

<sub>Author implementation · <a href="https://github.com/nie-lang/StabStitch">nie-lang/StabStitch</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** ECCV 2024

Good image-level alignment does not guarantee stable video; latency, distortion and dynamic-scene behavior need separate evaluation.

</details>

---

<a id="n13"></a>
#### SEA-RAFT: Simple, Efficient, Accurate RAFT for Optical Flow (ECCV 2024)

[`T4`](#t4)

[![arXiv: 2405.14793](https://img.shields.io/badge/arXiv-2405.14793-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2405.14793) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2405.14793) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/princeton-vl/SEA-RAFT) [![GitHub stars](https://img.shields.io/github/stars/princeton-vl/SEA-RAFT?style=flat-square&label=stars&color=C58A18)](https://github.com/princeton-vl/SEA-RAFT/stargazers) [![GitHub forks](https://img.shields.io/github/forks/princeton-vl/SEA-RAFT?style=flat-square&label=forks&color=64748B)](https://github.com/princeton-vl/SEA-RAFT/forks)

Improves RAFT's efficiency and accuracy through initial-flow regression, a mixture-of-Laplace loss and rigid-motion pretraining.

<sub>Author implementation · <a href="https://github.com/princeton-vl/SEA-RAFT">princeton-vl/SEA-RAFT</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** ECCV 2024

An improvement to correspondence estimation; outcomes depend on the evaluation protocol.

</details>

---

<a id="n14"></a>
#### uniGradICON: A Foundation Model for Medical Image Registration (MICCAI 2024)

[`T5`](#t5)

[![arXiv: 2403.05780](https://img.shields.io/badge/arXiv-2403.05780-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2403.05780) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/uncbiag/uniGradICON) [![GitHub stars](https://img.shields.io/github/stars/uncbiag/uniGradICON?style=flat-square&label=stars&color=C58A18)](https://github.com/uncbiag/uniGradICON/stargazers) [![GitHub forks](https://img.shields.io/github/forks/uncbiag/uniGradICON?style=flat-square&label=forks&color=64748B)](https://github.com/uncbiag/uniGradICON/forks)

Moves learned registration toward a reusable model across datasets, anatomical regions and new tasks, including zero-shot use and initialization for adaptation.

<sub>Author implementation · <a href="https://github.com/uncbiag/uniGradICON">uncbiag/uniGradICON</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** MICCAI 2024

Generalization is not guaranteed for arbitrary modalities or anatomy.

[Publication / primary source](https://papers.miccai.org/miccai-2024/816-Paper0527.html)

</details>

---

<a id="n15"></a>
#### GenWarp: Single Image to Novel Views with Semantic-Preserving Generative Warping (NeurIPS 2024)

[`T6`](#t6) [`T9`](#t9)

[![arXiv: 2405.17251](https://img.shields.io/badge/arXiv-2405.17251-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2405.17251) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2405.17251) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://genwarp-nvs.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sony/genwarp) [![GitHub stars](https://img.shields.io/github/stars/sony/genwarp?style=flat-square&label=stars&color=C58A18)](https://github.com/sony/genwarp/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sony/genwarp?style=flat-square&label=forks&color=64748B)](https://github.com/sony/genwarp/forks)

Combines depth-induced coordinate information with cross-view and self-attention, learning which content to transfer and which missing regions to generate.

<sub>Author implementation · <a href="https://github.com/sony/genwarp">sony/genwarp</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** NeurIPS 2024

Generative warping does not mean that generated regions are exact copies transported from the source image.

[Publication / primary source](https://proceedings.neurips.cc/paper_files/paper/2024/hash/92e886487a8354b03d8bf4416eae6d7d-Abstract-Conference.html)

</details>

---

<a id="n16"></a>
#### How I Warped Your Noise: a Temporally-Correlated Noise Prior for Diffusion Models (ICLR 2024)

[`T7`](#t7) [`T9`](#t9)

[![arXiv: 2504.03072](https://img.shields.io/badge/arXiv-2504.03072-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.03072) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://warpyournoise.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/mskwak01/How-I-Warped-Your-Noise-Unofficial) [![GitHub stars](https://img.shields.io/github/stars/mskwak01/How-I-Warped-Your-Noise-Unofficial?style=flat-square&label=stars&color=C58A18)](https://github.com/mskwak01/How-I-Warped-Your-Noise-Unofficial/stargazers) [![GitHub forks](https://img.shields.io/github/forks/mskwak01/How-I-Warped-Your-Noise-Unofficial?style=flat-square&label=forks&color=64748B)](https://github.com/mskwak01/How-I-Warped-Your-Noise-Unofficial/forks)

Interprets pixel noise as integrals over a continuous white-noise field and designs transport for Gaussian statistics while retaining motion-induced temporal correlation.

<sub>Unofficial reimplementation · <a href="https://github.com/mskwak01/How-I-Warped-Your-Noise-Unofficial">mskwak01/How-I-Warped-Your-Noise-Unofficial</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** ICLR 2024

The goal differs from ordinary RGB interpolation. Its 2025 arXiv upload postdates the ICLR 2024 paper and should not be treated as the first publication.

[Publication / primary source](https://openreview.net/pdf?id=pzElnMrgSD)

</details>

---

<a id="n17"></a>
#### Warped Diffusion: Solving Video Inverse Problems with Image Diffusion Models (NeurIPS 2024)

[`T9`](#t9)

[![arXiv: 2410.16152](https://img.shields.io/badge/arXiv-2410.16152-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2410.16152) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2410.16152) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://giannisdaras.github.io/warped_diffusion.github.io/) ![GitHub: Unverified](https://img.shields.io/badge/GitHub-Unverified-89939E?style=flat-square&logo=github&logoColor=white)

Uses continuous function spaces and transformation equivariance for video inverse problems, improving temporal consistency with test-time self-equivariance guidance.

<details>
<summary>Limitations and notes</summary>

**Publication history:** NeurIPS 2024

Not simply a one-time warp of initialization noise; the applications include video inpainting and super-resolution.

</details>

---

<a id="n18"></a>
#### StableVITON: Learning Semantic Correspondence with Latent Diffusion Model for Virtual Try-On (CVPR 2024)

[`T9`](#t9)

[![arXiv: 2312.01725](https://img.shields.io/badge/arXiv-2312.01725-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2312.01725) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2312.01725) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/rlawjdghek/StableVITON) [![GitHub stars](https://img.shields.io/github/stars/rlawjdghek/StableVITON?style=flat-square&label=stars&color=C58A18)](https://github.com/rlawjdghek/StableVITON/stargazers) [![GitHub forks](https://img.shields.io/github/forks/rlawjdghek/StableVITON?style=flat-square&label=forks&color=64748B)](https://github.com/rlawjdghek/StableVITON/forks)

Learns semantic garment-to-person correspondence inside a latent diffusion model, using attention for implicit alignment and detail transfer.

<sub>Author implementation · <a href="https://github.com/rlawjdghek/StableVITON">rlawjdghek/StableVITON</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** CVPR 2024 · preprint 2023

Implicit semantic association should not be treated as the same operator as an explicit TPS or flow-based coordinate warp.

</details>

[↑ Back to years](#recent)

---

<a id="year-2023"></a>
### 2023 · 3 works

<a id="n08"></a>
#### Parallax-Tolerant Unsupervised Deep Image Stitching (ICCV 2023)

[`T1`](#t1) [`T2`](#t2) [`T3`](#t3)

[![arXiv: 2302.08207](https://img.shields.io/badge/arXiv-2302.08207-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2302.08207) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2302.08207) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nie-lang/UDIS2) [![GitHub stars](https://img.shields.io/github/stars/nie-lang/UDIS2?style=flat-square&label=stars&color=C58A18)](https://github.com/nie-lang/UDIS2/stargazers) [![GitHub forks](https://img.shields.io/github/forks/nie-lang/UDIS2?style=flat-square&label=forks&color=64748B)](https://github.com/nie-lang/UDIS2/forks)

Combines global homography with local TPS, jointly considering overlap alignment, non-overlap shape preservation and seam composition.

<sub>Author implementation · <a href="https://github.com/nie-lang/UDIS2">nie-lang/UDIS2</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** ICCV 2023

Tolerance of large parallax does not imply that all 3D visibility and occlusion problems are solved.

</details>

---

<a id="n09"></a>
#### Unifying Flow, Stereo and Depth Estimation (TPAMI 2023)

[`T4`](#t4) [`T6`](#t6)

[![arXiv: 2211.05783](https://img.shields.io/badge/arXiv-2211.05783-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2211.05783) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2211.05783) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://haofeixu.github.io/unimatch/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/autonomousvision/unimatch) [![GitHub stars](https://img.shields.io/github/stars/autonomousvision/unimatch?style=flat-square&label=stars&color=C58A18)](https://github.com/autonomousvision/unimatch/stargazers) [![GitHub forks](https://img.shields.io/github/forks/autonomousvision/unimatch?style=flat-square&label=forks&color=64748B)](https://github.com/autonomousvision/unimatch/forks)

Unifies optical flow, stereo disparity and depth from posed views as dense correspondence-matching problems.

<sub>Author implementation · <a href="https://github.com/autonomousvision/unimatch">autonomousvision/unimatch</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** TPAMI 2023

The preprint appeared in 2022; output structure, geometric constraints and refinement still depend on the task.

</details>

---

<a id="n10"></a>
#### ImWIP: Open-source image warping toolbox with adjoints and derivatives (SoftwareX 2023)

[`T7`](#t7)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1016/j.softx.2023.101524) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://imwip.readthedocs.io/en/latest/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/RendersJens/ImWIP) [![GitHub stars](https://img.shields.io/github/stars/RendersJens/ImWIP?style=flat-square&label=stars&color=C58A18)](https://github.com/RendersJens/ImWIP/stargazers) [![GitHub forks](https://img.shields.io/github/forks/RendersJens/ImWIP?style=flat-square&label=forks&color=64748B)](https://github.com/RendersJens/ImWIP/forks)

Provides differentiable image-warp operators with exact discrete adjoints and derivatives for inverse-problem optimization.

<sub>Author implementation · <a href="https://github.com/RendersJens/ImWIP">RendersJens/ImWIP</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** SoftwareX 2023

The adjoint is not an inverse warp. Exactness concerns the selected discretization, up to floating-point error.

</details>

[↑ Back to years](#recent)

---

<a id="year-2022"></a>
### 2022 · 7 works

<a id="n01"></a>
#### GMFlow: Learning Optical Flow via Global Matching (CVPR 2022)

[`T4`](#t4)

[![arXiv: 2111.13680](https://img.shields.io/badge/arXiv-2111.13680-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2111.13680) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2111.13680) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/haofeixu/gmflow) [![GitHub stars](https://img.shields.io/github/stars/haofeixu/gmflow?style=flat-square&label=stars&color=C58A18)](https://github.com/haofeixu/gmflow/stargazers) [![GitHub forks](https://img.shields.io/github/forks/haofeixu/gmflow?style=flat-square&label=forks&color=64748B)](https://github.com/haofeixu/gmflow/forks)

Uses Transformer-enhanced cross-image features and global matching to estimate flow with less reliance on long sequences of iterative refinement.

<sub>Author implementation · <a href="https://github.com/haofeixu/gmflow">haofeixu/gmflow</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** CVPR 2022

Improves correspondence estimation rather than the resampling kernel; the preprint appeared in 2021.

</details>

---

<a id="n02"></a>
#### FlowFormer: A Transformer Architecture for Optical Flow (ECCV 2022)

[`T4`](#t4)

[![arXiv: 2203.16194](https://img.shields.io/badge/arXiv-2203.16194-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2203.16194) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://drinkingcoder.github.io/publication/flowformer/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/drinkingcoder/FlowFormer-Official) [![GitHub stars](https://img.shields.io/github/stars/drinkingcoder/FlowFormer-Official?style=flat-square&label=stars&color=C58A18)](https://github.com/drinkingcoder/FlowFormer-Official/stargazers) [![GitHub forks](https://img.shields.io/github/forks/drinkingcoder/FlowFormer-Official?style=flat-square&label=forks&color=64748B)](https://github.com/drinkingcoder/FlowFormer-Official/forks)

Encodes a 4D cost volume with Transformers and recurrently decodes motion updates.

<sub>Author implementation · <a href="https://github.com/drinkingcoder/FlowFormer-Official">drinkingcoder/FlowFormer-Official</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** ECCV 2022

The cost representation and high-resolution memory requirements need consideration.

</details>

---

<a id="n03"></a>
#### Thin-Plate Spline Motion Model for Image Animation (CVPR 2022)

[`T2`](#t2) [`T8`](#t8)

[![arXiv: 2203.14367](https://img.shields.io/badge/arXiv-2203.14367-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2203.14367) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2203.14367) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/yoyo-nb/Thin-Plate-Spline-Motion-Model) [![GitHub stars](https://img.shields.io/github/stars/yoyo-nb/Thin-Plate-Spline-Motion-Model?style=flat-square&label=stars&color=C58A18)](https://github.com/yoyo-nb/Thin-Plate-Spline-Motion-Model/stargazers) [![GitHub forks](https://img.shields.io/github/forks/yoyo-nb/Thin-Plate-Spline-Motion-Model?style=flat-square&label=forks&color=64748B)](https://github.com/yoyo-nb/Thin-Plate-Spline-Motion-Model/forks)

Extends local affine motion representations to multiple TPS transformations, using multiscale occlusion masks for feature warping in image animation.

<sub>Author implementation · <a href="https://github.com/yoyo-nb/Thin-Plate-Spline-Motion-Model">yoyo-nb/Thin-Plate-Spline-Motion-Model</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** CVPR 2022

A learned composition of classical TPS models, not the invention of TPS itself; extreme identity differences remain challenging.

[Publication / primary source](https://openaccess.thecvf.com/content/CVPR2022/html/Zhao_Thin-Plate_Spline_Motion_Model_for_Image_Animation_CVPR_2022_paper.html)

</details>

---

<a id="n04"></a>
#### FILM: Frame Interpolation for Large Motion (ECCV 2022)

[`T4`](#t4) [`T8`](#t8)

[![arXiv: 2202.04901](https://img.shields.io/badge/arXiv-2202.04901-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2202.04901) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2202.04901) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://film-net.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/google-research/frame-interpolation) [![GitHub stars](https://img.shields.io/github/stars/google-research/frame-interpolation?style=flat-square&label=stars&color=C58A18)](https://github.com/google-research/frame-interpolation/stargazers) [![GitHub forks](https://img.shields.io/github/forks/google-research/frame-interpolation?style=flat-square&label=forks&color=64748B)](https://github.com/google-research/frame-interpolation/forks)

Shares feature extraction and motion estimation across scales to improve large-motion frame interpolation using training from image frames alone.

<sub>Author implementation · <a href="https://github.com/google-research/frame-interpolation">google-research/frame-interpolation</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** ECCV 2022

Large disocclusions still require synthesis; this is an interpolation system rather than one universal warp operator.

</details>

---

<a id="n05"></a>
#### TransMorph: Transformer for unsupervised medical image registration (Medical Image Analysis 2022)

[`T5`](#t5)

[![arXiv: 2111.10480](https://img.shields.io/badge/arXiv-2111.10480-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2111.10480) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration) [![GitHub stars](https://img.shields.io/github/stars/junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration?style=flat-square&label=stars&color=C58A18)](https://github.com/junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration/stargazers) [![GitHub forks](https://img.shields.io/github/forks/junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration?style=flat-square&label=forks&color=64748B)](https://github.com/junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration/forks)

Uses a hybrid Transformer–ConvNet architecture to model long-range relationships in volumetric medical registration.

<sub>Author implementation · <a href="https://github.com/junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration">junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** Medical Image Analysis 2022

The preprint appeared in 2021. Whether a variant is diffeomorphic depends on its specific formulation.

</details>

---

<a id="n06"></a>
#### SynthMorph: learning contrast-invariant registration without acquired images (IEEE TMI 2022)

[`T5`](#t5)

[![arXiv: 2004.10282](https://img.shields.io/badge/arXiv-2004.10282-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2004.10282) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2004.10282) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://w3id.org/synthmorph) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/voxelmorph/voxelmorph) [![GitHub stars](https://img.shields.io/github/stars/voxelmorph/voxelmorph?style=flat-square&label=stars&color=C58A18)](https://github.com/voxelmorph/voxelmorph/stargazers) [![GitHub forks](https://img.shields.io/github/forks/voxelmorph/voxelmorph?style=flat-square&label=forks&color=64748B)](https://github.com/voxelmorph/voxelmorph/forks)

Trains with synthetic label maps and diverse image appearances to improve deformable registration across MRI contrasts.

<sub>Shared framework; counts refer to the entire repository · <a href="https://github.com/voxelmorph/voxelmorph">voxelmorph/voxelmorph</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** IEEE TMI 2022 · online publication 2021

The preprint appeared in 2020; the main advance concerns training strategy and generalization.

</details>

---

<a id="n07"></a>
#### BasicVSR++: Improving Video Super-Resolution with Enhanced Propagation and Alignment (CVPR 2022)

[`T4`](#t4) [`T8`](#t8)

[![arXiv: 2104.13371](https://img.shields.io/badge/arXiv-2104.13371-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2104.13371) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2104.13371) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ckkelvinchan/BasicVSR_PlusPlus) [![GitHub stars](https://img.shields.io/github/stars/ckkelvinchan/BasicVSR_PlusPlus?style=flat-square&label=stars&color=C58A18)](https://github.com/ckkelvinchan/BasicVSR_PlusPlus/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ckkelvinchan/BasicVSR_PlusPlus?style=flat-square&label=forks&color=64748B)](https://github.com/ckkelvinchan/BasicVSR_PlusPlus/forks)

Combines second-order propagation with flow-guided deformable alignment to integrate optical-flow priors and adaptive feature sampling for video restoration.

<sub>Author implementation · <a href="https://github.com/ckkelvinchan/BasicVSR_PlusPlus">ckkelvinchan/BasicVSR_PlusPlus</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** CVPR 2022

The preprint appeared in 2021; the method is part of a video-restoration pipeline.

[Publication / primary source](https://openaccess.thecvf.com/content/CVPR2022/html/Chan_BasicVSR_Improving_Video_Super-Resolution_With_Enhanced_Propagation_and_Alignment_CVPR_2022_paper.html)

</details>

[↑ Back to years](#recent)

---


<a id="classics"></a>
## 🏛️ Classical foundations · Before 2022

### Parametric geometry and motion estimation

<a id="c01"></a>
#### Rigid / Similarity / Affine / Homography (Foundational models)

[`T1`](#t1)

[![Reference: Read](https://img.shields.io/badge/Reference-Read-2563EB?style=flat-square)](https://docs.opencv.org/4.x/d9/dab/tutorial_homography.html) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) ![GitHub: Unverified](https://img.shields.io/badge/GitHub-Unverified-89939E?style=flat-square&logo=github&logoColor=white)

Global rigid, similarity, affine and projective maps provide compact coordinate transformations. A homography models a plane or a change of view under pure rotation about a fixed optical center.

<details>
<summary>Limitations and notes</summary>

**Publication history:** Foundational models

One global matrix cannot generally explain 3D translation with parallax or nonrigid motion.

</details>

---

<a id="c02"></a>
#### Lucas-Kanade 20 Years On: A Unifying Framework (IJCV 2004)

[`T1`](#t1) [`T4`](#t4)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.ri.cmu.edu/pub_files/pub3/baker_simon_2004_1/baker_simon_2004_1.pdf) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) ![GitHub: Unverified](https://img.shields.io/badge/GitHub-Unverified-89939E?style=flat-square&logo=github&logoColor=white)

Optimizes warp parameters using image residuals. The inverse compositional formulation reuses parts of the computation and remains a foundation of direct image alignment.

<details>
<summary>Limitations and notes</summary>

**Publication history:** 1981 · IJCV 2004 unifying framework

Sensitive to initialization, photometric assumptions and local minima.

</details>

---

<a id="c03"></a>
#### Determining optical flow (Artificial Intelligence 1981)

[`T4`](#t4)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1016/0004-3702(81)90024-2) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) ![GitHub: Unverified](https://img.shields.io/badge/GitHub-Unverified-89939E?style=flat-square&logo=github&logoColor=white)

Combines brightness constancy with a global smoothness regularizer, establishing a classical variational formulation of dense optical flow.

<details>
<summary>Limitations and notes</summary>

**Publication history:** 1981

The basic formulation can oversmooth motion boundaries and struggles with large displacement.

</details>

---

<a id="c27"></a>
#### High Accuracy Optical Flow Estimation Based on a Theory for Warping (ECCV 2004)

[`T4`](#t4)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.mia.uni-saarland.de/Publications/brox-eccv04-of.pdf) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) ![GitHub: Unverified](https://img.shields.io/badge/GitHub-Unverified-89939E?style=flat-square&logo=github&logoColor=white)

Combines brightness and gradient constancy with edge-preserving regularization, and gives a theoretical interpretation of coarse-to-fine warping in the numerical solver.

<details>
<summary>Limitations and notes</summary>

**Publication history:** ECCV 2004

Large illumination changes and severe occlusion violate its data assumptions.

</details>

---

<a id="c15"></a>
#### PWC-Net: CNNs for Optical Flow Using Pyramid, Warping, and Cost Volume (CVPR 2018)

[`T4`](#t4)

[![arXiv: 1709.02371](https://img.shields.io/badge/arXiv-1709.02371-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1709.02371) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/NVlabs/PWC-Net) [![GitHub stars](https://img.shields.io/github/stars/NVlabs/PWC-Net?style=flat-square&label=stars&color=C58A18)](https://github.com/NVlabs/PWC-Net/stargazers) [![GitHub forks](https://img.shields.io/github/forks/NVlabs/PWC-Net?style=flat-square&label=forks&color=64748B)](https://github.com/NVlabs/PWC-Net/forks)

Combines feature pyramids, feature warping and cost volumes to learn residual motion from coarse to fine.

<sub>Author implementation · <a href="https://github.com/NVlabs/PWC-Net">NVlabs/PWC-Net</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** CVPR 2018 · preprint 2017

Errors can propagate between pyramid levels; occlusions require additional treatment.

</details>

---

<a id="c20"></a>
#### RAFT: Recurrent All-Pairs Field Transforms for Optical Flow (ECCV 2020)

[`T4`](#t4)

[![arXiv: 2003.12039](https://img.shields.io/badge/arXiv-2003.12039-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2003.12039) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2003.12039) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/princeton-vl/RAFT) [![GitHub stars](https://img.shields.io/github/stars/princeton-vl/RAFT?style=flat-square&label=stars&color=C58A18)](https://github.com/princeton-vl/RAFT/stargazers) [![GitHub forks](https://img.shields.io/github/forks/princeton-vl/RAFT?style=flat-square&label=forks&color=64748B)](https://github.com/princeton-vl/RAFT/forks)

Builds all-pairs correlation volumes and updates a dense flow field recurrently, providing an influential baseline for correspondence estimation.

<sub>Author implementation · <a href="https://github.com/princeton-vl/RAFT">princeton-vl/RAFT</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** ECCV 2020

Correlation storage grows with resolution. RAFT estimates flow; it does not introduce a new image interpolation kernel.

</details>

[↑ Back to classics](#classics)

---

### Control points, splines and local shape

<a id="c04"></a>
#### Free-Form Deformation of Solid Geometric Models (SIGGRAPH 1986)

[`T2`](#t2)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.cse.iitd.ac.in/~jatin/minor_p/papers/sederberg.pdf) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) ![GitHub: Unverified](https://img.shields.io/badge/GitHub-Unverified-89939E?style=flat-square&logo=github&logoColor=white)

Sederberg and Parry deform geometric objects through a control lattice and Bernstein polynomials, establishing a foundation for volumetric free-form deformation.

<details>
<summary>Limitations and notes</summary>

**Publication history:** SIGGRAPH 1986

Lattice resolution trades detail against complexity; the model does not automatically prevent folding.

</details>

---

<a id="c05"></a>
#### Principal warps: thin-plate splines and the decomposition of deformations (TPAMI 1989)

[`T2`](#t2)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1109/34.24792) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) ![GitHub: Unverified](https://img.shields.io/badge/GitHub-Unverified-89939E?style=flat-square&logo=github&logoColor=white)

Bookstein uses thin-plate splines for landmark-based deformation analysis, defining smooth nonrigid maps through bending energy. The underlying mathematics of TPS predates this paper.

<details>
<summary>Limitations and notes</summary>

**Publication history:** TPAMI 1989

Global support, outlier landmarks and extrapolation can produce implausible deformation.

</details>

---

<a id="c06"></a>
#### Feature-Based Image Metamorphosis (SIGGRAPH 1992)

[`T2`](#t2)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://wcours.gel.ulaval.ca/GIF4105/old/h20/tps/tp3/beierneely92.pdf) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) ![GitHub: Unverified](https://img.shields.io/badge/GitHub-Unverified-89939E?style=flat-square&logo=github&logoColor=white)

Uses corresponding feature-line pairs to control an inverse warp, then blends image colors to produce morphing effects.

<details>
<summary>Limitations and notes</summary>

**Publication history:** SIGGRAPH 1992

Requires manually specified correspondences and can distort complex regions.

</details>

---

<a id="c07"></a>
#### Nonrigid registration using free-form deformations: application to breast MR images (IEEE TMI 1999)

[`T2`](#t2) [`T5`](#t5)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1109/42.796284) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) ![GitHub: Unverified](https://img.shields.io/badge/GitHub-Unverified-89939E?style=flat-square&logo=github&logoColor=white)

Rueckert and colleagues combine global affine alignment with local B-spline free-form deformation for nonrigid breast MR registration.

<details>
<summary>Limitations and notes</summary>

**Publication history:** IEEE TMI 1999

An ordinary B-spline FFD does not automatically satisfy diffeomorphic constraints.

</details>

---

<a id="c08"></a>
#### Image deformation using moving least squares (SIGGRAPH / TOG 2006)

[`T2`](#t2)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1145/1141911.1141920) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) ![GitHub: Unverified](https://img.shields.io/badge/GitHub-Unverified-89939E?style=flat-square&logo=github&logoColor=white)

Schaefer and colleagues construct affine, similarity and rigid image deformations through locally weighted fitting, enabling interactive point and line controls.

<details>
<summary>Limitations and notes</summary>

**Publication history:** SIGGRAPH / TOG 2006

Results depend on weights, landmark layout and extrapolation; local fitting does not guarantee global invertibility.

</details>

---

<a id="c09"></a>
#### As-Rigid-As-Possible Surface Modeling (SGP 2007)

[`T3`](#t3)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://igl.ethz.ch/projects/ARAP/arap_web.pdf) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://igl.ethz.ch/projects/ARAP/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/libigl/libigl) [![GitHub stars](https://img.shields.io/github/stars/libigl/libigl?style=flat-square&label=stars&color=C58A18)](https://github.com/libigl/libigl/stargazers) [![GitHub forks](https://img.shields.io/github/forks/libigl/libigl?style=flat-square&label=forks&color=64748B)](https://github.com/libigl/libigl/forks)

Sorkine and Alexa preserve local shape through an as-rigid-as-possible energy, establishing a widely used approach to detail-preserving mesh editing.

<sub>Shared framework; counts refer to the entire repository · <a href="https://github.com/libigl/libigl">libigl/libigl</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** SGP 2007

Requires a mesh and numerical optimization; large deformations may still self-intersect.

</details>

---

<a id="c29"></a>
#### Content-Preserving Warps for 3D Video Stabilization (SIGGRAPH / TOG 2009)

[`T3`](#t3)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://pages.cs.wisc.edu/~fliu/papers/siggraph09.pdf) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://web.cecs.pdx.edu/~fliu/project/3dstab.htm) ![GitHub: Unverified](https://img.shields.io/badge/GitHub-Unverified-89939E?style=flat-square&logo=github&logoColor=white)

Combines reconstructed 3D camera motion with content-preserving mesh warps to stabilize video while balancing alignment and salient-region shape.

<details>
<summary>Limitations and notes</summary>

**Publication history:** SIGGRAPH / TOG 2009

Depends on reliable motion reconstruction, with trade-offs between cropping, depth variation and residual distortion.

</details>

---

<a id="c12"></a>
#### As-Projective-As-Possible Image Stitching with Moving DLT (CVPR 2013)

[`T3`](#t3)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content_cvpr_2013/papers/Zaragoza_As-Projective-As-Possible_Image_Stitching_2013_CVPR_paper.pdf) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) ![GitHub: Unverified](https://img.shields.io/badge/GitHub-Unverified-89939E?style=flat-square&logo=github&logoColor=white)

Zaragoza and colleagues allow local departures from a global projective map through Moving DLT, accommodating parallax and nonplanarity in image stitching.

<details>
<summary>Limitations and notes</summary>

**Publication history:** CVPR 2013

Large parallax, heavy occlusion and extrapolation outside overlap remain challenging.

</details>

[↑ Back to classics](#classics)

---

### Topology preservation and medical registration

<a id="c26"></a>
#### Computing Large Deformation Metric Mappings via Geodesic Flows of Diffeomorphisms (IJCV 2005)

[`T5`](#t5)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.cs.jhu.edu/~misha/ReadingSeminar/Papers/Beg05.pdf) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://www.cis.jhu.edu/software/lddmm-volume/index.php) ![GitHub: Unverified](https://img.shields.io/badge/GitHub-Unverified-89939E?style=flat-square&logo=github&logoColor=white)

Beg and colleagues construct large diffeomorphic deformations through smooth velocity fields and geodesic flows, forming a foundation of computational anatomy.

<details>
<summary>Limitations and notes</summary>

**Publication history:** IJCV 2005

Optimization and numerical integration can be expensive; discretization and regularization scale affect results.

</details>

---

<a id="c10"></a>
#### Symmetric Diffeomorphic Image Registration with Cross-Correlation: Evaluating Automated Labeling of Elderly and Neurodegenerative Brain (Medical Image Analysis 2008)

[`T5`](#t5)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2276735/) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ANTsX/ANTs) [![GitHub stars](https://img.shields.io/github/stars/ANTsX/ANTs?style=flat-square&label=stars&color=C58A18)](https://github.com/ANTsX/ANTs/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ANTsX/ANTs?style=flat-square&label=forks&color=64748B)](https://github.com/ANTsX/ANTs/forks)

Uses symmetric diffeomorphic registration with cross-correlation for anatomical alignment; SyN is a representative method in ANTs.

<sub>Shared framework; counts refer to the entire repository · <a href="https://github.com/ANTsX/ANTs">ANTsX/ANTs</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** Medical Image Analysis 2008

Pairwise optimization can be costly, and results depend on similarity measures, regularization and discretization.

</details>

---

<a id="c11"></a>
#### Diffeomorphic demons: Efficient non-parametric image registration (NeuroImage 2009)

[`T5`](#t5)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1016/j.neuroimage.2008.10.040) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) ![GitHub: Unverified](https://img.shields.io/badge/GitHub-Unverified-89939E?style=flat-square&logo=github&logoColor=white)

Introduces diffeomorphic updates within the Demons framework, combining efficient nonparametric registration with smooth, invertible deformation models.

<details>
<summary>Limitations and notes</summary>

**Publication history:** NeuroImage 2009

The continuous model's invertibility does not remove the need to inspect numerical Jacobians.

</details>

---

<a id="c18"></a>
#### VoxelMorph: A Learning Framework for Deformable Medical Image Registration (IEEE TMI 2019)

[`T5`](#t5)

[![arXiv: 1809.05231](https://img.shields.io/badge/arXiv-1809.05231-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1809.05231) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://voxelmorph.csail.mit.edu/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/voxelmorph/voxelmorph) [![GitHub stars](https://img.shields.io/github/stars/voxelmorph/voxelmorph?style=flat-square&label=stars&color=C58A18)](https://github.com/voxelmorph/voxelmorph/stargazers) [![GitHub forks](https://img.shields.io/github/forks/voxelmorph/voxelmorph?style=flat-square&label=forks&color=64748B)](https://github.com/voxelmorph/voxelmorph/forks)

Amortizes pairwise optimization into a network that predicts deformation fields, trained with differentiable warping and image-similarity objectives.

<sub>Author implementation · <a href="https://github.com/voxelmorph/voxelmorph">voxelmorph/voxelmorph</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** MICCAI 2018 / IEEE TMI 2019

Distinguish the baseline displacement-field model from diffeomorphic extensions; performance depends on the training distribution.

</details>

[↑ Back to classics](#classics)

---

### Differentiable sampling and antialiasing

<a id="c25"></a>
#### EWA Volume Splatting (IEEE Visualization 2001)

[`T7`](#t7)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://dash.harvard.edu/bitstream/handle/1/4138240/Zwicker_EWA.pdf) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) ![GitHub: Unverified](https://img.shields.io/badge/GitHub-Unverified-89939E?style=flat-square&logo=github&logoColor=white)

Uses elliptical weighted-average kernels for projected reconstruction and low-pass filtering, providing a classic reference for splat footprints and antialiasing.

<details>
<summary>Limitations and notes</summary>

**Publication history:** IEEE Visualization 2001

This is a volume-rendering operator, not the same operation as 2D optical-flow warping or a complete modern 3DGS system.

</details>

---

<a id="c13"></a>
#### Spatial Transformer Networks (NeurIPS 2015)

[`T7`](#t7)

[![arXiv: 1506.02025](https://img.shields.io/badge/arXiv-1506.02025-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1506.02025) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/1506.02025) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) ![GitHub: Unverified](https://img.shields.io/badge/GitHub-Unverified-89939E?style=flat-square&logo=github&logoColor=white)

Jointly trains transformation prediction, grid generation and differentiable sampling, making spatial transformation a learnable neural-network module.

<details>
<summary>Limitations and notes</summary>

**Publication history:** NeurIPS 2015

The transformation family limits expressiveness. Bilinear sampling does not itself solve occlusion completion or rigorous antialiasing.

</details>

---

<a id="c19"></a>
#### Softmax Splatting for Video Frame Interpolation (CVPR 2020)

[`T7`](#t7)

[![arXiv: 2003.05534](https://img.shields.io/badge/arXiv-2003.05534-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2003.05534) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://sniklaus.com/softsplat) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sniklaus/softmax-splatting) [![GitHub stars](https://img.shields.io/github/stars/sniklaus/softmax-splatting?style=flat-square&label=stars&color=C58A18)](https://github.com/sniklaus/softmax-splatting/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sniklaus/softmax-splatting?style=flat-square&label=forks&color=64748B)](https://github.com/sniklaus/softmax-splatting/forks)

Niklaus and Liu use softmax weighting to resolve many-to-one conflicts in a differentiable forward warp, supporting both image and feature splatting.

<sub>Author implementation · <a href="https://github.com/sniklaus/softmax-splatting">sniklaus/softmax-splatting</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** CVPR 2020

Depends on the flow and importance metric; disocclusion holes still need synthesis or another completion mechanism.

</details>

[↑ Back to classics](#classics)

---

### Feature alignment, animation and 3D deformation

<a id="c28"></a>
#### Depth-image-based rendering (DIBR), compression, and transmission for a new approach on 3D-TV (SPIE 2004)

[`T6`](#t6)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1117/12.524762) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) ![GitHub: Unverified](https://img.shields.io/badge/GitHub-Unverified-89939E?style=flat-square&logo=github&logoColor=white)

Synthesizes virtual views from color and depth, providing a classic route to depth reprojection, visibility reasoning and hole handling. This paper did not originate the general idea of reprojection.

<details>
<summary>Limitations and notes</summary>

**Publication history:** Fehn · SPIE 2004 representative work

Depth discontinuities, disocclusion and projection collisions require dedicated handling.

</details>

---

<a id="c14"></a>
#### Deformable Convolutional Networks (ICCV 2017)

[`T8`](#t8)

[![arXiv: 1703.06211](https://img.shields.io/badge/arXiv-1703.06211-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1703.06211) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/msracver/Deformable-ConvNets) [![GitHub stars](https://img.shields.io/github/stars/msracver/Deformable-ConvNets?style=flat-square&label=stars&color=C58A18)](https://github.com/msracver/Deformable-ConvNets/stargazers) [![GitHub forks](https://img.shields.io/github/forks/msracver/Deformable-ConvNets?style=flat-square&label=forks&color=64748B)](https://github.com/msracver/Deformable-ConvNets/forks)

Learns offsets for convolutional sampling locations, allowing features to adapt to local geometric variation.

<sub>Author implementation · <a href="https://github.com/msracver/Deformable-ConvNets">msracver/Deformable-ConvNets</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** ICCV 2017

Offsets are associated with individual kernel samples and are not equivalent to one physically meaningful global motion field.

</details>

---

<a id="c24"></a>
#### Toward Characteristic-Preserving Image-based Virtual Try-On Network (ECCV 2018)

[`T2`](#t2) [`T9`](#t9)

[![arXiv: 1807.07688](https://img.shields.io/badge/arXiv-1807.07688-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1807.07688) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/1807.07688) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sergeywong/cp-vton) [![GitHub stars](https://img.shields.io/github/stars/sergeywong/cp-vton?style=flat-square&label=stars&color=C58A18)](https://github.com/sergeywong/cp-vton/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sergeywong/cp-vton?style=flat-square&label=forks&color=64748B)](https://github.com/sergeywong/cp-vton/forks)

Learns a TPS with a geometric matching module to align an in-shop garment with a person, then learns a composition mask.

<sub>Reimplementation, as described by the repository · <a href="https://github.com/sergeywong/cp-vton">sergeywong/cp-vton</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** ECCV 2018

TPS has limited capacity for large pose changes, complex occlusion and fine clothing details.

</details>

---

<a id="c16"></a>
#### Digging Into Self-Supervised Monocular Depth Estimation (ICCV 2019)

[`T6`](#t6)

[![arXiv: 1806.01260](https://img.shields.io/badge/arXiv-1806.01260-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1806.01260) ![Project: Unverified](https://img.shields.io/badge/Project-Unverified-89939E?style=flat-square) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nianticlabs/monodepth2) [![GitHub stars](https://img.shields.io/github/stars/nianticlabs/monodepth2?style=flat-square&label=stars&color=C58A18)](https://github.com/nianticlabs/monodepth2/stargazers) [![GitHub forks](https://img.shields.io/github/forks/nianticlabs/monodepth2?style=flat-square&label=forks&color=64748B)](https://github.com/nianticlabs/monodepth2/forks)

Uses depth, pose and differentiable reprojection for self-supervised view reconstruction, introducing minimum reprojection loss and automasking.

<sub>Author implementation · <a href="https://github.com/nianticlabs/monodepth2">nianticlabs/monodepth2</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** ICCV 2019 · preprint 2018

A depth-estimation system rather than a standalone warp operator; dynamic objects, reflections and unobserved regions remain challenges.

</details>

---

<a id="c17"></a>
#### First Order Motion Model for Image Animation (NeurIPS 2019)

[`T8`](#t8) [`T9`](#t9)

[![arXiv: 2003.00196](https://img.shields.io/badge/arXiv-2003.00196-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2003.00196) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2003.00196) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://aliaksandrsiarohin.github.io/first-order-model-website/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AliaksandrSiarohin/first-order-model) [![GitHub stars](https://img.shields.io/github/stars/AliaksandrSiarohin/first-order-model?style=flat-square&label=stars&color=C58A18)](https://github.com/AliaksandrSiarohin/first-order-model/stargazers) [![GitHub forks](https://img.shields.io/github/forks/AliaksandrSiarohin/first-order-model?style=flat-square&label=forks&color=64748B)](https://github.com/AliaksandrSiarohin/first-order-model/forks)

Learns keypoints and local first-order affine motion to construct dense feature warps and occlusion maps for image animation.

<sub>Author implementation · <a href="https://github.com/AliaksandrSiarohin/first-order-model">AliaksandrSiarohin/first-order-model</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** NeurIPS 2019 · arXiv 2020

Large identity differences, rotations and disocclusions remain difficult.

[Publication / primary source](https://papers.nips.cc/paper/8935-first-order-motion-model-for-image-animation.pdf)

</details>

---

<a id="c21"></a>
#### D-NeRF: Neural Radiance Fields for Dynamic Scenes (CVPR 2021)

[`T8`](#t8)

[![arXiv: 2011.13961](https://img.shields.io/badge/arXiv-2011.13961-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2011.13961) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://www.albertpumarola.com/research/D-NeRF/index.html) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/albertpumarola/D-NeRF) [![GitHub stars](https://img.shields.io/github/stars/albertpumarola/D-NeRF?style=flat-square&label=stars&color=C58A18)](https://github.com/albertpumarola/D-NeRF/stargazers) [![GitHub forks](https://img.shields.io/github/forks/albertpumarola/D-NeRF?style=flat-square&label=forks&color=64748B)](https://github.com/albertpumarola/D-NeRF/forks)

Learns time-conditioned deformation that maps dynamic-scene coordinates into a canonical radiance field.

<sub>Author implementation · <a href="https://github.com/albertpumarola/D-NeRF">albertpumarola/D-NeRF</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** CVPR 2021 · preprint 2020

Monocular reconstruction is ambiguous; dynamic detail and training efficiency are limited.

</details>

---

<a id="c22"></a>
#### Nerfies: Deformable Neural Radiance Fields (ICCV 2021)

[`T8`](#t8)

[![arXiv: 2011.12948](https://img.shields.io/badge/arXiv-2011.12948-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2011.12948) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2011.12948) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://nerfies.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/google/nerfies) [![GitHub stars](https://img.shields.io/github/stars/google/nerfies?style=flat-square&label=stars&color=C58A18)](https://github.com/google/nerfies/stargazers) [![GitHub forks](https://img.shields.io/github/forks/google/nerfies?style=flat-square&label=forks&color=64748B)](https://github.com/google/nerfies/forks)

Combines continuous 3D deformation, elastic regularization and coarse-to-fine optimization to reconstruct casually captured nonrigid scenes.

<sub>Author implementation · <a href="https://github.com/google/nerfies">google/nerfies</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** ICCV 2021 · preprint 2020

Continuous canonical warps struggle with topology changes, and optimization may reach local minima.

</details>

---

<a id="c23"></a>
#### HyperNeRF: A Higher-Dimensional Representation for Topologically Varying Neural Radiance Fields (SIGGRAPH Asia / TOG 2021)

[`T8`](#t8)

[![arXiv: 2106.13228](https://img.shields.io/badge/arXiv-2106.13228-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2106.13228) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://hypernerf.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/google/hypernerf) [![GitHub stars](https://img.shields.io/github/stars/google/hypernerf?style=flat-square&label=stars&color=C58A18)](https://github.com/google/hypernerf/stargazers) [![GitHub forks](https://img.shields.io/github/forks/google/hypernerf?style=flat-square&label=forks&color=64748B)](https://github.com/google/hypernerf/forks)

Lifts the representation into a higher-dimensional space and uses slices to model topology changes beyond ordinary continuous 3D warps.

<sub>Author implementation · <a href="https://github.com/google/hypernerf">google/hypernerf</a></sub>

<details>
<summary>Limitations and notes</summary>

**Publication history:** SIGGRAPH Asia / TOG 2021

The higher-dimensional representation is not an everywhere-invertible deformation of ordinary 3D space.

</details>

[↑ Back to classics](#classics)

---


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

Please include the **paper title, publication year/status, Paper, Project, GitHub, technique family and application area**. Leave unavailable links empty, and distinguish author implementations, third-party reimplementations and shared frameworks.

Edit [the bilingual catalog](data/catalog.json) and run `python3 scripts/build_readme.py` to update both READMEs. Counts and indexes use the same data; check consistency with `python3 scripts/build_readme.py --check`.

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
