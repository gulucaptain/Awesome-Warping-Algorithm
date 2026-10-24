<!-- Generated from data/catalog.json by scripts/build_readme.py. -->
<a id="top"></a>

<div align="center">

<img src="assets/warping-banner-v2.png" alt="Luminous coordinate grids deform into a continuous three-dimensional flow surface" width="100%">

# Awesome Warping Algorithms · 中文版

*空间 Warping 算法与研究资源图谱。*

[English](README.md) · **简体中文**

<p align="justify">
Warping 将像素、特征与噪声在空间和时间中建立映射，是图像对齐、三维重建与可控生成的重要基础。本仓库连接经典方法与前沿进展，按六个研究板块及其 Topic 整理论文与代码，帮助研究者梳理技术脉络、比较不同思路，并在已有工作上继续探索。
</p>

<b>212</b> 篇论文 &nbsp; · &nbsp; <b>132</b> 个代码仓库 &nbsp; · &nbsp; <b>6</b> 个研究板块 &nbsp; · &nbsp; <b>16</b> 个主题

</div>

---

<a id="start"></a>
## 🧭 从这里开始

| 想了解什么？ | 阅读入口 |
| --- | --- |
| **Warping 的基础与实现** | [TPS](#c05) → [MLS](#c08) → [STN](#c13) → [Softmax Splatting](#c19) |
| **运动估计与视频对齐** | [PWC-Net](#c15) → [RAFT](#c20) → [GMFlow](#n01) → [SEA-RAFT](#n13) → [MEMFOF](#n20) |
| **三维形变与动态场景** | [D-NeRF](#c21) → [Nerfies](#c22) → [Deformable 3D Gaussians](#n11) → [4D-GS](#n12) |
| **扩散模型与运动控制** | [∫-noise](#n16) → [Go-with-the-Flow](#n19) → [CameraNoise](#n24) · [GenWarp](#n15) → [SplatDiff](#n23) |

<details>
<summary><b>收录范围与年份口径</b></summary>

以计算机视觉、图形学和医学图像中的**空间 warping** 为主。区分变换模型、对应估计、采样算子及其应用系统；DTW 时间序列对齐和 GPU warp 不在本目录内。

正文按 **研究板块 → Topic** 编排，各 Topic 内论文按年份从新到旧直接列出，不另设年份导航或分组；子类别以独立简介块开头，论文按“完整标题（出处 年份）→ 资源徽章与技术标签同一行 → 贡献说明”统一展示，方法之间以分隔线区分。完整发表记录、实现来源与局限保留在中英文文献数据和研究指南中。经典与近期工作统一展示。正式发表工作采用代表性发表年份，预印本采用预印本年份，并保留发表历史；合并介绍多个基础方法的条目按所链接代表论文的发表年份排序。通用概念和文档移至研究指南，不列入论文正文与统计。同年条目保持数据中的顺序。覆盖截至 2026-10-24 的公开资料。方法贡献和局限来自原论文、作者资料与原版调研；本合集未对所有实现做统一复现。

每篇工作只有一个主 Topic；交叉方向通过关联标签和关联阅读连接。扩展方向明确区分空间地图与记忆、预测世界模型、交互模拟器和具身闭环系统；基础表示与预测模型也与显式空间 Warping 算子区分。新增论文须符合所属 Topic 的范围。

[完整定义、Forward / Backward 与核验原则 →](docs/RESEARCH_GUIDE.zh-CN.md#scope)

</details>

<a id="topics"></a>
## 🗂️ Topic 导航

6 个研究板块、16 个 Topic。计数仅包含主条目，关联阅读不重复计数。

<table>
<thead>
<tr><th align="left">研究板块</th><th align="left">Topic</th><th align="left">主条目 / 状态</th></tr>
</thead>
<tbody>
<tr>
<td rowspan="2" valign="middle"><a href="#area-foundations">1. Warping 基础与算子</a></td>
<td><a href="#topic-geometry-editing">1.1 几何变换与形变编辑</a></td>
<td>15</td>
</tr>
<tr>
<td><a href="#topic-sampling-splatting">1.2 可微采样与 Splatting</a></td>
<td>14</td>
</tr>
<tr>
<td rowspan="3" valign="middle"><a href="#area-alignment">2. 对应估计与图像对齐</a></td>
<td><a href="#topic-optical-flow">2.1 光流与稠密对应</a></td>
<td>25</td>
</tr>
<tr>
<td><a href="#topic-image-alignment">2.2 图像配准、拼接与视频稳像</a></td>
<td>13</td>
</tr>
<tr>
<td><a href="#topic-medical-registration">2.3 医学图像配准与可逆形变</a></td>
<td>17</td>
</tr>
<tr>
<td rowspan="2" valign="middle"><a href="#area-video-processing">3. 视频处理与人物形变</a></td>
<td><a href="#topic-video-restoration">3.1 视频插帧与复原</a></td>
<td>18</td>
</tr>
<tr>
<td><a href="#topic-human-deformation">3.2 人物动画、运动迁移与虚拟试衣</a></td>
<td>16</td>
</tr>
<tr>
<td rowspan="2" valign="middle"><a href="#area-video-generation">4. 视频生成与运动控制</a></td>
<td><a href="#topic-noise-warping">4.1 噪声 Warping 与时序一致性</a></td>
<td>11</td>
</tr>
<tr>
<td><a href="#topic-controlled-generation">4.2 相机、轨迹与运动可控生成</a></td>
<td>13</td>
</tr>
<tr>
<td rowspan="4" valign="middle"><a href="#area-spatial-intelligence">5. 空间智能</a></td>
<td><a href="#topic-spatial-perception">5.1 空间感知、深度与三维重建</a></td>
<td>12</td>
</tr>
<tr>
<td><a href="#topic-novel-view-synthesis">5.2 重投影与新视角合成</a></td>
<td>14</td>
</tr>
<tr>
<td><a href="#topic-dynamic-3d">5.3 动态三维与 4D 场景</a></td>
<td>13</td>
</tr>
<tr>
<td><a href="#topic-spatial-reasoning">5.4 空间推理与场景记忆</a></td>
<td>10</td>
</tr>
<tr>
<td rowspan="3" valign="middle"><a href="#area-world-models-agents">6. 世界模型与具身智能体</a></td>
<td><a href="#topic-world-models">6.1 世界模型与环境预测</a></td>
<td>7</td>
</tr>
<tr>
<td><a href="#topic-interactive-simulation">6.2 交互式环境与模拟</a></td>
<td>6</td>
</tr>
<tr>
<td><a href="#topic-embodied-agents">6.3 具身智能体、规划与控制</a></td>
<td>8</td>
</tr>
</tbody>
</table>

<a id="area-foundations"></a>
## 1. Warping 基础与算子

<a id="topic-08"></a>
<a id="topic-16"></a>
<a id="topic-geometry-editing"></a>
### 1.1 几何变换与形变编辑

> **本类关注** · 参数化变换、TPS、FFD、MLS、ARAP、Morphing、频率感知形变与 Warp–Unwarp
>
> **15 篇论文 · 按年份从新到旧排列**

---

<a id="n26"></a>
#### WarpI2I: Image Warping for Image-to-Image Translation (ECCV 2026)

[![arXiv: 2606.31018](https://img.shields.io/badge/arXiv-2606.31018-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.31018) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2606.31018) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://shenzheng2000.github.io/WarpI2I.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ShenZheng2000/WarpI2I) [![GitHub stars](https://img.shields.io/github/stars/ShenZheng2000/WarpI2I?style=flat-square&label=stars&color=C58A18)](https://github.com/ShenZheng2000/WarpI2I/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ShenZheng2000/WarpI2I?style=flat-square&label=forks&color=64748B)](https://github.com/ShenZheng2000/WarpI2I/forks) &nbsp; [`T2`](#t2) [`T9`](#t9)

在编码前用 saliency-guided warp 向显著区域分配更多空间表示，处理后 unwarp，改善紧凑 latent 模型的结构保留。

---

<a id="n21"></a>
#### LookingGlass: Generative Anamorphoses via Laplacian Pyramid Warping (CVPR 2025)

[![arXiv: 2504.08902](https://img.shields.io/badge/arXiv-2504.08902-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.08902) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2504.08902) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://lookingglass-lpw.github.io/) &nbsp; [`T7`](#t7) [`T9`](#t9)

用 Laplacian 金字塔进行频率感知的图像 warp 与视图聚合，支持多视角生成式 anamorphosis。

---

<a id="s003"></a>
#### Inpaint4Drag: Repurposing Inpainting Models for Drag-Based Image Editing via Bidirectional Warping (ICCV 2025)

[![arXiv: 2509.04582](https://img.shields.io/badge/arXiv-2509.04582-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.04582) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2509.04582) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://visual-ai.github.io/inpaint4drag/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Visual-AI/Inpaint4Drag) [![GitHub stars](https://img.shields.io/github/stars/Visual-AI/Inpaint4Drag?style=flat-square&label=stars&color=C58A18)](https://github.com/Visual-AI/Inpaint4Drag/stargazers) [![GitHub forks](https://img.shields.io/github/forks/Visual-AI/Inpaint4Drag?style=flat-square&label=forks&color=64748B)](https://github.com/Visual-AI/Inpaint4Drag/forks) &nbsp; [`T3`](#t3) [`T9`](#t9)

将拖拽编辑分解为像素空间双向 Warping 与图像修复，先建立几何对应，再补全显露区域。

---

<a id="s004"></a>
#### FlowDrag: 3D-aware Drag-based Image Editing with Mesh-guided Deformation Vector Flow Fields (ICML 2025)

[![arXiv: 2507.08285](https://img.shields.io/badge/arXiv-2507.08285-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.08285) &nbsp; [`T3`](#t3) [`T6`](#t6) [`T9`](#t9)

由单图构建三维网格，用控制点驱动网格变形，再将位移投影为二维流场引导扩散编辑。

---

<a id="s005"></a>
#### DragDiffusion: Harnessing Diffusion Models for Interactive Point-based Image Editing (CVPR 2024)

[![arXiv: 2306.14435](https://img.shields.io/badge/arXiv-2306.14435-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2306.14435) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2306.14435) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://yujun-shi.github.io/projects/dragdiffusion.html) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Yujun-Shi/DragDiffusion) [![GitHub stars](https://img.shields.io/github/stars/Yujun-Shi/DragDiffusion?style=flat-square&label=stars&color=C58A18)](https://github.com/Yujun-Shi/DragDiffusion/stargazers) [![GitHub forks](https://img.shields.io/github/forks/Yujun-Shi/DragDiffusion?style=flat-square&label=forks&color=64748B)](https://github.com/Yujun-Shi/DragDiffusion/forks) &nbsp; [`T8`](#t8) [`T9`](#t9)

通过 UNet 特征上的运动监督优化扩散潜变量，实现交互式点拖拽和形状编辑。

---

<a id="p03"></a>
#### Bounded Biharmonic Weights for Real-Time Deformation (SIGGRAPH / TOG 2011)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://igl.ethz.ch/projects/bbw/bounded-biharmonic-weights-siggraph-2011-jacobson-et-al.pdf) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://igl.ethz.ch/projects/bbw/) &nbsp; [`T2`](#t2) [`T3`](#t3)

通过带边界约束的双调和能量求解形状感知混合权重，统一点、骨骼和笼式控制下的二维与三维形变。

---

<a id="s002"></a>
#### Green Coordinates (SIGGRAPH / TOG 2008)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.wisdom.weizmann.ac.il/~ylipman/GC/gc_techrep.pdf) &nbsp; [`T3`](#t3)

以笼体顶点与面法向共同定义 Green 坐标，构造二维保角及三维近似保角的形变映射。

---

<a id="c09"></a>
#### As-Rigid-As-Possible Surface Modeling (SGP 2007)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://igl.ethz.ch/projects/ARAP/arap_web.pdf) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://igl.ethz.ch/projects/ARAP/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/libigl/libigl) [![GitHub stars](https://img.shields.io/github/stars/libigl/libigl?style=flat-square&label=stars&color=C58A18)](https://github.com/libigl/libigl/stargazers) [![GitHub forks](https://img.shields.io/github/forks/libigl/libigl?style=flat-square&label=forks&color=64748B)](https://github.com/libigl/libigl/forks) &nbsp; [`T3`](#t3)

Sorkine–Alexa 以局部刚性约束保留形状细节，是网格编辑的经典能量设计。

---

<a id="p02"></a>
#### Embedded Deformation for Shape Manipulation (SIGGRAPH / TOG 2007)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://cgl.ethz.ch/~sumnerb/research/embdef/Sumner2007EDF.pdf) &nbsp; [`T3`](#t3)

用稀疏形变图及节点局部仿射变换驱动复杂形状，为非刚性重建和形状操控提供通用模型。

---

<a id="s001"></a>
#### Harmonic Coordinates for Character Articulation (SIGGRAPH / TOG 2007)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.cs.jhu.edu/~misha/ReadingSeminar/Papers/Joshi07.pdf) &nbsp; [`T3`](#t3)

通过求解笼体内部的调和权重控制体积形变，在凹形区域保持非负权重与内部局部性。

---

<a id="c08"></a>
#### Image deformation using moving least squares (SIGGRAPH / TOG 2006)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1145/1141911.1141920) &nbsp; [`T2`](#t2)

Schaefer 等用局部加权拟合构造仿射、相似、刚性图像形变，支持交互控制。

---

<a id="p01"></a>
#### Laplacian Surface Editing (SGP 2004)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://diglib.eg.org/items/ee43c2c6-4956-4ff0-9db1-c946306a5b99) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://igl.ethz.ch/projects/Laplacian-mesh-processing/Laplacian-mesh-editing/) &nbsp; [`T3`](#t3)

通过局部拉普拉斯坐标与控制柄约束实现保留几何细节的网格编辑，是局部形变表示的重要基础。

---

<a id="c06"></a>
#### Feature-Based Image Metamorphosis (SIGGRAPH 1992)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://wcours.gel.ulaval.ca/GIF4105/old/h20/tps/tp3/beierneely92.pdf) &nbsp; [`T2`](#t2)

用成对特征线段控制 inverse warp，再结合颜色混合实现 morphing。

---

<a id="c05"></a>
#### Principal warps: thin-plate splines and the decomposition of deformations (TPAMI 1989)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1109/34.24792) &nbsp; [`T2`](#t2)

Bookstein 将 TPS 用于地标形变分析，以弯曲能量定义平滑非刚性映射；TPS 的数学起源更早。

---

<a id="c04"></a>
#### Free-Form Deformation of Solid Geometric Models (SIGGRAPH 1986)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.cse.iitd.ac.in/~jatin/minor_p/papers/sederberg.pdf) &nbsp; [`T2`](#t2)

Sederberg–Parry 通过控制格与 Bernstein 多项式变形几何对象，奠定体积控制形变基础。

---

<details>
<summary>关联阅读 · 9 篇其他 Topic 的论文</summary>

- [Tether / Autonomous Functional Play](#s077) (2026)
- [SC-GS](#s061) (2024)
- [Unsupervised Deep Image Stitching (UDIS)](#p14) (2021)
- [Transporter Networks](#p65) (2021)
- [Neural 3D Mesh Renderer](#p05) (2018)
- [X2Face](#p30) (2018)
- [Deep Image Homography Estimation](#p13) (2016)
- [DynamicFusion](#p50) (2015)
- [EWA Volume Splatting](#c25) (2001)

</details>

[↑ 1.1 本类开头](#topic-geometry-editing) · [↑ 返回 Topic 导航](#topics)

---

<a id="topic-15"></a>
<a id="topic-sampling-splatting"></a>
### 1.2 可微采样与 Splatting

> **本类关注** · 插值、重采样、可微空间变换、采样核、伴随与导数
>
> **14 篇论文 · 按年份从新到旧排列**

---

<a id="s010"></a>
#### gsplat: An Open-Source Library for Gaussian Splatting (JMLR 2025)

[![arXiv: 2409.06765](https://img.shields.io/badge/arXiv-2409.06765-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2409.06765) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2409.06765) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nerfstudio-project/gsplat) [![GitHub stars](https://img.shields.io/github/stars/nerfstudio-project/gsplat?style=flat-square&label=stars&color=C58A18)](https://github.com/nerfstudio-project/gsplat/stargazers) [![GitHub forks](https://img.shields.io/github/forks/nerfstudio-project/gsplat?style=flat-square&label=forks&color=64748B)](https://github.com/nerfstudio-project/gsplat/forks) &nbsp; [`T7`](#t7)

以可微高斯投影与光栅化核心实现高效训练和渲染，并提供公开的高斯 Splatting 软件论文。

---

<a id="s008"></a>
#### Mip-Splatting: Alias-free 3D Gaussian Splatting (CVPR 2024)

[![arXiv: 2311.16493](https://img.shields.io/badge/arXiv-2311.16493-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2311.16493) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2311.16493) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://niujinshuchong.github.io/mip-splatting/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/autonomousvision/mip-splatting) [![GitHub stars](https://img.shields.io/github/stars/autonomousvision/mip-splatting?style=flat-square&label=stars&color=C58A18)](https://github.com/autonomousvision/mip-splatting/stargazers) [![GitHub forks](https://img.shields.io/github/forks/autonomousvision/mip-splatting?style=flat-square&label=forks&color=64748B)](https://github.com/autonomousvision/mip-splatting/forks) &nbsp; [`T7`](#t7)

结合三维平滑滤波和二维 Mip 滤波，减轻高斯 Splatting 在缩放与采样率变化下的混叠。

---

<a id="s079"></a>
#### Towards Progressive Multi-Frequency Representation for Image Warping (CVPR 2024)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content/CVPR2024/html/Xiao_Towards_Progressive_Multi-Frequency_Representation_for_Image_Warping_CVPR_2024_paper.html) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/junxiao01/MFR) [![GitHub stars](https://img.shields.io/github/stars/junxiao01/MFR?style=flat-square&label=stars&color=C58A18)](https://github.com/junxiao01/MFR/stargazers) [![GitHub forks](https://img.shields.io/github/forks/junxiao01/MFR?style=flat-square&label=forks&color=64748B)](https://github.com/junxiao01/MFR/forks) &nbsp; [`T7`](#t7)

通过渐进频带表示和可学习 Gabor 滤波器捕获局部空间频率，提高非规则网格变换中的图像细节。

---

<a id="n10"></a>
#### ImWIP: Open-source image warping toolbox with adjoints and derivatives (SoftwareX 2023)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1016/j.softx.2023.101524) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://imwip.readthedocs.io/en/latest/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/RendersJens/ImWIP) [![GitHub stars](https://img.shields.io/github/stars/RendersJens/ImWIP?style=flat-square&label=stars&color=C58A18)](https://github.com/RendersJens/ImWIP/stargazers) [![GitHub forks](https://img.shields.io/github/forks/RendersJens/ImWIP?style=flat-square&label=forks&color=64748B)](https://github.com/RendersJens/ImWIP/forks) &nbsp; [`T7`](#t7)

提供可微图像 warp 及其精确离散伴随与导数，服务逆问题优化。

---

<a id="s006"></a>
#### Kernel Aware Resampler (CVPR 2023)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content/CVPR2023/html/Bernasconi_Kernel_Aware_Resampler_CVPR_2023_paper.html) &nbsp; [`T7`](#t7)

联合建模重建核、局部几何畸变和抗混叠核，以空间变化的退化信息控制通用图像重采样。

---

<a id="s085"></a>
#### Learning Local Implicit Fourier Representation for Image Warping (ECCV 2022)

[![arXiv: 2207.01831](https://img.shields.io/badge/arXiv-2207.01831-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2207.01831) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/jaewon-lee-b/ltew) [![GitHub stars](https://img.shields.io/github/stars/jaewon-lee-b/ltew?style=flat-square&label=stars&color=C58A18)](https://github.com/jaewon-lee-b/ltew/stargazers) [![GitHub forks](https://img.shields.io/github/forks/jaewon-lee-b/ltew?style=flat-square&label=forks&color=64748B)](https://github.com/jaewon-lee-b/ltew/forks) &nbsp; [`T7`](#t7)

利用局部纹理估计和坐标变换的 Jacobian 调整傅里叶响应，在连续表示中重采样非规则图像形状。

---

<a id="s086"></a>
#### SRWarp: Generalized Image Super-Resolution under Arbitrary Transformation (CVPR 2021)

[![arXiv: 2104.10325](https://img.shields.io/badge/arXiv-2104.10325-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2104.10325) &nbsp; [`T7`](#t7)

将图像超分推广到任意空间变换，通过多尺度特征和自适应 Warping 支持非规则输出形状。

---

<a id="s009"></a>
#### Modular Primitives for High-Performance Differentiable Rendering (SIGGRAPH Asia / TOG 2020)

[![arXiv: 2011.03277](https://img.shields.io/badge/arXiv-2011.03277-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2011.03277) &nbsp; [`T7`](#t7)

将光栅化、属性插值、纹理采样和抗混叠拆为可微模块，支持硬件加速的逆渲染。

---

<a id="p06"></a>
#### Soft Rasterizer: A Differentiable Renderer for Image-based 3D Reasoning (ICCV 2019)

[![arXiv: 1904.01786](https://img.shields.io/badge/arXiv-1904.01786-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1904.01786) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ShichenLiu/SoftRas) [![GitHub stars](https://img.shields.io/github/stars/ShichenLiu/SoftRas?style=flat-square&label=stars&color=C58A18)](https://github.com/ShichenLiu/SoftRas/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ShichenLiu/SoftRas?style=flat-square&label=forks&color=64748B)](https://github.com/ShichenLiu/SoftRas/forks) &nbsp; [`T7`](#t7)

以概率覆盖和软聚合替代硬光栅化，将轮廓和颜色误差传播到网格几何与相机参数。

---

<a id="s007"></a>
#### Linearized Multi-Sampling for Differentiable Image Transformation (ICCV 2019)

[![arXiv: 1901.07124](https://img.shields.io/badge/arXiv-1901.07124-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1901.07124) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/vcg-uvic/linearized_multisampling_release) [![GitHub stars](https://img.shields.io/github/stars/vcg-uvic/linearized_multisampling_release?style=flat-square&label=stars&color=C58A18)](https://github.com/vcg-uvic/linearized_multisampling_release/stargazers) [![GitHub forks](https://img.shields.io/github/forks/vcg-uvic/linearized_multisampling_release?style=flat-square&label=forks&color=64748B)](https://github.com/vcg-uvic/linearized_multisampling_release/forks) &nbsp; [`T7`](#t7)

在采样点邻域生成辅助样本并建立局部线性近似，改善可微图像变换的梯度传播。

---

<a id="p05"></a>
#### Neural 3D Mesh Renderer (CVPR 2018)

[![arXiv: 1711.07566](https://img.shields.io/badge/arXiv-1711.07566-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1711.07566) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/hiroharu-kato/neural_renderer) [![GitHub stars](https://img.shields.io/github/stars/hiroharu-kato/neural_renderer?style=flat-square&label=stars&color=C58A18)](https://github.com/hiroharu-kato/neural_renderer/stargazers) [![GitHub forks](https://img.shields.io/github/forks/hiroharu-kato/neural_renderer?style=flat-square&label=forks&color=64748B)](https://github.com/hiroharu-kato/neural_renderer/forks) &nbsp; [`T7`](#t7)

为三角形光栅化设计近似梯度，使二维图像损失能够优化三维网格形状与相机参数。

---

<a id="c13"></a>
#### Spatial Transformer Networks (NeurIPS 2015)

[![arXiv: 1506.02025](https://img.shields.io/badge/arXiv-1506.02025-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1506.02025) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/1506.02025) &nbsp; [`T7`](#t7)

参数预测、网格生成和可微采样联合训练，使空间变换可嵌入神经网络。

---

<a id="c25"></a>
#### EWA Volume Splatting (IEEE Visualization 2001)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://dash.harvard.edu/bitstream/handle/1/4138240/Zwicker_EWA.pdf) &nbsp; [`T7`](#t7)

用椭圆加权平均核处理投影重建与低通滤波，是理解 splatting 足迹和抗混叠的经典工作。

---

<a id="p04"></a>
#### Surface Splatting (SIGGRAPH 2001)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.cs.umd.edu/~zwicker/publications/SurfaceSplatting-SIG01.pdf) &nbsp; [`T7`](#t7)

将屏幕空间 EWA 滤波推广到不规则表面点采样，结合可见性处理实现抗混叠点基元渲染。

---

<details>
<summary>关联阅读 · 9 篇其他 Topic 的论文</summary>

- [Fast Forward](#s084) (2026)
- [Infinite-Resolution Integral Noise Warping](#s043) (2025)
- [Warped Diffusion](#n17) (2024)
- [Dynamic 3D Gaussians](#p51) (2024)
- [3D Gaussian Splatting (3DGS)](#p45) (2023)
- [Deep Learning Image Registration (DLIR)](#p18) (2019)
- [Depth-Aware Interpolation (DAIN)](#p22) (2019)
- [Stereo Magnification / Multiplane Images](#p48) (2018)
- [B-spline FFD Registration](#c07) (1999)

</details>

[↑ 1.2 本类开头](#topic-sampling-splatting) · [↑ 返回 Topic 导航](#topics)

---

<a id="area-alignment"></a>
## 2. 对应估计与图像对齐

<a id="topic-05"></a>
<a id="topic-optical-flow"></a>
### 2.1 光流与稠密对应

> **本类关注** · 运动估计、相关体、全局匹配与多帧对应
>
> **25 篇论文 · 按年份从新到旧排列**

---

<a id="n20"></a>
#### MEMFOF: High-Resolution Training for Memory-Efficient Multi-Frame Optical Flow Estimation (ICCV 2025)

[![arXiv: 2506.23151](https://img.shields.io/badge/arXiv-2506.23151-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.23151) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2506.23151) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://msu-video-group.github.io/memfof/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/msu-video-group/memfof) [![GitHub stars](https://img.shields.io/github/stars/msu-video-group/memfof?style=flat-square&label=stars&color=C58A18)](https://github.com/msu-video-group/memfof/stargazers) [![GitHub forks](https://img.shields.io/github/forks/msu-video-group/memfof?style=flat-square&label=forks&color=64748B)](https://github.com/msu-video-group/memfof/forks) &nbsp; [`T4`](#t4)

精简相关表示并引入多帧估计与高分辨率训练，推进原生 FullHD 光流的显存效率。

---

<a id="s015"></a>
#### UFM: A Simple Path towards Unified Dense Correspondence with Flow (NeurIPS 2025)

[![arXiv: 2506.09278](https://img.shields.io/badge/arXiv-2506.09278-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.09278) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2506.09278) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://uniflowmatch.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/UniFlowMatch/UFM) [![GitHub stars](https://img.shields.io/github/stars/UniFlowMatch/UFM?style=flat-square&label=stars&color=C58A18)](https://github.com/UniFlowMatch/UFM/stargazers) [![GitHub forks](https://img.shields.io/github/forks/UniFlowMatch/UFM?style=flat-square&label=forks&color=64748B)](https://github.com/UniFlowMatch/UFM/forks) &nbsp; [`T4`](#t4)

以统一的可共视训练数据和 Transformer 直接回归二维位移，将光流与宽基线稠密匹配合并建模。

---

<a id="n13"></a>
#### SEA-RAFT: Simple, Efficient, Accurate RAFT for Optical Flow (ECCV 2024)

[![arXiv: 2405.14793](https://img.shields.io/badge/arXiv-2405.14793-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2405.14793) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2405.14793) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/princeton-vl/SEA-RAFT) [![GitHub stars](https://img.shields.io/github/stars/princeton-vl/SEA-RAFT?style=flat-square&label=stars&color=C58A18)](https://github.com/princeton-vl/SEA-RAFT/stargazers) [![GitHub forks](https://img.shields.io/github/forks/princeton-vl/SEA-RAFT?style=flat-square&label=forks&color=64748B)](https://github.com/princeton-vl/SEA-RAFT/forks) &nbsp; [`T4`](#t4)

通过初始 flow 回归、混合 Laplace 损失和刚性运动预训练，改善 RAFT 的效率与精度。

---

<a id="p71"></a>
#### RoMa: Robust Dense Feature Matching (CVPR 2024)

[![arXiv: 2305.15404](https://img.shields.io/badge/arXiv-2305.15404-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2305.15404) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2305.15404) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Parskatt/RoMa) [![GitHub stars](https://img.shields.io/github/stars/Parskatt/RoMa?style=flat-square&label=stars&color=C58A18)](https://github.com/Parskatt/RoMa/stargazers) [![GitHub forks](https://img.shields.io/github/forks/Parskatt/RoMa?style=flat-square&label=forks&color=64748B)](https://github.com/Parskatt/RoMa/forks) &nbsp; [`T4`](#t4)

结合冻结的基础模型特征、局部卷积特征和匹配解码器，预测对视角与外观变化更稳健的稠密坐标映射。

---

<a id="n09"></a>
#### Unifying Flow, Stereo and Depth Estimation (TPAMI 2023)

[![arXiv: 2211.05783](https://img.shields.io/badge/arXiv-2211.05783-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2211.05783) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2211.05783) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://haofeixu.github.io/unimatch/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/autonomousvision/unimatch) [![GitHub stars](https://img.shields.io/github/stars/autonomousvision/unimatch?style=flat-square&label=stars&color=C58A18)](https://github.com/autonomousvision/unimatch/stargazers) [![GitHub forks](https://img.shields.io/github/forks/autonomousvision/unimatch?style=flat-square&label=forks&color=64748B)](https://github.com/autonomousvision/unimatch/forks) &nbsp; [`T4`](#t4) [`T6`](#t6)

把 flow、双目视差与有位姿的跨视图深度统一为对应匹配任务。

---

<a id="p12"></a>
#### FlowFormer++: Masked Cost Volume Autoencoding for Pretraining Optical Flow Estimation (CVPR 2023)

[![arXiv: 2303.01237](https://img.shields.io/badge/arXiv-2303.01237-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2303.01237) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/XiaoyuShi97/FlowFormerPlusPlus) [![GitHub stars](https://img.shields.io/github/stars/XiaoyuShi97/FlowFormerPlusPlus?style=flat-square&label=stars&color=C58A18)](https://github.com/XiaoyuShi97/FlowFormerPlusPlus/stargazers) [![GitHub forks](https://img.shields.io/github/forks/XiaoyuShi97/FlowFormerPlusPlus?style=flat-square&label=forks&color=64748B)](https://github.com/XiaoyuShi97/FlowFormerPlusPlus/forks) &nbsp; [`T4`](#t4)

通过遮蔽代价体自编码预训练学习对应表示，增强光流网络对匹配结构的建模。

---

<a id="p70"></a>
#### DKM: Dense Kernelized Feature Matching for Geometry Estimation (CVPR 2023)

[![arXiv: 2202.00667](https://img.shields.io/badge/arXiv-2202.00667-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2202.00667) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2202.00667) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://parskatt.github.io/DKM/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Parskatt/DKM) [![GitHub stars](https://img.shields.io/github/stars/Parskatt/DKM?style=flat-square&label=stars&color=C58A18)](https://github.com/Parskatt/DKM/stargazers) [![GitHub forks](https://img.shields.io/github/forks/Parskatt/DKM?style=flat-square&label=forks&color=64748B)](https://github.com/Parskatt/DKM/forks) &nbsp; [`T4`](#t4)

通过全局核化回归和局部细化预测稠密匹配及置信度，服务于相机几何估计。

---

<a id="s012"></a>
#### PDC-Net+: Enhanced Probabilistic Dense Correspondence Network (TPAMI 2023)

[![arXiv: 2109.13912](https://img.shields.io/badge/arXiv-2109.13912-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2109.13912) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/PruneTruong/DenseMatching) [![GitHub stars](https://img.shields.io/github/stars/PruneTruong/DenseMatching?style=flat-square&label=stars&color=C58A18)](https://github.com/PruneTruong/DenseMatching/stargazers) [![GitHub forks](https://img.shields.io/github/forks/PruneTruong/DenseMatching?style=flat-square&label=forks&color=64748B)](https://github.com/PruneTruong/DenseMatching/forks) &nbsp; [`T4`](#t4)

联合预测稠密对应与概率置信度，为大位移、遮挡和跨视角匹配提供不确定性信息。

---

<a id="s014"></a>
#### CroCo v2: Improved Cross-view Completion Pre-training for Stereo Matching and Optical Flow (ICCV 2023)

[![arXiv: 2211.10408](https://img.shields.io/badge/arXiv-2211.10408-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2211.10408) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2211.10408) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/naver/croco) [![GitHub stars](https://img.shields.io/github/stars/naver/croco?style=flat-square&label=stars&color=C58A18)](https://github.com/naver/croco/stargazers) [![GitHub forks](https://img.shields.io/github/forks/naver/croco?style=flat-square&label=forks&color=64748B)](https://github.com/naver/croco/forks) &nbsp; [`T4`](#t4)

通过跨视图补全预训练与相对位置编码学习光流和双目匹配，不依赖显式图像 Warping 组件。

---

<a id="n01"></a>
#### GMFlow: Learning Optical Flow via Global Matching (CVPR 2022)

[![arXiv: 2111.13680](https://img.shields.io/badge/arXiv-2111.13680-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2111.13680) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2111.13680) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/haofeixu/gmflow) [![GitHub stars](https://img.shields.io/github/stars/haofeixu/gmflow?style=flat-square&label=stars&color=C58A18)](https://github.com/haofeixu/gmflow/stargazers) [![GitHub forks](https://img.shields.io/github/forks/haofeixu/gmflow?style=flat-square&label=forks&color=64748B)](https://github.com/haofeixu/gmflow/forks) &nbsp; [`T4`](#t4)

Transformer 增强跨图特征，以全局匹配生成 flow，减少对大量顺序迭代的依赖。

---

<a id="n02"></a>
#### FlowFormer: A Transformer Architecture for Optical Flow (ECCV 2022)

[![arXiv: 2203.16194](https://img.shields.io/badge/arXiv-2203.16194-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2203.16194) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://drinkingcoder.github.io/publication/flowformer/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/drinkingcoder/FlowFormer-Official) [![GitHub stars](https://img.shields.io/github/stars/drinkingcoder/FlowFormer-Official?style=flat-square&label=stars&color=C58A18)](https://github.com/drinkingcoder/FlowFormer-Official/stargazers) [![GitHub forks](https://img.shields.io/github/forks/drinkingcoder/FlowFormer-Official?style=flat-square&label=forks&color=64748B)](https://github.com/drinkingcoder/FlowFormer-Official/forks) &nbsp; [`T4`](#t4)

对 4D cost volume 进行 Transformer 编码，并通过循环解码更新运动。

---

<a id="p11"></a>
#### Learning to Estimate Hidden Motions with Global Motion Aggregation (ICCV 2021)

[![arXiv: 2104.02409](https://img.shields.io/badge/arXiv-2104.02409-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2104.02409) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2104.02409) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/zacjiang/GMA) [![GitHub stars](https://img.shields.io/github/stars/zacjiang/GMA?style=flat-square&label=stars&color=C58A18)](https://github.com/zacjiang/GMA/stargazers) [![GitHub forks](https://img.shields.io/github/forks/zacjiang/GMA?style=flat-square&label=forks&color=64748B)](https://github.com/zacjiang/GMA/forks) &nbsp; [`T4`](#t4)

用全局运动聚合将可见区域的运动信息传递到遮挡区域，增强基于 RAFT 的光流估计。

---

<a id="p69"></a>
#### LoFTR: Detector-Free Local Feature Matching with Transformers (CVPR 2021)

[![arXiv: 2104.00680](https://img.shields.io/badge/arXiv-2104.00680-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2104.00680) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2104.00680) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://zju3dv.github.io/loftr/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/zju3dv/LoFTR) [![GitHub stars](https://img.shields.io/github/stars/zju3dv/LoFTR?style=flat-square&label=stars&color=C58A18)](https://github.com/zju3dv/LoFTR/stargazers) [![GitHub forks](https://img.shields.io/github/forks/zju3dv/LoFTR?style=flat-square&label=forks&color=64748B)](https://github.com/zju3dv/LoFTR/forks) &nbsp; [`T4`](#t4)

用图像对条件化 Transformer 特征进行粗到细匹配，在低纹理区域建立无需关键点检测的稠密候选对应。

---

<a id="s011"></a>
#### COTR: Correspondence Transformer for Matching Across Images (ICCV 2021)

[![arXiv: 2103.14167](https://img.shields.io/badge/arXiv-2103.14167-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2103.14167) &nbsp; [`T4`](#t4)

用跨图像 Transformer 为连续坐标查询预测对应点，并通过局部细化实现精确匹配。

---

<a id="c20"></a>
#### RAFT: Recurrent All-Pairs Field Transforms for Optical Flow (ECCV 2020)

[![arXiv: 2003.12039](https://img.shields.io/badge/arXiv-2003.12039-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2003.12039) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2003.12039) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/princeton-vl/RAFT) [![GitHub stars](https://img.shields.io/github/stars/princeton-vl/RAFT?style=flat-square&label=stars&color=C58A18)](https://github.com/princeton-vl/RAFT/stargazers) [![GitHub forks](https://img.shields.io/github/forks/princeton-vl/RAFT?style=flat-square&label=forks&color=64748B)](https://github.com/princeton-vl/RAFT/forks) &nbsp; [`T4`](#t4)

全像素对相关体与循环更新，成为稠密流估计的重要基线。

---

<a id="s013"></a>
#### GLU-Net: Global-Local Universal Network for Dense Flow and Correspondences (CVPR 2020)

[![arXiv: 1912.05524](https://img.shields.io/badge/arXiv-1912.05524-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1912.05524) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/PruneTruong/GLU-Net) [![GitHub stars](https://img.shields.io/github/stars/PruneTruong/GLU-Net?style=flat-square&label=stars&color=C58A18)](https://github.com/PruneTruong/GLU-Net/stargazers) [![GitHub forks](https://img.shields.io/github/forks/PruneTruong/GLU-Net?style=flat-square&label=forks&color=64748B)](https://github.com/PruneTruong/GLU-Net/forks) &nbsp; [`T4`](#t4)

结合全局与局部相关层以及自适应分辨率，统一几何匹配、光流与语义对应估计。

---

<a id="c15"></a>
#### PWC-Net: CNNs for Optical Flow Using Pyramid, Warping, and Cost Volume (CVPR 2018)

[![arXiv: 1709.02371](https://img.shields.io/badge/arXiv-1709.02371-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1709.02371) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/NVlabs/PWC-Net) [![GitHub stars](https://img.shields.io/github/stars/NVlabs/PWC-Net?style=flat-square&label=stars&color=C58A18)](https://github.com/NVlabs/PWC-Net/stargazers) [![GitHub forks](https://img.shields.io/github/forks/NVlabs/PWC-Net?style=flat-square&label=forks&color=64748B)](https://github.com/NVlabs/PWC-Net/forks) &nbsp; [`T4`](#t4)

金字塔 + 特征 warping + cost volume，学习粗到细残余运动。

---

<a id="p10"></a>
#### LiteFlowNet: A Lightweight Convolutional Neural Network for Optical Flow Estimation (CVPR 2018)

[![arXiv: 1805.07036](https://img.shields.io/badge/arXiv-1805.07036-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1805.07036) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/twhui/LiteFlowNet) [![GitHub stars](https://img.shields.io/github/stars/twhui/LiteFlowNet?style=flat-square&label=stars&color=C58A18)](https://github.com/twhui/LiteFlowNet/stargazers) [![GitHub forks](https://img.shields.io/github/forks/twhui/LiteFlowNet?style=flat-square&label=forks&color=64748B)](https://github.com/twhui/LiteFlowNet/forks) &nbsp; [`T4`](#t4)

结合特征金字塔、特征 Warping、匹配和局部正则，以紧凑网络估计光流。

---

<a id="p08"></a>
#### FlowNet 2.0: Evolution of Optical Flow Estimation with Deep Networks (CVPR 2017)

[![arXiv: 1612.01925](https://img.shields.io/badge/arXiv-1612.01925-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1612.01925) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/1612.01925) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/lmb-freiburg/flownet2) [![GitHub stars](https://img.shields.io/github/stars/lmb-freiburg/flownet2?style=flat-square&label=stars&color=C58A18)](https://github.com/lmb-freiburg/flownet2/stargazers) [![GitHub forks](https://img.shields.io/github/forks/lmb-freiburg/flownet2?style=flat-square&label=forks&color=64748B)](https://github.com/lmb-freiburg/flownet2/forks) &nbsp; [`T4`](#t4)

通过级联网络、基于中间光流的图像 Warping 和专门的小位移分支，改进学习式光流估计。

---

<a id="p09"></a>
#### Optical Flow Estimation using a Spatial Pyramid Network (CVPR 2017)

[![arXiv: 1611.00850](https://img.shields.io/badge/arXiv-1611.00850-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1611.00850) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/anuragranj/spynet) [![GitHub stars](https://img.shields.io/github/stars/anuragranj/spynet?style=flat-square&label=stars&color=C58A18)](https://github.com/anuragranj/spynet/stargazers) [![GitHub forks](https://img.shields.io/github/forks/anuragranj/spynet?style=flat-square&label=forks&color=64748B)](https://github.com/anuragranj/spynet/forks) &nbsp; [`T4`](#t4)

在经典空间金字塔中用小型卷积网络逐层估计残差光流，以粗到细 Warping 处理大运动。

---

<a id="p07"></a>
#### FlowNet: Learning Optical Flow with Convolutional Networks (ICCV 2015)

[![arXiv: 1504.06852](https://img.shields.io/badge/arXiv-1504.06852-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1504.06852) &nbsp; [`T4`](#t4)

将稠密光流估计引入端到端卷积网络，并以相关层和 Flying Chairs 合成数据建立学习式光流的重要基线。

---

<a id="p72"></a>
#### SIFT Flow: Dense Correspondence across Scenes and its Applications (TPAMI 2011)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://people.csail.mit.edu/celiu/SIFTflow/) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://people.csail.mit.edu/celiu/SIFTflow/) &nbsp; [`T4`](#t4)

在稠密 SIFT 描述子上优化保边空间匹配，将光流式对应推广到不同场景和不同外观的图像对齐。

---

<a id="c02"></a>
#### Lucas-Kanade 20 Years On: A Unifying Framework (IJCV 2004)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.ri.cmu.edu/pub_files/pub3/baker_simon_2004_1/baker_simon_2004_1.pdf) &nbsp; [`T1`](#t1) [`T4`](#t4)

用图像残差优化 warp 参数；逆组合形式允许复用部分计算，是直接法对齐的重要基础。

---

<a id="c27"></a>
#### High Accuracy Optical Flow Estimation Based on a Theory for Warping (ECCV 2004)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.mia.uni-saarland.de/Publications/brox-eccv04-of.pdf) &nbsp; [`T4`](#t4)

结合亮度/梯度一致性和保边正则，为粗到细 warping 的数值求解提供理论解释。

---

<a id="c03"></a>
#### Determining optical flow (Artificial Intelligence 1981)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1016/0004-3702(81)90024-2) &nbsp; [`T4`](#t4)

亮度一致性与全局平滑正则结合，建立稠密变分光流的经典范式。

---

<details>
<summary>关联阅读 · 6 篇其他 Topic 的论文</summary>

- [MASt3R](#p42) (2024)
- [SceNeRFlow](#s062) (2024)
- [E2FGVI](#s025) (2022)
- [Neural Scene Flow Fields (NSFF)](#p49) (2021)
- [RAFT-Stereo](#s053) (2021)
- [Dense Object Nets](#s074) (2018)

</details>

[↑ 2.1 本类开头](#topic-optical-flow) · [↑ 返回 Topic 导航](#topics)

---

<a id="topic-01"></a>
<a id="topic-03"></a>
<a id="topic-04"></a>
<a id="topic-image-alignment"></a>
### 2.2 图像配准、拼接与视频稳像

> **本类关注** · 图像对齐、全景拼接、视差处理与时序稳定
>
> **13 篇论文 · 按年份从新到旧排列**

---

<a id="n25"></a>
#### DMAligner: Enhancing Image Alignment via Diffusion Model Based View Synthesis (CVPR 2026)

[![arXiv: 2602.23022](https://img.shields.io/badge/arXiv-2602.23022-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.23022) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://boomluo02.github.io/DMAligner/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/boomluo02/DMAligner) [![GitHub stars](https://img.shields.io/github/stars/boomluo02/DMAligner?style=flat-square&label=stars&color=C58A18)](https://github.com/boomluo02/DMAligner/stargazers) [![GitHub forks](https://img.shields.io/github/forks/boomluo02/DMAligner?style=flat-square&label=forks&color=64748B)](https://github.com/boomluo02/DMAligner/forks) &nbsp; [`T9`](#t9)

将图像对齐转为 diffusion-based view synthesis，以动态感知训练处理遮挡与光照变化。

---

<a id="s018"></a>
#### PixelStitch: Structure-Preserving Pixel-Wise Bidirectional Warps for Unsupervised Image Stitching (ICCV 2025)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content/ICCV2025/html/Jin_PixelStitch_Structure-Preserving_Pixel-Wise_Bidirectional_Warps_for_Unsupervised_Image_Stitching_ICCV_2025_paper.html) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MakiseChris666/PixelStitch) [![GitHub stars](https://img.shields.io/github/stars/MakiseChris666/PixelStitch?style=flat-square&label=stars&color=C58A18)](https://github.com/MakiseChris666/PixelStitch/stargazers) [![GitHub forks](https://img.shields.io/github/forks/MakiseChris666/PixelStitch?style=flat-square&label=forks&color=64748B)](https://github.com/MakiseChris666/PixelStitch/forks) &nbsp; [`T1`](#t1) [`T4`](#t4)

通过单应性分解建立中间投影平面，再学习双向逐像素残差形变以兼顾对齐与结构保持。

---

<a id="n28"></a>
#### Eliminating Warping Shakes for Unsupervised Online Video Stitching (ECCV 2024)

[![arXiv: 2403.06378](https://img.shields.io/badge/arXiv-2403.06378-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2403.06378) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2403.06378) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nie-lang/StabStitch) [![GitHub stars](https://img.shields.io/github/stars/nie-lang/StabStitch?style=flat-square&label=stars&color=C58A18)](https://github.com/nie-lang/StabStitch/stargazers) [![GitHub forks](https://img.shields.io/github/forks/nie-lang/StabStitch?style=flat-square&label=forks&color=64748B)](https://github.com/nie-lang/StabStitch/forks) &nbsp; [`T2`](#t2) [`T3`](#t3)

将视频拼接与稳像统一到无监督在线框架，约束空间对齐和时间稳定性，抑制逐帧 warp 抖动。

---

<a id="n08"></a>
#### Parallax-Tolerant Unsupervised Deep Image Stitching (ICCV 2023)

[![arXiv: 2302.08207](https://img.shields.io/badge/arXiv-2302.08207-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2302.08207) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2302.08207) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nie-lang/UDIS2) [![GitHub stars](https://img.shields.io/github/stars/nie-lang/UDIS2?style=flat-square&label=stars&color=C58A18)](https://github.com/nie-lang/UDIS2/stargazers) [![GitHub forks](https://img.shields.io/github/forks/nie-lang/UDIS2?style=flat-square&label=forks&color=64748B)](https://github.com/nie-lang/UDIS2/forks) &nbsp; [`T1`](#t1) [`T2`](#t2) [`T3`](#t3)

全局 homography + 局部 TPS，联合考虑重叠区对齐、非重叠区形状与接缝合成。

---

<a id="s019"></a>
#### DUT: Learning Video Stabilization by Simply Watching Unstable Videos (IEEE TIP 2022)

[![arXiv: 2011.14574](https://img.shields.io/badge/arXiv-2011.14574-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2011.14574) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Annbless/DUTCode) [![GitHub stars](https://img.shields.io/github/stars/Annbless/DUTCode?style=flat-square&label=stars&color=C58A18)](https://github.com/Annbless/DUTCode/stargazers) [![GitHub forks](https://img.shields.io/github/forks/Annbless/DUTCode?style=flat-square&label=forks&color=64748B)](https://github.com/Annbless/DUTCode/forks) &nbsp; [`T1`](#t1) [`T3`](#t3)

从不稳定视频中无监督学习网格轨迹估计与动态平滑，再用平滑后的网格路径完成视频稳像。

---

<a id="p14"></a>
#### Unsupervised Deep Image Stitching: Reconstructing Stitched Features to Images (IEEE TIP 2021)

[![arXiv: 2106.12859](https://img.shields.io/badge/arXiv-2106.12859-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2106.12859) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nie-lang/UnsupervisedDeepImageStitching) [![GitHub stars](https://img.shields.io/github/stars/nie-lang/UnsupervisedDeepImageStitching?style=flat-square&label=stars&color=C58A18)](https://github.com/nie-lang/UnsupervisedDeepImageStitching/stargazers) [![GitHub forks](https://img.shields.io/github/forks/nie-lang/UnsupervisedDeepImageStitching?style=flat-square&label=forks&color=64748B)](https://github.com/nie-lang/UnsupervisedDeepImageStitching/forks) &nbsp; [`T1`](#t1) [`T3`](#t3)

在无真实单应性标注下学习图像对齐，并通过特征到图像重建完成拼接。

---

<a id="p13"></a>
#### Deep Image Homography Estimation (arXiv 2016)

[![arXiv: 1606.03798](https://img.shields.io/badge/arXiv-1606.03798-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1606.03798) &nbsp; [`T1`](#t1)

直接从图像对预测四角点参数化单应性，为学习式平面配准提供早期代表方法。

---

<a id="p16"></a>
#### MeshFlow: Minimum Latency Online Video Stabilization (ECCV 2016)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1007/978-3-319-46466-4_48) &nbsp; [`T3`](#t3) [`T4`](#t4)

将特征运动传播到网格顶点，以顶点轨迹自适应平滑实现低延迟在线视频稳像。

---

<a id="s016"></a>
#### Shape-Preserving Half-Projective Warps for Image Stitching (CVPR 2014)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content_cvpr_2014/html/Chang_Shape-Preserving_Half-Projective_Warps_2014_CVPR_paper.html) &nbsp; [`T1`](#t1)

在重叠区域保留投影对齐，向非重叠区域平滑过渡到相似变换，以降低全景拼接畸变。

---

<a id="s017"></a>
#### Parallax-tolerant Image Stitching (CVPR 2014)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content_cvpr_2014/html/Zhang_Parallax-tolerant_Image_Stitching_2014_CVPR_paper.html) &nbsp; [`T1`](#t1) [`T3`](#t3)

结合单应性、保内容局部形变与接缝选择，在存在较大视差的图像间寻找可自然融合的区域。

---

<a id="c12"></a>
#### As-Projective-As-Possible Image Stitching with Moving DLT (CVPR 2013)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content_cvpr_2013/papers/Zaragoza_As-Projective-As-Possible_Image_Stitching_2013_CVPR_paper.pdf) &nbsp; [`T3`](#t3)

Zaragoza 等允许局部偏离全局投影变换，以适应拼接中的非平面与视差。

---

<a id="p15"></a>
#### Bundled Camera Paths for Video Stabilization (SIGGRAPH / TOG 2013)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/Stabilization_SIGGRAPH13.pdf) &nbsp; [`T3`](#t3)

以网格顶点对应的多条相机路径描述空间变化运动，并联合时空平滑与几何约束完成视频稳像。

---

<a id="c29"></a>
#### Content-Preserving Warps for 3D Video Stabilization (SIGGRAPH / TOG 2009)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://pages.cs.wisc.edu/~fliu/papers/siggraph09.pdf) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://web.cecs.pdx.edu/~fliu/project/3dstab.htm) &nbsp; [`T3`](#t3)

由三维相机运动与内容保持网格 warp 构造稳定视频，兼顾对齐和显著区域形状。

---

<details>
<summary>关联阅读 · 12 篇其他 Topic 的论文</summary>

- [HomoGen](#s028) (2025)
- [Robust Dense Matching (RoMa)](#p71) (2024)
- [Dense Kernelized Matching (DKM)](#p70) (2023)
- [PDC-Net+](#s012) (2023)
- [LoFTR](#p69) (2021)
- [COTR](#s011) (2021)
- [GLU-Net](#s013) (2020)
- [COLMAP / Structure-from-Motion Revisited](#p38) (2016)
- [SIFT Flow](#p72) (2011)
- [Lucas–Kanade / Inverse Compositional](#c02) (2004)
- [B-spline FFD Registration](#c07) (1999)
- [Thin-Plate Spline (TPS) / Principal Warps](#c05) (1989)

</details>

[↑ 2.2 本类开头](#topic-image-alignment) · [↑ 返回 Topic 导航](#topics)

---

<a id="topic-02"></a>
<a id="topic-medical-registration"></a>
### 2.3 医学图像配准与可逆形变

> **本类关注** · 跨模态配准、微分同胚、拓扑保持与逆一致性
>
> **17 篇论文 · 按年份从新到旧排列**

---

<a id="s023"></a>
#### Learning Diffeomorphism for Medical Image Registration with Time-Embedded Architectures Using Semigroup Regularization (CVPR 2026)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content/CVPR2026/html/Matinkia_Learning_Diffeomorphism_for_Medical_Image_Registration_with_Time-Embedded_Architectures_Using_CVPR_2026_paper.html) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://mattkia.github.io/SGDIR/) &nbsp; [`T5`](#t5)

以时间嵌入网络表示连续形变，并通过半群正则学习具有逆一致性与周期一致性的配准映射。

---

<a id="s084"></a>
#### Fast forward: Rephrasing 3D deformable image registration through density alignment and splatting (MIDL 2025 / PMLR 2026)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://proceedings.mlr.press/v301/heinrich26a.html) &nbsp; [`T5`](#t5) [`T7`](#t7)

将医学形变配准重述为点云前向 Splatting 得到的密度体对齐，用可微光栅化替代仅依赖反向插值的流程。

---

<a id="n14"></a>
#### uniGradICON: A Foundation Model for Medical Image Registration (MICCAI 2024)

[![arXiv: 2403.05780](https://img.shields.io/badge/arXiv-2403.05780-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2403.05780) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/uncbiag/uniGradICON) [![GitHub stars](https://img.shields.io/github/stars/uncbiag/uniGradICON?style=flat-square&label=stars&color=C58A18)](https://github.com/uncbiag/uniGradICON/stargazers) [![GitHub forks](https://img.shields.io/github/forks/uncbiag/uniGradICON?style=flat-square&label=forks&color=64748B)](https://github.com/uncbiag/uniGradICON/forks) &nbsp; [`T5`](#t5)

将学习式配准推进到多数据集、跨解剖区域和新任务的通用初始化与零样本使用。

---

<a id="s020"></a>
#### GradICON: Approximate Diffeomorphisms via Gradient Inverse Consistency (CVPR 2023)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content/CVPR2023/html/Tian_GradICON_Approximate_Diffeomorphisms_via_Gradient_Inverse_Consistency_CVPR_2023_paper.html) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/uncbiag/ICON) [![GitHub stars](https://img.shields.io/github/stars/uncbiag/ICON?style=flat-square&label=stars&color=C58A18)](https://github.com/uncbiag/ICON/stargazers) [![GitHub forks](https://img.shields.io/github/forks/uncbiag/ICON?style=flat-square&label=forks&color=64748B)](https://github.com/uncbiag/ICON/forks) &nbsp; [`T5`](#t5)

对双向变换复合的 Jacobian 与单位矩阵的偏差施加正则，学习更规则的医学配准映射。

---

<a id="s022"></a>
#### Fourier-Net: Fast Image Registration with Band-limited Deformation (AAAI 2023)

[![arXiv: 2211.16342](https://img.shields.io/badge/arXiv-2211.16342-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2211.16342) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/xi-jia/Fourier-Net) [![GitHub stars](https://img.shields.io/github/stars/xi-jia/Fourier-Net?style=flat-square&label=stars&color=C58A18)](https://github.com/xi-jia/Fourier-Net/stargazers) [![GitHub forks](https://img.shields.io/github/forks/xi-jia/Fourier-Net?style=flat-square&label=forks&color=64748B)](https://github.com/xi-jia/Fourier-Net/forks) &nbsp; [`T5`](#t5)

预测带限傅里叶域中的低维形变表示，再通过零填充和逆变换还原高分辨率位移场。

---

<a id="n05"></a>
#### TransMorph: Transformer for unsupervised medical image registration (Medical Image Analysis 2022)

[![arXiv: 2111.10480](https://img.shields.io/badge/arXiv-2111.10480-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2111.10480) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration) [![GitHub stars](https://img.shields.io/github/stars/junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration?style=flat-square&label=stars&color=C58A18)](https://github.com/junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration/stargazers) [![GitHub forks](https://img.shields.io/github/forks/junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration?style=flat-square&label=forks&color=64748B)](https://github.com/junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration/forks) &nbsp; [`T5`](#t5)

Transformer–ConvNet 混合模型用于三维医学配准，增强长程空间关系建模。

---

<a id="n06"></a>
#### SynthMorph: learning contrast-invariant registration without acquired images (IEEE TMI 2022)

[![arXiv: 2004.10282](https://img.shields.io/badge/arXiv-2004.10282-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2004.10282) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2004.10282) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://w3id.org/synthmorph) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/voxelmorph/voxelmorph) [![GitHub stars](https://img.shields.io/github/stars/voxelmorph/voxelmorph?style=flat-square&label=stars&color=C58A18)](https://github.com/voxelmorph/voxelmorph/stargazers) [![GitHub forks](https://img.shields.io/github/forks/voxelmorph/voxelmorph?style=flat-square&label=forks&color=64748B)](https://github.com/voxelmorph/voxelmorph/forks) &nbsp; [`T5`](#t5)

用合成标签和多样图像训练，提升跨 MRI 对比度的形变配准泛化。

---

<a id="p20"></a>
#### ICON: Learning Regular Maps Through Inverse Consistency (ICCV 2021)

[![arXiv: 2105.04459](https://img.shields.io/badge/arXiv-2105.04459-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2105.04459) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/uncbiag/ICON) [![GitHub stars](https://img.shields.io/github/stars/uncbiag/ICON?style=flat-square&label=stars&color=C58A18)](https://github.com/uncbiag/ICON/stargazers) [![GitHub forks](https://img.shields.io/github/forks/uncbiag/ICON?style=flat-square&label=forks&color=64748B)](https://github.com/uncbiag/ICON/forks) &nbsp; [`T5`](#t5)

利用逆一致性损失与随机离网格插值促进空间映射正则化，学习近似微分同胚配准。

---

<a id="p19"></a>
#### Fast Symmetric Diffeomorphic Image Registration with Convolutional Neural Networks (CVPR 2020)

[![arXiv: 2003.09514](https://img.shields.io/badge/arXiv-2003.09514-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2003.09514) &nbsp; [`T5`](#t5)

在对称微分同胚空间中同时估计前向与反向变换，以无监督方式实现快速医学配准。

---

<a id="s021"></a>
#### Large Deformation Diffeomorphic Image Registration with Laplacian Pyramid Networks (MICCAI 2020)

[![arXiv: 2006.16148](https://img.shields.io/badge/arXiv-2006.16148-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2006.16148) &nbsp; [`T5`](#t5)

在拉普拉斯金字塔中由粗到细估计形变，并在微分同胚映射空间逐级完成医学图像配准。

---

<a id="c18"></a>
#### VoxelMorph: A Learning Framework for Deformable Medical Image Registration (IEEE TMI 2019)

[![arXiv: 1809.05231](https://img.shields.io/badge/arXiv-1809.05231-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1809.05231) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://voxelmorph.csail.mit.edu/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/voxelmorph/voxelmorph) [![GitHub stars](https://img.shields.io/github/stars/voxelmorph/voxelmorph?style=flat-square&label=stars&color=C58A18)](https://github.com/voxelmorph/voxelmorph/stargazers) [![GitHub forks](https://img.shields.io/github/forks/voxelmorph/voxelmorph?style=flat-square&label=forks&color=64748B)](https://github.com/voxelmorph/voxelmorph/forks) &nbsp; [`T5`](#t5)

将逐对优化摊销为网络预测形变场，结合可微 warp 与图像相似性训练。

---

<a id="p18"></a>
#### A deep learning framework for unsupervised affine and deformable image registration (Medical Image Analysis 2019)

[![arXiv: 1809.06130](https://img.shields.io/badge/arXiv-1809.06130-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1809.06130) &nbsp; [`T2`](#t2) [`T5`](#t5)

结合全局仿射与局部非刚性网络，以图像相似性训练无监督医学配准框架。

---

<a id="c11"></a>
#### Diffeomorphic demons: Efficient non-parametric image registration (NeuroImage 2009)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1016/j.neuroimage.2008.10.040) &nbsp; [`T5`](#t5)

在 Demons 框架中使用微分同胚更新，兼顾高效非参数配准与平滑可逆变形。

---

<a id="c10"></a>
#### Symmetric Diffeomorphic Image Registration with Cross-Correlation: Evaluating Automated Labeling of Elderly and Neurodegenerative Brain (Medical Image Analysis 2008)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2276735/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ANTsX/ANTs) [![GitHub stars](https://img.shields.io/github/stars/ANTsX/ANTs?style=flat-square&label=stars&color=C58A18)](https://github.com/ANTsX/ANTs/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ANTsX/ANTs?style=flat-square&label=forks&color=64748B)](https://github.com/ANTsX/ANTs/forks) &nbsp; [`T5`](#t5)

对称微分同胚配准，结合互相关用于解剖图像对齐，是 ANTs 的代表性方法。

---

<a id="c26"></a>
#### Computing Large Deformation Metric Mappings via Geodesic Flows of Diffeomorphisms (IJCV 2005)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.cs.jhu.edu/~misha/ReadingSeminar/Papers/Beg05.pdf) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://www.cis.jhu.edu/software/lddmm-volume/index.php) &nbsp; [`T5`](#t5)

Beg 等通过平滑速度场的时间积分与测地流构造大形变微分同胚映射，是计算解剖的重要基础。

---

<a id="c07"></a>
#### Nonrigid registration using free-form deformations: application to breast MR images (IEEE TMI 1999)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1109/42.796284) &nbsp; [`T2`](#t2) [`T5`](#t5)

Rueckert 等将全局仿射与局部 B-spline FFD 结合，用于乳腺 MR 非刚性配准。

---

<a id="p17"></a>
#### Image matching as a diffusion process: an analogy with Maxwell's demons (Medical Image Analysis 1998)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1016/s1361-8415(98)80022-4) &nbsp; [`T5`](#t5)

以扩散过程类比构造稠密图像匹配更新，为医学图像非刚性配准提供经典迭代方法。

[↑ 2.3 本类开头](#topic-medical-registration) · [↑ 返回 Topic 导航](#topics)

---

<a id="area-video-processing"></a>
## 3. 视频处理与人物形变

<a id="topic-06"></a>
<a id="topic-07"></a>
<a id="topic-video-restoration"></a>
### 3.1 视频插帧与复原

> **本类关注** · 插帧、超分、去噪、补全、跨帧特征对齐与视频逆问题
>
> **18 篇论文 · 按年份从新到旧排列**

---

<a id="s028"></a>
#### HomoGen: Enhanced Video Inpainting via Homography Propagation and Diffusion (CVPR 2025)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content/CVPR2025/html/Ding_HomoGen_Enhanced_Video_Inpainting_via_Homography_Propagation_and_Diffusion_CVPR_2025_paper.html) &nbsp; [`T1`](#t1) [`T9`](#t9)

通过单应性配准传播上下文像素，将所得结构先验以自适应强度注入视频扩散修复过程。

---

<a id="s029"></a>
#### BiM-VFI: Bidirectional Motion Field-Guided Frame Interpolation for Video with Non-uniform Motions (CVPR 2025)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content/CVPR2025/html/Seo_BiM-VFI_Bidirectional_Motion_Field-Guided_Frame_Interpolation_for_Video_with_Non-uniform_CVPR_2025_paper.html) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://kaist-viclab.github.io/BiM-VFI_site/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/KAIST-VICLab/BiM-VFI) [![GitHub stars](https://img.shields.io/github/stars/KAIST-VICLab/BiM-VFI?style=flat-square&label=stars&color=C58A18)](https://github.com/KAIST-VICLab/BiM-VFI/stargazers) [![GitHub forks](https://img.shields.io/github/forks/KAIST-VICLab/BiM-VFI?style=flat-square&label=forks&color=64748B)](https://github.com/KAIST-VICLab/BiM-VFI/forks) &nbsp; [`T4`](#t4)

用双向运动场描述非匀速运动，结合流估计、内容自适应上采样和蒸馏来生成中间帧。

---

<a id="n17"></a>
#### Warped Diffusion: Solving Video Inverse Problems with Image Diffusion Models (NeurIPS 2024)

[![arXiv: 2410.16152](https://img.shields.io/badge/arXiv-2410.16152-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2410.16152) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2410.16152) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://giannisdaras.github.io/warped_diffusion.github.io/) &nbsp; [`T9`](#t9)

用连续函数空间和变换等变性处理视频逆问题，以测试时自等变引导提高时序一致性。

---

<a id="s027"></a>
#### Coherent Video Inpainting Using Optical Flow-Guided Efficient Diffusion (arXiv 2024)

[![arXiv: 2412.00857](https://img.shields.io/badge/arXiv-2412.00857-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2412.00857) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2412.00857) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://nevsnev.github.io/FloED/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/NevSNev/FloED-main) [![GitHub stars](https://img.shields.io/github/stars/NevSNev/FloED-main?style=flat-square&label=stars&color=C58A18)](https://github.com/NevSNev/FloED-main/stargazers) [![GitHub forks](https://img.shields.io/github/forks/NevSNev/FloED-main?style=flat-square&label=forks&color=64748B)](https://github.com/NevSNev/FloED-main/forks) &nbsp; [`T4`](#t4) [`T9`](#t9)

以光流补全分支和多尺度流适配器引导视频修复，并用流 Warping 的潜变量插值加速去噪。

---

<a id="s030"></a>
#### Upscale-A-Video: Temporal-Consistent Diffusion Model for Real-World Video Super-Resolution (CVPR 2024)

[![arXiv: 2312.06640](https://img.shields.io/badge/arXiv-2312.06640-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2312.06640) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2312.06640) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://shangchenzhou.com/projects/upscale-a-video/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sczhou/Upscale-A-Video) [![GitHub stars](https://img.shields.io/github/stars/sczhou/Upscale-A-Video?style=flat-square&label=stars&color=C58A18)](https://github.com/sczhou/Upscale-A-Video/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sczhou/Upscale-A-Video?style=flat-square&label=forks&color=64748B)](https://github.com/sczhou/Upscale-A-Video/forks) &nbsp; [`T4`](#t4) [`T9`](#t9)

结合局部时序层与全局光流引导的循环潜变量传播，在扩散视频超分中保持跨帧一致性。

---

<a id="s024"></a>
#### ProPainter: Improving Propagation and Transformer for Video Inpainting (ICCV 2023)

[![arXiv: 2309.03897](https://img.shields.io/badge/arXiv-2309.03897-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2309.03897) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2309.03897) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://shangchenzhou.com/projects/ProPainter/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sczhou/ProPainter) [![GitHub stars](https://img.shields.io/github/stars/sczhou/ProPainter?style=flat-square&label=stars&color=C58A18)](https://github.com/sczhou/ProPainter/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sczhou/ProPainter?style=flat-square&label=forks&color=64748B)](https://github.com/sczhou/ProPainter/forks) &nbsp; [`T4`](#t4) [`T8`](#t8)

结合循环光流补全、图像与特征双域 Warping，以及稀疏视频 Transformer，实现视频内容修复。

---

<a id="n04"></a>
#### FILM: Frame Interpolation for Large Motion (ECCV 2022)

[![arXiv: 2202.04901](https://img.shields.io/badge/arXiv-2202.04901-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2202.04901) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2202.04901) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://film-net.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/google-research/frame-interpolation) [![GitHub stars](https://img.shields.io/github/stars/google-research/frame-interpolation?style=flat-square&label=stars&color=C58A18)](https://github.com/google-research/frame-interpolation/stargazers) [![GitHub forks](https://img.shields.io/github/forks/google-research/frame-interpolation?style=flat-square&label=forks&color=64748B)](https://github.com/google-research/frame-interpolation/forks) &nbsp; [`T4`](#t4) [`T8`](#t8)

跨尺度共享的特征与运动估计，提高大运动插帧能力；可仅从图像帧训练。

---

<a id="n07"></a>
#### BasicVSR++: Improving Video Super-Resolution with Enhanced Propagation and Alignment (CVPR 2022)

[![arXiv: 2104.13371](https://img.shields.io/badge/arXiv-2104.13371-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2104.13371) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2104.13371) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ckkelvinchan/BasicVSR_PlusPlus) [![GitHub stars](https://img.shields.io/github/stars/ckkelvinchan/BasicVSR_PlusPlus?style=flat-square&label=stars&color=C58A18)](https://github.com/ckkelvinchan/BasicVSR_PlusPlus/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ckkelvinchan/BasicVSR_PlusPlus?style=flat-square&label=forks&color=64748B)](https://github.com/ckkelvinchan/BasicVSR_PlusPlus/forks) &nbsp; [`T4`](#t4) [`T8`](#t8)

二阶传播与 flow-guided deformable alignment，把光流先验与可形变特征采样结合。

---

<a id="p23"></a>
#### Real-Time Intermediate Flow Estimation for Video Frame Interpolation (ECCV 2022)

[![arXiv: 2011.06294](https://img.shields.io/badge/arXiv-2011.06294-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2011.06294) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2011.06294) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/megvii-research/ECCV2022-RIFE) [![GitHub stars](https://img.shields.io/github/stars/megvii-research/ECCV2022-RIFE?style=flat-square&label=stars&color=C58A18)](https://github.com/megvii-research/ECCV2022-RIFE/stargazers) [![GitHub forks](https://img.shields.io/github/forks/megvii-research/ECCV2022-RIFE?style=flat-square&label=forks&color=64748B)](https://github.com/megvii-research/ECCV2022-RIFE/forks) &nbsp; [`T4`](#t4)

直接估计任意中间时刻的光流，结合特权蒸馏和时间编码实现高效视频插帧。

---

<a id="s025"></a>
#### Towards An End-to-End Framework for Flow-Guided Video Inpainting (CVPR 2022)

[![arXiv: 2204.02663](https://img.shields.io/badge/arXiv-2204.02663-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2204.02663) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2204.02663) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MCG-NKU/E2FGVI) [![GitHub stars](https://img.shields.io/github/stars/MCG-NKU/E2FGVI?style=flat-square&label=stars&color=C58A18)](https://github.com/MCG-NKU/E2FGVI/stargazers) [![GitHub forks](https://img.shields.io/github/forks/MCG-NKU/E2FGVI?style=flat-square&label=forks&color=64748B)](https://github.com/MCG-NKU/E2FGVI/forks) &nbsp; [`T4`](#t4) [`T8`](#t8)

联合训练光流补全、对齐特征传播和内容补全模块，构成端到端的流引导视频修复框架。

---

<a id="p25"></a>
#### BasicVSR: The Search for Essential Components in Video Super-Resolution and Beyond (CVPR 2021)

[![arXiv: 2012.02181](https://img.shields.io/badge/arXiv-2012.02181-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2012.02181) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ckkelvinchan/BasicVSR-IconVSR) [![GitHub stars](https://img.shields.io/github/stars/ckkelvinchan/BasicVSR-IconVSR?style=flat-square&label=stars&color=C58A18)](https://github.com/ckkelvinchan/BasicVSR-IconVSR/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ckkelvinchan/BasicVSR-IconVSR?style=flat-square&label=forks&color=64748B)](https://github.com/ckkelvinchan/BasicVSR-IconVSR/forks) &nbsp; [`T4`](#t4)

系统分析传播、对齐、聚合与上采样，以双向特征传播和光流 Warping 构建视频超分基线。

---

<a id="c19"></a>
#### Softmax Splatting for Video Frame Interpolation (CVPR 2020)

[![arXiv: 2003.05534](https://img.shields.io/badge/arXiv-2003.05534-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2003.05534) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://sniklaus.com/softsplat) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sniklaus/softmax-splatting) [![GitHub stars](https://img.shields.io/github/stars/sniklaus/softmax-splatting?style=flat-square&label=stars&color=C58A18)](https://github.com/sniklaus/softmax-splatting/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sniklaus/softmax-splatting?style=flat-square&label=forks&color=64748B)](https://github.com/sniklaus/softmax-splatting/forks) &nbsp; [`T7`](#t7)

Niklaus–Liu 用 softmax 加权处理 forward warp 的多对一冲突，并支持图像和特征的可微前向投影。

---

<a id="p22"></a>
#### Depth-Aware Video Frame Interpolation (CVPR 2019)

[![arXiv: 1904.00830](https://img.shields.io/badge/arXiv-1904.00830-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1904.00830) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/baowenbo/DAIN) [![GitHub stars](https://img.shields.io/github/stars/baowenbo/DAIN?style=flat-square&label=stars&color=C58A18)](https://github.com/baowenbo/DAIN/stargazers) [![GitHub forks](https://img.shields.io/github/forks/baowenbo/DAIN?style=flat-square&label=forks&color=64748B)](https://github.com/baowenbo/DAIN/forks) &nbsp; [`T4`](#t4) [`T6`](#t6) [`T7`](#t7)

在光流投影时利用深度优先处理近处物体，并融合 Warping 后的图像与上下文特征生成中间帧。

---

<a id="p24"></a>
#### EDVR: Video Restoration with Enhanced Deformable Convolutional Networks (CVPR Workshops 2019)

[![arXiv: 1905.02716](https://img.shields.io/badge/arXiv-1905.02716-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1905.02716) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/xinntao/EDVR) [![GitHub stars](https://img.shields.io/github/stars/xinntao/EDVR?style=flat-square&label=stars&color=C58A18)](https://github.com/xinntao/EDVR/stargazers) [![GitHub forks](https://img.shields.io/github/forks/xinntao/EDVR?style=flat-square&label=forks&color=64748B)](https://github.com/xinntao/EDVR/forks) &nbsp; [`T4`](#t4) [`T8`](#t8)

以金字塔级联可形变对齐处理跨帧大运动，再用时空注意力融合实现视频复原。

---

<a id="p26"></a>
#### Video Enhancement with Task-Oriented Flow (IJCV 2019)

[![arXiv: 1711.09078](https://img.shields.io/badge/arXiv-1711.09078-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1711.09078) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/1711.09078) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/anchen1011/toflow) [![GitHub stars](https://img.shields.io/github/stars/anchen1011/toflow?style=flat-square&label=stars&color=C58A18)](https://github.com/anchen1011/toflow/stargazers) [![GitHub forks](https://img.shields.io/github/forks/anchen1011/toflow?style=flat-square&label=forks&color=64748B)](https://github.com/anchen1011/toflow/forks) &nbsp; [`T4`](#t4)

针对复原目标联合学习运动表示与视频处理网络，使跨帧 Warping 服务于插帧、去噪和超分任务。

---

<a id="s026"></a>
#### Deep Flow-Guided Video Inpainting (CVPR 2019)

[![arXiv: 1905.02884](https://img.shields.io/badge/arXiv-1905.02884-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1905.02884) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/1905.02884) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://nbei.github.io/video-inpainting.html) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nbei/Deep-Flow-Guided-Video-Inpainting) [![GitHub stars](https://img.shields.io/github/stars/nbei/Deep-Flow-Guided-Video-Inpainting?style=flat-square&label=stars&color=C58A18)](https://github.com/nbei/Deep-Flow-Guided-Video-Inpainting/stargazers) [![GitHub forks](https://img.shields.io/github/forks/nbei/Deep-Flow-Guided-Video-Inpainting?style=flat-square&label=forks&color=64748B)](https://github.com/nbei/Deep-Flow-Guided-Video-Inpainting/forks) &nbsp; [`T4`](#t4)

先补全时空连续的光流，再沿完整流场传播可见像素，修复视频中被遮罩的内容。

---

<a id="p21"></a>
#### Super SloMo: High Quality Estimation of Multiple Intermediate Frames for Video Interpolation (CVPR 2018)

[![arXiv: 1712.00080](https://img.shields.io/badge/arXiv-1712.00080-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1712.00080) &nbsp; [`T4`](#t4)

联合估计双向光流、任意中间时刻光流和软可见性，通过 Warping 与融合生成多帧慢动作。

---

<a id="c14"></a>
#### Deformable Convolutional Networks (ICCV 2017)

[![arXiv: 1703.06211](https://img.shields.io/badge/arXiv-1703.06211-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1703.06211) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/msracver/Deformable-ConvNets) [![GitHub stars](https://img.shields.io/github/stars/msracver/Deformable-ConvNets?style=flat-square&label=stars&color=C58A18)](https://github.com/msracver/Deformable-ConvNets/stargazers) [![GitHub forks](https://img.shields.io/github/forks/msracver/Deformable-ConvNets?style=flat-square&label=forks&color=64748B)](https://github.com/msracver/Deformable-ConvNets/forks) &nbsp; [`T8`](#t8)

为卷积采样位置学习 offset，使特征支持局部几何适应。

---

<details>
<summary>关联阅读 · 7 篇其他 Topic 的论文</summary>

- [Global Motion Aggregation (GMA)](#p11) (2021)
- [RAFT](#c20) (2020)
- [PWC-Net](#c15) (2018)
- [LiteFlowNet](#p10) (2018)
- [FlowNet 2.0](#p08) (2017)
- [SPyNet](#p09) (2017)
- [FlowNet](#p07) (2015)

</details>

[↑ 3.1 本类开头](#topic-video-restoration) · [↑ 返回 Topic 导航](#topics)

---

<a id="topic-09"></a>
<a id="topic-10"></a>
<a id="topic-human-deformation"></a>
### 3.2 人物动画、运动迁移与虚拟试衣

> **本类关注** · 人物驱动、外观保持、姿态迁移与服装对齐
>
> **16 篇论文 · 按年份从新到旧排列**

---

<a id="s032"></a>
#### Learning Implicit Features with Flow-Infused Transformations for Realistic Virtual Try-On (ICCV 2025)

[![arXiv: 2412.11435](https://img.shields.io/badge/arXiv-2412.11435-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2412.11435) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2412.11435) &nbsp; [`T4`](#t4) [`T9`](#t9)

将稠密 warp flow 与服装特征注入 Flow Infused Attention，以隐式空间引导替代对变形服装图像的完全依赖。

---

<a id="n18"></a>
#### StableVITON: Learning Semantic Correspondence with Latent Diffusion Model for Virtual Try-On (CVPR 2024)

[![arXiv: 2312.01725](https://img.shields.io/badge/arXiv-2312.01725-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2312.01725) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2312.01725) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/rlawjdghek/StableVITON) [![GitHub stars](https://img.shields.io/github/stars/rlawjdghek/StableVITON?style=flat-square&label=stars&color=C58A18)](https://github.com/rlawjdghek/StableVITON/stargazers) [![GitHub forks](https://img.shields.io/github/forks/rlawjdghek/StableVITON?style=flat-square&label=forks&color=64748B)](https://github.com/rlawjdghek/StableVITON/forks) &nbsp; [`T9`](#t9)

在扩散 latent 中学习服装与人体的语义对应，以 attention 实现隐式对齐与细节传递。

---

<a id="s033"></a>
#### FloAt: Flow Warping of Self-Attention for Clothing Animation Generation (arXiv 2024)

[![arXiv: 2411.15028](https://img.shields.io/badge/arXiv-2411.15028-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2411.15028) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2411.15028) &nbsp; [`T4`](#t4) [`T9`](#t9)

从连续法线图估计光流，Warp 前一帧的自注意力特征并与当前帧融合，以生成一致的服装动画。

---

<a id="s036"></a>
#### D4-VTON: Dynamic Semantics Disentangling for Differential Diffusion based Virtual Try-On (ECCV 2024)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6231_ECCV_2024_paper.php) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Jerome-Young/D4-VTON) [![GitHub stars](https://img.shields.io/github/stars/Jerome-Young/D4-VTON?style=flat-square&label=stars&color=C58A18)](https://github.com/Jerome-Young/D4-VTON/stargazers) [![GitHub forks](https://img.shields.io/github/forks/Jerome-Young/D4-VTON?style=flat-square&label=forks&color=64748B)](https://github.com/Jerome-Young/D4-VTON/forks) &nbsp; [`T4`](#t4) [`T9`](#t9)

自发现服装语义层并预测分层局部流，再以差分信息跟踪改善扩散试衣中的服装细节。

---

<a id="s031"></a>
#### Taming the Power of Diffusion Models for High-Quality Virtual Try-On with Appearance Flow (ACM MM 2023)

[![arXiv: 2308.06101](https://img.shields.io/badge/arXiv-2308.06101-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2308.06101) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2308.06101) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/bcmi/DCI-VTON-Virtual-Try-On) [![GitHub stars](https://img.shields.io/github/stars/bcmi/DCI-VTON-Virtual-Try-On?style=flat-square&label=stars&color=C58A18)](https://github.com/bcmi/DCI-VTON-Virtual-Try-On/stargazers) [![GitHub forks](https://img.shields.io/github/forks/bcmi/DCI-VTON-Virtual-Try-On?style=flat-square&label=forks&color=64748B)](https://github.com/bcmi/DCI-VTON-Virtual-Try-On/forks) &nbsp; [`T4`](#t4) [`T9`](#t9)

用外观流显式变形服装图像，将对齐后的服装作为输入和局部条件引导扩散试衣。

---

<a id="s035"></a>
#### GP-VTON: Towards General Purpose Virtual Try-on via Collaborative Local-Flow Global-Parsing Learning (CVPR 2023)

[![arXiv: 2303.13756](https://img.shields.io/badge/arXiv-2303.13756-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2303.13756) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2303.13756) &nbsp; [`T4`](#t4) [`T9`](#t9)

以局部流与全局解析协同学习服装部件对齐，并通过动态梯度截断减轻边界处纹理挤压。

---

<a id="n03"></a>
#### Thin-Plate Spline Motion Model for Image Animation (CVPR 2022)

[![arXiv: 2203.14367](https://img.shields.io/badge/arXiv-2203.14367-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2203.14367) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2203.14367) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/yoyo-nb/Thin-Plate-Spline-Motion-Model) [![GitHub stars](https://img.shields.io/github/stars/yoyo-nb/Thin-Plate-Spline-Motion-Model?style=flat-square&label=stars&color=C58A18)](https://github.com/yoyo-nb/Thin-Plate-Spline-Motion-Model/stargazers) [![GitHub forks](https://img.shields.io/github/forks/yoyo-nb/Thin-Plate-Spline-Motion-Model?style=flat-square&label=forks&color=64748B)](https://github.com/yoyo-nb/Thin-Plate-Spline-Motion-Model/forks) &nbsp; [`T2`](#t2) [`T8`](#t8)

从局部仿射运动扩展到多个 TPS 变换，并结合多尺度遮挡掩码进行特征形变。

---

<a id="s034"></a>
#### High-Resolution Virtual Try-On with Misalignment and Occlusion-Handled Conditions (ECCV 2022)

[![arXiv: 2206.14180](https://img.shields.io/badge/arXiv-2206.14180-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2206.14180) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2206.14180) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sangyun884/hr-viton) [![GitHub stars](https://img.shields.io/github/stars/sangyun884/hr-viton?style=flat-square&label=stars&color=C58A18)](https://github.com/sangyun884/hr-viton/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sangyun884/hr-viton?style=flat-square&label=forks&color=64748B)](https://github.com/sangyun884/hr-viton/forks) &nbsp; [`T4`](#t4) [`T9`](#t9)

在同一条件生成器中交互学习服装变形与人体分割，缓解错位和遮挡处的纹理挤压。

---

<a id="s078"></a>
#### ClothFormer: Taming Video Virtual Try-On in All Module (CVPR 2022)

[![arXiv: 2204.12151](https://img.shields.io/badge/arXiv-2204.12151-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2204.12151) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://cloth-former.github.io) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/luxiangju-PersonAI/ClothFormer) [![GitHub stars](https://img.shields.io/github/stars/luxiangju-PersonAI/ClothFormer?style=flat-square&label=stars&color=C58A18)](https://github.com/luxiangju-PersonAI/ClothFormer/stargazers) [![GitHub forks](https://img.shields.io/github/forks/luxiangju-PersonAI/ClothFormer?style=flat-square&label=forks&color=64748B)](https://github.com/luxiangju-PersonAI/ClothFormer/forks) &nbsp; [`T4`](#t4) [`T9`](#t9)

通过抗遮挡外观流 Warping、流序列平滑与双流 Transformer，生成时空一致的视频试衣结果。

---

<a id="p29"></a>
#### Parser-Free Virtual Try-on via Distilling Appearance Flows (CVPR 2021)

[![arXiv: 2103.04559](https://img.shields.io/badge/arXiv-2103.04559-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2103.04559) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/geyuying/PF-AFN) [![GitHub stars](https://img.shields.io/github/stars/geyuying/PF-AFN?style=flat-square&label=stars&color=C58A18)](https://github.com/geyuying/PF-AFN/stargazers) [![GitHub forks](https://img.shields.io/github/forks/geyuying/PF-AFN?style=flat-square&label=forks&color=64748B)](https://github.com/geyuying/PF-AFN/forks) &nbsp; [`T4`](#t4) [`T9`](#t9)

通过教师—辅导—学生蒸馏学习服装与人体的外观流，使推理阶段不再依赖人体解析。

---

<a id="s037"></a>
#### One-Shot Free-View Neural Talking-Head Synthesis for Video Conferencing (CVPR 2021)

[![arXiv: 2011.15126](https://img.shields.io/badge/arXiv-2011.15126-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2011.15126) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2011.15126) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://nvlabs.github.io/face-vid2vid/) &nbsp; [`T8`](#t8)

分解身份与运动关键点，用三维运动表示构造稠密形变并搬运源图像特征，生成可控人像视频。

---

<a id="p28"></a>
#### Towards Photo-Realistic Virtual Try-On by Adaptively Generating-Preserving Image Content (CVPR 2020)

[![arXiv: 2003.05863](https://img.shields.io/badge/arXiv-2003.05863-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2003.05863) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2003.05863) &nbsp; [`T2`](#t2) [`T9`](#t9)

根据试衣后的语义布局选择生成或保留内容，并用服装 Warping 与融合处理姿态和遮挡变化。

---

<a id="c17"></a>
#### First Order Motion Model for Image Animation (NeurIPS 2019)

[![arXiv: 2003.00196](https://img.shields.io/badge/arXiv-2003.00196-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2003.00196) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2003.00196) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://aliaksandrsiarohin.github.io/first-order-model-website/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AliaksandrSiarohin/first-order-model) [![GitHub stars](https://img.shields.io/github/stars/AliaksandrSiarohin/first-order-model?style=flat-square&label=stars&color=C58A18)](https://github.com/AliaksandrSiarohin/first-order-model/stargazers) [![GitHub forks](https://img.shields.io/github/forks/AliaksandrSiarohin/first-order-model?style=flat-square&label=forks&color=64748B)](https://github.com/AliaksandrSiarohin/first-order-model/forks) &nbsp; [`T8`](#t8) [`T9`](#t9)

自学习关键点与局部一阶仿射运动，构造稠密特征 warp 和遮挡图实现图像动画。

---

<a id="c24"></a>
#### Toward Characteristic-Preserving Image-based Virtual Try-On Network (ECCV 2018)

[![arXiv: 1807.07688](https://img.shields.io/badge/arXiv-1807.07688-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1807.07688) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/1807.07688) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sergeywong/cp-vton) [![GitHub stars](https://img.shields.io/github/stars/sergeywong/cp-vton?style=flat-square&label=stars&color=C58A18)](https://github.com/sergeywong/cp-vton/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sergeywong/cp-vton?style=flat-square&label=forks&color=64748B)](https://github.com/sergeywong/cp-vton/forks) &nbsp; [`T2`](#t2) [`T9`](#t9)

用 Geometric Matching Module 学习 TPS，将商品服装形变到人体，再学习融合掩码。

---

<a id="p27"></a>
#### VITON: An Image-based Virtual Try-on Network (CVPR 2018)

[![arXiv: 1711.08447](https://img.shields.io/badge/arXiv-1711.08447-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1711.08447) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/xthan/VITON) [![GitHub stars](https://img.shields.io/github/stars/xthan/VITON?style=flat-square&label=stars&color=C58A18)](https://github.com/xthan/VITON/stargazers) [![GitHub forks](https://img.shields.io/github/forks/xthan/VITON?style=flat-square&label=forks&color=64748B)](https://github.com/xthan/VITON/forks) &nbsp; [`T2`](#t2) [`T9`](#t9)

利用粗到细生成、服装形变与融合，将服装图像迁移到目标人物并保留纹理细节。

---

<a id="p30"></a>
#### X2Face: A network for controlling face generation using images, audio, and pose codes (ECCV 2018)

[![arXiv: 1807.10550](https://img.shields.io/badge/arXiv-1807.10550-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1807.10550) &nbsp; [`T8`](#t8) [`T9`](#t9)

学习源人脸的嵌入表示及驱动采样场，通过空间重采样实现图像、姿态或音频驱动的人脸动画。

---

<details>
<summary>关联阅读 · 4 篇其他 Topic 的论文</summary>

- [Go-with-the-Flow](#n19) (2025)
- [Bounded Biharmonic Weights (BBW)](#p03) (2011)
- [Green Coordinates](#s002) (2008)
- [Harmonic Coordinates](#s001) (2007)

</details>

[↑ 3.2 本类开头](#topic-human-deformation) · [↑ 返回 Topic 导航](#topics)

---

<a id="area-video-generation"></a>
## 4. 视频生成与运动控制


<a id="topic-noise-warping"></a>
### 4.1 噪声 Warping 与时序一致性

> **本类关注** · 随机场输运、噪声统计、运动相关噪声与跨帧一致性
>
> **11 篇论文 · 按年份从新到旧排列**

---

<a id="s043"></a>
#### Infinite-Resolution Integral Noise Warping for Diffusion Models (ICLR 2025)

[![arXiv: 2411.01212](https://img.shields.io/badge/arXiv-2411.01212-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2411.01212) &nbsp; [`T9`](#t9)

分析积分噪声 Warping 的无限分辨率极限，以 Brownian bridge 增量构造高效、分布保持的噪声输运。

---

<a id="s044"></a>
#### On Equivariance and Fast Sampling in Video Diffusion Models Trained with Warped Noise (arXiv 2025)

[![arXiv: 2504.09789](https://img.shields.io/badge/arXiv-2504.09789-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.09789) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2504.09789) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://research.nvidia.com/labs/genair/equivdm/) &nbsp; [`T9`](#t9)

分析相关 Warping 噪声训练如何促进空间等变性，并将该性质用于高效视频生成与采样蒸馏。

---

<a id="n16"></a>
#### How I Warped Your Noise: a Temporally-Correlated Noise Prior for Diffusion Models (ICLR 2024)

[![arXiv: 2504.03072](https://img.shields.io/badge/arXiv-2504.03072-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.03072) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://warpyournoise.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/mskwak01/How-I-Warped-Your-Noise-Unofficial) [![GitHub stars](https://img.shields.io/github/stars/mskwak01/How-I-Warped-Your-Noise-Unofficial?style=flat-square&label=stars&color=C58A18)](https://github.com/mskwak01/How-I-Warped-Your-Noise-Unofficial/stargazers) [![GitHub forks](https://img.shields.io/github/forks/mskwak01/How-I-Warped-Your-Noise-Unofficial?style=flat-square&label=forks&color=64748B)](https://github.com/mskwak01/How-I-Warped-Your-Noise-Unofficial/forks) &nbsp; [`T7`](#t7) [`T9`](#t9)

把像素噪声解释为连续白噪声场的区域积分，设计面向 Gaussian 统计的输运，兼顾运动相关性和噪声性质。

---

<a id="p32"></a>
#### FreeNoise: Tuning-Free Longer Video Diffusion via Noise Rescheduling (ICLR 2024)

[![arXiv: 2310.15169](https://img.shields.io/badge/arXiv-2310.15169-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2310.15169) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2310.15169) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AILab-CVC/FreeNoise) [![GitHub stars](https://img.shields.io/github/stars/AILab-CVC/FreeNoise?style=flat-square&label=stars&color=C58A18)](https://github.com/AILab-CVC/FreeNoise/stargazers) [![GitHub forks](https://img.shields.io/github/forks/AILab-CVC/FreeNoise?style=flat-square&label=forks&color=64748B)](https://github.com/AILab-CVC/FreeNoise/forks) &nbsp; [`T9`](#t9)

通过重调度初始噪声形成长程相关，并结合窗口时序注意力扩展预训练视频扩散模型的生成长度。

---

<a id="p33"></a>
#### ConsistI2V: Enhancing Visual Consistency for Image-to-Video Generation (TMLR 2024)

[![arXiv: 2402.04324](https://img.shields.io/badge/arXiv-2402.04324-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2402.04324) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2402.04324) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/TIGER-AI-Lab/ConsistI2V) [![GitHub stars](https://img.shields.io/github/stars/TIGER-AI-Lab/ConsistI2V?style=flat-square&label=stars&color=C58A18)](https://github.com/TIGER-AI-Lab/ConsistI2V/stargazers) [![GitHub forks](https://img.shields.io/github/forks/TIGER-AI-Lab/ConsistI2V?style=flat-square&label=forks&color=64748B)](https://github.com/TIGER-AI-Lab/ConsistI2V/forks) &nbsp; [`T9`](#t9)

结合首帧时空注意力与低频噪声初始化，改善图生视频中的布局、外观和时序一致性。

---

<a id="s038"></a>
#### FlowVid: Taming Imperfect Optical Flows for Consistent Video-to-Video Synthesis (CVPR 2024)

[![arXiv: 2312.17681](https://img.shields.io/badge/arXiv-2312.17681-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2312.17681) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2312.17681) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://jeff-liangf.github.io/projects/flowvid/) &nbsp; [`T4`](#t4) [`T9`](#t9)

用光流将编辑首帧 Warp 到后续帧，联合深度等空间条件引导扩散模型传播视频编辑。

---

<a id="s039"></a>
#### FLATTEN: optical FLow-guided ATTENtion for consistent text-to-video editing (ICLR 2024)

[![arXiv: 2310.05922](https://img.shields.io/badge/arXiv-2310.05922-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2310.05922) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2310.05922) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://flatten-video-editing.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/yrcong/flatten) [![GitHub stars](https://img.shields.io/github/stars/yrcong/flatten?style=flat-square&label=stars&color=C58A18)](https://github.com/yrcong/flatten/stargazers) [![GitHub forks](https://img.shields.io/github/forks/yrcong/flatten?style=flat-square&label=forks&color=64748B)](https://github.com/yrcong/flatten/forks) &nbsp; [`T4`](#t4) [`T9`](#t9)

让视频中同一光流轨迹上的图像块在注意力模块中相互关联，改善文本引导编辑的跨帧一致性。

---

<a id="s042"></a>
#### WAVE: Warping DDIM Inversion Features for Zero-shot Text-to-Video Editing (ECCV 2024)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9682_ECCV_2024_paper.php) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://ree1s.github.io/wave/) &nbsp; [`T4`](#t4) [`T9`](#t9)

在 DDIM 反演过程中利用光流传播关键帧特征，以获得更一致的反演潜变量并支持视频编辑。

---

<a id="p31"></a>
#### Preserve Your Own Correlation: A Noise Prior for Video Diffusion Models (ICCV 2023)

[![arXiv: 2305.10474](https://img.shields.io/badge/arXiv-2305.10474-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2305.10474) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2305.10474) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://research.nvidia.com/labs/dir/pyoco/) &nbsp; [`T9`](#t9)

设计混合与渐进式时序相关噪声先验，将图像扩散模型适配到视频生成。

---

<a id="s040"></a>
#### LatentWarp: Consistent Diffusion Latents for Zero-Shot Video-to-Video Translation (arXiv 2023)

[![arXiv: 2311.00353](https://img.shields.io/badge/arXiv-2311.00353-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2311.00353) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2311.00353) &nbsp; [`T4`](#t4) [`T9`](#t9)

用光流在扩散潜空间中执行 Warping，约束跨帧 query token，以改善零样本视频翻译。

---

<a id="s041"></a>
#### Rerender A Video: Zero-Shot Text-Guided Video-to-Video Translation (SIGGRAPH Asia / TOG 2023)

[![arXiv: 2306.07954](https://img.shields.io/badge/arXiv-2306.07954-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2306.07954) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2306.07954) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://www.mmlab-ntu.com/project/rerender/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/williamyang1991/Rerender_A_Video) [![GitHub stars](https://img.shields.io/github/stars/williamyang1991/Rerender_A_Video?style=flat-square&label=stars&color=C58A18)](https://github.com/williamyang1991/Rerender_A_Video/stargazers) [![GitHub forks](https://img.shields.io/github/forks/williamyang1991/Rerender_A_Video?style=flat-square&label=forks&color=64748B)](https://github.com/williamyang1991/Rerender_A_Video/forks) &nbsp; [`T4`](#t4) [`T9`](#t9)

对关键帧施加跨帧形状和纹理约束，再通过时序感知的匹配与混合传播完整视频编辑。

---

<details>
<summary>关联阅读 · 9 篇其他 Topic 的论文</summary>

- [CameraNoise](#n24) (2026)
- [Go-with-the-Flow](#n19) (2025)
- [FIA-VTON](#s032) (2025)
- [FloED](#s027) (2024)
- [Upscale-A-Video](#s030) (2024)
- [FloAt](#s033) (2024)
- [MotionCraft](#s046) (2024)
- [ProPainter](#s024) (2023)
- [ClothFormer](#s078) (2022)

</details>

[↑ 4.1 本类开头](#topic-noise-warping) · [↑ 返回 Topic 导航](#topics)

---

<a id="topic-14"></a>
<a id="topic-controlled-generation"></a>
### 4.2 相机、轨迹与运动可控生成

> **本类关注** · 相机控制、物体运动控制、几何引导与历史帧对齐
>
> **13 篇论文 · 按年份从新到旧排列**

---

<a id="n24"></a>
#### CameraNoise: Enabling Faithful Camera Control in Video Diffusion through Geometry-Flow-Guided Noise Warping (ICML 2026)

[![arXiv: 2605.30774](https://img.shields.io/badge/arXiv-2605.30774-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.30774) [![Hugging Face: Model](https://img.shields.io/badge/Hugging%20Face-Model-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/gulucaptain/CameraNoise-I2V) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://gulucaptain.github.io/CameraNoise/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/gulucaptain/CameraNoise) [![GitHub stars](https://img.shields.io/github/stars/gulucaptain/CameraNoise?style=flat-square&label=stars&color=C58A18)](https://github.com/gulucaptain/CameraNoise/stargazers) [![GitHub forks](https://img.shields.io/github/forks/gulucaptain/CameraNoise?style=flat-square&label=forks&color=64748B)](https://github.com/gulucaptain/CameraNoise/forks) &nbsp; [`T6`](#t6) [`T9`](#t9)

以 Geometry-guided Reprojection Flow 与噪声 warping 将相机运动编码到时序相关噪声中，同时关注 Gaussian 先验与轨迹控制。

---

<a id="n27"></a>
#### Warp-as-History: Generalizable Camera-Controlled Video Generation from One Training Video (arXiv 2026)

[![arXiv: 2605.15182](https://img.shields.io/badge/arXiv-2605.15182-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.15182) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2605.15182) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://yyfz.github.io/warp-as-history/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/yyfz/Warp-as-History) [![GitHub stars](https://img.shields.io/github/stars/yyfz/Warp-as-History?style=flat-square&label=stars&color=C58A18)](https://github.com/yyfz/Warp-as-History/stargazers) [![GitHub forks](https://img.shields.io/github/forks/yyfz/Warp-as-History?style=flat-square&label=forks&color=64748B)](https://github.com/yyfz/Warp-as-History/forks) &nbsp; [`T6`](#t6) [`T9`](#t9)

将相机诱导的 warp 作为对齐目标位置的伪历史，结合有效 token 选择利用冻结模型的历史输入通路；另探索单视频 LoRA。

---

<a id="n19"></a>
#### Go-with-the-Flow: Motion-Controllable Video Diffusion Models Using Real-Time Warped Noise (CVPR 2025)

[![arXiv: 2501.08331](https://img.shields.io/badge/arXiv-2501.08331-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2501.08331) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2501.08331) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://eyeline-labs.github.io/Go-with-the-Flow/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Eyeline-Labs/Go-with-the-Flow) [![GitHub stars](https://img.shields.io/github/stars/Eyeline-Labs/Go-with-the-Flow?style=flat-square&label=stars&color=C58A18)](https://github.com/Eyeline-Labs/Go-with-the-Flow/stargazers) [![GitHub forks](https://img.shields.io/github/forks/Eyeline-Labs/Go-with-the-Flow?style=flat-square&label=forks&color=64748B)](https://github.com/Eyeline-Labs/Go-with-the-Flow/forks) &nbsp; [`T9`](#t9)

高效生成 warped noise 并微调视频模型，把运动模式作为噪声先验，用于运动迁移及相机/物体控制。

---

<a id="s047"></a>
#### FloVD: Optical Flow Meets Video Diffusion Model for Enhanced Camera-Controlled Video Synthesis (CVPR 2025)

[![arXiv: 2502.08244](https://img.shields.io/badge/arXiv-2502.08244-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.08244) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2502.08244) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://jinwonjoon.github.io/flovd_site/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/JinWonjoon/FloVD) [![GitHub stars](https://img.shields.io/github/stars/JinWonjoon/FloVD?style=flat-square&label=stars&color=C58A18)](https://github.com/JinWonjoon/FloVD/stargazers) [![GitHub forks](https://img.shields.io/github/forks/JinWonjoon/FloVD?style=flat-square&label=forks&color=64748B)](https://github.com/JinWonjoon/FloVD/forks) &nbsp; [`T4`](#t4) [`T9`](#t9)

将相机与物体运动表示为光流，先生成流场，再以流条件视频扩散实现相机控制与动态合成。

---

<a id="s048"></a>
#### TrajectoryCrafter: Redirecting Camera Trajectory for Monocular Videos via Diffusion Models (ICCV 2025)

[![arXiv: 2503.05638](https://img.shields.io/badge/arXiv-2503.05638-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2503.05638) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2503.05638) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://TrajectoryCrafter.github.io) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/TrajectoryCrafter/TrajectoryCrafter) [![GitHub stars](https://img.shields.io/github/stars/TrajectoryCrafter/TrajectoryCrafter?style=flat-square&label=stars&color=C58A18)](https://github.com/TrajectoryCrafter/TrajectoryCrafter/stargazers) [![GitHub forks](https://img.shields.io/github/forks/TrajectoryCrafter/TrajectoryCrafter?style=flat-square&label=forks&color=64748B)](https://github.com/TrajectoryCrafter/TrajectoryCrafter/forks) &nbsp; [`T6`](#t6) [`T9`](#t9)

将源视频与按目标轨迹渲染的点云共同作为扩散条件，并以双重重投影构建训练数据。

---

<a id="s049"></a>
#### Latent-Reframe: Enabling Camera Control for Video Diffusion Models without Training (ICCV 2025)

[![arXiv: 2412.06029](https://img.shields.io/badge/arXiv-2412.06029-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2412.06029) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2412.06029) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://latent-reframe.github.io) &nbsp; [`T6`](#t6) [`T9`](#t9)

通过时间感知点云将视频潜变量重构到目标相机轨迹，再用潜空间修复与协调完成视频生成。

---

<a id="s050"></a>
#### MotionPro: A Precise Motion Controller for Image-to-Video Generation (CVPR 2025)

[![arXiv: 2505.20287](https://img.shields.io/badge/arXiv-2505.20287-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.20287) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2505.20287) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://zhw-zhang.github.io/MotionPro-page/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/HiDream-ai/MotionPro) [![GitHub stars](https://img.shields.io/github/stars/HiDream-ai/MotionPro?style=flat-square&label=stars&color=C58A18)](https://github.com/HiDream-ai/MotionPro/stargazers) [![GitHub forks](https://img.shields.io/github/forks/HiDream-ai/MotionPro?style=flat-square&label=forks&color=64748B)](https://github.com/HiDream-ai/MotionPro/forks) &nbsp; [`T4`](#t4) [`T9`](#t9)

以局部区域轨迹和运动掩码区分物体与相机运动，为视频生成提供精细的运动条件。

---

<a id="p34"></a>
#### MotionCtrl: A Unified and Flexible Motion Controller for Video Generation (SIGGRAPH 2024)

[![arXiv: 2312.03641](https://img.shields.io/badge/arXiv-2312.03641-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2312.03641) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2312.03641) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/TencentARC/MotionCtrl) [![GitHub stars](https://img.shields.io/github/stars/TencentARC/MotionCtrl?style=flat-square&label=stars&color=C58A18)](https://github.com/TencentARC/MotionCtrl/stargazers) [![GitHub forks](https://img.shields.io/github/forks/TencentARC/MotionCtrl?style=flat-square&label=forks&color=64748B)](https://github.com/TencentARC/MotionCtrl/forks) &nbsp; [`T6`](#t6) [`T9`](#t9)

以相机位姿和物体轨迹分别建模相机与物体运动，支持视频生成中的独立控制与组合。

---

<a id="p35"></a>
#### CameraCtrl: Enabling Camera Control for Text-to-Video Generation (ECCV 2024)

[![arXiv: 2404.02101](https://img.shields.io/badge/arXiv-2404.02101-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2404.02101) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2404.02101) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://hehao13.github.io/projects-CameraCtrl/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/hehao13/CameraCtrl) [![GitHub stars](https://img.shields.io/github/stars/hehao13/CameraCtrl?style=flat-square&label=stars&color=C58A18)](https://github.com/hehao13/CameraCtrl/stargazers) [![GitHub forks](https://img.shields.io/github/forks/hehao13/CameraCtrl?style=flat-square&label=forks&color=64748B)](https://github.com/hehao13/CameraCtrl/forks) &nbsp; [`T6`](#t6) [`T9`](#t9)

将相机轨迹编码到可插拔相机模块，在尽量保留基础视频模型的同时实现位姿控制。

---

<a id="p37"></a>
#### DragAnything: Motion Control for Anything using Entity Representation (ECCV 2024)

[![arXiv: 2403.07420](https://img.shields.io/badge/arXiv-2403.07420-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2403.07420) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2403.07420) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/showlab/DragAnything) [![GitHub stars](https://img.shields.io/github/stars/showlab/DragAnything?style=flat-square&label=stars&color=C58A18)](https://github.com/showlab/DragAnything/stargazers) [![GitHub forks](https://img.shields.io/github/forks/showlab/DragAnything?style=flat-square&label=forks&color=64748B)](https://github.com/showlab/DragAnything/forks) &nbsp; [`T4`](#t4) [`T9`](#t9)

利用实体表示将用户绘制的轨迹关联到对象，支持多个对象及背景的运动控制。

---

<a id="s045"></a>
#### Motion-I2V: Consistent and Controllable Image-to-Video Generation with Explicit Motion Modeling (SIGGRAPH 2024)

[![arXiv: 2401.15977](https://img.shields.io/badge/arXiv-2401.15977-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2401.15977) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2401.15977) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://xiaoyushi97.github.io/Motion-I2V/) &nbsp; [`T4`](#t4) [`T9`](#t9)

先预测参考图像像素的运动轨迹，再通过运动增强时序注意力传播特征，并支持稀疏轨迹控制。

---

<a id="s046"></a>
#### MotionCraft: Physics-Based Zero-Shot Video Generation (NeurIPS 2024)

[![arXiv: 2405.13557](https://img.shields.io/badge/arXiv-2405.13557-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2405.13557) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2405.13557) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://mezzelfo.github.io/MotionCraft/) &nbsp; [`T4`](#t4) [`T9`](#t9)

将物理模拟得到的光流作用于扩散噪声潜空间，以零样本方式控制视频中的物理运动。

---

<a id="p36"></a>
#### DragNUWA: Fine-grained Control in Video Generation by Integrating Text, Image, and Trajectory (arXiv 2023)

[![arXiv: 2308.08089](https://img.shields.io/badge/arXiv-2308.08089-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2308.08089) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2308.08089) &nbsp; [`T4`](#t4) [`T9`](#t9)

融合文本、图像与轨迹条件，通过轨迹采样和多尺度控制实现开放域运动引导。

---

<details>
<summary>关联阅读 · 11 篇其他 Topic 的论文</summary>

- [Inpaint4Drag](#s003) (2025)
- [FlowDrag](#s004) (2025)
- [EquiVDM / Warped-Noise Equivariance](#s044) (2025)
- [How I Warped Your Noise / ∫-noise](#n16) (2024)
- [ConsistI2V](#p33) (2024)
- [DragDiffusion](#s005) (2024)
- [FloAt](#s033) (2024)
- [FlowVid](#s038) (2024)
- [face-vid2vid](#s037) (2021)
- [RAFT](#c20) (2020)
- [Softmax Splatting](#c19) (2020)

</details>

[↑ 4.2 本类开头](#topic-controlled-generation) · [↑ 返回 Topic 导航](#topics)

---

<a id="area-spatial-intelligence"></a>
## 5. 空间智能

<a id="topic-11"></a>
<a id="topic-spatial-perception"></a>
### 5.1 空间感知、深度与三维重建

> **本类关注** · 深度、双目、多视图几何、相机位姿与场景重建
>
> **12 篇论文 · 按年份从新到旧排列**

---

<a id="s054"></a>
#### VGGT: Visual Geometry Grounded Transformer (CVPR 2025)

[![arXiv: 2503.11651](https://img.shields.io/badge/arXiv-2503.11651-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2503.11651) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2503.11651) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://vgg-t.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/facebookresearch/vggt) [![GitHub stars](https://img.shields.io/github/stars/facebookresearch/vggt?style=flat-square&label=stars&color=C58A18)](https://github.com/facebookresearch/vggt/stargazers) [![GitHub forks](https://img.shields.io/github/forks/facebookresearch/vggt?style=flat-square&label=forks&color=64748B)](https://github.com/facebookresearch/vggt/forks) &nbsp; [`T6`](#t6)

从单幅或多幅图像联合预测相机、深度、三维点与点轨迹，为几何重建和后续重投影提供基础。

---

<a id="s055"></a>
#### FoundationStereo: Zero-Shot Stereo Matching (CVPR 2025)

[![arXiv: 2501.09898](https://img.shields.io/badge/arXiv-2501.09898-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2501.09898) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2501.09898) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://nvlabs.github.io/FoundationStereo/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/NVlabs/FoundationStereo) [![GitHub stars](https://img.shields.io/github/stars/NVlabs/FoundationStereo?style=flat-square&label=stars&color=C58A18)](https://github.com/NVlabs/FoundationStereo/stargazers) [![GitHub forks](https://img.shields.io/github/forks/NVlabs/FoundationStereo?style=flat-square&label=forks&color=64748B)](https://github.com/NVlabs/FoundationStereo/forks) &nbsp; [`T4`](#t4) [`T6`](#t6)

利用大规模合成双目数据、单目先验与长程代价体推理，学习跨域泛化的双目深度匹配。

---

<a id="p41"></a>
#### DUSt3R: Geometric 3D Vision Made Easy (CVPR 2024)

[![arXiv: 2312.14132](https://img.shields.io/badge/arXiv-2312.14132-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2312.14132) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2312.14132) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/naver/dust3r) [![GitHub stars](https://img.shields.io/github/stars/naver/dust3r?style=flat-square&label=stars&color=C58A18)](https://github.com/naver/dust3r/stargazers) [![GitHub forks](https://img.shields.io/github/forks/naver/dust3r?style=flat-square&label=forks&color=64748B)](https://github.com/naver/dust3r/forks) &nbsp; [`T6`](#t6)

将无标定多视图重建转化为成对点图回归，再通过全局对齐建立统一三维坐标系。

---

<a id="p42"></a>
#### Grounding Image Matching in 3D with MASt3R (ECCV 2024)

[![arXiv: 2406.09756](https://img.shields.io/badge/arXiv-2406.09756-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2406.09756) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2406.09756) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/naver/mast3r) [![GitHub stars](https://img.shields.io/github/stars/naver/mast3r?style=flat-square&label=stars&color=C58A18)](https://github.com/naver/mast3r/stargazers) [![GitHub forks](https://img.shields.io/github/forks/naver/mast3r?style=flat-square&label=forks&color=64748B)](https://github.com/naver/mast3r/forks) &nbsp; [`T4`](#t4) [`T6`](#t6)

在 DUSt3R 三维点图基础上加入局部描述子与高效匹配，使图像对应与场景几何联合建模。

---

<a id="p40"></a>
#### DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras (NeurIPS 2021)

[![arXiv: 2108.10869](https://img.shields.io/badge/arXiv-2108.10869-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2108.10869) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2108.10869) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/princeton-vl/DROID-SLAM) [![GitHub stars](https://img.shields.io/github/stars/princeton-vl/DROID-SLAM?style=flat-square&label=stars&color=C58A18)](https://github.com/princeton-vl/DROID-SLAM/stargazers) [![GitHub forks](https://img.shields.io/github/forks/princeton-vl/DROID-SLAM?style=flat-square&label=forks&color=64748B)](https://github.com/princeton-vl/DROID-SLAM/forks) &nbsp; [`T4`](#t4) [`T6`](#t6)

通过循环更新和稠密束调整联合优化相机位姿与逐像素深度，统一单目、双目及 RGB-D SLAM。

---

<a id="s053"></a>
#### RAFT-Stereo: Multilevel Recurrent Field Transforms for Stereo Matching (3DV 2021)

[![arXiv: 2109.07547](https://img.shields.io/badge/arXiv-2109.07547-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2109.07547) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2109.07547) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/princeton-vl/RAFT-Stereo) [![GitHub stars](https://img.shields.io/github/stars/princeton-vl/RAFT-Stereo?style=flat-square&label=stars&color=C58A18)](https://github.com/princeton-vl/RAFT-Stereo/stargazers) [![GitHub forks](https://img.shields.io/github/forks/princeton-vl/RAFT-Stereo?style=flat-square&label=forks&color=64748B)](https://github.com/princeton-vl/RAFT-Stereo/forks) &nbsp; [`T4`](#t4) [`T6`](#t6)

在校正后的双目图像上构建相关金字塔，用多层循环更新预测稠密视差。

---

<a id="s051"></a>
#### Cascade Cost Volume for High-Resolution Multi-View Stereo and Stereo Matching (CVPR 2020)

[![arXiv: 1912.06378](https://img.shields.io/badge/arXiv-1912.06378-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1912.06378) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/alibaba/cascade-stereo) [![GitHub stars](https://img.shields.io/github/stars/alibaba/cascade-stereo?style=flat-square&label=stars&color=C58A18)](https://github.com/alibaba/cascade-stereo/stargazers) [![GitHub forks](https://img.shields.io/github/forks/alibaba/cascade-stereo?style=flat-square&label=forks&color=64748B)](https://github.com/alibaba/cascade-stereo/forks) &nbsp; [`T6`](#t6)

利用前一级深度缩小后续假设范围，通过金字塔级联代价体进行高分辨率多视图与双目匹配。

---

<a id="c16"></a>
#### Digging Into Self-Supervised Monocular Depth Estimation (ICCV 2019)

[![arXiv: 1806.01260](https://img.shields.io/badge/arXiv-1806.01260-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1806.01260) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nianticlabs/monodepth2) [![GitHub stars](https://img.shields.io/github/stars/nianticlabs/monodepth2?style=flat-square&label=stars&color=C58A18)](https://github.com/nianticlabs/monodepth2/stargazers) [![GitHub forks](https://img.shields.io/github/forks/nianticlabs/monodepth2?style=flat-square&label=forks&color=64748B)](https://github.com/nianticlabs/monodepth2/forks) &nbsp; [`T6`](#t6)

用深度、位姿和可微重投影进行自监督视图重建，引入最小重投影误差与自动掩码。

---

<a id="s052"></a>
#### DPSNet: End-to-end Deep Plane Sweep Stereo (ICLR 2019)

[![arXiv: 1905.00538](https://img.shields.io/badge/arXiv-1905.00538-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1905.00538) &nbsp; [`T6`](#t6) [`T7`](#t7)

通过可微平面扫描 Warping 构建跨视图特征代价体，再聚合并回归场景深度。

---

<a id="p39"></a>
#### MVSNet: Depth Inference for Unstructured Multi-view Stereo (ECCV 2018)

[![arXiv: 1804.02505](https://img.shields.io/badge/arXiv-1804.02505-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1804.02505) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/YoYo000/MVSNet) [![GitHub stars](https://img.shields.io/github/stars/YoYo000/MVSNet?style=flat-square&label=stars&color=C58A18)](https://github.com/YoYo000/MVSNet/stargazers) [![GitHub forks](https://img.shields.io/github/forks/YoYo000/MVSNet?style=flat-square&label=forks&color=64748B)](https://github.com/YoYo000/MVSNet/forks) &nbsp; [`T6`](#t6)

用可微单应性 Warping 构建多视图代价体，并通过三维正则化推断参考视图深度。

---

<a id="p43"></a>
#### Unsupervised Learning of Depth and Ego-Motion from Video (CVPR 2017)

[![arXiv: 1704.07813](https://img.shields.io/badge/arXiv-1704.07813-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1704.07813) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/1704.07813) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tinghuiz/SfMLearner) [![GitHub stars](https://img.shields.io/github/stars/tinghuiz/SfMLearner?style=flat-square&label=stars&color=C58A18)](https://github.com/tinghuiz/SfMLearner/stargazers) [![GitHub forks](https://img.shields.io/github/forks/tinghuiz/SfMLearner?style=flat-square&label=forks&color=64748B)](https://github.com/tinghuiz/SfMLearner/forks) &nbsp; [`T6`](#t6)

用可微视图重建连接单目深度与相机运动网络，以无监督光度误差学习几何。

---

<a id="p38"></a>
#### Structure-from-Motion Revisited (CVPR 2016)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content_cvpr_2016/html/Schonberger_Structure-From-Motion_Revisited_CVPR_2016_paper.html) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://colmap.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/colmap/colmap) [![GitHub stars](https://img.shields.io/github/stars/colmap/colmap?style=flat-square&label=stars&color=C58A18)](https://github.com/colmap/colmap/stargazers) [![GitHub forks](https://img.shields.io/github/forks/colmap/colmap?style=flat-square&label=forks&color=64748B)](https://github.com/colmap/colmap/forks) &nbsp; [`T1`](#t1) [`T6`](#t6)

改进增量式运动恢复结构流程，从无序图像估计相机和稀疏几何，为跨视图重投影提供基础。

---

<details>
<summary>关联阅读 · 14 篇其他 Topic 的论文</summary>

- [UFM](#s015) (2025)
- [DepthSplat](#s059) (2025)
- [Robust Dense Matching (RoMa)](#p71) (2024)
- [MVSplat](#s058) (2024)
- [UniMatch: Unifying Flow, Stereo and Depth Estimation](#n09) (2023)
- [ConceptFusion](#p55) (2023)
- [Dense Kernelized Matching (DKM)](#p70) (2023)
- [PDC-Net+](#s012) (2023)
- [CroCo v2](#s014) (2023)
- [Trans4Map](#s082) (2023)
- [IBRNet](#p46) (2021)
- [pixelNeRF](#p47) (2021)
- [LoFTR](#p69) (2021)
- [COTR](#s011) (2021)

</details>

[↑ 5.1 本类开头](#topic-spatial-perception) · [↑ 返回 Topic 导航](#topics)

---

<a id="topic-12"></a>
<a id="topic-novel-view-synthesis"></a>
### 5.2 重投影与新视角合成

> **本类关注** · DIBR、跨视图 Warping、可见性与反遮挡补全
>
> **14 篇论文 · 按年份从新到旧排列**

---

<a id="n22"></a>
#### WAVE: Warp-Based View Guidance for Consistent Novel View Synthesis Using a Single Image (ICCV 2025)

[![arXiv: 2506.23518](https://img.shields.io/badge/arXiv-2506.23518-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.23518) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/jwoo-park0/WAVE) [![GitHub stars](https://img.shields.io/github/stars/jwoo-park0/WAVE?style=flat-square&label=stars&color=C58A18)](https://github.com/jwoo-park0/WAVE/stargazers) [![GitHub forks](https://img.shields.io/github/forks/jwoo-park0/WAVE?style=flat-square&label=forks&color=64748B)](https://github.com/jwoo-park0/WAVE/forks) &nbsp; [`T6`](#t6) [`T9`](#t9)

用视图 warping 引导自适应 attention 与噪声重新初始化，提高单图新视角一致性，无需额外训练。

---

<a id="n23"></a>
#### High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion (SIGGRAPH 2025)

[![arXiv: 2502.12752](https://img.shields.io/badge/arXiv-2502.12752-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.12752) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2502.12752) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://studios.disneyresearch.com/2025/07/16/splatdiff/) &nbsp; [`T6`](#t6) [`T7`](#t7) [`T9`](#t9)

以 pixel splatting 约束目标视角，结合对齐合成与 texture bridge，平衡几何一致性和纹理保真。

---

<a id="s059"></a>
#### DepthSplat: Connecting Gaussian Splatting and Depth (CVPR 2025)

[![arXiv: 2410.13862](https://img.shields.io/badge/arXiv-2410.13862-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2410.13862) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2410.13862) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://haofeixu.github.io/depthsplat/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/cvg/depthsplat) [![GitHub stars](https://img.shields.io/github/stars/cvg/depthsplat?style=flat-square&label=stars&color=C58A18)](https://github.com/cvg/depthsplat/stargazers) [![GitHub forks](https://img.shields.io/github/forks/cvg/depthsplat?style=flat-square&label=forks&color=64748B)](https://github.com/cvg/depthsplat/forks) &nbsp; [`T6`](#t6) [`T7`](#t7)

结合预训练单目特征与多视图深度估计来构建高斯场景，并用渲染监督促进深度学习。

---

<a id="n15"></a>
#### GenWarp: Single Image to Novel Views with Semantic-Preserving Generative Warping (NeurIPS 2024)

[![arXiv: 2405.17251](https://img.shields.io/badge/arXiv-2405.17251-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2405.17251) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2405.17251) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://genwarp-nvs.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sony/genwarp) [![GitHub stars](https://img.shields.io/github/stars/sony/genwarp?style=flat-square&label=stars&color=C58A18)](https://github.com/sony/genwarp/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sony/genwarp?style=flat-square&label=forks&color=64748B)](https://github.com/sony/genwarp/forks) &nbsp; [`T6`](#t6) [`T9`](#t9)

结合深度诱导的坐标信息与跨视图/自注意力，让模型学习保留可迁移内容并生成缺失部分。

---

<a id="s058"></a>
#### MVSplat: Efficient 3D Gaussian Splatting from Sparse Multi-View Images (ECCV 2024)

[![arXiv: 2403.14627](https://img.shields.io/badge/arXiv-2403.14627-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2403.14627) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2403.14627) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://donydchen.github.io/mvsplat/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/donydchen/mvsplat) [![GitHub stars](https://img.shields.io/github/stars/donydchen/mvsplat?style=flat-square&label=stars&color=C58A18)](https://github.com/donydchen/mvsplat/stargazers) [![GitHub forks](https://img.shields.io/github/forks/donydchen/mvsplat?style=flat-square&label=forks&color=64748B)](https://github.com/donydchen/mvsplat/forks) &nbsp; [`T6`](#t6) [`T7`](#t7)

以平面扫描代价体估计几何并预测三维高斯，从稀疏多视图实现前馈式新视角渲染。

---

<a id="s060"></a>
#### MultiDiff: Consistent Novel View Synthesis from a Single Image (CVPR 2024)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content/CVPR2024/html/Muller_MultiDiff_Consistent_Novel_View_Synthesis_from_a_Single_Image_CVPR_2024_paper.html) &nbsp; [`T6`](#t6) [`T9`](#t9)

用单目深度将参考图像 Warp 到目标视角，再以视频扩散先验联合生成一致的多视图序列。

---

<a id="p45"></a>
#### 3D Gaussian Splatting for Real-Time Radiance Field Rendering (SIGGRAPH / TOG 2023)

[![arXiv: 2308.04079](https://img.shields.io/badge/arXiv-2308.04079-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2308.04079) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2308.04079) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/graphdeco-inria/gaussian-splatting) [![GitHub stars](https://img.shields.io/github/stars/graphdeco-inria/gaussian-splatting?style=flat-square&label=stars&color=C58A18)](https://github.com/graphdeco-inria/gaussian-splatting/stargazers) [![GitHub forks](https://img.shields.io/github/forks/graphdeco-inria/gaussian-splatting?style=flat-square&label=forks&color=64748B)](https://github.com/graphdeco-inria/gaussian-splatting/forks) &nbsp; [`T6`](#t6) [`T7`](#t7)

优化各向异性三维高斯及其密度，通过可见性感知 Splatting 实现高效新视角渲染。

---

<a id="p46"></a>
#### IBRNet: Learning Multi-View Image-Based Rendering (CVPR 2021)

[![arXiv: 2102.13090](https://img.shields.io/badge/arXiv-2102.13090-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2102.13090) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/googleinterns/IBRNet) [![GitHub stars](https://img.shields.io/github/stars/googleinterns/IBRNet?style=flat-square&label=stars&color=C58A18)](https://github.com/googleinterns/IBRNet/stargazers) [![GitHub forks](https://img.shields.io/github/forks/googleinterns/IBRNet?style=flat-square&label=forks&color=64748B)](https://github.com/googleinterns/IBRNet/forks) &nbsp; [`T6`](#t6) [`T7`](#t7)

将邻近源视图投影特征与射线聚合结合，学习可跨场景泛化的图像式新视角渲染。

---

<a id="p47"></a>
#### pixelNeRF: Neural Radiance Fields from One or Few Images (CVPR 2021)

[![arXiv: 2012.02190](https://img.shields.io/badge/arXiv-2012.02190-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2012.02190) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2012.02190) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sxyu/pixel-nerf) [![GitHub stars](https://img.shields.io/github/stars/sxyu/pixel-nerf?style=flat-square&label=stars&color=C58A18)](https://github.com/sxyu/pixel-nerf/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sxyu/pixel-nerf?style=flat-square&label=forks&color=64748B)](https://github.com/sxyu/pixel-nerf/forks) &nbsp; [`T6`](#t6)

将三维采样点投影到源图像特征，以一幅或少量图像条件化辐射场并生成新视角。

---

<a id="p44"></a>
#### NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis (ECCV 2020)

[![arXiv: 2003.08934](https://img.shields.io/badge/arXiv-2003.08934-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2003.08934) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2003.08934) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://www.matthewtancik.com/nerf) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/bmild/nerf) [![GitHub stars](https://img.shields.io/github/stars/bmild/nerf?style=flat-square&label=stars&color=C58A18)](https://github.com/bmild/nerf/stargazers) [![GitHub forks](https://img.shields.io/github/forks/bmild/nerf?style=flat-square&label=forks&color=64748B)](https://github.com/bmild/nerf/forks) &nbsp; [`T6`](#t6)

用连续辐射场与可微体渲染表示场景，从已知相机图像优化新视角合成。

---

<a id="s056"></a>
#### SynSin: End-to-End View Synthesis From a Single Image (CVPR 2020)

[![arXiv: 1912.08804](https://img.shields.io/badge/arXiv-1912.08804-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1912.08804) &nbsp; [`T6`](#t6) [`T7`](#t7)

将源图像特征提升为三维点云并可微投影到目标视角，再通过细化网络补全缺失区域。

---

<a id="s083"></a>
#### 3D Photography Using Context-Aware Layered Depth Inpainting (CVPR 2020)

[![arXiv: 2004.04727](https://img.shields.io/badge/arXiv-2004.04727-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2004.04727) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2004.04727) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://shihmengli.github.io/3D-Photo-Inpainting/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/vt-vl-lab/3d-photo-inpainting) [![GitHub stars](https://img.shields.io/github/stars/vt-vl-lab/3d-photo-inpainting?style=flat-square&label=stars&color=C58A18)](https://github.com/vt-vl-lab/3d-photo-inpainting/stargazers) [![GitHub forks](https://img.shields.io/github/forks/vt-vl-lab/3d-photo-inpainting?style=flat-square&label=forks&color=64748B)](https://github.com/vt-vl-lab/3d-photo-inpainting/forks) &nbsp; [`T6`](#t6)

将单幅 RGB-D 图像转为带显式像素连接的分层深度表示，并补全遮挡区域的颜色与深度来渲染运动视差。

---

<a id="p48"></a>
#### Stereo Magnification: Learning view synthesis using multiplane images (SIGGRAPH / TOG 2018)

[![arXiv: 1805.09817](https://img.shields.io/badge/arXiv-1805.09817-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1805.09817) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/1805.09817) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://tinghuiz.github.io/projects/mpi/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/google/stereo-magnification) [![GitHub stars](https://img.shields.io/github/stars/google/stereo-magnification?style=flat-square&label=stars&color=C58A18)](https://github.com/google/stereo-magnification/stargazers) [![GitHub forks](https://img.shields.io/github/forks/google/stereo-magnification?style=flat-square&label=forks&color=64748B)](https://github.com/google/stereo-magnification/forks) &nbsp; [`T6`](#t6)

从窄基线双目图像预测多平面图像，以深度平面的单应性 Warping 合成更大基线的新视角。

---

<a id="c28"></a>
#### Depth-image-based rendering (DIBR), compression, and transmission for a new approach on 3D-TV (SPIE 2004)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1117/12.524762) &nbsp; [`T6`](#t6)

用颜色图与深度生成虚拟视角，是理解深度重投影、遮挡和空洞的经典路线；该论文不是重投影思想的首次提出。

---

<details>
<summary>关联阅读 · 21 篇其他 Topic 的论文</summary>

- [gsplat](#s010) (2025)
- [TrajectoryCrafter](#s048) (2025)
- [Latent-Reframe](#s049) (2025)
- [VGGT](#s054) (2025)
- [MoSca](#s063) (2025)
- [Dynamic 3D Gaussians](#p51) (2024)
- [Mip-Splatting](#s008) (2024)
- [RVT](#s075) (2023)
- [TiNeuVox](#p52) (2022)
- [D-NeRF](#c21) (2021)
- [Nerfies](#c22) (2021)
- [Neural Scene Flow Fields (NSFF)](#p49) (2021)
- [NR-NeRF](#s064) (2021)
- [nvdiffrast](#s009) (2020)
- [CasMVSNet](#s051) (2020)
- [Monodepth2](#c16) (2019)
- [Soft Rasterizer (SoftRas)](#p06) (2019)
- [DPSNet](#s052) (2019)
- [MVSNet](#p39) (2018)
- [Gibson Env](#s071) (2018)
- [SfMLearner](#p43) (2017)

</details>

[↑ 5.2 本类开头](#topic-novel-view-synthesis) · [↑ 返回 Topic 导航](#topics)

---

<a id="topic-13"></a>
<a id="topic-dynamic-3d"></a>
### 5.3 动态三维与 4D 场景

> **本类关注** · Canonical Deformation、动态 NeRF、可形变 Gaussian 与时空场景表示
>
> **13 篇论文 · 按年份从新到旧排列**

---

<a id="s063"></a>
#### MoSca: Dynamic Gaussian Fusion from Casual Videos via 4D Motion Scaffolds (CVPR 2025)

[![arXiv: 2405.17421](https://img.shields.io/badge/arXiv-2405.17421-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2405.17421) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2405.17421) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/JiahuiLei/MoSca) [![GitHub stars](https://img.shields.io/github/stars/JiahuiLei/MoSca?style=flat-square&label=stars&color=C58A18)](https://github.com/JiahuiLei/MoSca/stargazers) [![GitHub forks](https://img.shields.io/github/forks/JiahuiLei/MoSca?style=flat-square&label=forks&color=64748B)](https://github.com/JiahuiLei/MoSca/forks) &nbsp; [`T6`](#t6) [`T8`](#t8)

将视频先验提升为四维运动支架，并融合附着其上的高斯，以分离场景外观和动态形变。

---

<a id="n11"></a>
#### Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction (CVPR 2024)

[![arXiv: 2309.13101](https://img.shields.io/badge/arXiv-2309.13101-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2309.13101) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2309.13101) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://ingra14m.github.io/Deformable-Gaussians/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ingra14m/Deformable-3D-Gaussians) [![GitHub stars](https://img.shields.io/github/stars/ingra14m/Deformable-3D-Gaussians?style=flat-square&label=stars&color=C58A18)](https://github.com/ingra14m/Deformable-3D-Gaussians/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ingra14m/Deformable-3D-Gaussians?style=flat-square&label=forks&color=64748B)](https://github.com/ingra14m/Deformable-3D-Gaussians/forks) &nbsp; [`T8`](#t8)

在 canonical Gaussian 表示上学习形变场，将动态重建与快速 splatting 渲染结合。

---

<a id="n12"></a>
#### 4D Gaussian Splatting for Real-Time Dynamic Scene Rendering (CVPR 2024)

[![arXiv: 2310.08528](https://img.shields.io/badge/arXiv-2310.08528-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2310.08528) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2310.08528) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://guanjunwu.github.io/4dgs/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/hustvl/4DGaussians) [![GitHub stars](https://img.shields.io/github/stars/hustvl/4DGaussians?style=flat-square&label=stars&color=C58A18)](https://github.com/hustvl/4DGaussians/stargazers) [![GitHub forks](https://img.shields.io/github/forks/hustvl/4DGaussians?style=flat-square&label=forks&color=64748B)](https://github.com/hustvl/4DGaussians/forks) &nbsp; [`T8`](#t8)

结合时空特征与 Gaussian 形变，提升动态场景表示的训练、存储及渲染效率。

---

<a id="p51"></a>
#### Dynamic 3D Gaussians: Tracking by Persistent Dynamic View Synthesis (3DV 2024)

[![arXiv: 2308.09713](https://img.shields.io/badge/arXiv-2308.09713-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2308.09713) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2308.09713) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://dynamic3dgaussians.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/JonathonLuiten/Dynamic3DGaussians) [![GitHub stars](https://img.shields.io/github/stars/JonathonLuiten/Dynamic3DGaussians?style=flat-square&label=stars&color=C58A18)](https://github.com/JonathonLuiten/Dynamic3DGaussians/stargazers) [![GitHub forks](https://img.shields.io/github/forks/JonathonLuiten/Dynamic3DGaussians?style=flat-square&label=forks&color=64748B)](https://github.com/JonathonLuiten/Dynamic3DGaussians/forks) &nbsp; [`T6`](#t6) [`T7`](#t7) [`T8`](#t8)

以随时间运动旋转、外观持久的三维高斯及局部刚性约束，联合实现动态视角合成与稠密跟踪。

---

<a id="s061"></a>
#### SC-GS: Sparse-Controlled Gaussian Splatting for Editable Dynamic Scenes (CVPR 2024)

[![arXiv: 2312.14937](https://img.shields.io/badge/arXiv-2312.14937-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2312.14937) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2312.14937) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://yihua7.github.io/SC-GS-web/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/CVMI-Lab/SC-GS) [![GitHub stars](https://img.shields.io/github/stars/CVMI-Lab/SC-GS?style=flat-square&label=stars&color=C58A18)](https://github.com/CVMI-Lab/SC-GS/stargazers) [![GitHub forks](https://img.shields.io/github/forks/CVMI-Lab/SC-GS?style=flat-square&label=forks&color=64748B)](https://github.com/CVMI-Lab/SC-GS/forks) &nbsp; [`T8`](#t8)

以稀疏控制点的时变六自由度变换，经局部插值驱动稠密三维高斯，实现动态重建与编辑。

---

<a id="s062"></a>
#### SceNeRFlow: Time-Consistent Reconstruction of General Dynamic Scenes (3DV 2024)

[![arXiv: 2308.08258](https://img.shields.io/badge/arXiv-2308.08258-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2308.08258) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2308.08258) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://vcai.mpi-inf.mpg.de/projects/scenerflow/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/facebookresearch/SceNeRFlow) [![GitHub stars](https://img.shields.io/github/stars/facebookresearch/SceNeRFlow?style=flat-square&label=stars&color=C58A18)](https://github.com/facebookresearch/SceNeRFlow/stargazers) [![GitHub forks](https://img.shields.io/github/forks/facebookresearch/SceNeRFlow?style=flat-square&label=forks&color=64748B)](https://github.com/facebookresearch/SceNeRFlow/forks) &nbsp; [`T8`](#t8)

通过反向形变将动态观测映射到固定规范场景，恢复长期、较大运动下的跨时刻对应。

---

<a id="p52"></a>
#### Fast Dynamic Radiance Fields with Time-Aware Neural Voxels (SIGGRAPH Asia 2022)

[![arXiv: 2205.15285](https://img.shields.io/badge/arXiv-2205.15285-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2205.15285) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://jaminfong.cn/tineuvox/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/hustvl/TiNeuVox) [![GitHub stars](https://img.shields.io/github/stars/hustvl/TiNeuVox?style=flat-square&label=stars&color=C58A18)](https://github.com/hustvl/TiNeuVox/stargazers) [![GitHub forks](https://img.shields.io/github/forks/hustvl/TiNeuVox?style=flat-square&label=forks&color=64748B)](https://github.com/hustvl/TiNeuVox/forks) &nbsp; [`T6`](#t6) [`T8`](#t8)

将时感知体素特征、小型坐标形变网络与多距离插值结合，加速动态辐射场优化。

---

<a id="c21"></a>
#### D-NeRF: Neural Radiance Fields for Dynamic Scenes (CVPR 2021)

[![arXiv: 2011.13961](https://img.shields.io/badge/arXiv-2011.13961-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2011.13961) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://www.albertpumarola.com/research/D-NeRF/index.html) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/albertpumarola/D-NeRF) [![GitHub stars](https://img.shields.io/github/stars/albertpumarola/D-NeRF?style=flat-square&label=stars&color=C58A18)](https://github.com/albertpumarola/D-NeRF/stargazers) [![GitHub forks](https://img.shields.io/github/forks/albertpumarola/D-NeRF?style=flat-square&label=forks&color=64748B)](https://github.com/albertpumarola/D-NeRF/forks) &nbsp; [`T8`](#t8)

学习时间条件形变，把动态场景坐标映射到 canonical radiance field。

---

<a id="c22"></a>
#### Nerfies: Deformable Neural Radiance Fields (ICCV 2021)

[![arXiv: 2011.12948](https://img.shields.io/badge/arXiv-2011.12948-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2011.12948) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2011.12948) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://nerfies.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/google/nerfies) [![GitHub stars](https://img.shields.io/github/stars/google/nerfies?style=flat-square&label=stars&color=C58A18)](https://github.com/google/nerfies/stargazers) [![GitHub forks](https://img.shields.io/github/forks/google/nerfies?style=flat-square&label=forks&color=64748B)](https://github.com/google/nerfies/forks) &nbsp; [`T8`](#t8)

连续三维形变场、弹性正则与粗到细优化，重建随意拍摄的非刚性场景。

---

<a id="c23"></a>
#### HyperNeRF: A Higher-Dimensional Representation for Topologically Varying Neural Radiance Fields (SIGGRAPH Asia / TOG 2021)

[![arXiv: 2106.13228](https://img.shields.io/badge/arXiv-2106.13228-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2106.13228) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://hypernerf.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/google/hypernerf) [![GitHub stars](https://img.shields.io/github/stars/google/hypernerf?style=flat-square&label=stars&color=C58A18)](https://github.com/google/hypernerf/stargazers) [![GitHub forks](https://img.shields.io/github/forks/google/hypernerf?style=flat-square&label=forks&color=64748B)](https://github.com/google/hypernerf/forks) &nbsp; [`T8`](#t8)

把表示提升到高维空间，通过切片建模拓扑变化，扩展普通连续三维 warp 的能力。

---

<a id="p49"></a>
#### Neural Scene Flow Fields for Space-Time View Synthesis of Dynamic Scenes (CVPR 2021)

[![arXiv: 2011.13084](https://img.shields.io/badge/arXiv-2011.13084-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2011.13084) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://www.cs.cornell.edu/~zl548/NSFF/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/zhengqili/Neural-Scene-Flow-Fields) [![GitHub stars](https://img.shields.io/github/stars/zhengqili/Neural-Scene-Flow-Fields?style=flat-square&label=stars&color=C58A18)](https://github.com/zhengqili/Neural-Scene-Flow-Fields/stargazers) [![GitHub forks](https://img.shields.io/github/forks/zhengqili/Neural-Scene-Flow-Fields?style=flat-square&label=forks&color=64748B)](https://github.com/zhengqili/Neural-Scene-Flow-Fields/forks) &nbsp; [`T4`](#t4) [`T6`](#t6) [`T8`](#t8)

联合建模外观、几何和三维场景流，以单目视频约束动态场景的时间与视角合成。

---

<a id="s064"></a>
#### Non-Rigid Neural Radiance Fields: Reconstruction and Novel View Synthesis of a Dynamic Scene From Monocular Video (ICCV 2021)

[![arXiv: 2012.12247](https://img.shields.io/badge/arXiv-2012.12247-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2012.12247) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://vcai.mpi-inf.mpg.de/projects/nonrigid_nerf/) &nbsp; [`T8`](#t8)

通过射线弯曲和刚性约束分离规范辐射场与场景形变，从单目动态视频建立时空表示。

---

<a id="p50"></a>
#### DynamicFusion: Reconstruction and Tracking of Non-rigid Scenes in Real-Time (CVPR 2015)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content_cvpr_2015/html/Newcombe_DynamicFusion_Reconstruction_and_2015_CVPR_paper.html) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://grail.cs.washington.edu/projects/dynamicfusion/) &nbsp; [`T3`](#t3) [`T6`](#t6) [`T8`](#t8)

在规范空间中融合 RGB-D 观测，并估计将几何映射到当前帧的非刚性形变场，实现在线动态重建。

---

<details>
<summary>关联阅读 · 1 篇其他 Topic 的论文</summary>

- [Embedded Deformation](#p02) (2007)

</details>

[↑ 5.3 本类开头](#topic-dynamic-3d) · [↑ 返回 Topic 导航](#topics)

---


<a id="topic-spatial-reasoning"></a>
### 5.4 空间推理与场景记忆

> **本类关注** · 空间关系、跨视角理解、持久地图与空间记忆
>
> **10 篇论文 · 按年份从新到旧排列**

---

<a id="s066"></a>
#### 3D-Mem: 3D Scene Memory for Embodied Exploration and Reasoning (CVPR 2025)

[![arXiv: 2411.17735](https://img.shields.io/badge/arXiv-2411.17735-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2411.17735) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2411.17735) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://umass-embodied-agi.github.io/3D-Mem/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/UMass-Embodied-AGI/3D-Mem) [![GitHub stars](https://img.shields.io/github/stars/UMass-Embodied-AGI/3D-Mem?style=flat-square&label=stars&color=C58A18)](https://github.com/UMass-Embodied-AGI/3D-Mem/stargazers) [![GitHub forks](https://img.shields.io/github/forks/UMass-Embodied-AGI/3D-Mem?style=flat-square&label=forks&color=64748B)](https://github.com/UMass-Embodied-AGI/3D-Mem/forks) &nbsp; [`T6`](#t6)

结合三维场景表示、信息丰富的多视图记忆快照与前沿快照，支持具身探索和问答。

---

<a id="s067"></a>
#### GraphEQA: Using 3D Semantic Scene Graphs for Real-time Embodied Question Answering (CoRL 2025 / PMLR 2025)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://proceedings.mlr.press/v305/saxena25a.html) &nbsp; [`T6`](#t6)

将在线三维度量语义场景图与相关图像组成多模态记忆，用于结构化探索和具身问答。

---

<a id="p56"></a>
#### ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning (ICRA 2024)

[![arXiv: 2309.16650](https://img.shields.io/badge/arXiv-2309.16650-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2309.16650) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2309.16650) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://concept-graphs.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/concept-graphs/concept-graphs) [![GitHub stars](https://img.shields.io/github/stars/concept-graphs/concept-graphs?style=flat-square&label=stars&color=C58A18)](https://github.com/concept-graphs/concept-graphs/stargazers) [![GitHub forks](https://img.shields.io/github/forks/concept-graphs/concept-graphs?style=flat-square&label=forks&color=64748B)](https://github.com/concept-graphs/concept-graphs/forks) &nbsp; [`T6`](#t6)

将二维基础模型输出经跨视图关联融合为开放词汇三维场景图，用对象及关系支撑空间推理与规划。

---

<a id="p54"></a>
#### Visual Language Maps for Robot Navigation (ICRA 2023)

[![arXiv: 2210.05714](https://img.shields.io/badge/arXiv-2210.05714-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2210.05714) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2210.05714) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://vlmaps.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/vlmaps/vlmaps) [![GitHub stars](https://img.shields.io/github/stars/vlmaps/vlmaps?style=flat-square&label=stars&color=C58A18)](https://github.com/vlmaps/vlmaps/stargazers) [![GitHub forks](https://img.shields.io/github/forks/vlmaps/vlmaps?style=flat-square&label=forks&color=64748B)](https://github.com/vlmaps/vlmaps/forks) &nbsp; [`T6`](#t6)

将预训练视觉语言特征融合到三维地图，支持开放词汇目标定位与空间关系驱动的导航。

---

<a id="p55"></a>
#### ConceptFusion: Open-set Multimodal 3D Mapping (RSS 2023)

[![arXiv: 2302.07241](https://img.shields.io/badge/arXiv-2302.07241-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2302.07241) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://concept-fusion.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/concept-fusion/concept-fusion) [![GitHub stars](https://img.shields.io/github/stars/concept-fusion/concept-fusion?style=flat-square&label=stars&color=C58A18)](https://github.com/concept-fusion/concept-fusion/stargazers) [![GitHub forks](https://img.shields.io/github/forks/concept-fusion/concept-fusion?style=flat-square&label=forks&color=64748B)](https://github.com/concept-fusion/concept-fusion/forks) &nbsp; [`T6`](#t6)

通过像素对齐开放集特征与多视图三维融合建立可用语言、图像或音频查询的空间地图。

---

<a id="s082"></a>
#### Trans4Map: Revisiting Holistic Bird's-Eye-View Mapping From Egocentric Images to Allocentric Semantics With Vision Transformers (WACV 2023)

[![arXiv: 2207.06205](https://img.shields.io/badge/arXiv-2207.06205-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2207.06205) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2207.06205) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/InSAI-Lab/Trans4Map) [![GitHub stars](https://img.shields.io/github/stars/InSAI-Lab/Trans4Map?style=flat-square&label=stars&color=C58A18)](https://github.com/InSAI-Lab/Trans4Map/stargazers) [![GitHub forks](https://img.shields.io/github/forks/InSAI-Lab/Trans4Map?style=flat-square&label=forks&color=64748B)](https://github.com/InSAI-Lab/Trans4Map/forks) &nbsp; [`T6`](#t6) [`T8`](#t8)

用 Transformer 提取自我视角特征，将其投影并累积到双向世界坐标记忆，预测俯视语义地图。

---

<a id="p53"></a>
#### Semantic MapNet: Building Allocentric Semantic Maps and Representations from Egocentric Views (AAAI 2021)

[![arXiv: 2010.01191](https://img.shields.io/badge/arXiv-2010.01191-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2010.01191) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2010.01191) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://vincentcartillier.github.io/smnet.html) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/vincentcartillier/Semantic-MapNet) [![GitHub stars](https://img.shields.io/github/stars/vincentcartillier/Semantic-MapNet?style=flat-square&label=stars&color=C58A18)](https://github.com/vincentcartillier/Semantic-MapNet/stargazers) [![GitHub forks](https://img.shields.io/github/forks/vincentcartillier/Semantic-MapNet?style=flat-square&label=forks&color=64748B)](https://github.com/vincentcartillier/Semantic-MapNet/forks) &nbsp; [`T6`](#t6)

把第一视角 RGB-D 特征投影到俯视坐标，并用空间记忆积累多帧信息，形成可供导航和问答使用的语义地图。

---

<a id="s080"></a>
#### EgoMap: Projective mapping and structured egocentric memory for Deep RL (ECML PKDD 2020)

[![arXiv: 2002.02286](https://img.shields.io/badge/arXiv-2002.02286-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2002.02286) &nbsp; [`T1`](#t1) [`T6`](#t6) [`T8`](#t8)

将图像特征可微反投影到俯视记忆地图，并依据自运动通过仿射变换更新记忆坐标。

---

<a id="s065"></a>
#### Neural Map: Structured Memory for Deep Reinforcement Learning (ICLR 2018)

[![arXiv: 1702.08360](https://img.shields.io/badge/arXiv-1702.08360-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1702.08360)

以空间结构化的二维神经记忆存储环境信息，通过位置相关的读写支持长期导航推理。

---

<a id="s081"></a>
#### MapNet: An Allocentric Spatial Memory for Mapping Environments (CVPR 2018)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content_cvpr_2018/html/Henriques_MapNet_An_Allocentric_CVPR_2018_paper.html) &nbsp; [`T6`](#t6) [`T8`](#t8)

将 RGB-D 感知注册到可学习的世界坐标记忆中，以卷积与反卷积形式实现定位和地图更新。

---

<details>
<summary>关联阅读 · 5 篇其他 Topic 的论文</summary>

- [WorldMem](#s072) (2025)
- [Spatial Memory World Models](#s073) (2025)
- [CLIPort](#p66) (2022)
- [Active Neural SLAM](#p63) (2020)
- [Goal-Oriented Semantic Exploration (SemExp)](#p64) (2020)

</details>

[↑ 5.4 本类开头](#topic-spatial-reasoning) · [↑ 返回 Topic 导航](#topics)

---

<a id="area-world-models-agents"></a>
## 6. 世界模型与具身智能体


<a id="topic-world-models"></a>
### 6.1 世界模型与环境预测

> **本类关注** · 状态表示、动态预测、动作条件预测与未来推演
>
> **7 篇论文 · 按年份从新到旧排列**

---

<a id="p68"></a>
#### Mastering diverse control tasks through world models (Nature 2025)

[![arXiv: 2301.04104](https://img.shields.io/badge/arXiv-2301.04104-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2301.04104) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2301.04104) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://danijar.com/project/dreamerv3/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/danijar/dreamerv3) [![GitHub stars](https://img.shields.io/github/stars/danijar/dreamerv3?style=flat-square&label=stars&color=C58A18)](https://github.com/danijar/dreamerv3/stargazers) [![GitHub forks](https://img.shields.io/github/forks/danijar/dreamerv3?style=flat-square&label=forks&color=64748B)](https://github.com/danijar/dreamerv3/forks) &nbsp; [`T9`](#t9)

从观测学习环境动力学、奖励与继续概率，在潜在想象轨迹中训练策略，并用归一化等机制提升跨任务稳定性。

---

<a id="p59"></a>
#### Driving into the Future: Multiview Visual Forecasting and Planning with World Model for Autonomous Driving (CVPR 2024)

[![arXiv: 2311.17918](https://img.shields.io/badge/arXiv-2311.17918-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2311.17918) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2311.17918) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://drive-wm.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/BraveGroup/Drive-WM) [![GitHub stars](https://img.shields.io/github/stars/BraveGroup/Drive-WM?style=flat-square&label=stars&color=C58A18)](https://github.com/BraveGroup/Drive-WM/stargazers) [![GitHub forks](https://img.shields.io/github/forks/BraveGroup/Drive-WM?style=flat-square&label=forks&color=64748B)](https://github.com/BraveGroup/Drive-WM/forks) &nbsp; [`T6`](#t6) [`T9`](#t9)

联合建模多视角和时间维度，生成不同驾驶动作对应的未来视频，并以图像奖励评估规划轨迹。

---

<a id="p62"></a>
#### Diffusion for World Modeling: Visual Details Matter in Atari (NeurIPS 2024)

[![arXiv: 2405.12399](https://img.shields.io/badge/arXiv-2405.12399-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2405.12399) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2405.12399) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://diamond-wm.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/eloialonso/diamond) [![GitHub stars](https://img.shields.io/github/stars/eloialonso/diamond?style=flat-square&label=stars&color=C58A18)](https://github.com/eloialonso/diamond/stargazers) [![GitHub forks](https://img.shields.io/github/forks/eloialonso/diamond?style=flat-square&label=forks&color=64748B)](https://github.com/eloialonso/diamond/forks) &nbsp; [`T9`](#t9)

在像素空间扩散世界模型中预测视觉动态，并利用模型想象训练强化学习策略。

---

<a id="p58"></a>
#### GAIA-1: A Generative World Model for Autonomous Driving (arXiv 2023)

[![arXiv: 2309.17080](https://img.shields.io/badge/arXiv-2309.17080-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2309.17080) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2309.17080) &nbsp; [`T9`](#t9)

将视频、文本与动作离散化并预测后续序列，用于驾驶场景的动作条件未来生成。

---

<a id="p67"></a>
#### Learning Latent Dynamics for Planning from Pixels (ICML 2019)

[![arXiv: 1811.04551](https://img.shields.io/badge/arXiv-1811.04551-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1811.04551) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/1811.04551) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://planetrl.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/google-research/planet) [![GitHub stars](https://img.shields.io/github/stars/google-research/planet?style=flat-square&label=stars&color=C58A18)](https://github.com/google-research/planet/stargazers) [![GitHub forks](https://img.shields.io/github/forks/google-research/planet?style=flat-square&label=forks&color=64748B)](https://github.com/google-research/planet/forks) &nbsp; [`T9`](#t9)

从像素学习含确定性与随机成分的潜在状态动力学，并通过多步预测在潜在空间中搜索动作。

---

<a id="s070"></a>
#### Stochastic Variational Video Prediction (ICLR 2018)

[![arXiv: 1710.11252](https://img.shields.io/badge/arXiv-1710.11252-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1710.11252) &nbsp; [`T7`](#t7)

在 CDNA 运动变换式视频预测器中引入随机潜变量，为同一动作与观测生成多个可能未来。

---

<a id="s068"></a>
#### Unsupervised Learning for Physical Interaction through Video Prediction (NeurIPS 2016)

[![arXiv: 1605.07157](https://img.shields.io/badge/arXiv-1605.07157-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1605.07157) &nbsp; [`T1`](#t1) [`T7`](#t7)

通过 DNA、CDNA 与空间变换预测器建模像素运动，将前帧内容变换和融合为动作条件的未来图像。

---

<details>
<summary>关联阅读 · 5 篇其他 Topic 的论文</summary>

- [GameNGen](#p61) (2025)
- [WorldMem](#s072) (2025)
- [Spatial Memory World Models](#s073) (2025)
- [UniSim](#p57) (2024)
- [Genie](#p60) (2024)

</details>

[↑ 6.1 本类开头](#topic-world-models) · [↑ 返回 Topic 导航](#topics)

---


<a id="topic-interactive-simulation"></a>
### 6.2 交互式环境与模拟

> **本类关注** · 可交互世界生成、场景持久性、训练与评估环境、合成数据
>
> **6 篇论文 · 按年份从新到旧排列**

---

<a id="p61"></a>
#### Diffusion Models Are Real-Time Game Engines (ICLR 2025)

[![arXiv: 2408.14837](https://img.shields.io/badge/arXiv-2408.14837-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2408.14837) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2408.14837) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://gamengen.github.io/) &nbsp; [`T9`](#t9)

用历史帧和动作条件化扩散模型，结合噪声增强训练生成可交互的 DOOM 画面序列。

---

<a id="s072"></a>
#### WorldMem: Long-term Consistent World Simulation with Memory (NeurIPS 2025)

[![arXiv: 2504.12369](https://img.shields.io/badge/arXiv-2504.12369-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.12369) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2504.12369) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://xizaoqu.github.io/worldmem/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/xizaoqu/WorldMem) [![GitHub stars](https://img.shields.io/github/stars/xizaoqu/WorldMem?style=flat-square&label=stars&color=C58A18)](https://github.com/xizaoqu/WorldMem/stargazers) [![GitHub forks](https://img.shields.io/github/forks/xizaoqu/WorldMem?style=flat-square&label=forks&color=64748B)](https://github.com/xizaoqu/WorldMem/forks)

保存历史帧、相机位姿与时间状态，通过记忆检索和注意力提高交互式世界模拟的长期一致性。

---

<a id="s073"></a>
#### Video World Models with Long-term Spatial Memory (NeurIPS 2025)

[![arXiv: 2506.05284](https://img.shields.io/badge/arXiv-2506.05284-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.05284) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2506.05284) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://spmem.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/spmem/spmem) [![GitHub stars](https://img.shields.io/github/stars/spmem/spmem?style=flat-square&label=stars&color=C58A18)](https://github.com/spmem/spmem/stargazers) [![GitHub forks](https://img.shields.io/github/forks/spmem/spmem?style=flat-square&label=forks&color=64748B)](https://github.com/spmem/spmem/forks) &nbsp; [`T6`](#t6) [`T9`](#t9)

将生成帧累积为几何空间记忆，再按目标相机视角检索和渲染，维持动作条件世界生成中的场景一致性。

---

<a id="p57"></a>
#### Learning Interactive Real-World Simulators (ICLR 2024)

[![arXiv: 2310.06114](https://img.shields.io/badge/arXiv-2310.06114-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2310.06114) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2310.06114) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://universal-simulator.github.io/unisim/) &nbsp; [`T9`](#t9)

从异质视频与交互数据学习动作条件模拟器，生成指令或低层动作引起的视觉变化，并用于智能体训练。

---

<a id="p60"></a>
#### Genie: Generative Interactive Environments (ICML 2024)

[![arXiv: 2402.15391](https://img.shields.io/badge/arXiv-2402.15391-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2402.15391) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2402.15391) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://sites.google.com/view/genie-2024/) &nbsp; [`T9`](#t9)

从无动作标注的视频学习潜在动作与时空动态，生成可逐帧交互的虚拟环境。

---

<a id="s071"></a>
#### Gibson Env: Real-World Perception for Embodied Agents (CVPR 2018)

[![arXiv: 1808.10654](https://img.shields.io/badge/arXiv-1808.10654-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1808.10654) &nbsp; [`T6`](#t6)

将真实扫描场景中的观测重投影到新视角并进行神经修复，构建用于具身感知与控制的模拟环境。

---

<details>
<summary>关联阅读 · 3 篇其他 Topic 的论文</summary>

- [Drive-WM](#p59) (2024)
- [DIAMOND](#p62) (2024)
- [SV2P](#s070) (2018)

</details>

[↑ 6.2 本类开头](#topic-interactive-simulation) · [↑ 返回 Topic 导航](#topics)

---


<a id="topic-embodied-agents"></a>
### 6.3 具身智能体、规划与控制

> **本类关注** · 视觉导航、机器人操作、主动感知、空间记忆驱动规划与感知—行动闭环
>
> **8 篇论文 · 按年份从新到旧排列**

---

<a id="s077"></a>
#### Autonomous Functional Play with Correspondence-Driven Trajectory Warping (ICLR 2026)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://proceedings.iclr.cc/paper_files/paper/2026/hash/b52ffc1e3ab14f7b423acbb14cdbfe8e-Abstract-Conference.html) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://tether-research.github.io) &nbsp; [`T3`](#t3) [`T4`](#t4)

以语义关键点对应将少量示范的动作轨迹 Warp 到目标场景，并通过自主任务交互持续收集经验。

---

<a id="s075"></a>
#### RVT: Robotic View Transformer for 3D Object Manipulation (CoRL 2023 / PMLR 2023)

[![arXiv: 2306.14896](https://img.shields.io/badge/arXiv-2306.14896-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2306.14896) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2306.14896) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://robotic-view-transformer.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nvlabs/rvt) [![GitHub stars](https://img.shields.io/github/stars/nvlabs/rvt?style=flat-square&label=stars&color=C58A18)](https://github.com/nvlabs/rvt/stargazers) [![GitHub forks](https://img.shields.io/github/forks/nvlabs/rvt?style=flat-square&label=forks&color=64748B)](https://github.com/nvlabs/rvt/forks) &nbsp; [`T6`](#t6)

将 RGB-D 点云重渲染为多个虚拟视图，融合跨视图特征并反投影来预测三维机器人动作。

---

<a id="p66"></a>
#### CLIPort: What and Where Pathways for Robotic Manipulation (CoRL 2021 / PMLR 2022)

[![arXiv: 2109.12098](https://img.shields.io/badge/arXiv-2109.12098-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2109.12098) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2109.12098) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://cliport.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/cliport/cliport) [![GitHub stars](https://img.shields.io/github/stars/cliport/cliport?style=flat-square&label=stars&color=C58A18)](https://github.com/cliport/cliport/stargazers) [![GitHub forks](https://img.shields.io/github/forks/cliport/cliport?style=flat-square&label=forks&color=64748B)](https://github.com/cliport/cliport/forks) &nbsp; [`T1`](#t1) [`T8`](#t8)

将 CLIP 的语言语义与 Transporter 的空间对应结合，学习语言条件下的精确抓取放置操作。

---

<a id="s076"></a>
#### FlowBot3D: Learning 3D Articulation Flow to Manipulate Articulated Objects (RSS 2022)

[![arXiv: 2205.04382](https://img.shields.io/badge/arXiv-2205.04382-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2205.04382) &nbsp; [`T8`](#t8)

预测关节物体点云上各点的潜在三维运动方向，再用该稠密向量场引导解析运动规划。

---

<a id="p65"></a>
#### Transporter Networks: Rearranging the Visual World for Robotic Manipulation (CoRL 2020 / PMLR 2021)

[![arXiv: 2010.14406](https://img.shields.io/badge/arXiv-2010.14406-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2010.14406) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2010.14406) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://transporternets.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/google-research/ravens) [![GitHub stars](https://img.shields.io/github/stars/google-research/ravens?style=flat-square&label=stars&color=C58A18)](https://github.com/google-research/ravens/stargazers) [![GitHub forks](https://img.shields.io/github/forks/google-research/ravens?style=flat-square&label=forks&color=64748B)](https://github.com/google-research/ravens/forks) &nbsp; [`T1`](#t1) [`T8`](#t8)

通过平移与旋转视觉特征并进行相关匹配，预测抓取和放置的空间位移，将对应建模用于机器人操作。

---

<a id="p63"></a>
#### Learning To Explore Using Active Neural SLAM (ICLR 2020)

[![arXiv: 2004.05155](https://img.shields.io/badge/arXiv-2004.05155-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2004.05155) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2004.05155) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/devendrachaplot/Neural-SLAM) [![GitHub stars](https://img.shields.io/github/stars/devendrachaplot/Neural-SLAM?style=flat-square&label=stars&color=C58A18)](https://github.com/devendrachaplot/Neural-SLAM/stargazers) [![GitHub forks](https://img.shields.io/github/forks/devendrachaplot/Neural-SLAM?style=flat-square&label=forks&color=64748B)](https://github.com/devendrachaplot/Neural-SLAM/forks) &nbsp; [`T6`](#t6)

结合可学习空间映射、全局探索策略与局部规划，将几何地图用于具身环境中的主动探索。

---

<a id="p64"></a>
#### Object Goal Navigation using Goal-Oriented Semantic Exploration (NeurIPS 2020)

[![arXiv: 2007.00643](https://img.shields.io/badge/arXiv-2007.00643-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2007.00643) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/devendrachaplot/Object-Goal-Navigation) [![GitHub stars](https://img.shields.io/github/stars/devendrachaplot/Object-Goal-Navigation?style=flat-square&label=stars&color=C58A18)](https://github.com/devendrachaplot/Object-Goal-Navigation/stargazers) [![GitHub forks](https://img.shields.io/github/forks/devendrachaplot/Object-Goal-Navigation?style=flat-square&label=forks&color=64748B)](https://github.com/devendrachaplot/Object-Goal-Navigation/forks) &nbsp; [`T6`](#t6)

建立情景语义地图并利用目标类别相关的空间先验规划探索，完成未知环境中的对象目标导航。

---

<a id="s074"></a>
#### Dense Object Nets: Learning Dense Visual Object Descriptors By and For Robotic Manipulation (CoRL 2018 / PMLR 2018)

[![arXiv: 1806.08756](https://img.shields.io/badge/arXiv-1806.08756-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1806.08756) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/RobotLocomotion/pytorch-dense-correspondence) [![GitHub stars](https://img.shields.io/github/stars/RobotLocomotion/pytorch-dense-correspondence?style=flat-square&label=stars&color=C58A18)](https://github.com/RobotLocomotion/pytorch-dense-correspondence/stargazers) [![GitHub forks](https://img.shields.io/github/forks/RobotLocomotion/pytorch-dense-correspondence?style=flat-square&label=forks&color=64748B)](https://github.com/RobotLocomotion/pytorch-dense-correspondence/forks) &nbsp; [`T4`](#t4) [`T6`](#t6)

利用多视图三维重建自动构造对应监督，学习支持跨姿态与跨物体操作的稠密视觉描述子。

---

<details>
<summary>关联阅读 · 15 篇其他 Topic 的论文</summary>

- [DreamerV3](#p68) (2025)
- [3D-Mem](#s066) (2025)
- [GraphEQA](#s067) (2025)
- [ConceptGraphs](#p56) (2024)
- [UniSim](#p57) (2024)
- [Visual Language Maps (VLMaps)](#p54) (2023)
- [ConceptFusion](#p55) (2023)
- [DROID-SLAM](#p40) (2021)
- [Semantic MapNet (SMNet)](#p53) (2021)
- [EgoMap](#s080) (2020)
- [PlaNet](#p67) (2019)
- [Neural Map](#s065) (2018)
- [Gibson Env](#s071) (2018)
- [MapNet](#s081) (2018)
- [DNA / CDNA / STP](#s068) (2016)

</details>

[↑ 6.3 本类开头](#topic-embodied-agents) · [↑ 返回 Topic 导航](#topics)

---


<a id="technology"></a>
## 🧩 基础技术交叉索引

一种方法可以跨多个技术族；点击方法名直达主条目，条目的 `T1–T9` 标签可返回本表。文献入口按年份倒序排列。

<details>
<summary><b>展开 9 类基础技术与文献索引</b></summary>

| 技术族 | 核心表示 | 文献入口 |
| --- | --- | --- |
| <a id="t1"></a>**T1 · 参数化几何变换** | 刚体 / 相似 / 仿射 / 单应性 | [PixelStitch](#s018) · [HomoGen](#s028) · [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) · [CLIPort](#p66) · [DUT](#s019) · [Unsupervised Deep Image Stitching (UDIS)](#p14) · [Transporter Networks](#p65) · [EgoMap](#s080) · [Deep Image Homography Estimation](#p13) · [COLMAP / Structure-from-Motion Revisited](#p38) · [DNA / CDNA / STP](#s068) · [SPHP](#s016) · [Parallax-tolerant Image Stitching](#s017) · [Lucas–Kanade / Inverse Compositional](#c02) |
| <a id="t2"></a>**T2 · 控制点、样条与连续插值** | TPS / RBF / FFD / B-spline / MLS | [WarpI2I](#n26) · [StabStitch](#n28) · [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) · [Thin-Plate Spline Motion Model for Image Animation](#n03) · [Adaptive Content Generation and Preservation (ACGPN)](#p28) · [Deep Learning Image Registration (DLIR)](#p18) · [CP-VTON](#c24) · [VITON](#p27) · [Bounded Biharmonic Weights (BBW)](#p03) · [Moving Least Squares (MLS)](#c08) · [B-spline FFD Registration](#c07) · [Beier–Neely Feature-Based Morphing](#c06) · [Thin-Plate Spline (TPS) / Principal Warps](#c05) · [Free-Form Deformation (FFD)](#c04) |
| <a id="t3"></a>**T3 · 网格与局部形状保持** | 分片变换 / ARAP / 局部投影 | [Tether / Autonomous Functional Play](#s077) · [Inpaint4Drag](#s003) · [FlowDrag](#s004) · [StabStitch](#n28) · [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) · [DUT](#s019) · [Unsupervised Deep Image Stitching (UDIS)](#p14) · [MeshFlow](#p16) · [DynamicFusion](#p50) · [Parallax-tolerant Image Stitching](#s017) · [As-Projective-As-Possible (APAP) / Moving DLT](#c12) · [Bundled Camera Paths](#p15) · [Bounded Biharmonic Weights (BBW)](#p03) · [Content-Preserving Warps for 3D Video Stabilization](#c29) · [Green Coordinates](#s002) · [As-Rigid-As-Possible (ARAP) Surface Modeling](#c09) · [Embedded Deformation](#p02) · [Harmonic Coordinates](#s001) · [Laplacian Surface Editing](#p01) |
| <a id="t4"></a>**T4 · 稠密对应与光流** | 稠密 flow / 相关体 / 全局匹配 | [Tether / Autonomous Functional Play](#s077) · [MEMFOF](#n20) · [UFM](#s015) · [PixelStitch](#s018) · [BiM-VFI](#s029) · [FIA-VTON](#s032) · [FloVD](#s047) · [MotionPro](#s050) · [FoundationStereo](#s055) · [SEA-RAFT](#n13) · [DragAnything](#p37) · [MASt3R](#p42) · [Robust Dense Matching (RoMa)](#p71) · [FloED](#s027) · [Upscale-A-Video](#s030) · [FloAt](#s033) · [D4-VTON](#s036) · [FlowVid](#s038) · [FLATTEN](#s039) · [WAVE (DDIM inversion)](#s042) · [Motion-I2V](#s045) · [MotionCraft](#s046) · [UniMatch: Unifying Flow, Stereo and Depth Estimation](#n09) · [FlowFormer++](#p12) · [DragNUWA](#p36) · [Dense Kernelized Matching (DKM)](#p70) · [PDC-Net+](#s012) · [CroCo v2](#s014) · [ProPainter](#s024) · [DCI-VTON](#s031) · [GP-VTON](#s035) · [LatentWarp](#s040) · [Rerender A Video](#s041) · [GMFlow](#n01) · [FlowFormer](#n02) · [FILM: Frame Interpolation for Large Motion](#n04) · [BasicVSR++](#n07) · [RIFE](#p23) · [E2FGVI](#s025) · [HR-VITON](#s034) · [ClothFormer](#s078) · [Global Motion Aggregation (GMA)](#p11) · [BasicVSR](#p25) · [Parser-Free Appearance Flow (PF-AFN)](#p29) · [DROID-SLAM](#p40) · [Neural Scene Flow Fields (NSFF)](#p49) · [LoFTR](#p69) · [COTR](#s011) · [RAFT-Stereo](#s053) · [RAFT](#c20) · [GLU-Net](#s013) · [Depth-Aware Interpolation (DAIN)](#p22) · [EDVR](#p24) · [Task-Oriented Flow (TOFlow)](#p26) · [Deep Flow-Guided Video Inpainting](#s026) · [PWC-Net](#c15) · [LiteFlowNet](#p10) · [Super SloMo](#p21) · [Dense Object Nets](#s074) · [FlowNet 2.0](#p08) · [SPyNet](#p09) · [MeshFlow](#p16) · [FlowNet](#p07) · [SIFT Flow](#p72) · [Lucas–Kanade / Inverse Compositional](#c02) · [Brox et al. Variational Optical Flow](#c27) · [Horn–Schunck](#c03) |
| <a id="t5"></a>**T5 · 可逆形变与医学配准** | 速度场 / 微分同胚 / 逆一致性 | [SGDIR](#s023) · [Fast Forward](#s084) · [uniGradICON](#n14) · [GradICON](#s020) · [Fourier-Net](#s022) · [TransMorph](#n05) · [SynthMorph](#n06) · [ICON](#p20) · [Symmetric Diffeomorphic Registration (SYMNet)](#p19) · [LapIRN](#s021) · [VoxelMorph](#c18) · [Deep Learning Image Registration (DLIR)](#p18) · [Diffeomorphic Demons](#c11) · [SyN: Symmetric Diffeomorphic Registration](#c10) · [LDDMM / Geodesic Flows of Diffeomorphisms](#c26) · [B-spline FFD Registration](#c07) · [Demons Registration](#p17) |
| <a id="t6"></a>**T6 · 深度与三维重投影** | 深度 / 相机位姿 / 投影与可见性 | [CameraNoise](#n24) · [Warp-as-History](#n27) · [WAVE: Warp-Based View Guidance](#n22) · [SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion](#n23) · [FlowDrag](#s004) · [TrajectoryCrafter](#s048) · [Latent-Reframe](#s049) · [VGGT](#s054) · [FoundationStereo](#s055) · [DepthSplat](#s059) · [MoSca](#s063) · [3D-Mem](#s066) · [GraphEQA](#s067) · [Spatial Memory World Models](#s073) · [GenWarp](#n15) · [MotionCtrl](#p34) · [CameraCtrl](#p35) · [DUSt3R](#p41) · [MASt3R](#p42) · [Dynamic 3D Gaussians](#p51) · [ConceptGraphs](#p56) · [Drive-WM](#p59) · [MVSplat](#s058) · [MultiDiff](#s060) · [UniMatch: Unifying Flow, Stereo and Depth Estimation](#n09) · [3D Gaussian Splatting (3DGS)](#p45) · [Visual Language Maps (VLMaps)](#p54) · [ConceptFusion](#p55) · [RVT](#s075) · [Trans4Map](#s082) · [TiNeuVox](#p52) · [DROID-SLAM](#p40) · [IBRNet](#p46) · [pixelNeRF](#p47) · [Neural Scene Flow Fields (NSFF)](#p49) · [Semantic MapNet (SMNet)](#p53) · [RAFT-Stereo](#s053) · [NeRF](#p44) · [Active Neural SLAM](#p63) · [Goal-Oriented Semantic Exploration (SemExp)](#p64) · [CasMVSNet](#s051) · [SynSin](#s056) · [EgoMap](#s080) · [3D Photography](#s083) · [Monodepth2](#c16) · [Depth-Aware Interpolation (DAIN)](#p22) · [DPSNet](#s052) · [MVSNet](#p39) · [Stereo Magnification / Multiplane Images](#p48) · [Gibson Env](#s071) · [Dense Object Nets](#s074) · [MapNet](#s081) · [SfMLearner](#p43) · [COLMAP / Structure-from-Motion Revisited](#p38) · [DynamicFusion](#p50) · [Depth-Image-Based Rendering (DIBR)](#c28) |
| <a id="t7"></a>**T7 · 可微采样与 Splatting** | 插值 / 核足迹 / 冲突聚合 / 伴随 | [Fast Forward](#s084) · [LookingGlass / Laplacian Pyramid Warping (LPW)](#n21) · [SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion](#n23) · [gsplat](#s010) · [DepthSplat](#s059) · [How I Warped Your Noise / ∫-noise](#n16) · [Dynamic 3D Gaussians](#p51) · [Mip-Splatting](#s008) · [MVSplat](#s058) · [Multi-Frequency Representation (MFR)](#s079) · [ImWIP](#n10) · [3D Gaussian Splatting (3DGS)](#p45) · [Kernel Aware Resampler](#s006) · [Local Texture Estimator for Warping (LTEW)](#s085) · [IBRNet](#p46) · [SRWarp](#s086) · [Softmax Splatting](#c19) · [nvdiffrast](#s009) · [SynSin](#s056) · [Soft Rasterizer (SoftRas)](#p06) · [Depth-Aware Interpolation (DAIN)](#p22) · [Linearized Multi-Sampling](#s007) · [DPSNet](#s052) · [Neural 3D Mesh Renderer](#p05) · [SV2P](#s070) · [DNA / CDNA / STP](#s068) · [Spatial Transformer Networks (STN)](#c13) · [EWA Volume Splatting](#c25) · [Surface Splatting](#p04) |
| <a id="t8"></a>**T8 · 学习式特征与三维形变** | Offset / 局部仿射 / Canonical field | [MoSca](#s063) · [Deformable 3D Gaussians](#n11) · [4D Gaussian Splatting for Real-Time Dynamic Scene Rendering](#n12) · [Dynamic 3D Gaussians](#p51) · [DragDiffusion](#s005) · [SC-GS](#s061) · [SceNeRFlow](#s062) · [ProPainter](#s024) · [Trans4Map](#s082) · [Thin-Plate Spline Motion Model for Image Animation](#n03) · [FILM: Frame Interpolation for Large Motion](#n04) · [BasicVSR++](#n07) · [TiNeuVox](#p52) · [CLIPort](#p66) · [E2FGVI](#s025) · [FlowBot3D](#s076) · [D-NeRF](#c21) · [Nerfies](#c22) · [HyperNeRF](#c23) · [Neural Scene Flow Fields (NSFF)](#p49) · [Transporter Networks](#p65) · [face-vid2vid](#s037) · [NR-NeRF](#s064) · [EgoMap](#s080) · [First Order Motion Model (FOMM)](#c17) · [EDVR](#p24) · [X2Face](#p30) · [MapNet](#s081) · [Deformable ConvNets (DCN)](#c14) · [DynamicFusion](#p50) |
| <a id="t9"></a>**T9 · 生成式、频率与随机场** | 几何生成融合 / Noise transport / 频率处理 | [CameraNoise](#n24) · [DMAligner](#n25) · [WarpI2I](#n26) · [Warp-as-History](#n27) · [Go-with-the-Flow](#n19) · [LookingGlass / Laplacian Pyramid Warping (LPW)](#n21) · [WAVE: Warp-Based View Guidance](#n22) · [SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion](#n23) · [GameNGen](#p61) · [DreamerV3](#p68) · [Inpaint4Drag](#s003) · [FlowDrag](#s004) · [HomoGen](#s028) · [FIA-VTON](#s032) · [Infinite-Resolution Integral Noise Warping](#s043) · [EquiVDM / Warped-Noise Equivariance](#s044) · [FloVD](#s047) · [TrajectoryCrafter](#s048) · [Latent-Reframe](#s049) · [MotionPro](#s050) · [Spatial Memory World Models](#s073) · [GenWarp](#n15) · [How I Warped Your Noise / ∫-noise](#n16) · [Warped Diffusion](#n17) · [StableVITON](#n18) · [FreeNoise](#p32) · [ConsistI2V](#p33) · [MotionCtrl](#p34) · [CameraCtrl](#p35) · [DragAnything](#p37) · [UniSim](#p57) · [Drive-WM](#p59) · [Genie](#p60) · [DIAMOND](#p62) · [DragDiffusion](#s005) · [FloED](#s027) · [Upscale-A-Video](#s030) · [FloAt](#s033) · [D4-VTON](#s036) · [FlowVid](#s038) · [FLATTEN](#s039) · [WAVE (DDIM inversion)](#s042) · [Motion-I2V](#s045) · [MotionCraft](#s046) · [MultiDiff](#s060) · [Preserve Your Own Correlation (PYoCo)](#p31) · [DragNUWA](#p36) · [GAIA-1](#p58) · [DCI-VTON](#s031) · [GP-VTON](#s035) · [LatentWarp](#s040) · [Rerender A Video](#s041) · [HR-VITON](#s034) · [ClothFormer](#s078) · [Parser-Free Appearance Flow (PF-AFN)](#p29) · [Adaptive Content Generation and Preservation (ACGPN)](#p28) · [First Order Motion Model (FOMM)](#c17) · [PlaNet](#p67) · [CP-VTON](#c24) · [VITON](#p27) · [X2Face](#p30) |

</details>

<a id="resources"></a>
## 🛠️ 评估与实现资源

| 资源 | 入口 |
| --- | --- |
| 评估指标与比较原则 | [各方向的评估建议](docs/RESEARCH_GUIDE.zh-CN.md#topics) |
| 图像变换、可微采样与形变实现 | [常用实现入口](docs/RESEARCH_GUIDE.zh-CN.md#practice) |
| 数据集与基准 | 待补充；新增时注明任务、数据版本、指标与评估协议 |

<a id="guide"></a>
## 📖 阅读指南

| 阅读主题 | 入口 |
| --- | --- |
| 概念、坐标方向与收录边界 | [Warping 的三个层次 / Forward 与 Backward](docs/RESEARCH_GUIDE.zh-CN.md#scope) |
| 进展、方法局限与关键问题 | [技术演进与仍未解决的问题](docs/RESEARCH_GUIDE.zh-CN.md#trends) |
| 噪声 Warping 的统计要求 | [普通插值为什么会改变高斯噪声？](docs/RESEARCH_GUIDE.zh-CN.md#trends) |
| 工具、实现与方案选择 | [实现入口与快速选型](docs/RESEARCH_GUIDE.zh-CN.md#practice) |
| 收录依据与引用快照 | [2026-10-24 论文扩充核验记录](docs/EXPANSION_AUDIT.md) |
| 全 Topic 系统检索 | [检索词、相关性判断与版本核查](docs/SYSTEMATIC_SEARCH.zh-CN.md) |

<a id="contributing"></a>
## 🤝 参与贡献

欢迎通过 [Issue](https://github.com/gulucaptain/Awesome-Warping-Algorithm/issues) 或 [Pull Request](https://github.com/gulucaptain/Awesome-Warping-Algorithm/pulls) 补充论文、作者主页、代码或纠正分类。

每条建议包含 **论文名、发表年份/状态、Paper、Project、GitHub、技术族、主 Topic 和交叉 Topic 标签**。未公开的资源留空；第三方复现、共享框架与作者实现请明确区分。

维护者可编辑 [中英文文献数据](data/catalog.json)，再运行 `python3 scripts/build_readme.py` 同时更新中英文页面；计数与索引由同一份数据生成，运行 `python3 scripts/build_readme.py --check` 检查一致性。每条记录用 `primary_topic` 指定唯一主归属，用 `topics` 保存包括主归属在内的关联方向；新增论文后，将对应 Topic 的 `reserved` 设为 `false`。优先核对主题匹配、正式发表信息与方法影响力；引用快照须注明提供方、匹配记录及查询日期，不叠加预印本与正式版本的计数。详见 [扩充核验记录](docs/EXPANSION_AUDIT.md)。详细原理与旧版逐项备注保留在 [研究指南](docs/RESEARCH_GUIDE.zh-CN.md)。

系统补充时，先按应用任务、空间机制与被变换对象发现候选，再核验准确标题。保留检索词、排除理由和版本关系；分别说明显式 Warping、对应估计、流条件引导与空间记忆。详见 [全 Topic 系统检索记录](docs/SYSTEMATIC_SEARCH.zh-CN.md)。通用文档不计入论文，预印本与正式发表版本不重复统计。

<details>
<summary>版式参考与致谢</summary>

本页采用 GPT-Image 生成的无文字空间形变封面和 GitHub 原生 Markdown 排版。分类导航与论文入口的组织参考了以下合集及模板，没有复制其论文描述或图像：

- [Awesome Diffusion Models in Medical Imaging](https://github.com/amirhossein-kz/Awesome-Diffusion-Models-in-Medical-Imaging)
- [Awesome Diffusion Models](https://github.com/diff-usion/Awesome-Diffusion-Models)
- [Awesome Diffusion Categorized](https://github.com/wangkai930418/awesome-diffusion-categorized)
- [Awesome list guidelines](https://github.com/sindresorhus/awesome/blob/main/awesome.md)
- [Best README Template](https://github.com/othneildrew/Best-README-Template)
- [Shields.io](https://shields.io/) 与 [Simple Icons](https://simpleicons.org/)：品牌图标徽章与 GitHub 动态计数
- [Hugging Face 品牌资源](https://huggingface.co/brand)：品牌图标参考

</details>

<div align="center">

**[↑ 返回顶部](#top)**

<sub>映射坐标，保留结构，探索运动。</sub>

</div>
