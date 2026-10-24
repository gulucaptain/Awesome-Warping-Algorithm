<!-- Generated from data/catalog.json by scripts/build_readme.py. -->
<a id="top"></a>

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/warping-banner-dark.svg">
  <img src="assets/warping-banner-light.svg" alt="Awesome Warping Algorithms — from geometric maps to generative motion; a regular grid becomes a deformed coordinate field" width="100%">
</picture>

# Awesome Warping Algorithms

**Geometry · Correspondence · Resampling · Generative Motion**

从经典几何变换到生成式运动控制，按 **基础技术 × 应用领域** 探索 Warping。

[![Works: 57](https://img.shields.io/badge/Works-57-243247?style=flat-square)](#recent) [![Classics: 29](https://img.shields.io/badge/Classics-29-64748B?style=flat-square)](#classics) [![Recent: 28](https://img.shields.io/badge/Recent-28-087F8C?style=flat-square)](#recent) [![GitHub repos: 37](https://img.shields.io/badge/GitHub%20repos-37-2563EB?style=flat-square)](#topics)

**[基础技术](#technology)** · **[应用领域](#topics)** · **[2022–2026](#recent)** · **[经典方法](#classics)** · **[研究指南](docs/RESEARCH_GUIDE.zh-CN.md)**

<sub>更新于 2026-10-24 · 中文导读 / English paper titles · 持续维护的研究地图</sub>

</div>

---

<a id="start"></a>
## 从这里开始

| 想了解什么？ | 阅读入口 |
| --- | --- |
| **Warping 的基础与实现** | [TPS](#c05) → [MLS](#c08) → [STN](#c13) → [Softmax Splatting](#c19) |
| **运动估计与视频对齐** | [PWC-Net](#c15) → [RAFT](#c20) → [GMFlow](#n01) → [SEA-RAFT](#n13) → [MEMFOF](#n20) |
| **三维形变与动态场景** | [D-NeRF](#c21) → [Nerfies](#c22) → [Deformable 3D Gaussians](#n11) → [4D-GS](#n12) |
| **扩散模型与运动控制** | [∫-noise](#n16) → [Go-with-the-Flow](#n19) → [CameraNoise](#n24) · [GenWarp](#n15) → [SplatDiff](#n23) |

**资源图例**　蓝色 **Paper**：原论文 · 青色 **Project**：作者项目/文档 · 深色 **GitHub**：代码 · **Stars / Forks**：该代码仓库的动态计数。

<sub>灰色「未核实」表示尚无已核验的对应入口，不表示资源一定不存在。复现代码与通用实现框架会单独标注；框架计数属于整个仓库。Stars / Forks 由 Shields.io 提供并有缓存，不作为论文质量排名。</sub>

<details>
<summary><b>收录范围与年份口径</b></summary>

以计算机视觉、图形学和医学图像中的**空间 warping** 为主。区分变换模型、对应估计、采样算子及其应用系统；DTW 时间序列对齐和 GPU warp 不在本目录内。

“经典”指截至 2021 年的工作；2022–2026 按代表性正式发表年份整理，并保留早期预印本说明。2026 年覆盖截至 2026-10-24 的公开资料。方法贡献和局限来自原论文、作者资料与原版调研；本合集未对所有实现做统一复现。

[完整定义、Forward / Backward 与核验原则 →](docs/RESEARCH_GUIDE.zh-CN.md#scope)

</details>

<a id="technology"></a>
## 基础技术 · Technology map

一种方法可以跨多个技术族；点击方法名直达条目，条目的 `T1–T9` 标签可返回本表。

<details>
<summary><b>展开 9 类基础技术与文献索引</b></summary>

| 技术族 | 核心表示 | 文献入口 |
| --- | --- | --- |
| <a id="t1"></a>**T1 · 参数化几何变换** | 刚体 / 相似 / 仿射 / 单应性 | [Rigid / Similarity / Affine / Homography](#c01) · [Lucas–Kanade / Inverse Compositional](#c02) · [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) |
| <a id="t2"></a>**T2 · 控制点、样条与连续插值** | TPS / RBF / FFD / B-spline / MLS | [Free-Form Deformation (FFD)](#c04) · [Thin-Plate Spline (TPS) / Principal Warps](#c05) · [Beier–Neely Feature-Based Morphing](#c06) · [B-spline FFD Registration](#c07) · [Moving Least Squares (MLS)](#c08) · [CP-VTON](#c24) · [Thin-Plate Spline Motion Model for Image Animation](#n03) · [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) · [StabStitch](#n28) · [WarpI2I](#n26) |
| <a id="t3"></a>**T3 · 网格与局部形状保持** | 分片变换 / ARAP / 局部投影 | [As-Rigid-As-Possible (ARAP) Surface Modeling](#c09) · [Content-Preserving Warps for 3D Video Stabilization](#c29) · [As-Projective-As-Possible (APAP) / Moving DLT](#c12) · [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) · [StabStitch](#n28) |
| <a id="t4"></a>**T4 · 稠密对应与光流** | 稠密 flow / 相关体 / 全局匹配 | [Lucas–Kanade / Inverse Compositional](#c02) · [Horn–Schunck](#c03) · [Brox et al. Variational Optical Flow](#c27) · [PWC-Net](#c15) · [RAFT](#c20) · [GMFlow](#n01) · [FlowFormer](#n02) · [FILM: Frame Interpolation for Large Motion](#n04) · [BasicVSR++](#n07) · [UniMatch: Unifying Flow, Stereo and Depth Estimation](#n09) · [SEA-RAFT](#n13) · [MEMFOF](#n20) |
| <a id="t5"></a>**T5 · 可逆形变与医学配准** | 速度场 / 微分同胚 / 逆一致性 | [B-spline FFD Registration](#c07) · [LDDMM / Geodesic Flows of Diffeomorphisms](#c26) · [SyN: Symmetric Diffeomorphic Registration](#c10) · [Diffeomorphic Demons](#c11) · [VoxelMorph](#c18) · [TransMorph](#n05) · [SynthMorph](#n06) · [uniGradICON](#n14) |
| <a id="t6"></a>**T6 · 深度与三维重投影** | 深度 / 相机位姿 / 投影与可见性 | [Depth-Image-Based Rendering (DIBR)](#c28) · [Monodepth2](#c16) · [UniMatch: Unifying Flow, Stereo and Depth Estimation](#n09) · [GenWarp](#n15) · [WAVE: Warp-Based View Guidance](#n22) · [SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion](#n23) · [CameraNoise](#n24) · [Warp-as-History](#n27) |
| <a id="t7"></a>**T7 · 可微采样与 Splatting** | 插值 / 核足迹 / 冲突聚合 / 伴随 | [EWA Volume Splatting](#c25) · [Spatial Transformer Networks (STN)](#c13) · [Softmax Splatting](#c19) · [ImWIP](#n10) · [How I Warped Your Noise / ∫-noise](#n16) · [LookingGlass / Laplacian Pyramid Warping (LPW)](#n21) · [SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion](#n23) |
| <a id="t8"></a>**T8 · 学习式特征与三维形变** | Offset / 局部仿射 / Canonical field | [Deformable ConvNets (DCN)](#c14) · [First Order Motion Model (FOMM)](#c17) · [D-NeRF](#c21) · [Nerfies](#c22) · [HyperNeRF](#c23) · [Thin-Plate Spline Motion Model for Image Animation](#n03) · [FILM: Frame Interpolation for Large Motion](#n04) · [BasicVSR++](#n07) · [Deformable 3D Gaussians](#n11) · [4D Gaussian Splatting for Real-Time Dynamic Scene Rendering](#n12) |
| <a id="t9"></a>**T9 · 生成式、频率与随机场** | 几何生成融合 / Noise transport / 频率处理 | [CP-VTON](#c24) · [First Order Motion Model (FOMM)](#c17) · [GenWarp](#n15) · [How I Warped Your Noise / ∫-noise](#n16) · [Warped Diffusion](#n17) · [StableVITON](#n18) · [Go-with-the-Flow](#n19) · [LookingGlass / Laplacian Pyramid Warping (LPW)](#n21) · [WAVE: Warp-Based View Guidance](#n22) · [SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion](#n23) · [CameraNoise](#n24) · [DMAligner](#n25) · [WarpI2I](#n26) · [Warp-as-History](#n27) |

</details>

<a id="topics"></a>
## 应用领域 · Topic index

<details>
<summary><b>展开 16 个应用领域与文献索引</b></summary>

| Topic / 领域 | 关注的问题 | 文献入口 |
| --- | --- | --- |
| <a id="topic-01"></a>**图像配准**<br>Registration | 两幅图的空间对齐 | [Rigid / Similarity / Affine / Homography](#c01) · [Lucas–Kanade / Inverse Compositional](#c02) · [Thin-Plate Spline (TPS) / Principal Warps](#c05) · [B-spline FFD Registration](#c07) · [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) · [DMAligner](#n25) |
| <a id="topic-02"></a>**医学图像**<br>Medical imaging | 三维器官、跨模态与跨个体配准 | [LDDMM / Geodesic Flows of Diffeomorphisms](#c26) · [SyN: Symmetric Diffeomorphic Registration](#c10) · [Diffeomorphic Demons](#c11) · [VoxelMorph](#c18) · [TransMorph](#n05) · [SynthMorph](#n06) · [uniGradICON](#n14) |
| <a id="topic-03"></a>**拼接与全景**<br>Stitching | 对齐重叠区，同时控制非重叠区畸变 | [Rigid / Similarity / Affine / Homography](#c01) · [As-Projective-As-Possible (APAP) / Moving DLT](#c12) · [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) |
| <a id="topic-04"></a>**视频稳像与在线拼接**<br>Stabilization | 抑制相机抖动和逐帧 warp 的时间不一致 | [Content-Preserving Warps for 3D Video Stabilization](#c29) · [StabStitch](#n28) |
| <a id="topic-05"></a>**光流与稠密对应**<br>Optical flow | 寻找跨帧像素对应，生成可供 warp 使用的 flow | [Lucas–Kanade / Inverse Compositional](#c02) · [Horn–Schunck](#c03) · [Brox et al. Variational Optical Flow](#c27) · [PWC-Net](#c15) · [RAFT](#c20) · [GMFlow](#n01) · [FlowFormer](#n02) · [UniMatch: Unifying Flow, Stereo and Depth Estimation](#n09) · [SEA-RAFT](#n13) · [MEMFOF](#n20) |
| <a id="topic-06"></a>**视频插帧**<br>Frame interpolation | 构造中间时刻，对冲突和反遮挡进行处理 | [Softmax Splatting](#c19) · [FILM: Frame Interpolation for Large Motion](#n04) |
| <a id="topic-07"></a>**视频复原**<br>Video restoration | 对齐并融合跨帧信息 | [Deformable ConvNets (DCN)](#c14) · [PWC-Net](#c15) · [RAFT](#c20) · [BasicVSR++](#n07) · [Warped Diffusion](#n17) |
| <a id="topic-08"></a>**图像编辑与形状操控**<br>Image editing | 由点、线或网格控制局部形变 | [Free-Form Deformation (FFD)](#c04) · [Thin-Plate Spline (TPS) / Principal Warps](#c05) · [Beier–Neely Feature-Based Morphing](#c06) · [Moving Least Squares (MLS)](#c08) · [As-Rigid-As-Possible (ARAP) Surface Modeling](#c09) · [LookingGlass / Laplacian Pyramid Warping (LPW)](#n21) · [WarpI2I](#n26) |
| <a id="topic-09"></a>**人物动画与运动迁移**<br>Animation | 从 driving motion 驱动 source appearance | [First Order Motion Model (FOMM)](#c17) · [Thin-Plate Spline Motion Model for Image Animation](#n03) · [Go-with-the-Flow](#n19) |
| <a id="topic-10"></a>**虚拟试衣**<br>Virtual try-on | 服装到人体的对齐，保持纹理与标识 | [CP-VTON](#c24) · [StableVITON](#n18) |
| <a id="topic-11"></a>**深度与多视图几何**<br>Multi-view geometry | 由几何约束建立跨视图对应 | [Rigid / Similarity / Affine / Homography](#c01) · [Monodepth2](#c16) · [UniMatch: Unifying Flow, Stereo and Depth Estimation](#n09) |
| <a id="topic-12"></a>**新视角合成**<br>Novel view synthesis | 相机改变后的几何投影与内容补全 | [Depth-Image-Based Rendering (DIBR)](#c28) · [Monodepth2](#c16) · [D-NeRF](#c21) · [Nerfies](#c22) · [GenWarp](#n15) · [WAVE: Warp-Based View Guidance](#n22) · [SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion](#n23) |
| <a id="topic-13"></a>**动态三维与4D重建**<br>Dynamic 3D / 4D | 将时间变化映射到 canonical representation | [D-NeRF](#c21) · [Nerfies](#c22) · [HyperNeRF](#c23) · [Deformable 3D Gaussians](#n11) · [4D Gaussian Splatting for Real-Time Dynamic Scene Rendering](#n12) |
| <a id="topic-14"></a>**视频扩散与运动控制**<br>Video diffusion | 将运动或几何约束传递给生成模型 | [Softmax Splatting](#c19) · [RAFT](#c20) · [How I Warped Your Noise / ∫-noise](#n16) · [Go-with-the-Flow](#n19) · [CameraNoise](#n24) · [Warp-as-History](#n27) |
| <a id="topic-15"></a>**计算成像与逆问题**<br>Inverse problems | 把 motion warp 纳入测量算子与梯度计算 | [B-spline FFD Registration](#c07) · [Spatial Transformer Networks (STN)](#c13) · [ImWIP](#n10) · [Warped Diffusion](#n17) |
| <a id="topic-16"></a>**投影艺术与视觉幻象**<br>Anamorphosis | 通过镜面、透镜或视角变换产生不同解释 | [Beier–Neely Feature-Based Morphing](#c06) · [EWA Volume Splatting](#c25) · [LookingGlass / Laplacian Pyramid Warping (LPW)](#n21) |

</details>

<a id="recent"></a>
## 2022–2026 · Recent developments

**[2026](#year-2026)** · **[2025](#year-2025)** · **[2024](#year-2024)** · **[2023](#year-2023)** · **[2022](#year-2022)**

由近及远浏览。每条保留原始来源、技术标签和一句贡献；详细边界与选型见 [研究指南](docs/RESEARCH_GUIDE.zh-CN.md#recent)。

<a id="year-2026"></a>
### 2026 · 4 works

<a id="n24"></a>
#### CameraNoise

****ICML 2026，PMLR 正式论文**** · [`T6`](#t6) [`T9`](#t9)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://proceedings.mlr.press/v306/zhao26l.html) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://gulucaptain.github.io/CameraNoise/) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/gulucaptain/CameraNoise) [![GitHub stars](https://img.shields.io/github/stars/gulucaptain/CameraNoise?style=flat-square&label=stars&color=C58A18)](https://github.com/gulucaptain/CameraNoise/stargazers) [![GitHub forks](https://img.shields.io/github/forks/gulucaptain/CameraNoise?style=flat-square&label=forks&color=64748B)](https://github.com/gulucaptain/CameraNoise/forks)

以 Geometry-guided Reprojection Flow 与噪声 warping 将相机运动编码到时序相关噪声中，同时关注 Gaussian 先验与轨迹控制。

<sub>作者实现 · <a href="https://github.com/gulucaptain/CameraNoise">gulucaptain/CameraNoise</a></sub>

<details>
<summary>方法边界与备注</summary>

效果依赖场景几何和运动估计；不能据此推导任意非刚性运动均可精确控制

</details>

<a id="n25"></a>
#### DMAligner

**2026；arXiv v2 注明 **CVPR 2026 接收**** · [`T9`](#t9)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2602.23022) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://boomluo02.github.io/DMAligner/) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/boomluo02/DMAligner) [![GitHub stars](https://img.shields.io/github/stars/boomluo02/DMAligner?style=flat-square&label=stars&color=C58A18)](https://github.com/boomluo02/DMAligner/stargazers) [![GitHub forks](https://img.shields.io/github/forks/boomluo02/DMAligner?style=flat-square&label=forks&color=64748B)](https://github.com/boomluo02/DMAligner/forks)

将图像对齐转为 diffusion-based view synthesis，以动态感知训练处理遮挡与光照变化。

<sub>作者实现 · <a href="https://github.com/boomluo02/DMAligner">boomluo02/DMAligner</a></sub>

<details>
<summary>方法边界与备注</summary>

是对传统 flow warp 局限的生成式替代路线；合成对齐不等同于恢复真实逐像素对应

</details>

<a id="n26"></a>
#### WarpI2I

**2026；arXiv 注明 **ECCV 2026**** · [`T2`](#t2) [`T9`](#t9)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2606.31018) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://shenzheng2000.github.io/WarpI2I.github.io/) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/ShenZheng2000/WarpI2I) [![GitHub stars](https://img.shields.io/github/stars/ShenZheng2000/WarpI2I?style=flat-square&label=stars&color=C58A18)](https://github.com/ShenZheng2000/WarpI2I/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ShenZheng2000/WarpI2I?style=flat-square&label=forks&color=64748B)](https://github.com/ShenZheng2000/WarpI2I/forks)

在编码前用 saliency-guided warp 向显著区域分配更多空间表示，处理后 unwarp，改善紧凑 latent 模型的结构保留。

<sub>作者实现 · <a href="https://github.com/ShenZheng2000/WarpI2I">ShenZheng2000/WarpI2I</a></sub>

<details>
<summary>方法边界与备注</summary>

用 warp 分配表示预算，不以运动估计为核心；逆映射受数值采样影响

</details>

<a id="n27"></a>
#### Warp-as-History

****2026 预印本**** · [`T6`](#t6) [`T9`](#t9)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2605.15182) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://yyfz.github.io/warp-as-history/) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/yyfz/Warp-as-History) [![GitHub stars](https://img.shields.io/github/stars/yyfz/Warp-as-History?style=flat-square&label=stars&color=C58A18)](https://github.com/yyfz/Warp-as-History/stargazers) [![GitHub forks](https://img.shields.io/github/forks/yyfz/Warp-as-History?style=flat-square&label=forks&color=64748B)](https://github.com/yyfz/Warp-as-History/forks)

将相机诱导的 warp 作为对齐目标位置的伪历史，结合有效 token 选择利用冻结模型的历史输入通路；另探索单视频 LoRA。

<sub>作者实现 · <a href="https://github.com/yyfz/Warp-as-History">yyfz/Warp-as-History</a></sub>

<details>
<summary>方法边界与备注</summary>

截止本版仅按公开预印本收录；控制能力仍需跨数据与轨迹验证

</details>

[↑ 返回年份导航](#recent)

---

<a id="year-2025"></a>
### 2025 · 5 works

<a id="n19"></a>
#### Go-with-the-Flow

**CVPR 2025** · [`T9`](#t9)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2501.08331) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://eyeline-labs.github.io/Go-with-the-Flow/) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/Eyeline-Labs/Go-with-the-Flow) [![GitHub stars](https://img.shields.io/github/stars/Eyeline-Labs/Go-with-the-Flow?style=flat-square&label=stars&color=C58A18)](https://github.com/Eyeline-Labs/Go-with-the-Flow/stargazers) [![GitHub forks](https://img.shields.io/github/forks/Eyeline-Labs/Go-with-the-Flow?style=flat-square&label=forks&color=64748B)](https://github.com/Eyeline-Labs/Go-with-the-Flow/forks)

高效生成 warped noise 并微调视频模型，把运动模式作为噪声先验，用于运动迁移及相机/物体控制。

<sub>作者实现 · <a href="https://github.com/Eyeline-Labs/Go-with-the-Flow">Eyeline-Labs/Go-with-the-Flow</a></sub>

<details>
<summary>方法边界与备注</summary>

需要相应模型适配；普通 pretrained 模型不必然直接支持相同控制

</details>

<a id="n20"></a>
#### MEMFOF

**ICCV 2025** · [`T4`](#t4)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2506.23151) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://msu-video-group.github.io/memfof/) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/msu-video-group/memfof) [![GitHub stars](https://img.shields.io/github/stars/msu-video-group/memfof?style=flat-square&label=stars&color=C58A18)](https://github.com/msu-video-group/memfof/stargazers) [![GitHub forks](https://img.shields.io/github/forks/msu-video-group/memfof?style=flat-square&label=forks&color=64748B)](https://github.com/msu-video-group/memfof/forks)

精简相关表示并引入多帧估计与高分辨率训练，推进原生 FullHD 光流的显存效率。

<sub>作者实现 · <a href="https://github.com/msu-video-group/memfof">msu-video-group/memfof</a></sub>

<details>
<summary>方法边界与备注</summary>

不是新的采样核；资源数据应按作者指定硬件、精度和分辨率复测

</details>

<a id="n21"></a>
#### LookingGlass / Laplacian Pyramid Warping (LPW)

**CVPR 2025** · [`T7`](#t7) [`T9`](#t9)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2504.08902) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://lookingglass-lpw.github.io/) ![GitHub: 未核实](https://img.shields.io/badge/GitHub-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square)

用 Laplacian 金字塔进行频率感知的图像 warp 与视图聚合，支持多视角生成式 anamorphosis。

<details>
<summary>方法边界与备注</summary>

主要针对多变换生成与频率保真，不直接保证随机噪声统计

</details>

<a id="n22"></a>
#### WAVE: Warp-Based View Guidance

**ICCV 2025** · [`T6`](#t6) [`T9`](#t9)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content/ICCV2025/html/Park_WAVE_Warp-Based_View_Guidance_for_Consistent_Novel_View_Synthesis_Using_ICCV_2025_paper.html) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/jwoo-park0/WAVE) [![GitHub stars](https://img.shields.io/github/stars/jwoo-park0/WAVE?style=flat-square&label=stars&color=C58A18)](https://github.com/jwoo-park0/WAVE/stargazers) [![GitHub forks](https://img.shields.io/github/forks/jwoo-park0/WAVE?style=flat-square&label=forks&color=64748B)](https://github.com/jwoo-park0/WAVE/forks)

用视图 warping 引导自适应 attention 与噪声重新初始化，提高单图新视角一致性，无需额外训练。

<sub>作者实现 · <a href="https://github.com/jwoo-park0/WAVE">jwoo-park0/WAVE</a></sub>

<details>
<summary>方法边界与备注</summary>

依赖基础新视角模型与几何估计；与其他同名 WAVE 工作应区分；作者论文所列项目页在本次核验时返回 404，暂不提供失效入口

</details>

<a id="n23"></a>
#### SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion

**SIGGRAPH 2025** · [`T6`](#t6) [`T7`](#t7) [`T9`](#t9)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2502.12752) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://studios.disneyresearch.com/2025/07/16/splatdiff/) ![GitHub: 未核实](https://img.shields.io/badge/GitHub-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square)

以 pixel splatting 约束目标视角，结合对齐合成与 texture bridge，平衡几何一致性和纹理保真。

<details>
<summary>方法边界与备注</summary>

深度和 splat 错误仍可能传播；生成细节需要单独核验真实性

</details>

[↑ 返回年份导航](#recent)

---

<a id="year-2024"></a>
### 2024 · 9 works

<a id="n11"></a>
#### Deformable 3D Gaussians

**CVPR 2024；预印本 2023** · [`T8`](#t8)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2309.13101) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://ingra14m.github.io/Deformable-Gaussians/) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/ingra14m/Deformable-3D-Gaussians) [![GitHub stars](https://img.shields.io/github/stars/ingra14m/Deformable-3D-Gaussians?style=flat-square&label=stars&color=C58A18)](https://github.com/ingra14m/Deformable-3D-Gaussians/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ingra14m/Deformable-3D-Gaussians?style=flat-square&label=forks&color=64748B)](https://github.com/ingra14m/Deformable-3D-Gaussians/forks)

在 canonical Gaussian 表示上学习形变场，将动态重建与快速 splatting 渲染结合。

<sub>作者实现 · <a href="https://github.com/ingra14m/Deformable-3D-Gaussians">ingra14m/Deformable-3D-Gaussians</a></sub>

<details>
<summary>方法边界与备注</summary>

三维参数形变 + 渲染，不等同于二维图像插值；有逐场景优化需求

</details>

<a id="n12"></a>
#### 4D Gaussian Splatting for Real-Time Dynamic Scene Rendering

**CVPR 2024；预印本 2023** · [`T8`](#t8)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2310.08528) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://guanjunwu.github.io/4dgs/) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/hustvl/4DGaussians) [![GitHub stars](https://img.shields.io/github/stars/hustvl/4DGaussians?style=flat-square&label=stars&color=C58A18)](https://github.com/hustvl/4DGaussians/stargazers) [![GitHub forks](https://img.shields.io/github/forks/hustvl/4DGaussians?style=flat-square&label=forks&color=64748B)](https://github.com/hustvl/4DGaussians/forks)

结合时空特征与 Gaussian 形变，提升动态场景表示的训练、存储及渲染效率。

<sub>作者实现 · <a href="https://github.com/hustvl/4DGaussians">hustvl/4DGaussians</a></sub>

<details>
<summary>方法边界与备注</summary>

此处专指 Wu 等的 4D-GS，不泛指所有名字含 4D Gaussian 的方法

</details>

<a id="n28"></a>
#### StabStitch

**ECCV 2024** · [`T2`](#t2) [`T3`](#t3)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2403.06378) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/nie-lang/StabStitch) [![GitHub stars](https://img.shields.io/github/stars/nie-lang/StabStitch?style=flat-square&label=stars&color=C58A18)](https://github.com/nie-lang/StabStitch/stargazers) [![GitHub forks](https://img.shields.io/github/forks/nie-lang/StabStitch?style=flat-square&label=forks&color=64748B)](https://github.com/nie-lang/StabStitch/forks)

将视频拼接与稳像统一到无监督在线框架，约束空间对齐和时间稳定性，抑制逐帧 warp 抖动。

<sub>作者实现 · <a href="https://github.com/nie-lang/StabStitch">nie-lang/StabStitch</a></sub>

<details>
<summary>方法边界与备注</summary>

图像级对齐好不等于视频稳定；仍需比较延迟、畸变和动态场景效果

</details>

<a id="n13"></a>
#### SEA-RAFT

**ECCV 2024** · [`T4`](#t4)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2405.14793) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/princeton-vl/SEA-RAFT) [![GitHub stars](https://img.shields.io/github/stars/princeton-vl/SEA-RAFT?style=flat-square&label=stars&color=C58A18)](https://github.com/princeton-vl/SEA-RAFT/stargazers) [![GitHub forks](https://img.shields.io/github/forks/princeton-vl/SEA-RAFT?style=flat-square&label=forks&color=64748B)](https://github.com/princeton-vl/SEA-RAFT/forks)

通过初始 flow 回归、混合 Laplace 损失和刚性运动预训练，改善 RAFT 的效率与精度。

<sub>作者实现 · <a href="https://github.com/princeton-vl/SEA-RAFT">princeton-vl/SEA-RAFT</a></sub>

<details>
<summary>方法边界与备注</summary>

属于对应估计的工程与建模改进；效果依赖评测协议

</details>

<a id="n14"></a>
#### uniGradICON

**MICCAI 2024** · [`T5`](#t5)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://papers.miccai.org/miccai-2024/816-Paper0527.html) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/uncbiag/uniGradICON) [![GitHub stars](https://img.shields.io/github/stars/uncbiag/uniGradICON?style=flat-square&label=stars&color=C58A18)](https://github.com/uncbiag/uniGradICON/stargazers) [![GitHub forks](https://img.shields.io/github/forks/uncbiag/uniGradICON?style=flat-square&label=forks&color=64748B)](https://github.com/uncbiag/uniGradICON/forks)

将学习式配准推进到多数据集、跨解剖区域和新任务的通用初始化与零样本使用。

<sub>作者实现 · <a href="https://github.com/uncbiag/uniGradICON">uncbiag/uniGradICON</a></sub>

<details>
<summary>方法边界与备注</summary>

泛化并非对任意模态、任意器官的保证

</details>

<a id="n15"></a>
#### GenWarp

**NeurIPS 2024** · [`T6`](#t6) [`T9`](#t9)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://proceedings.neurips.cc/paper_files/paper/2024/hash/92e886487a8354b03d8bf4416eae6d7d-Abstract-Conference.html) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://genwarp-nvs.github.io/) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/sony/genwarp) [![GitHub stars](https://img.shields.io/github/stars/sony/genwarp?style=flat-square&label=stars&color=C58A18)](https://github.com/sony/genwarp/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sony/genwarp?style=flat-square&label=forks&color=64748B)](https://github.com/sony/genwarp/forks)

结合深度诱导的坐标信息与跨视图/自注意力，让模型学习保留可迁移内容并生成缺失部分。

<sub>作者实现 · <a href="https://github.com/sony/genwarp">sony/genwarp</a></sub>

<details>
<summary>方法边界与备注</summary>

属于 generative warping，生成区域并非从源图精确搬运

</details>

<a id="n16"></a>
#### How I Warped Your Noise / ∫-noise

**ICLR 2024** · [`T7`](#t7) [`T9`](#t9)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openreview.net/pdf?id=pzElnMrgSD) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://warpyournoise.github.io/) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/mskwak01/How-I-Warped-Your-Noise-Unofficial) [![GitHub stars](https://img.shields.io/github/stars/mskwak01/How-I-Warped-Your-Noise-Unofficial?style=flat-square&label=stars&color=C58A18)](https://github.com/mskwak01/How-I-Warped-Your-Noise-Unofficial/stargazers) [![GitHub forks](https://img.shields.io/github/forks/mskwak01/How-I-Warped-Your-Noise-Unofficial?style=flat-square&label=forks&color=64748B)](https://github.com/mskwak01/How-I-Warped-Your-Noise-Unofficial/forks)

把像素噪声解释为连续白噪声场的区域积分，设计面向 Gaussian 统计的输运，兼顾运动相关性和噪声性质。

<sub>非官方复现 · <a href="https://github.com/mskwak01/How-I-Warped-Your-Noise-Unofficial">mskwak01/How-I-Warped-Your-Noise-Unofficial</a></sub>

<details>
<summary>方法边界与备注</summary>

与普通 RGB 插值目标不同；会议早于 **2025** arXiv 上传，不能按该 ID 误判为 2025 首发

</details>

<a id="n17"></a>
#### Warped Diffusion

**NeurIPS 2024** · [`T9`](#t9)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2410.16152) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://giannisdaras.github.io/warped_diffusion.github.io/) ![GitHub: 未核实](https://img.shields.io/badge/GitHub-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square)

用连续函数空间和变换等变性处理视频逆问题，以测试时自等变引导提高时序一致性。

<details>
<summary>方法边界与备注</summary>

不是仅对初始化噪声做一次 warp；关注视频补全与超分

</details>

<a id="n18"></a>
#### StableVITON

**CVPR 2024；预印本 2023** · [`T9`](#t9)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2312.01725) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/rlawjdghek/StableVITON) [![GitHub stars](https://img.shields.io/github/stars/rlawjdghek/StableVITON?style=flat-square&label=stars&color=C58A18)](https://github.com/rlawjdghek/StableVITON/stargazers) [![GitHub forks](https://img.shields.io/github/forks/rlawjdghek/StableVITON?style=flat-square&label=forks&color=64748B)](https://github.com/rlawjdghek/StableVITON/forks)

在扩散 latent 中学习服装与人体的语义对应，以 attention 实现隐式对齐与细节传递。

<sub>作者实现 · <a href="https://github.com/rlawjdghek/StableVITON">rlawjdghek/StableVITON</a></sub>

<details>
<summary>方法边界与备注</summary>

不应与显式 TPS/flow 坐标 warp 直接视作相同算子

</details>

[↑ 返回年份导航](#recent)

---

<a id="year-2023"></a>
### 2023 · 3 works

<a id="n08"></a>
#### UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching

**ICCV 2023** · [`T1`](#t1) [`T2`](#t2) [`T3`](#t3)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2302.08207) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/nie-lang/UDIS2) [![GitHub stars](https://img.shields.io/github/stars/nie-lang/UDIS2?style=flat-square&label=stars&color=C58A18)](https://github.com/nie-lang/UDIS2/stargazers) [![GitHub forks](https://img.shields.io/github/forks/nie-lang/UDIS2?style=flat-square&label=forks&color=64748B)](https://github.com/nie-lang/UDIS2/forks)

全局 homography + 局部 TPS，联合考虑重叠区对齐、非重叠区形状与接缝合成。

<sub>作者实现 · <a href="https://github.com/nie-lang/UDIS2">nie-lang/UDIS2</a></sub>

<details>
<summary>方法边界与备注</summary>

对大视差的容忍不意味着解决所有三维遮挡

</details>

<a id="n09"></a>
#### UniMatch: Unifying Flow, Stereo and Depth Estimation

**TPAMI 2023** · [`T4`](#t4) [`T6`](#t6)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2211.05783) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://haofeixu.github.io/unimatch/) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/autonomousvision/unimatch) [![GitHub stars](https://img.shields.io/github/stars/autonomousvision/unimatch?style=flat-square&label=stars&color=C58A18)](https://github.com/autonomousvision/unimatch/stargazers) [![GitHub forks](https://img.shields.io/github/forks/autonomousvision/unimatch?style=flat-square&label=forks&color=64748B)](https://github.com/autonomousvision/unimatch/forks)

把 flow、双目视差与有位姿的跨视图深度统一为对应匹配任务。

<sub>作者实现 · <a href="https://github.com/autonomousvision/unimatch">autonomousvision/unimatch</a></sub>

<details>
<summary>方法边界与备注</summary>

预印本 **2022**；输出、几何约束和细化仍随任务变化

</details>

<a id="n10"></a>
#### ImWIP

**SoftwareX 2023** · [`T7`](#t7)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1016/j.softx.2023.101524) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://imwip.readthedocs.io/en/latest/) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/RendersJens/ImWIP) [![GitHub stars](https://img.shields.io/github/stars/RendersJens/ImWIP?style=flat-square&label=stars&color=C58A18)](https://github.com/RendersJens/ImWIP/stargazers) [![GitHub forks](https://img.shields.io/github/forks/RendersJens/ImWIP?style=flat-square&label=forks&color=64748B)](https://github.com/RendersJens/ImWIP/forks)

提供可微图像 warp 及其精确离散伴随与导数，服务逆问题优化。

<sub>作者实现 · <a href="https://github.com/RendersJens/ImWIP">RendersJens/ImWIP</a></sub>

<details>
<summary>方法边界与备注</summary>

伴随 `Wᵀ` 不等于逆 warp；精确性针对选定离散算子和浮点精度

</details>

[↑ 返回年份导航](#recent)

---

<a id="year-2022"></a>
### 2022 · 7 works

<a id="n01"></a>
#### GMFlow

**CVPR 2022** · [`T4`](#t4)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2111.13680) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/haofeixu/gmflow) [![GitHub stars](https://img.shields.io/github/stars/haofeixu/gmflow?style=flat-square&label=stars&color=C58A18)](https://github.com/haofeixu/gmflow/stargazers) [![GitHub forks](https://img.shields.io/github/forks/haofeixu/gmflow?style=flat-square&label=forks&color=64748B)](https://github.com/haofeixu/gmflow/forks)

Transformer 增强跨图特征，以全局匹配生成 flow，减少对大量顺序迭代的依赖。

<sub>作者实现 · <a href="https://github.com/haofeixu/gmflow">haofeixu/gmflow</a></sub>

<details>
<summary>方法边界与备注</summary>

改进 flow 估计而非重采样核；预印本 **2021**

</details>

<a id="n02"></a>
#### FlowFormer

**ECCV 2022** · [`T4`](#t4)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2203.16194) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://drinkingcoder.github.io/publication/flowformer/) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/drinkingcoder/FlowFormer-Official) [![GitHub stars](https://img.shields.io/github/stars/drinkingcoder/FlowFormer-Official?style=flat-square&label=stars&color=C58A18)](https://github.com/drinkingcoder/FlowFormer-Official/stargazers) [![GitHub forks](https://img.shields.io/github/forks/drinkingcoder/FlowFormer-Official?style=flat-square&label=forks&color=64748B)](https://github.com/drinkingcoder/FlowFormer-Official/forks)

对 4D cost volume 进行 Transformer 编码，并通过循环解码更新运动。

<sub>作者实现 · <a href="https://github.com/drinkingcoder/FlowFormer-Official">drinkingcoder/FlowFormer-Official</a></sub>

<details>
<summary>方法边界与备注</summary>

需要关注相关表示和高分辨率显存开销

</details>

<a id="n03"></a>
#### Thin-Plate Spline Motion Model for Image Animation

**CVPR 2022** · [`T2`](#t2) [`T8`](#t8)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content/CVPR2022/html/Zhao_Thin-Plate_Spline_Motion_Model_for_Image_Animation_CVPR_2022_paper.html) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/yoyo-nb/Thin-Plate-Spline-Motion-Model) [![GitHub stars](https://img.shields.io/github/stars/yoyo-nb/Thin-Plate-Spline-Motion-Model?style=flat-square&label=stars&color=C58A18)](https://github.com/yoyo-nb/Thin-Plate-Spline-Motion-Model/stargazers) [![GitHub forks](https://img.shields.io/github/forks/yoyo-nb/Thin-Plate-Spline-Motion-Model?style=flat-square&label=forks&color=64748B)](https://github.com/yoyo-nb/Thin-Plate-Spline-Motion-Model/forks)

从局部仿射运动扩展到多个 TPS 变换，并结合多尺度遮挡掩码进行特征形变。

<sub>作者实现 · <a href="https://github.com/yoyo-nb/Thin-Plate-Spline-Motion-Model">yoyo-nb/Thin-Plate-Spline-Motion-Model</a></sub>

<details>
<summary>方法边界与备注</summary>

经典 TPS 的学习式组合，不是新发明 TPS；极端身份差异仍有限

</details>

<a id="n04"></a>
#### FILM: Frame Interpolation for Large Motion

**ECCV 2022** · [`T4`](#t4) [`T8`](#t8)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2202.04901) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://film-net.github.io/) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/google-research/frame-interpolation) [![GitHub stars](https://img.shields.io/github/stars/google-research/frame-interpolation?style=flat-square&label=stars&color=C58A18)](https://github.com/google-research/frame-interpolation/stargazers) [![GitHub forks](https://img.shields.io/github/forks/google-research/frame-interpolation?style=flat-square&label=forks&color=64748B)](https://github.com/google-research/frame-interpolation/forks)

跨尺度共享的特征与运动估计，提高大运动插帧能力；可仅从图像帧训练。

<sub>作者实现 · <a href="https://github.com/google-research/frame-interpolation">google-research/frame-interpolation</a></sub>

<details>
<summary>方法边界与备注</summary>

大反遮挡区域仍需合成；不是单一通用 warp 算子

</details>

<a id="n05"></a>
#### TransMorph

**Medical Image Analysis 2022** · [`T5`](#t5)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2111.10480) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration) [![GitHub stars](https://img.shields.io/github/stars/junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration?style=flat-square&label=stars&color=C58A18)](https://github.com/junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration/stargazers) [![GitHub forks](https://img.shields.io/github/forks/junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration?style=flat-square&label=forks&color=64748B)](https://github.com/junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration/forks)

Transformer–ConvNet 混合模型用于三维医学配准，增强长程空间关系建模。

<sub>作者实现 · <a href="https://github.com/junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration">junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration</a></sub>

<details>
<summary>方法边界与备注</summary>

预印本 **2021**；是否微分同胚取决于具体模型版本

</details>

<a id="n06"></a>
#### SynthMorph

**IEEE TMI 2022（在线发表 2021）** · [`T5`](#t5)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2004.10282) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://w3id.org/synthmorph) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/voxelmorph/voxelmorph) [![GitHub stars](https://img.shields.io/github/stars/voxelmorph/voxelmorph?style=flat-square&label=stars&color=C58A18)](https://github.com/voxelmorph/voxelmorph/stargazers) [![GitHub forks](https://img.shields.io/github/forks/voxelmorph/voxelmorph?style=flat-square&label=forks&color=64748B)](https://github.com/voxelmorph/voxelmorph/forks)

用合成标签和多样图像训练，提升跨 MRI 对比度的形变配准泛化。

<sub>通用实现框架，计数属于整个仓库 · <a href="https://github.com/voxelmorph/voxelmorph">voxelmorph/voxelmorph</a></sub>

<details>
<summary>方法边界与备注</summary>

预印本 **2020**；进步主要来自训练策略与泛化能力

</details>

<a id="n07"></a>
#### BasicVSR++

**CVPR 2022** · [`T4`](#t4) [`T8`](#t8)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content/CVPR2022/html/Chan_BasicVSR_Improving_Video_Super-Resolution_With_Enhanced_Propagation_and_Alignment_CVPR_2022_paper.html) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/ckkelvinchan/BasicVSR_PlusPlus) [![GitHub stars](https://img.shields.io/github/stars/ckkelvinchan/BasicVSR_PlusPlus?style=flat-square&label=stars&color=C58A18)](https://github.com/ckkelvinchan/BasicVSR_PlusPlus/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ckkelvinchan/BasicVSR_PlusPlus?style=flat-square&label=forks&color=64748B)](https://github.com/ckkelvinchan/BasicVSR_PlusPlus/forks)

二阶传播与 flow-guided deformable alignment，把光流先验与可形变特征采样结合。

<sub>作者实现 · <a href="https://github.com/ckkelvinchan/BasicVSR_PlusPlus">ckkelvinchan/BasicVSR_PlusPlus</a></sub>

<details>
<summary>方法边界与备注</summary>

预印本 **2021**；针对视频复原系统

</details>

[↑ 返回年份导航](#recent)

---


<a id="classics"></a>
## Before 2022 · Classical foundations

### 参数化几何与运动估计

<a id="c01"></a>
#### Rigid / Similarity / Affine / Homography

**基础模型** · [`T1`](#t1)

[![Reference: Read](https://img.shields.io/badge/Reference-Read-2563EB?style=flat-square)](https://docs.opencv.org/4.x/d9/dab/tutorial_homography.html) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) ![GitHub: 未核实](https://img.shields.io/badge/GitHub-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square)

从全局刚体到投影变换；单应性可描述平面场景或固定光心纯旋转下的视图关系。

<details>
<summary>方法边界与备注</summary>

通用三维平移、视差与非刚性运动不能由单一矩阵解释

</details>

<a id="c02"></a>
#### Lucas–Kanade / Inverse Compositional

**1981 · IJCV 2004 统一框架** · [`T1`](#t1) [`T4`](#t4)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.ri.cmu.edu/pub_files/pub3/baker_simon_2004_1/baker_simon_2004_1.pdf) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) ![GitHub: 未核实](https://img.shields.io/badge/GitHub-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square)

用图像残差优化 warp 参数；逆组合形式允许复用部分计算，是直接法对齐的重要基础。

<details>
<summary>方法边界与备注</summary>

对初始化、光度假设和局部极小值敏感

</details>

<a id="c03"></a>
#### Horn–Schunck

**1981** · [`T4`](#t4)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1016/0004-3702(81)90024-2) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) ![GitHub: 未核实](https://img.shields.io/badge/GitHub-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square)

亮度一致性与全局平滑正则结合，建立稠密变分光流的经典范式。

<details>
<summary>方法边界与备注</summary>

运动边界易过度平滑；基础形式不适合大位移

</details>

<a id="c27"></a>
#### Brox et al. Variational Optical Flow

**ECCV 2004** · [`T4`](#t4)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.mia.uni-saarland.de/Publications/brox-eccv04-of.pdf) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) ![GitHub: 未核实](https://img.shields.io/badge/GitHub-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square)

结合亮度/梯度一致性和保边正则，为粗到细 warping 的数值求解提供理论解释。

<details>
<summary>方法边界与备注</summary>

强光照变化与严重遮挡会破坏数据假设

</details>

<a id="c15"></a>
#### PWC-Net

**CVPR 2018；预印本 2017** · [`T4`](#t4)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/1709.02371) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/NVlabs/PWC-Net) [![GitHub stars](https://img.shields.io/github/stars/NVlabs/PWC-Net?style=flat-square&label=stars&color=C58A18)](https://github.com/NVlabs/PWC-Net/stargazers) [![GitHub forks](https://img.shields.io/github/forks/NVlabs/PWC-Net?style=flat-square&label=forks&color=64748B)](https://github.com/NVlabs/PWC-Net/forks)

金字塔 + 特征 warping + cost volume，学习粗到细残余运动。

<sub>作者实现 · <a href="https://github.com/NVlabs/PWC-Net">NVlabs/PWC-Net</a></sub>

<details>
<summary>方法边界与备注</summary>

逐层 warping 的误差可能传播；遮挡仍需额外处理

</details>

<a id="c20"></a>
#### RAFT

**ECCV 2020** · [`T4`](#t4)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2003.12039) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/princeton-vl/RAFT) [![GitHub stars](https://img.shields.io/github/stars/princeton-vl/RAFT?style=flat-square&label=stars&color=C58A18)](https://github.com/princeton-vl/RAFT/stargazers) [![GitHub forks](https://img.shields.io/github/forks/princeton-vl/RAFT?style=flat-square&label=forks&color=64748B)](https://github.com/princeton-vl/RAFT/forks)

全像素对相关体与循环更新，成为稠密流估计的重要基线。

<sub>作者实现 · <a href="https://github.com/princeton-vl/RAFT">princeton-vl/RAFT</a></sub>

<details>
<summary>方法边界与备注</summary>

相关体开销随分辨率增加；它估计 flow，不是新的图像插值核

</details>

[↑ 返回经典方法](#classics)

---

### 控制点、样条与局部形状

<a id="c04"></a>
#### Free-Form Deformation (FFD)

**SIGGRAPH 1986** · [`T2`](#t2)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.cse.iitd.ac.in/~jatin/minor_p/papers/sederberg.pdf) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) ![GitHub: 未核实](https://img.shields.io/badge/GitHub-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square)

Sederberg–Parry 通过控制格与 Bernstein 多项式变形几何对象，奠定体积控制形变基础。

<details>
<summary>方法边界与备注</summary>

格分辨率控制细节与复杂度；不自动保证无折叠

</details>

<a id="c05"></a>
#### Thin-Plate Spline (TPS) / Principal Warps

**TPAMI 1989** · [`T2`](#t2)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1109/34.24792) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) ![GitHub: 未核实](https://img.shields.io/badge/GitHub-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square)

Bookstein 将 TPS 用于地标形变分析，以弯曲能量定义平滑非刚性映射；TPS 的数学起源更早。

<details>
<summary>方法边界与备注</summary>

全局支撑、离群控制点和边界外推可能产生不自然形变

</details>

<a id="c06"></a>
#### Beier–Neely Feature-Based Morphing

**SIGGRAPH 1992** · [`T2`](#t2)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://wcours.gel.ulaval.ca/GIF4105/old/h20/tps/tp3/beierneely92.pdf) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) ![GitHub: 未核实](https://img.shields.io/badge/GitHub-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square)

用成对特征线段控制 inverse warp，再结合颜色混合实现 morphing。

<details>
<summary>方法边界与备注</summary>

依赖手工对应；复杂区域可能产生局部扭曲

</details>

<a id="c07"></a>
#### B-spline FFD Registration

**IEEE TMI 1999** · [`T2`](#t2) [`T5`](#t5)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1109/42.796284) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) ![GitHub: 未核实](https://img.shields.io/badge/GitHub-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square)

Rueckert 等将全局仿射与局部 B-spline FFD 结合，用于乳腺 MR 非刚性配准。

<details>
<summary>方法边界与备注</summary>

普通 B-spline FFD 不自动满足微分同胚约束

</details>

<a id="c08"></a>
#### Moving Least Squares (MLS)

**SIGGRAPH / TOG 2006** · [`T2`](#t2)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1145/1141911.1141920) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) ![GitHub: 未核实](https://img.shields.io/badge/GitHub-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square)

Schaefer 等用局部加权拟合构造仿射、相似、刚性图像形变，支持交互控制。

<details>
<summary>方法边界与备注</summary>

权重、控制点布局与外推影响结果；不是全局可逆性的保证

</details>

<a id="c09"></a>
#### As-Rigid-As-Possible (ARAP) Surface Modeling

**SGP 2007** · [`T3`](#t3)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://igl.ethz.ch/projects/ARAP/arap_web.pdf) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://igl.ethz.ch/projects/ARAP/) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/libigl/libigl) [![GitHub stars](https://img.shields.io/github/stars/libigl/libigl?style=flat-square&label=stars&color=C58A18)](https://github.com/libigl/libigl/stargazers) [![GitHub forks](https://img.shields.io/github/forks/libigl/libigl?style=flat-square&label=forks&color=64748B)](https://github.com/libigl/libigl/forks)

Sorkine–Alexa 以局部刚性约束保留形状细节，是网格编辑的经典能量设计。

<sub>通用实现框架，计数属于整个仓库 · <a href="https://github.com/libigl/libigl">libigl/libigl</a></sub>

<details>
<summary>方法边界与备注</summary>

需要网格与优化；大形变仍可能自交

</details>

<a id="c29"></a>
#### Content-Preserving Warps for 3D Video Stabilization

**SIGGRAPH / TOG 2009** · [`T3`](#t3)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://pages.cs.wisc.edu/~fliu/papers/siggraph09.pdf) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://web.cecs.pdx.edu/~fliu/project/3dstab.htm) ![GitHub: 未核实](https://img.shields.io/badge/GitHub-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square)

由三维相机运动与内容保持网格 warp 构造稳定视频，兼顾对齐和显著区域形状。

<details>
<summary>方法边界与备注</summary>

依赖可靠运动重建；裁切、深度差异与残余畸变存在权衡

</details>

<a id="c12"></a>
#### As-Projective-As-Possible (APAP) / Moving DLT

**CVPR 2013** · [`T3`](#t3)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content_cvpr_2013/papers/Zaragoza_As-Projective-As-Possible_Image_Stitching_2013_CVPR_paper.pdf) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) ![GitHub: 未核实](https://img.shields.io/badge/GitHub-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square)

Zaragoza 等允许局部偏离全局投影变换，以适应拼接中的非平面与视差。

<details>
<summary>方法边界与备注</summary>

大视差、重遮挡和非重叠区域的外推仍有挑战

</details>

[↑ 返回经典方法](#classics)

---

### 拓扑保持与医学配准

<a id="c26"></a>
#### LDDMM / Geodesic Flows of Diffeomorphisms

**IJCV 2005** · [`T5`](#t5)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.cs.jhu.edu/~misha/ReadingSeminar/Papers/Beg05.pdf) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://www.cis.jhu.edu/software/lddmm-volume/index.php) ![GitHub: 未核实](https://img.shields.io/badge/GitHub-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square)

Beg 等通过平滑速度场的时间积分与测地流构造大形变微分同胚映射，是计算解剖的重要基础。

<details>
<summary>方法边界与备注</summary>

优化与数值积分成本较高；离散精度和正则尺度影响结果

</details>

<a id="c10"></a>
#### SyN: Symmetric Diffeomorphic Registration

**Medical Image Analysis 2008** · [`T5`](#t5)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2276735/) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/ANTsX/ANTs) [![GitHub stars](https://img.shields.io/github/stars/ANTsX/ANTs?style=flat-square&label=stars&color=C58A18)](https://github.com/ANTsX/ANTs/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ANTsX/ANTs?style=flat-square&label=forks&color=64748B)](https://github.com/ANTsX/ANTs/forks)

对称微分同胚配准，结合互相关用于解剖图像对齐，是 ANTs 的代表性方法。

<sub>通用实现框架，计数属于整个仓库 · <a href="https://github.com/ANTsX/ANTs">ANTsX/ANTs</a></sub>

<details>
<summary>方法边界与备注</summary>

逐对优化成本较高；结果依赖相似度、正则与离散化

</details>

<a id="c11"></a>
#### Diffeomorphic Demons

**NeuroImage 2009** · [`T5`](#t5)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1016/j.neuroimage.2008.10.040) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) ![GitHub: 未核实](https://img.shields.io/badge/GitHub-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square)

在 Demons 框架中使用微分同胚更新，兼顾高效非参数配准与平滑可逆变形。

<details>
<summary>方法边界与备注</summary>

数学模型的可逆性不免除数值 Jacobian 检查

</details>

<a id="c18"></a>
#### VoxelMorph

**MICCAI 2018 / IEEE TMI 2019** · [`T5`](#t5)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/1809.05231) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://voxelmorph.csail.mit.edu/) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/voxelmorph/voxelmorph) [![GitHub stars](https://img.shields.io/github/stars/voxelmorph/voxelmorph?style=flat-square&label=stars&color=C58A18)](https://github.com/voxelmorph/voxelmorph/stargazers) [![GitHub forks](https://img.shields.io/github/forks/voxelmorph/voxelmorph?style=flat-square&label=forks&color=64748B)](https://github.com/voxelmorph/voxelmorph/forks)

将逐对优化摊销为网络预测形变场，结合可微 warp 与图像相似性训练。

<sub>作者实现 · <a href="https://github.com/voxelmorph/voxelmorph">voxelmorph/voxelmorph</a></sub>

<details>
<summary>方法边界与备注</summary>

基础位移场版本与微分同胚扩展应区分；有数据分布依赖

</details>

[↑ 返回经典方法](#classics)

---

### 可微采样与抗混叠

<a id="c25"></a>
#### EWA Volume Splatting

**IEEE Visualization 2001** · [`T7`](#t7)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://dash.harvard.edu/bitstream/handle/1/4138240/Zwicker_EWA.pdf) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) ![GitHub: 未核实](https://img.shields.io/badge/GitHub-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square)

用椭圆加权平均核处理投影重建与低通滤波，是理解 splatting 足迹和抗混叠的经典工作。

<details>
<summary>方法边界与备注</summary>

体渲染算子，不能直接等同于二维光流 warp 或后来的 3DGS 系统

</details>

<a id="c13"></a>
#### Spatial Transformer Networks (STN)

**NeurIPS 2015** · [`T7`](#t7)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/1506.02025) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) ![GitHub: 未核实](https://img.shields.io/badge/GitHub-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square)

参数预测、网格生成和可微采样联合训练，使空间变换可嵌入神经网络。

<details>
<summary>方法边界与备注</summary>

学到的变换受参数化限制；双线性采样不负责遮挡补全与严格抗混叠

</details>

<a id="c19"></a>
#### Softmax Splatting

**CVPR 2020** · [`T7`](#t7)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2003.05534) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://sniklaus.com/softsplat) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/sniklaus/softmax-splatting) [![GitHub stars](https://img.shields.io/github/stars/sniklaus/softmax-splatting?style=flat-square&label=stars&color=C58A18)](https://github.com/sniklaus/softmax-splatting/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sniklaus/softmax-splatting?style=flat-square&label=forks&color=64748B)](https://github.com/sniklaus/softmax-splatting/forks)

Niklaus–Liu 用 softmax 加权处理 forward warp 的多对一冲突，并支持图像和特征的可微前向投影。

<sub>作者实现 · <a href="https://github.com/sniklaus/softmax-splatting">sniklaus/softmax-splatting</a></sub>

<details>
<summary>方法边界与备注</summary>

依赖 flow 与重要性度量；反遮挡空洞需要合成网络或其他补全

</details>

[↑ 返回经典方法](#classics)

---

### 特征对齐、动画与三维形变

<a id="c28"></a>
#### Depth-Image-Based Rendering (DIBR)

**Fehn，SPIE 2004 代表工作** · [`T6`](#t6)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1117/12.524762) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) ![GitHub: 未核实](https://img.shields.io/badge/GitHub-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square)

用颜色图与深度生成虚拟视角，是理解深度重投影、遮挡和空洞的经典路线；该论文不是重投影思想的首次提出。

<details>
<summary>方法边界与备注</summary>

深度边界、反遮挡和投影冲突需专门处理

</details>

<a id="c14"></a>
#### Deformable ConvNets (DCN)

**ICCV 2017** · [`T8`](#t8)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/1703.06211) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/msracver/Deformable-ConvNets) [![GitHub stars](https://img.shields.io/github/stars/msracver/Deformable-ConvNets?style=flat-square&label=stars&color=C58A18)](https://github.com/msracver/Deformable-ConvNets/stargazers) [![GitHub forks](https://img.shields.io/github/forks/msracver/Deformable-ConvNets?style=flat-square&label=forks&color=64748B)](https://github.com/msracver/Deformable-ConvNets/forks)

为卷积采样位置学习 offset，使特征支持局部几何适应。

<sub>作者实现 · <a href="https://github.com/msracver/Deformable-ConvNets">msracver/Deformable-ConvNets</a></sub>

<details>
<summary>方法边界与备注</summary>

每个核位置有偏移，不等价于一个全图物理运动场

</details>

<a id="c24"></a>
#### CP-VTON

**ECCV 2018** · [`T2`](#t2) [`T9`](#t9)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/1807.07688) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/sergeywong/cp-vton) [![GitHub stars](https://img.shields.io/github/stars/sergeywong/cp-vton?style=flat-square&label=stars&color=C58A18)](https://github.com/sergeywong/cp-vton/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sergeywong/cp-vton?style=flat-square&label=forks&color=64748B)](https://github.com/sergeywong/cp-vton/forks)

用 Geometric Matching Module 学习 TPS，将商品服装形变到人体，再学习融合掩码。

<sub>复现代码；仓库自述为 reimplementation · <a href="https://github.com/sergeywong/cp-vton">sergeywong/cp-vton</a></sub>

<details>
<summary>方法边界与备注</summary>

TPS 对大姿态变化、复杂遮挡和细纹理的表示有限

</details>

<a id="c16"></a>
#### Monodepth2

**ICCV 2019；预印本 2018** · [`T6`](#t6)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/1806.01260) ![Project: 未核实](https://img.shields.io/badge/Project-%E6%9C%AA%E6%A0%B8%E5%AE%9E-89939E?style=flat-square) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/nianticlabs/monodepth2) [![GitHub stars](https://img.shields.io/github/stars/nianticlabs/monodepth2?style=flat-square&label=stars&color=C58A18)](https://github.com/nianticlabs/monodepth2/stargazers) [![GitHub forks](https://img.shields.io/github/forks/nianticlabs/monodepth2?style=flat-square&label=forks&color=64748B)](https://github.com/nianticlabs/monodepth2/forks)

用深度、位姿和可微重投影进行自监督视图重建，引入最小重投影误差与自动掩码。

<sub>作者实现 · <a href="https://github.com/nianticlabs/monodepth2">nianticlabs/monodepth2</a></sub>

<details>
<summary>方法边界与备注</summary>

是深度估计系统；几何 warp 仍受动态物体、反光与不可见区域影响

</details>

<a id="c17"></a>
#### First Order Motion Model (FOMM)

**NeurIPS 2019；arXiv 2020** · [`T8`](#t8) [`T9`](#t9)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://papers.nips.cc/paper/8935-first-order-motion-model-for-image-animation.pdf) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://aliaksandrsiarohin.github.io/first-order-model-website/) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/AliaksandrSiarohin/first-order-model) [![GitHub stars](https://img.shields.io/github/stars/AliaksandrSiarohin/first-order-model?style=flat-square&label=stars&color=C58A18)](https://github.com/AliaksandrSiarohin/first-order-model/stargazers) [![GitHub forks](https://img.shields.io/github/forks/AliaksandrSiarohin/first-order-model?style=flat-square&label=forks&color=64748B)](https://github.com/AliaksandrSiarohin/first-order-model/forks)

自学习关键点与局部一阶仿射运动，构造稠密特征 warp 和遮挡图实现图像动画。

<sub>作者实现 · <a href="https://github.com/AliaksandrSiarohin/first-order-model">AliaksandrSiarohin/first-order-model</a></sub>

<details>
<summary>方法边界与备注</summary>

大身份差异、大旋转与显著反遮挡仍困难

</details>

<a id="c21"></a>
#### D-NeRF

**CVPR 2021；预印本 2020** · [`T8`](#t8)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2011.13961) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://www.albertpumarola.com/research/D-NeRF/index.html) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/albertpumarola/D-NeRF) [![GitHub stars](https://img.shields.io/github/stars/albertpumarola/D-NeRF?style=flat-square&label=stars&color=C58A18)](https://github.com/albertpumarola/D-NeRF/stargazers) [![GitHub forks](https://img.shields.io/github/forks/albertpumarola/D-NeRF?style=flat-square&label=forks&color=64748B)](https://github.com/albertpumarola/D-NeRF/forks)

学习时间条件形变，把动态场景坐标映射到 canonical radiance field。

<sub>作者实现 · <a href="https://github.com/albertpumarola/D-NeRF">albertpumarola/D-NeRF</a></sub>

<details>
<summary>方法边界与备注</summary>

单目重建有歧义，动态细节和训练效率受限

</details>

<a id="c22"></a>
#### Nerfies

**ICCV 2021；预印本 2020** · [`T8`](#t8)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2011.12948) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://nerfies.github.io/) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/google/nerfies) [![GitHub stars](https://img.shields.io/github/stars/google/nerfies?style=flat-square&label=stars&color=C58A18)](https://github.com/google/nerfies/stargazers) [![GitHub forks](https://img.shields.io/github/forks/google/nerfies?style=flat-square&label=forks&color=64748B)](https://github.com/google/nerfies/forks)

连续三维形变场、弹性正则与粗到细优化，重建随意拍摄的非刚性场景。

<sub>作者实现 · <a href="https://github.com/google/nerfies">google/nerfies</a></sub>

<details>
<summary>方法边界与备注</summary>

连续 canonical warp 难以处理拓扑变化；优化可能陷入局部极小值

</details>

<a id="c23"></a>
#### HyperNeRF

**SIGGRAPH Asia / TOG 2021** · [`T8`](#t8)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://arxiv.org/abs/2106.13228) [![Project: Visit](https://img.shields.io/badge/Project-Visit-087F8C?style=flat-square)](https://hypernerf.github.io/) [![GitHub: Visit](https://img.shields.io/badge/GitHub-Visit-243247?style=flat-square)](https://github.com/google/hypernerf) [![GitHub stars](https://img.shields.io/github/stars/google/hypernerf?style=flat-square&label=stars&color=C58A18)](https://github.com/google/hypernerf/stargazers) [![GitHub forks](https://img.shields.io/github/forks/google/hypernerf?style=flat-square&label=forks&color=64748B)](https://github.com/google/hypernerf/forks)

把表示提升到高维空间，通过切片建模拓扑变化，扩展普通连续三维 warp 的能力。

<sub>作者实现 · <a href="https://github.com/google/hypernerf">google/hypernerf</a></sub>

<details>
<summary>方法边界与备注</summary>

高维表示不是对三维空间直接构造一个处处可逆的形变

</details>

[↑ 返回经典方法](#classics)

---


<a id="guide"></a>
## 深入阅读 · Research guide

| 阅读主题 | 入口 |
| --- | --- |
| 概念、坐标方向与收录边界 | [Warping 的三个层次 / Forward 与 Backward](docs/RESEARCH_GUIDE.zh-CN.md#scope) |
| 进展、方法局限与关键问题 | [技术演进与仍未解决的问题](docs/RESEARCH_GUIDE.zh-CN.md#trends) |
| 噪声 Warping 的统计要求 | [普通插值为什么会改变高斯噪声？](docs/RESEARCH_GUIDE.zh-CN.md#trends) |
| 工具、实现与方案选择 | [实现入口与快速选型](docs/RESEARCH_GUIDE.zh-CN.md#practice) |

<a id="contributing"></a>
## 贡献 · Contributing

欢迎通过 [Issue](https://github.com/gulucaptain/Awesome-Warping-Algorithm/issues) 或 [Pull Request](https://github.com/gulucaptain/Awesome-Warping-Algorithm/pulls) 补充论文、作者主页、代码或纠正分类。

每条建议包含 **论文名、发表年份/状态、Paper、Project、GitHub、技术族和应用领域**。未公开的资源留空；第三方复现、共享框架与作者实现请明确区分。

维护者可编辑 [文献数据](data/catalog.json)，再运行 `python3 scripts/build_readme.py` 更新页面；计数与索引由同一份数据生成。详细原理与旧版逐项备注保留在 [研究指南](docs/RESEARCH_GUIDE.zh-CN.md)。

<details>
<summary>版式参考与致谢</summary>

本页采用原创的坐标网格封面和 GitHub 原生 Markdown 排版。分类导航与论文入口的组织参考了以下合集及模板，没有复制其论文描述或图像：

- [Awesome Diffusion Models in Medical Imaging](https://github.com/amirhossein-kz/Awesome-Diffusion-Models-in-Medical-Imaging)
- [Awesome Diffusion Models](https://github.com/diff-usion/Awesome-Diffusion-Models)
- [Awesome Diffusion Categorized](https://github.com/wangkai930418/awesome-diffusion-categorized)
- [Awesome list guidelines](https://github.com/sindresorhus/awesome/blob/main/awesome.md)
- [Best README Template](https://github.com/othneildrew/Best-README-Template)
- [Shields.io](https://shields.io/)：资源徽章与动态 GitHub 计数

</details>

<div align="center">

**[↑ Back to top](#top)**

<sub>Map coordinates. Preserve structure. Explore motion.</sub>

</div>
