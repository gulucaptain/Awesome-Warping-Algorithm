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

<b>57</b> 篇论文 &nbsp; · &nbsp; <b>37</b> 个代码仓库 &nbsp; · &nbsp; <b>6</b> 个研究板块 &nbsp; · &nbsp; <b>16</b> 个主题

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

正文按 **研究板块 → Topic** 编排，各 Topic 内论文按年份从新到旧直接列出，不另设年份导航或分组；子类别以独立简介块开头，论文按“完整标题（出处 年份）→ 资源徽章与技术标签同一行 → 贡献说明”统一展示，方法之间以分隔线区分。完整发表记录、实现来源与局限保留在中英文文献数据和研究指南中。经典与近期工作统一展示。正式发表工作采用代表性发表年份，预印本采用预印本年份，并保留发表历史；合并介绍多个基础方法的条目按所链接代表论文的发表年份排序。无单一年份的基础模型放在所属 Topic 末尾。同年条目保持数据中的顺序。覆盖截至 2026-10-24 的公开资料。方法贡献和局限来自原论文、作者资料与原版调研；本合集未对所有实现做统一复现。

每篇工作只有一个主 Topic；交叉方向通过关联标签和关联阅读连接。空间推理、世界模型、交互模拟与具身智能体方向先预留，后续优先收录与 Warping 直接相关的工作。

[完整定义、Forward / Backward 与核验原则 →](docs/RESEARCH_GUIDE.zh-CN.md#scope)

</details>

<a id="topics"></a>
## 🗂️ Topic 导航

6 个研究板块、16 个 Topic，其中 4 个待扩展。计数仅包含主条目，关联阅读不重复计数。

<table>
<thead>
<tr><th align="left">研究板块</th><th align="left">Topic</th><th align="left">主条目 / 状态</th></tr>
</thead>
<tbody>
<tr>
<td rowspan="2" valign="middle"><a href="#area-foundations">1. Warping 基础与算子</a></td>
<td><a href="#topic-geometry-editing">1.1 几何变换与形变编辑</a></td>
<td>8</td>
</tr>
<tr>
<td><a href="#topic-sampling-splatting">1.2 可微采样与 Splatting</a></td>
<td>3</td>
</tr>
<tr>
<td rowspan="3" valign="middle"><a href="#area-alignment">2. 对应估计与图像对齐</a></td>
<td><a href="#topic-optical-flow">2.1 光流与稠密对应</a></td>
<td>10</td>
</tr>
<tr>
<td><a href="#topic-image-alignment">2.2 图像配准、拼接与视频稳像</a></td>
<td>5</td>
</tr>
<tr>
<td><a href="#topic-medical-registration">2.3 医学图像配准与可逆形变</a></td>
<td>8</td>
</tr>
<tr>
<td rowspan="2" valign="middle"><a href="#area-video-processing">3. 视频处理与人物形变</a></td>
<td><a href="#topic-video-restoration">3.1 视频插帧与复原</a></td>
<td>5</td>
</tr>
<tr>
<td><a href="#topic-human-deformation">3.2 人物动画、运动迁移与虚拟试衣</a></td>
<td>4</td>
</tr>
<tr>
<td rowspan="2" valign="middle"><a href="#area-video-generation">4. 视频生成与运动控制</a></td>
<td><a href="#topic-noise-warping">4.1 噪声 Warping 与时序一致性</a></td>
<td>1</td>
</tr>
<tr>
<td><a href="#topic-controlled-generation">4.2 相机、轨迹与运动可控生成</a></td>
<td>3</td>
</tr>
<tr>
<td rowspan="4" valign="middle"><a href="#area-spatial-intelligence">5. 空间智能</a></td>
<td><a href="#topic-spatial-perception">5.1 空间感知、深度与三维重建</a></td>
<td>1</td>
</tr>
<tr>
<td><a href="#topic-novel-view-synthesis">5.2 重投影与新视角合成</a></td>
<td>4</td>
</tr>
<tr>
<td><a href="#topic-dynamic-3d">5.3 动态三维与 4D 场景</a></td>
<td>5</td>
</tr>
<tr>
<td><a href="#topic-spatial-reasoning">5.4 空间推理与场景记忆</a></td>
<td>待扩展</td>
</tr>
<tr>
<td rowspan="3" valign="middle"><a href="#area-world-models-agents">6. 世界模型与具身智能体</a></td>
<td><a href="#topic-world-models">6.1 世界模型与环境预测</a></td>
<td>待扩展</td>
</tr>
<tr>
<td><a href="#topic-interactive-simulation">6.2 交互式环境与模拟</a></td>
<td>待扩展</td>
</tr>
<tr>
<td><a href="#topic-embodied-agents">6.3 具身智能体、规划与控制</a></td>
<td>待扩展</td>
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
> **8 篇论文 · 按年份从新到旧排列**

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

<a id="c09"></a>
#### As-Rigid-As-Possible Surface Modeling (SGP 2007)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://igl.ethz.ch/projects/ARAP/arap_web.pdf) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://igl.ethz.ch/projects/ARAP/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/libigl/libigl) [![GitHub stars](https://img.shields.io/github/stars/libigl/libigl?style=flat-square&label=stars&color=C58A18)](https://github.com/libigl/libigl/stargazers) [![GitHub forks](https://img.shields.io/github/forks/libigl/libigl?style=flat-square&label=forks&color=64748B)](https://github.com/libigl/libigl/forks) &nbsp; [`T3`](#t3)

Sorkine–Alexa 以局部刚性约束保留形状细节，是网格编辑的经典能量设计。

---

<a id="c08"></a>
#### Image deformation using moving least squares (SIGGRAPH / TOG 2006)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1145/1141911.1141920) &nbsp; [`T2`](#t2)

Schaefer 等用局部加权拟合构造仿射、相似、刚性图像形变，支持交互控制。

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

<a id="c01"></a>
#### Rigid / Similarity / Affine / Homography (Foundational models)

[![Reference: Read](https://img.shields.io/badge/Reference-Read-2563EB?style=flat-square)](https://docs.opencv.org/4.x/d9/dab/tutorial_homography.html) &nbsp; [`T1`](#t1)

从全局刚体到投影变换；单应性可描述平面场景或固定光心纯旋转下的视图关系。

---

<details>
<summary>关联阅读 · 1 篇其他 Topic 的论文</summary>

- [EWA Volume Splatting](#c25) (2001)

</details>

[↑ 1.1 本类开头](#topic-geometry-editing) · [↑ 返回 Topic 导航](#topics)

---

<a id="topic-15"></a>
<a id="topic-sampling-splatting"></a>
### 1.2 可微采样与 Splatting

> **本类关注** · 插值、重采样、可微空间变换、采样核、伴随与导数
>
> **3 篇论文 · 按年份从新到旧排列**

---

<a id="n10"></a>
#### ImWIP: Open-source image warping toolbox with adjoints and derivatives (SoftwareX 2023)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1016/j.softx.2023.101524) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://imwip.readthedocs.io/en/latest/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/RendersJens/ImWIP) [![GitHub stars](https://img.shields.io/github/stars/RendersJens/ImWIP?style=flat-square&label=stars&color=C58A18)](https://github.com/RendersJens/ImWIP/stargazers) [![GitHub forks](https://img.shields.io/github/forks/RendersJens/ImWIP?style=flat-square&label=forks&color=64748B)](https://github.com/RendersJens/ImWIP/forks) &nbsp; [`T7`](#t7)

提供可微图像 warp 及其精确离散伴随与导数，服务逆问题优化。

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

<details>
<summary>关联阅读 · 2 篇其他 Topic 的论文</summary>

- [Warped Diffusion](#n17) (2024)
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
> **10 篇论文 · 按年份从新到旧排列**

---

<a id="n20"></a>
#### MEMFOF: High-Resolution Training for Memory-Efficient Multi-Frame Optical Flow Estimation (ICCV 2025)

[![arXiv: 2506.23151](https://img.shields.io/badge/arXiv-2506.23151-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.23151) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2506.23151) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://msu-video-group.github.io/memfof/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/msu-video-group/memfof) [![GitHub stars](https://img.shields.io/github/stars/msu-video-group/memfof?style=flat-square&label=stars&color=C58A18)](https://github.com/msu-video-group/memfof/stargazers) [![GitHub forks](https://img.shields.io/github/forks/msu-video-group/memfof?style=flat-square&label=forks&color=64748B)](https://github.com/msu-video-group/memfof/forks) &nbsp; [`T4`](#t4)

精简相关表示并引入多帧估计与高分辨率训练，推进原生 FullHD 光流的显存效率。

---

<a id="n13"></a>
#### SEA-RAFT: Simple, Efficient, Accurate RAFT for Optical Flow (ECCV 2024)

[![arXiv: 2405.14793](https://img.shields.io/badge/arXiv-2405.14793-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2405.14793) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2405.14793) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/princeton-vl/SEA-RAFT) [![GitHub stars](https://img.shields.io/github/stars/princeton-vl/SEA-RAFT?style=flat-square&label=stars&color=C58A18)](https://github.com/princeton-vl/SEA-RAFT/stargazers) [![GitHub forks](https://img.shields.io/github/forks/princeton-vl/SEA-RAFT?style=flat-square&label=forks&color=64748B)](https://github.com/princeton-vl/SEA-RAFT/forks) &nbsp; [`T4`](#t4)

通过初始 flow 回归、混合 Laplace 损失和刚性运动预训练，改善 RAFT 的效率与精度。

---

<a id="n09"></a>
#### Unifying Flow, Stereo and Depth Estimation (TPAMI 2023)

[![arXiv: 2211.05783](https://img.shields.io/badge/arXiv-2211.05783-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2211.05783) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2211.05783) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://haofeixu.github.io/unimatch/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/autonomousvision/unimatch) [![GitHub stars](https://img.shields.io/github/stars/autonomousvision/unimatch?style=flat-square&label=stars&color=C58A18)](https://github.com/autonomousvision/unimatch/stargazers) [![GitHub forks](https://img.shields.io/github/forks/autonomousvision/unimatch?style=flat-square&label=forks&color=64748B)](https://github.com/autonomousvision/unimatch/forks) &nbsp; [`T4`](#t4) [`T6`](#t6)

把 flow、双目视差与有位姿的跨视图深度统一为对应匹配任务。

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

<a id="c20"></a>
#### RAFT: Recurrent All-Pairs Field Transforms for Optical Flow (ECCV 2020)

[![arXiv: 2003.12039](https://img.shields.io/badge/arXiv-2003.12039-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2003.12039) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2003.12039) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/princeton-vl/RAFT) [![GitHub stars](https://img.shields.io/github/stars/princeton-vl/RAFT?style=flat-square&label=stars&color=C58A18)](https://github.com/princeton-vl/RAFT/stargazers) [![GitHub forks](https://img.shields.io/github/forks/princeton-vl/RAFT?style=flat-square&label=forks&color=64748B)](https://github.com/princeton-vl/RAFT/forks) &nbsp; [`T4`](#t4)

全像素对相关体与循环更新，成为稠密流估计的重要基线。

---

<a id="c15"></a>
#### PWC-Net: CNNs for Optical Flow Using Pyramid, Warping, and Cost Volume (CVPR 2018)

[![arXiv: 1709.02371](https://img.shields.io/badge/arXiv-1709.02371-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1709.02371) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/NVlabs/PWC-Net) [![GitHub stars](https://img.shields.io/github/stars/NVlabs/PWC-Net?style=flat-square&label=stars&color=C58A18)](https://github.com/NVlabs/PWC-Net/stargazers) [![GitHub forks](https://img.shields.io/github/forks/NVlabs/PWC-Net?style=flat-square&label=forks&color=64748B)](https://github.com/NVlabs/PWC-Net/forks) &nbsp; [`T4`](#t4)

金字塔 + 特征 warping + cost volume，学习粗到细残余运动。

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

[↑ 2.1 本类开头](#topic-optical-flow) · [↑ 返回 Topic 导航](#topics)

---

<a id="topic-01"></a>
<a id="topic-03"></a>
<a id="topic-04"></a>
<a id="topic-image-alignment"></a>
### 2.2 图像配准、拼接与视频稳像

> **本类关注** · 图像对齐、全景拼接、视差处理与时序稳定
>
> **5 篇论文 · 按年份从新到旧排列**

---

<a id="n25"></a>
#### DMAligner: Enhancing Image Alignment via Diffusion Model Based View Synthesis (CVPR 2026)

[![arXiv: 2602.23022](https://img.shields.io/badge/arXiv-2602.23022-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.23022) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://boomluo02.github.io/DMAligner/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/boomluo02/DMAligner) [![GitHub stars](https://img.shields.io/github/stars/boomluo02/DMAligner?style=flat-square&label=stars&color=C58A18)](https://github.com/boomluo02/DMAligner/stargazers) [![GitHub forks](https://img.shields.io/github/forks/boomluo02/DMAligner?style=flat-square&label=forks&color=64748B)](https://github.com/boomluo02/DMAligner/forks) &nbsp; [`T9`](#t9)

将图像对齐转为 diffusion-based view synthesis，以动态感知训练处理遮挡与光照变化。

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

<a id="c12"></a>
#### As-Projective-As-Possible Image Stitching with Moving DLT (CVPR 2013)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://openaccess.thecvf.com/content_cvpr_2013/papers/Zaragoza_As-Projective-As-Possible_Image_Stitching_2013_CVPR_paper.pdf) &nbsp; [`T3`](#t3)

Zaragoza 等允许局部偏离全局投影变换，以适应拼接中的非平面与视差。

---

<a id="c29"></a>
#### Content-Preserving Warps for 3D Video Stabilization (SIGGRAPH / TOG 2009)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://pages.cs.wisc.edu/~fliu/papers/siggraph09.pdf) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://web.cecs.pdx.edu/~fliu/project/3dstab.htm) &nbsp; [`T3`](#t3)

由三维相机运动与内容保持网格 warp 构造稳定视频，兼顾对齐和显著区域形状。

---

<details>
<summary>关联阅读 · 4 篇其他 Topic 的论文</summary>

- [Lucas–Kanade / Inverse Compositional](#c02) (2004)
- [B-spline FFD Registration](#c07) (1999)
- [Thin-Plate Spline (TPS) / Principal Warps](#c05) (1989)
- [Rigid / Similarity / Affine / Homography](#c01) (基础模型（无单一年份）)

</details>

[↑ 2.2 本类开头](#topic-image-alignment) · [↑ 返回 Topic 导航](#topics)

---

<a id="topic-02"></a>
<a id="topic-medical-registration"></a>
### 2.3 医学图像配准与可逆形变

> **本类关注** · 跨模态配准、微分同胚、拓扑保持与逆一致性
>
> **8 篇论文 · 按年份从新到旧排列**

---

<a id="n14"></a>
#### uniGradICON: A Foundation Model for Medical Image Registration (MICCAI 2024)

[![arXiv: 2403.05780](https://img.shields.io/badge/arXiv-2403.05780-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2403.05780) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/uncbiag/uniGradICON) [![GitHub stars](https://img.shields.io/github/stars/uncbiag/uniGradICON?style=flat-square&label=stars&color=C58A18)](https://github.com/uncbiag/uniGradICON/stargazers) [![GitHub forks](https://img.shields.io/github/forks/uncbiag/uniGradICON?style=flat-square&label=forks&color=64748B)](https://github.com/uncbiag/uniGradICON/forks) &nbsp; [`T5`](#t5)

将学习式配准推进到多数据集、跨解剖区域和新任务的通用初始化与零样本使用。

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

<a id="c18"></a>
#### VoxelMorph: A Learning Framework for Deformable Medical Image Registration (IEEE TMI 2019)

[![arXiv: 1809.05231](https://img.shields.io/badge/arXiv-1809.05231-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1809.05231) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://voxelmorph.csail.mit.edu/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/voxelmorph/voxelmorph) [![GitHub stars](https://img.shields.io/github/stars/voxelmorph/voxelmorph?style=flat-square&label=stars&color=C58A18)](https://github.com/voxelmorph/voxelmorph/stargazers) [![GitHub forks](https://img.shields.io/github/forks/voxelmorph/voxelmorph?style=flat-square&label=forks&color=64748B)](https://github.com/voxelmorph/voxelmorph/forks) &nbsp; [`T5`](#t5)

将逐对优化摊销为网络预测形变场，结合可微 warp 与图像相似性训练。

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
> **5 篇论文 · 按年份从新到旧排列**

---

<a id="n17"></a>
#### Warped Diffusion: Solving Video Inverse Problems with Image Diffusion Models (NeurIPS 2024)

[![arXiv: 2410.16152](https://img.shields.io/badge/arXiv-2410.16152-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2410.16152) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2410.16152) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://giannisdaras.github.io/warped_diffusion.github.io/) &nbsp; [`T9`](#t9)

用连续函数空间和变换等变性处理视频逆问题，以测试时自等变引导提高时序一致性。

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

<a id="c19"></a>
#### Softmax Splatting for Video Frame Interpolation (CVPR 2020)

[![arXiv: 2003.05534](https://img.shields.io/badge/arXiv-2003.05534-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2003.05534) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://sniklaus.com/softsplat) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sniklaus/softmax-splatting) [![GitHub stars](https://img.shields.io/github/stars/sniklaus/softmax-splatting?style=flat-square&label=stars&color=C58A18)](https://github.com/sniklaus/softmax-splatting/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sniklaus/softmax-splatting?style=flat-square&label=forks&color=64748B)](https://github.com/sniklaus/softmax-splatting/forks) &nbsp; [`T7`](#t7)

Niklaus–Liu 用 softmax 加权处理 forward warp 的多对一冲突，并支持图像和特征的可微前向投影。

---

<a id="c14"></a>
#### Deformable Convolutional Networks (ICCV 2017)

[![arXiv: 1703.06211](https://img.shields.io/badge/arXiv-1703.06211-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1703.06211) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/msracver/Deformable-ConvNets) [![GitHub stars](https://img.shields.io/github/stars/msracver/Deformable-ConvNets?style=flat-square&label=stars&color=C58A18)](https://github.com/msracver/Deformable-ConvNets/stargazers) [![GitHub forks](https://img.shields.io/github/forks/msracver/Deformable-ConvNets?style=flat-square&label=forks&color=64748B)](https://github.com/msracver/Deformable-ConvNets/forks) &nbsp; [`T8`](#t8)

为卷积采样位置学习 offset，使特征支持局部几何适应。

---

<details>
<summary>关联阅读 · 2 篇其他 Topic 的论文</summary>

- [RAFT](#c20) (2020)
- [PWC-Net](#c15) (2018)

</details>

[↑ 3.1 本类开头](#topic-video-restoration) · [↑ 返回 Topic 导航](#topics)

---

<a id="topic-09"></a>
<a id="topic-10"></a>
<a id="topic-human-deformation"></a>
### 3.2 人物动画、运动迁移与虚拟试衣

> **本类关注** · 人物驱动、外观保持、姿态迁移与服装对齐
>
> **4 篇论文 · 按年份从新到旧排列**

---

<a id="n18"></a>
#### StableVITON: Learning Semantic Correspondence with Latent Diffusion Model for Virtual Try-On (CVPR 2024)

[![arXiv: 2312.01725](https://img.shields.io/badge/arXiv-2312.01725-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2312.01725) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2312.01725) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/rlawjdghek/StableVITON) [![GitHub stars](https://img.shields.io/github/stars/rlawjdghek/StableVITON?style=flat-square&label=stars&color=C58A18)](https://github.com/rlawjdghek/StableVITON/stargazers) [![GitHub forks](https://img.shields.io/github/forks/rlawjdghek/StableVITON?style=flat-square&label=forks&color=64748B)](https://github.com/rlawjdghek/StableVITON/forks) &nbsp; [`T9`](#t9)

在扩散 latent 中学习服装与人体的语义对应，以 attention 实现隐式对齐与细节传递。

---

<a id="n03"></a>
#### Thin-Plate Spline Motion Model for Image Animation (CVPR 2022)

[![arXiv: 2203.14367](https://img.shields.io/badge/arXiv-2203.14367-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2203.14367) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2203.14367) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/yoyo-nb/Thin-Plate-Spline-Motion-Model) [![GitHub stars](https://img.shields.io/github/stars/yoyo-nb/Thin-Plate-Spline-Motion-Model?style=flat-square&label=stars&color=C58A18)](https://github.com/yoyo-nb/Thin-Plate-Spline-Motion-Model/stargazers) [![GitHub forks](https://img.shields.io/github/forks/yoyo-nb/Thin-Plate-Spline-Motion-Model?style=flat-square&label=forks&color=64748B)](https://github.com/yoyo-nb/Thin-Plate-Spline-Motion-Model/forks) &nbsp; [`T2`](#t2) [`T8`](#t8)

从局部仿射运动扩展到多个 TPS 变换，并结合多尺度遮挡掩码进行特征形变。

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

<details>
<summary>关联阅读 · 1 篇其他 Topic 的论文</summary>

- [Go-with-the-Flow](#n19) (2025)

</details>

[↑ 3.2 本类开头](#topic-human-deformation) · [↑ 返回 Topic 导航](#topics)

---

<a id="area-video-generation"></a>
## 4. 视频生成与运动控制


<a id="topic-noise-warping"></a>
### 4.1 噪声 Warping 与时序一致性

> **本类关注** · 随机场输运、噪声统计、运动相关噪声与跨帧一致性
>
> **1 篇论文 · 按年份从新到旧排列**

---

<a id="n16"></a>
#### How I Warped Your Noise: a Temporally-Correlated Noise Prior for Diffusion Models (ICLR 2024)

[![arXiv: 2504.03072](https://img.shields.io/badge/arXiv-2504.03072-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.03072) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://warpyournoise.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/mskwak01/How-I-Warped-Your-Noise-Unofficial) [![GitHub stars](https://img.shields.io/github/stars/mskwak01/How-I-Warped-Your-Noise-Unofficial?style=flat-square&label=stars&color=C58A18)](https://github.com/mskwak01/How-I-Warped-Your-Noise-Unofficial/stargazers) [![GitHub forks](https://img.shields.io/github/forks/mskwak01/How-I-Warped-Your-Noise-Unofficial?style=flat-square&label=forks&color=64748B)](https://github.com/mskwak01/How-I-Warped-Your-Noise-Unofficial/forks) &nbsp; [`T7`](#t7) [`T9`](#t9)

把像素噪声解释为连续白噪声场的区域积分，设计面向 Gaussian 统计的输运，兼顾运动相关性和噪声性质。

---

<details>
<summary>关联阅读 · 2 篇其他 Topic 的论文</summary>

- [CameraNoise](#n24) (2026)
- [Go-with-the-Flow](#n19) (2025)

</details>

[↑ 4.1 本类开头](#topic-noise-warping) · [↑ 返回 Topic 导航](#topics)

---

<a id="topic-14"></a>
<a id="topic-controlled-generation"></a>
### 4.2 相机、轨迹与运动可控生成

> **本类关注** · 相机控制、物体运动控制、几何引导与历史帧对齐
>
> **3 篇论文 · 按年份从新到旧排列**

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

<details>
<summary>关联阅读 · 3 篇其他 Topic 的论文</summary>

- [How I Warped Your Noise / ∫-noise](#n16) (2024)
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
> **1 篇论文 · 按年份从新到旧排列**

---

<a id="c16"></a>
#### Digging Into Self-Supervised Monocular Depth Estimation (ICCV 2019)

[![arXiv: 1806.01260](https://img.shields.io/badge/arXiv-1806.01260-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1806.01260) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nianticlabs/monodepth2) [![GitHub stars](https://img.shields.io/github/stars/nianticlabs/monodepth2?style=flat-square&label=stars&color=C58A18)](https://github.com/nianticlabs/monodepth2/stargazers) [![GitHub forks](https://img.shields.io/github/forks/nianticlabs/monodepth2?style=flat-square&label=forks&color=64748B)](https://github.com/nianticlabs/monodepth2/forks) &nbsp; [`T6`](#t6)

用深度、位姿和可微重投影进行自监督视图重建，引入最小重投影误差与自动掩码。

---

<details>
<summary>关联阅读 · 2 篇其他 Topic 的论文</summary>

- [UniMatch: Unifying Flow, Stereo and Depth Estimation](#n09) (2023)
- [Rigid / Similarity / Affine / Homography](#c01) (基础模型（无单一年份）)

</details>

[↑ 5.1 本类开头](#topic-spatial-perception) · [↑ 返回 Topic 导航](#topics)

---

<a id="topic-12"></a>
<a id="topic-novel-view-synthesis"></a>
### 5.2 重投影与新视角合成

> **本类关注** · DIBR、跨视图 Warping、可见性与反遮挡补全
>
> **4 篇论文 · 按年份从新到旧排列**

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

<a id="n15"></a>
#### GenWarp: Single Image to Novel Views with Semantic-Preserving Generative Warping (NeurIPS 2024)

[![arXiv: 2405.17251](https://img.shields.io/badge/arXiv-2405.17251-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2405.17251) [![Hugging Face: Paper](https://img.shields.io/badge/Hugging%20Face-Paper-FFD21E?style=flat-square&logo=huggingface&logoColor=FFD21E)](https://huggingface.co/papers/2405.17251) [![Project: Page](https://img.shields.io/badge/Project-Page-087F8C?style=flat-square)](https://genwarp-nvs.github.io/) [![GitHub: Code](https://img.shields.io/badge/GitHub-Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sony/genwarp) [![GitHub stars](https://img.shields.io/github/stars/sony/genwarp?style=flat-square&label=stars&color=C58A18)](https://github.com/sony/genwarp/stargazers) [![GitHub forks](https://img.shields.io/github/forks/sony/genwarp?style=flat-square&label=forks&color=64748B)](https://github.com/sony/genwarp/forks) &nbsp; [`T6`](#t6) [`T9`](#t9)

结合深度诱导的坐标信息与跨视图/自注意力，让模型学习保留可迁移内容并生成缺失部分。

---

<a id="c28"></a>
#### Depth-image-based rendering (DIBR), compression, and transmission for a new approach on 3D-TV (SPIE 2004)

[![Paper: Read](https://img.shields.io/badge/Paper-Read-2563EB?style=flat-square)](https://doi.org/10.1117/12.524762) &nbsp; [`T6`](#t6)

用颜色图与深度生成虚拟视角，是理解深度重投影、遮挡和空洞的经典路线；该论文不是重投影思想的首次提出。

---

<details>
<summary>关联阅读 · 3 篇其他 Topic 的论文</summary>

- [D-NeRF](#c21) (2021)
- [Nerfies](#c22) (2021)
- [Monodepth2](#c16) (2019)

</details>

[↑ 5.2 本类开头](#topic-novel-view-synthesis) · [↑ 返回 Topic 导航](#topics)

---

<a id="topic-13"></a>
<a id="topic-dynamic-3d"></a>
### 5.3 动态三维与 4D 场景

> **本类关注** · Canonical Deformation、动态 NeRF、可形变 Gaussian 与时空场景表示
>
> **5 篇论文 · 按年份从新到旧排列**

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

[↑ 5.3 本类开头](#topic-dynamic-3d) · [↑ 返回 Topic 导航](#topics)

---


<a id="topic-spatial-reasoning"></a>
### 5.4 空间推理与场景记忆

> **本类关注** · 空间关系、跨视角理解、持久地图与空间记忆
>
> **待扩展 · 暂无收录论文**

---

**待扩展：** 已预留方向，尚未收录论文。后续优先收录与空间对应、重投影、形变、噪声输运或时空对齐直接相关的工作。

[↑ 5.4 本类开头](#topic-spatial-reasoning) · [↑ 返回 Topic 导航](#topics)

---

<a id="area-world-models-agents"></a>
## 6. 世界模型与具身智能体


<a id="topic-world-models"></a>
### 6.1 世界模型与环境预测

> **本类关注** · 状态表示、动态预测、动作条件预测与未来推演
>
> **待扩展 · 暂无收录论文**

---

**待扩展：** 已预留方向，尚未收录论文。后续优先收录与空间对应、重投影、形变、噪声输运或时空对齐直接相关的工作。

[↑ 6.1 本类开头](#topic-world-models) · [↑ 返回 Topic 导航](#topics)

---


<a id="topic-interactive-simulation"></a>
### 6.2 交互式环境与模拟

> **本类关注** · 可交互世界生成、场景持久性、训练与评估环境、合成数据
>
> **待扩展 · 暂无收录论文**

---

**待扩展：** 已预留方向，尚未收录论文。后续优先收录与空间对应、重投影、形变、噪声输运或时空对齐直接相关的工作。

[↑ 6.2 本类开头](#topic-interactive-simulation) · [↑ 返回 Topic 导航](#topics)

---


<a id="topic-embodied-agents"></a>
### 6.3 具身智能体、规划与控制

> **本类关注** · 视觉导航、机器人操作、主动感知、空间记忆驱动规划与感知—行动闭环
>
> **待扩展 · 暂无收录论文**

---

**待扩展：** 已预留方向，尚未收录论文。后续优先收录与空间对应、重投影、形变、噪声输运或时空对齐直接相关的工作。

[↑ 6.3 本类开头](#topic-embodied-agents) · [↑ 返回 Topic 导航](#topics)

---


<a id="technology"></a>
## 🧩 基础技术交叉索引

一种方法可以跨多个技术族；点击方法名直达主条目，条目的 `T1–T9` 标签可返回本表。文献入口按年份倒序排列。

<details>
<summary><b>展开 9 类基础技术与文献索引</b></summary>

| 技术族 | 核心表示 | 文献入口 |
| --- | --- | --- |
| <a id="t1"></a>**T1 · 参数化几何变换** | 刚体 / 相似 / 仿射 / 单应性 | [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) · [Lucas–Kanade / Inverse Compositional](#c02) · [Rigid / Similarity / Affine / Homography](#c01) |
| <a id="t2"></a>**T2 · 控制点、样条与连续插值** | TPS / RBF / FFD / B-spline / MLS | [WarpI2I](#n26) · [StabStitch](#n28) · [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) · [Thin-Plate Spline Motion Model for Image Animation](#n03) · [CP-VTON](#c24) · [Moving Least Squares (MLS)](#c08) · [B-spline FFD Registration](#c07) · [Beier–Neely Feature-Based Morphing](#c06) · [Thin-Plate Spline (TPS) / Principal Warps](#c05) · [Free-Form Deformation (FFD)](#c04) |
| <a id="t3"></a>**T3 · 网格与局部形状保持** | 分片变换 / ARAP / 局部投影 | [StabStitch](#n28) · [UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching](#n08) · [As-Projective-As-Possible (APAP) / Moving DLT](#c12) · [Content-Preserving Warps for 3D Video Stabilization](#c29) · [As-Rigid-As-Possible (ARAP) Surface Modeling](#c09) |
| <a id="t4"></a>**T4 · 稠密对应与光流** | 稠密 flow / 相关体 / 全局匹配 | [MEMFOF](#n20) · [SEA-RAFT](#n13) · [UniMatch: Unifying Flow, Stereo and Depth Estimation](#n09) · [GMFlow](#n01) · [FlowFormer](#n02) · [FILM: Frame Interpolation for Large Motion](#n04) · [BasicVSR++](#n07) · [RAFT](#c20) · [PWC-Net](#c15) · [Lucas–Kanade / Inverse Compositional](#c02) · [Brox et al. Variational Optical Flow](#c27) · [Horn–Schunck](#c03) |
| <a id="t5"></a>**T5 · 可逆形变与医学配准** | 速度场 / 微分同胚 / 逆一致性 | [uniGradICON](#n14) · [TransMorph](#n05) · [SynthMorph](#n06) · [VoxelMorph](#c18) · [Diffeomorphic Demons](#c11) · [SyN: Symmetric Diffeomorphic Registration](#c10) · [LDDMM / Geodesic Flows of Diffeomorphisms](#c26) · [B-spline FFD Registration](#c07) |
| <a id="t6"></a>**T6 · 深度与三维重投影** | 深度 / 相机位姿 / 投影与可见性 | [CameraNoise](#n24) · [Warp-as-History](#n27) · [WAVE: Warp-Based View Guidance](#n22) · [SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion](#n23) · [GenWarp](#n15) · [UniMatch: Unifying Flow, Stereo and Depth Estimation](#n09) · [Monodepth2](#c16) · [Depth-Image-Based Rendering (DIBR)](#c28) |
| <a id="t7"></a>**T7 · 可微采样与 Splatting** | 插值 / 核足迹 / 冲突聚合 / 伴随 | [LookingGlass / Laplacian Pyramid Warping (LPW)](#n21) · [SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion](#n23) · [How I Warped Your Noise / ∫-noise](#n16) · [ImWIP](#n10) · [Softmax Splatting](#c19) · [Spatial Transformer Networks (STN)](#c13) · [EWA Volume Splatting](#c25) |
| <a id="t8"></a>**T8 · 学习式特征与三维形变** | Offset / 局部仿射 / Canonical field | [Deformable 3D Gaussians](#n11) · [4D Gaussian Splatting for Real-Time Dynamic Scene Rendering](#n12) · [Thin-Plate Spline Motion Model for Image Animation](#n03) · [FILM: Frame Interpolation for Large Motion](#n04) · [BasicVSR++](#n07) · [D-NeRF](#c21) · [Nerfies](#c22) · [HyperNeRF](#c23) · [First Order Motion Model (FOMM)](#c17) · [Deformable ConvNets (DCN)](#c14) |
| <a id="t9"></a>**T9 · 生成式、频率与随机场** | 几何生成融合 / Noise transport / 频率处理 | [CameraNoise](#n24) · [DMAligner](#n25) · [WarpI2I](#n26) · [Warp-as-History](#n27) · [Go-with-the-Flow](#n19) · [LookingGlass / Laplacian Pyramid Warping (LPW)](#n21) · [WAVE: Warp-Based View Guidance](#n22) · [SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion](#n23) · [GenWarp](#n15) · [How I Warped Your Noise / ∫-noise](#n16) · [Warped Diffusion](#n17) · [StableVITON](#n18) · [First Order Motion Model (FOMM)](#c17) · [CP-VTON](#c24) |

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

<a id="contributing"></a>
## 🤝 参与贡献

欢迎通过 [Issue](https://github.com/gulucaptain/Awesome-Warping-Algorithm/issues) 或 [Pull Request](https://github.com/gulucaptain/Awesome-Warping-Algorithm/pulls) 补充论文、作者主页、代码或纠正分类。

每条建议包含 **论文名、发表年份/状态、Paper、Project、GitHub、技术族、主 Topic 和交叉 Topic 标签**。未公开的资源留空；第三方复现、共享框架与作者实现请明确区分。

维护者可编辑 [中英文文献数据](data/catalog.json)，再运行 `python3 scripts/build_readme.py` 同时更新中英文页面；计数与索引由同一份数据生成，运行 `python3 scripts/build_readme.py --check` 检查一致性。每条记录用 `primary_topic` 指定唯一主归属，用 `topics` 保存包括主归属在内的关联方向；新增论文后，将对应 Topic 的 `reserved` 设为 `false`。详细原理与旧版逐项备注保留在 [研究指南](docs/RESEARCH_GUIDE.zh-CN.md)。

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
