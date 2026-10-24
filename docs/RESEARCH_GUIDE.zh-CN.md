# Warping 研究指南

> 当前文献主目录见 [中文 README 的 Topic 导航](../README.zh-CN.md#topics)：按六个研究板块、16 个 Topic 组织，每个 Topic 内按年份倒序排列。本指南保留原有年份表和领域表，作为历史研究备注；主分类以 README 和 `data/catalog.json` 为准。本轮新增论文与引用快照见 [扩充核验记录](EXPANSION_AUDIT.md)。

[← 中文文献主页](../README.zh-CN.md) · [English guide](RESEARCH_GUIDE.md) · 本指南保留详细原理、分类比较、方法边界与选型说明。

后续覆盖全部 16 个 Topic 的检索词、原文核查、相关性判断和版本关系见 [系统检索记录](SYSTEMATIC_SEARCH.zh-CN.md)。原 [扩充核验记录](EXPANSION_AUDIT.md) 保留为上一批次的历史记录。

一个持续整理 **Warping（空间变换、形变与重采样）** 的研究资源库：从经典几何变换、样条与网格形变，到光流、可微采样、动态三维表示，以及生成模型中的图像、特征和噪声 warping。

**调研更新：2026-10-24。** 本版以计算机视觉、计算机图形学和医学图像中的**空间 warping** 为主，采用“基础技术 × 应用领域”的双重索引。它是代表性工作的研究地图，不是穷尽式目录或统一性能排行榜。

## 目录

- [范围、符号与时间口径](#scope)
- [一、按照基础技术分类](#technology)
- [二、2022 年之前的经典方法](#classics)
- [三、2022–2026 年的发展与突破](#recent)
- [四、按照 Topic 和领域分类](#topics)
- [五、技术演进与仍未解决的问题](#trends)
- [六、实现与选型](#practice)
- [贡献方式与核验原则](#contributing)

<a id="scope"></a>
## 范围、符号与时间口径

### Warping 的三个层次

1. **变换模型 / 对应关系估计**：仿射、单应性、TPS、网格、光流、深度重投影、三维形变场等，决定“坐标移动到哪里”。
2. **采样 / 聚合算子**：backward sampling、forward splatting、插值与抗混叠，决定“移动后如何得到离散数值”。
3. **应用系统**：配准、拼接、插帧、动态重建、视角合成、扩散生成等，决定“为什么进行 warping，以及如何修复不可见区域”。

下文使用 **[模型]、[估计]、[算子]、[应用]、[相关]** 标注方法角色。光流网络是对应关系估计器；NeRF/3DGS 是场景表示与渲染体系；只有其中显式的形变、重投影或采样部分属于这里讨论的 warping。Attention 关联可用于隐式对齐，但通常不等价于一个可逆的几何坐标映射。

<a id="c01"></a>
### 基础概念：刚体、相似、仿射与单应性变换

这是概念资料，不是具体论文，不列入论文正文与统计。刚体、相似、仿射与投影变换以不同自由度描述全局坐标映射；单应性可描述平面场景或固定光心纯旋转下的视图关系。通用三维平移产生的视差与非刚性运动不能由单一矩阵普遍解释。

[OpenCV 几何原理与代码](https://docs.opencv.org/4.x/d9/dab/tutorial_homography.html)

### Forward 与 backward 的区别

- **Backward / pull**：给定目标位置 `y`，查询源位置 `φ(y)`，计算 `I_target(y) = sample(I_source, φ(y))`。方便填满目标网格，但需要目标到源的映射，且不能恢复源图中不存在的内容。
- **Forward / push / splat**：将源位置 `x` 投到 `ψ(x)`，再聚合源像素对目标网格的贡献。适合源深度重投影，需要处理多对一冲突、空洞和可见性。
- **Flow**：`ψ(x) = x + f(x)`。反向 flow 通常不是在同一坐标上直接取 `-f(x)`；遮挡区域甚至没有一一对应。
- **三维重投影**：使用深度、相机内外参，把源像素反投影为三维点，变换后投到目标相机。静态场景的相机运动 flow 与物体运动产生的 flow 应加以区分。

### 时间与证据口径

- “2022 年之前”指 **截至 2021 年**；“2022–2026”按代表性正式发表年份组织。若预印本更早，另行注明，因此第二组不意味着方法在 2022 年后才首次公开。
- 2026 年仅覆盖截至 **2026-10-24** 可核实的公开工作。正式会议、期刊与预印本分开标记；作者在 arXiv 自报接收的状态也注明来源。
- 每条记录提供原论文、出版社、会议页面或作者项目页。代码仅在有明确作者来源时链接；未列代码不表示没有代码。
- “突破”指下文说明的具体能力变化，不表示在所有数据集、分辨率、硬件上都优于经典方法。摘要、方法介绍与作者实现可支持分类，但不代替独立复现实验。
- **2026-10-24 范围审校**：删除 40 篇本身不构造显式空间 warp 的工作（可微光栅化与 3DGS 渲染库、仅以位姿/轨迹作为条件的视频生成、几何基础模型、语义地图与场景图记忆、潜空间世界模型与生成式模拟器等）；Lucas–Kanade 主 Topic 移至 2.2，Softmax Splatting 与 Deformable ConvNets 移至 1.2，Warped Diffusion 移至 4.1；FlowVid、WAVE (DDIM)、LatentWarp、Rerender A Video 由 4.1 移至 3.1（3.1 扩展为“视频插帧、复原与编辑”），DepthSplat 由 5.2 移至 5.1；另删除 SemExp、DMAligner、Dense Object Nets 与 FLATTEN（仅沿光流轨迹约束注意力，不做 warp）。随后按 16 个 Topic 补充检索，新增 43 篇显式构造或估计空间 warp 的工作（数据中 `selection.batch` 为 `2026-10-24-supplement`），每篇均核对原文与出处，并逐篇确认其 warping 机制。
- **不纳入主目录**：音频/时间序列的 Dynamic Time Warping（DTW）、操作系统 GPU warp、仅有名称相似而没有空间变换机制的方法。

<a id="technology"></a>
## 一、按照基础技术分类

这些技术轴可以组合：例如“深度重投影 + forward splatting + 扩散补全”同时属于 T6、T7 和 T9。

| 技术族 | 核心表示 / 操作 | 经典代表 | 2022–2026 代表 | 适用条件与局限 |
| --- | --- | --- | --- | --- |
| **T1 参数化几何变换** | 刚体、相似、仿射、单应矩阵 | [全局变换](#c01)、[Lucas–Kanade](#c02) | [UDIS++](#n08) 的全局分支 | 低自由度、稳定可解释；单一单应性无法普遍解释非平面视差 |
| **T2 控制点、样条与连续插值** | TPS/RBF、FFD、B-spline | [FFD](#c04)、[TPS](#c05)、[B-spline FFD](#c07)、[MLS](#c08) | [TPS Motion Model](#n03)、[UDIS++](#n08) | 稀疏控制易编辑；控制点质量、局部折叠和外推需关注 |
| **T3 网格与局部形状保持** | 分片变换、局部刚性/投影能量 | [ARAP](#c09)、[APAP](#c12) | [UDIS++](#n08)、[StabStitch](#n28) 的空间/时间约束 | 兼顾局部对齐与形状；优化成本和正则权重依赖场景 |
| **T4 稠密对应与光流** | 每像素位移、相关体、全局匹配 | [Horn–Schunck](#c03)、[PWC-Net](#c15)、[RAFT](#c20) | [GMFlow](#n01)、[FlowFormer](#n02)、[UniMatch](#n09)、[SEA-RAFT](#n13)、[MEMFOF](#n20) | 可描述复杂二维运动；遮挡、弱纹理、跨域与大位移仍困难 |
| **T5 可逆形变与医学配准** | 平滑速度场、微分同胚、逆一致性 | [LDDMM](#c26)、[SyN](#c10)、[Diffeomorphic Demons](#c11)、[VoxelMorph](#c18) | [TransMorph](#n05)、[SynthMorph](#n06)、[uniGradICON](#n14) | 关注拓扑、Jacobian 和解剖结构；离散实现仍须检查折叠 |
| **T6 深度与三维重投影** | 深度 + 相机位姿 + 投影 / 可见性 | [DIBR](#c28)、[Monodepth2](#c16) 中的视图重建 | [UniMatch](#n09)、[SplatDiff](#n23)、[CameraNoise](#n24) | 提供几何解释；受深度、标定、动态物体和反遮挡影响 |
| **T7 可微采样与 splatting** | 插值、核足迹、可微冲突聚合、伴随 | [EWA](#c25)、[STN](#c13)、[Softmax Splatting](#c19) | [ImWIP](#n10)、[Laplacian Pyramid Warping](#n21) | 属于算子层；不能自行解决错误对应或补全不可见内容 |
| **T8 学习式特征 / 三维形变** | offset、局部仿射、canonical deformation field | [DCN](#c14)、[FOMM](#c17)、[D-NeRF](#c21)、[Nerfies](#c22)、[HyperNeRF](#c23) | [BasicVSR++](#n07)、[Deformable 3D Gaussians](#n11)、[4D-GS](#n12) | 从二维特征对齐扩展到动态三维；不天然保证真实运动或可逆性 |
| **T9 生成式、频率与随机场 warping** | warp + generation、语义关联、噪声输运、频带处理 | [CP-VTON](#c24)、[FOMM](#c17) 是相关前驱 | [GenWarp](#n15)、[∫-noise](#n16)、[Warped Diffusion](#n17)、[Go-with-the-Flow](#n19)、[WarpI2I](#n26) | 从搬运像素扩展到生成先验；视觉合理性与几何/统计正确性要分别评估 |

<a id="classics"></a>
## 二、2022 年之前的经典方法

以下按技术族归组，组内尽量按年代排列。C 编号用于后面的领域索引。

### 2.1 参数化几何与运动估计

| ID | 方法 / 年份 | 技术角色与经典贡献 | 主要限制 | 原始资料 / 实现入口 |
| --- | --- | --- | --- | --- |
| <a id="c02"></a>C02 | **Lucas–Kanade**，1981；**Inverse Compositional**，统一框架 IJCV 2004 | [估计] 用图像残差优化 warp 参数；逆组合形式允许复用部分计算，是直接法对齐的重要基础 | 对初始化、光度假设和局部极小值敏感 | [Baker & Matthews 原文](https://www.ri.cmu.edu/pub_files/pub3/baker_simon_2004_1/baker_simon_2004_1.pdf) |
| <a id="c03"></a>C03 | **Horn–Schunck**，1981 | [估计] 亮度一致性与全局平滑正则结合，建立稠密变分光流的经典范式 | 运动边界易过度平滑；基础形式不适合大位移 | [Determining Optical Flow](https://doi.org/10.1016/0004-3702(81)90024-2) |
| <a id="c27"></a>C27 | **Brox et al. Variational Optical Flow**，ECCV 2004 | [估计] 结合亮度/梯度一致性和保边正则，为粗到细 warping 的数值求解提供理论解释 | 强光照变化与严重遮挡会破坏数据假设 | [High Accuracy Optical Flow Estimation Based on a Theory for Warping](https://www.mia.uni-saarland.de/Publications/brox-eccv04-of.pdf) |
| <a id="c15"></a>C15 | **PWC-Net**，CVPR 2018；预印本 2017 | [估计] 金字塔 + 特征 warping + cost volume，学习粗到细残余运动 | 逐层 warping 的误差可能传播；遮挡仍需额外处理 | [论文](https://arxiv.org/abs/1709.02371) · [作者代码](https://github.com/NVlabs/PWC-Net) |
| <a id="c20"></a>C20 | **RAFT**，ECCV 2020 | [估计] 全像素对相关体与循环更新，成为稠密流估计的重要基线 | 相关体开销随分辨率增加；它估计 flow，不是新的图像插值核 | [论文](https://arxiv.org/abs/2003.12039) · [作者代码](https://github.com/princeton-vl/RAFT) |

### 2.2 控制点、样条、网格与局部变换

| ID | 方法 / 年份 | 技术角色与经典贡献 | 主要限制 | 原始资料 / 实现入口 |
| --- | --- | --- | --- | --- |
| <a id="c04"></a>C04 | **Free-Form Deformation (FFD)**，SIGGRAPH 1986 | [模型] Sederberg–Parry 通过控制格与 Bernstein 多项式变形几何对象，奠定体积控制形变基础 | 格分辨率控制细节与复杂度；不自动保证无折叠 | [原文](https://www.cse.iitd.ac.in/~jatin/minor_p/papers/sederberg.pdf) |
| <a id="c05"></a>C05 | **Thin-Plate Spline (TPS) / Principal Warps**，TPAMI 1989 | [模型] Bookstein 将 TPS 用于地标形变分析，以弯曲能量定义平滑非刚性映射；TPS 的数学起源更早 | 全局支撑、离群控制点和边界外推可能产生不自然形变 | [原文 DOI](https://doi.org/10.1109/34.24792) |
| <a id="c06"></a>C06 | **Beier–Neely Feature-Based Morphing**，SIGGRAPH 1992 | [模型/应用] 用成对特征线段控制 inverse warp，再结合颜色混合实现 morphing | 依赖手工对应；复杂区域可能产生局部扭曲 | [原文](https://wcours.gel.ulaval.ca/GIF4105/old/h20/tps/tp3/beierneely92.pdf) |
| <a id="c07"></a>C07 | **B-spline FFD Registration**，IEEE TMI 1999 | [模型/估计] Rueckert 等将全局仿射与局部 B-spline FFD 结合，用于乳腺 MR 非刚性配准 | 普通 B-spline FFD 不自动满足微分同胚约束 | [原文 DOI](https://doi.org/10.1109/42.796284) |
| <a id="c08"></a>C08 | **Moving Least Squares (MLS)**，SIGGRAPH / TOG 2006 | [模型] Schaefer 等用局部加权拟合构造仿射、相似、刚性图像形变，支持交互控制 | 权重、控制点布局与外推影响结果；不是全局可逆性的保证 | [原文 DOI](https://doi.org/10.1145/1141911.1141920) |
| <a id="c09"></a>C09 | **As-Rigid-As-Possible (ARAP) Surface Modeling**，SGP 2007 | [模型/优化] Sorkine–Alexa 以局部刚性约束保留形状细节，是网格编辑的经典能量设计 | 需要网格与优化；大形变仍可能自交 | [作者项目页及论文](https://igl.ethz.ch/projects/ARAP/) · [libigl 实现教程](https://libigl.github.io/libigl/tutorial/) |
| <a id="c29"></a>C29 | **Content-Preserving Warps for 3D Video Stabilization**，SIGGRAPH / TOG 2009 | [模型/应用] 由三维相机运动与内容保持网格 warp 构造稳定视频，兼顾对齐和显著区域形状 | 依赖可靠运动重建；裁切、深度差异与残余畸变存在权衡 | [作者项目](https://web.cecs.pdx.edu/~fliu/project/3dstab.htm) · [论文](https://pages.cs.wisc.edu/~fliu/papers/siggraph09.pdf) |
| <a id="c12"></a>C12 | **As-Projective-As-Possible (APAP) / Moving DLT**，CVPR 2013 | [模型/估计] Zaragoza 等允许局部偏离全局投影变换，以适应拼接中的非平面与视差 | 大视差、重遮挡和非重叠区域的外推仍有挑战 | [原文](https://openaccess.thecvf.com/content_cvpr_2013/papers/Zaragoza_As-Projective-As-Possible_Image_Stitching_2013_CVPR_paper.pdf) |

### 2.3 拓扑保持与医学配准

| ID | 方法 / 年份 | 技术角色与经典贡献 | 主要限制 | 原始资料 / 实现入口 |
| --- | --- | --- | --- | --- |
| <a id="c26"></a>C26 | **LDDMM / Geodesic Flows of Diffeomorphisms**，IJCV 2005 | [模型/估计] Beg 等通过平滑速度场的时间积分与测地流构造大形变微分同胚映射，是计算解剖的重要基础 | 优化与数值积分成本较高；离散精度和正则尺度影响结果 | [原文](https://www.cs.jhu.edu/~misha/ReadingSeminar/Papers/Beg05.pdf) · [作者机构实现](https://www.cis.jhu.edu/software/lddmm-volume/index.php) |
| <a id="c10"></a>C10 | **SyN: Symmetric Diffeomorphic Registration**，Medical Image Analysis 2008 | [模型/估计] 对称微分同胚配准，结合互相关用于解剖图像对齐，是 ANTs 的代表性方法 | 逐对优化成本较高；结果依赖相似度、正则与离散化 | [原文全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC2276735/) |
| <a id="c11"></a>C11 | **Diffeomorphic Demons**，NeuroImage 2009 | [模型/估计] 在 Demons 框架中使用微分同胚更新，兼顾高效非参数配准与平滑可逆变形 | 数学模型的可逆性不免除数值 Jacobian 检查 | [原文 DOI](https://doi.org/10.1016/j.neuroimage.2008.10.040) · [原始摘要](https://pubmed.ncbi.nlm.nih.gov/19041946/) |
| <a id="c18"></a>C18 | **VoxelMorph**，MICCAI 2018 / IEEE TMI 2019 | [估计/应用] 将逐对优化摊销为网络预测形变场，结合可微 warp 与图像相似性训练 | 基础位移场版本与微分同胚扩展应区分；有数据分布依赖 | [TMI 论文](https://arxiv.org/abs/1809.05231) · [作者代码](https://github.com/voxelmorph/voxelmorph) |

### 2.4 可微采样与抗混叠

| ID | 方法 / 年份 | 技术角色与经典贡献 | 主要限制 | 原始资料 / 实现入口 |
| --- | --- | --- | --- | --- |
| <a id="c25"></a>C25 | **EWA Volume Splatting**，IEEE Visualization 2001 | [算子/相关] 用椭圆加权平均核处理投影重建与低通滤波，是理解 splatting 足迹和抗混叠的经典工作 | 体渲染算子，不能直接等同于二维光流 warp 或后来的 3DGS 系统 | [原文](https://dash.harvard.edu/bitstream/handle/1/4138240/Zwicker_EWA.pdf) |
| <a id="c13"></a>C13 | **Spatial Transformer Networks (STN)**，NeurIPS 2015 | [算子/学习模块] 参数预测、网格生成和可微采样联合训练，使空间变换可嵌入神经网络 | 学到的变换受参数化限制；双线性采样不负责遮挡补全与严格抗混叠 | [论文](https://arxiv.org/abs/1506.02025) |
| <a id="c19"></a>C19 | **Softmax Splatting**，CVPR 2020 | [算子] Niklaus–Liu 用 softmax 加权处理 forward warp 的多对一冲突，并支持图像和特征的可微前向投影 | 依赖 flow 与重要性度量；反遮挡空洞需要合成网络或其他补全 | [论文](https://arxiv.org/abs/2003.05534) · [作者代码](https://github.com/sniklaus/softmax-splatting) |

### 2.5 特征对齐、人物动画与三维形变

| ID | 方法 / 年份 | 技术角色与经典贡献 | 主要限制 | 原始资料 / 实现入口 |
| --- | --- | --- | --- | --- |
| <a id="c28"></a>C28 | **Depth-Image-Based Rendering (DIBR)**，Fehn，SPIE 2004 代表工作 | [模型/应用] 用颜色图与深度生成虚拟视角，是理解深度重投影、遮挡和空洞的经典路线；该论文不是重投影思想的首次提出 | 深度边界、反遮挡和投影冲突需专门处理 | [原文 DOI](https://doi.org/10.1117/12.524762) |
| <a id="c14"></a>C14 | **Deformable ConvNets (DCN)**，ICCV 2017 | [学习模块/相关] 为卷积采样位置学习 offset，使特征支持局部几何适应 | 每个核位置有偏移，不等价于一个全图物理运动场 | [论文](https://arxiv.org/abs/1703.06211) |
| <a id="c24"></a>C24 | **CP-VTON**，ECCV 2018 | [应用] 用 Geometric Matching Module 学习 TPS，将商品服装形变到人体，再学习融合掩码 | TPS 对大姿态变化、复杂遮挡和细纹理的表示有限 | [论文](https://arxiv.org/abs/1807.07688) |
| <a id="c16"></a>C16 | **Monodepth2**，ICCV 2019；预印本 2018 | [应用] 用深度、位姿和可微重投影进行自监督视图重建，引入最小重投影误差与自动掩码 | 是深度估计系统；几何 warp 仍受动态物体、反光与不可见区域影响 | [论文](https://arxiv.org/abs/1806.01260) · [作者代码](https://github.com/nianticlabs/monodepth2) |
| <a id="c17"></a>C17 | **First Order Motion Model (FOMM)**，NeurIPS 2019；arXiv 2020 | [模型/应用] 自学习关键点与局部一阶仿射运动，构造稠密特征 warp 和遮挡图实现图像动画 | 大身份差异、大旋转与显著反遮挡仍困难 | [会议论文](https://papers.nips.cc/paper/8935-first-order-motion-model-for-image-animation.pdf) · [作者代码](https://github.com/AliaksandrSiarohin/first-order-model) |
| <a id="c21"></a>C21 | **D-NeRF**，CVPR 2021；预印本 2020 | [模型/应用] 学习时间条件形变，把动态场景坐标映射到 canonical radiance field | 单目重建有歧义，动态细节和训练效率受限 | [论文](https://arxiv.org/abs/2011.13961) |
| <a id="c22"></a>C22 | **Nerfies**，ICCV 2021；预印本 2020 | [模型/应用] 连续三维形变场、弹性正则与粗到细优化，重建随意拍摄的非刚性场景 | 连续 canonical warp 难以处理拓扑变化；优化可能陷入局部极小值 | [论文](https://arxiv.org/abs/2011.12948) |
| <a id="c23"></a>C23 | **HyperNeRF**，SIGGRAPH Asia / TOG 2021 | [模型/应用] 把表示提升到高维空间，通过切片建模拓扑变化，扩展普通连续三维 warp 的能力 | 高维表示不是对三维空间直接构造一个处处可逆的形变 | [论文](https://arxiv.org/abs/2106.13228) |

<a id="recent"></a>
## 三、2022–2026 年的发展与突破

### 3.1 2022：全局匹配、更灵活的运动表示与学习式配准

| ID | 工作 / 发表信息 | 核心变化及与 warping 的关系 | 边界 / 首次公开时间 | 论文 / 作者资源 |
| --- | --- | --- | --- | --- |
| <a id="n01"></a>N01 | **GMFlow**，CVPR 2022 | [估计/T4] Transformer 增强跨图特征，以全局匹配生成 flow，减少对大量顺序迭代的依赖 | 改进 flow 估计而非重采样核；预印本 **2021** | [论文](https://arxiv.org/abs/2111.13680) · [代码](https://github.com/haofeixu/gmflow) |
| <a id="n02"></a>N02 | **FlowFormer**，ECCV 2022 | [估计/T4] 对 4D cost volume 进行 Transformer 编码，并通过循环解码更新运动 | 需要关注相关表示和高分辨率显存开销 | [论文](https://arxiv.org/abs/2203.16194) · [作者页](https://drinkingcoder.github.io/publication/flowformer/) |
| <a id="n03"></a>N03 | **Thin-Plate Spline Motion Model for Image Animation**，CVPR 2022 | [模型/应用/T2,T8] 从局部仿射运动扩展到多个 TPS 变换，并结合多尺度遮挡掩码进行特征形变 | 经典 TPS 的学习式组合，不是新发明 TPS；极端身份差异仍有限 | [论文](https://openaccess.thecvf.com/content/CVPR2022/html/Zhao_Thin-Plate_Spline_Motion_Model_for_Image_Animation_CVPR_2022_paper.html) · [代码](https://github.com/yoyo-nb/Thin-Plate-Spline-Motion-Model) |
| <a id="n04"></a>N04 | **FILM: Frame Interpolation for Large Motion**，ECCV 2022 | [应用/T4,T8] 跨尺度共享的特征与运动估计，提高大运动插帧能力；可仅从图像帧训练 | 大反遮挡区域仍需合成；不是单一通用 warp 算子 | [论文](https://arxiv.org/abs/2202.04901) · [代码](https://github.com/google-research/frame-interpolation) |
| <a id="n05"></a>N05 | **TransMorph**，Medical Image Analysis 2022 | [估计/应用/T5] Transformer–ConvNet 混合模型用于三维医学配准，增强长程空间关系建模 | 预印本 **2021**；是否微分同胚取决于具体模型版本 | [论文](https://arxiv.org/abs/2111.10480) · [作者代码](https://github.com/junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration) |
| <a id="n06"></a>N06 | **SynthMorph**，IEEE TMI 2022（在线发表 2021） | [估计/应用/T5] 用合成标签和多样图像训练，提升跨 MRI 对比度的形变配准泛化 | 预印本 **2020**；进步主要来自训练策略与泛化能力 | [论文](https://arxiv.org/abs/2004.10282) · [作者入口](https://w3id.org/synthmorph) |
| <a id="n07"></a>N07 | **BasicVSR++**，CVPR 2022 | [应用/T4,T8] 二阶传播与 flow-guided deformable alignment，把光流先验与可形变特征采样结合 | 预印本 **2021**；针对视频复原系统 | [会议论文](https://openaccess.thecvf.com/content/CVPR2022/html/Chan_BasicVSR_Improving_Video_Super-Resolution_With_Enhanced_Propagation_and_Alignment_CVPR_2022_paper.html) · [代码](https://github.com/ckkelvinchan/BasicVSR_PlusPlus) |

### 3.2 2023：混合几何模型、统一对应与算子正确性

| ID | 工作 / 发表信息 | 核心变化及与 warping 的关系 | 边界 | 论文 / 作者资源 |
| --- | --- | --- | --- | --- |
| <a id="n08"></a>N08 | **UDIS++: Parallax-Tolerant Unsupervised Deep Image Stitching**，ICCV 2023 | [模型/应用/T1,T2,T3] 全局 homography + 局部 TPS，联合考虑重叠区对齐、非重叠区形状与接缝合成 | 对大视差的容忍不意味着解决所有三维遮挡 | [论文](https://arxiv.org/abs/2302.08207) · [代码](https://github.com/nie-lang/UDIS2) |
| <a id="n09"></a>N09 | **UniMatch: Unifying Flow, Stereo and Depth Estimation**，TPAMI 2023 | [估计/T4,T6] 把 flow、双目视差与有位姿的跨视图深度统一为对应匹配任务 | 预印本 **2022**；输出、几何约束和细化仍随任务变化 | [论文](https://arxiv.org/abs/2211.05783) · [正式论文](https://www.cvlibs.net/publications/Xu2023PAMI.pdf) |
| <a id="n10"></a>N10 | **ImWIP**，SoftwareX 2023 | [算子/T7] 提供可微图像 warp 及其精确离散伴随与导数，服务逆问题优化 | 伴随 `Wᵀ` 不等于逆 warp；精确性针对选定离散算子和浮点精度 | [论文](https://doi.org/10.1016/j.softx.2023.101524) · [官方文档](https://imwip.readthedocs.io/en/latest/) |

### 3.3 2024：三维形变的显式化，以及生成与随机场的结合

| ID | 工作 / 发表信息 | 核心变化及与 warping 的关系 | 边界 | 论文 / 作者资源 |
| --- | --- | --- | --- | --- |
| <a id="n11"></a>N11 | **Deformable 3D Gaussians**，CVPR 2024；预印本 2023 | [模型/应用/T8] 在 canonical Gaussian 表示上学习形变场，将动态重建与快速 splatting 渲染结合 | 三维参数形变 + 渲染，不等同于二维图像插值；有逐场景优化需求 | [论文](https://arxiv.org/abs/2309.13101) · [代码](https://github.com/ingra14m/Deformable-3D-Gaussians) |
| <a id="n12"></a>N12 | **4D Gaussian Splatting for Real-Time Dynamic Scene Rendering**，CVPR 2024；预印本 2023 | [模型/应用/T8] 结合时空特征与 Gaussian 形变，提升动态场景表示的训练、存储及渲染效率 | 此处专指 Wu 等的 4D-GS，不泛指所有名字含 4D Gaussian 的方法 | [论文](https://arxiv.org/abs/2310.08528) |
| <a id="n28"></a>N28 | **StabStitch**，ECCV 2024 | [模型/应用/T2,T3] 将视频拼接与稳像统一到无监督在线框架，约束空间对齐和时间稳定性，抑制逐帧 warp 抖动 | 图像级对齐好不等于视频稳定；仍需比较延迟、畸变和动态场景效果 | [论文](https://arxiv.org/abs/2403.06378) · [作者代码](https://github.com/nie-lang/StabStitch) |
| <a id="n13"></a>N13 | **SEA-RAFT**，ECCV 2024 | [估计/T4] 通过初始 flow 回归、混合 Laplace 损失和刚性运动预训练，改善 RAFT 的效率与精度 | 属于对应估计的工程与建模改进；效果依赖评测协议 | [作者论文与代码](https://github.com/princeton-vl/SEA-RAFT) |
| <a id="n14"></a>N14 | **uniGradICON**，MICCAI 2024 | [估计/应用/T5] 将学习式配准推进到多数据集、跨解剖区域和新任务的通用初始化与零样本使用 | 泛化并非对任意模态、任意器官的保证 | [会议论文](https://papers.miccai.org/miccai-2024/816-Paper0527.html) · [代码](https://github.com/uncbiag/uniGradICON) |
| <a id="n15"></a>N15 | **GenWarp**，NeurIPS 2024 | [应用/T6,T9] 结合深度诱导的坐标信息与跨视图/自注意力，让模型学习保留可迁移内容并生成缺失部分 | 属于 generative warping，生成区域并非从源图精确搬运 | [会议论文](https://proceedings.neurips.cc/paper_files/paper/2024/hash/92e886487a8354b03d8bf4416eae6d7d-Abstract-Conference.html) · [代码](https://github.com/sony/genwarp) |
| <a id="n16"></a>N16 | **How I Warped Your Noise / ∫-noise**，ICLR 2024 | [算子/T7,T9] 把像素噪声解释为连续白噪声场的区域积分，设计面向 Gaussian 统计的输运，兼顾运动相关性和噪声性质 | 与普通 RGB 插值目标不同；会议早于 **2025** arXiv 上传，不能按该 ID 误判为 2025 首发 | [ICLR 原文](https://openreview.net/pdf?id=pzElnMrgSD) · [作者页](https://warpyournoise.github.io/) |
| <a id="n17"></a>N17 | **Warped Diffusion**，NeurIPS 2024 | [应用/T9] 用连续函数空间和变换等变性处理视频逆问题，以测试时自等变引导提高时序一致性 | 不是仅对初始化噪声做一次 warp；关注视频补全与超分 | [论文](https://arxiv.org/abs/2410.16152) |

### 3.4 2025：可控噪声、频率感知和几何引导生成

| ID | 工作 / 发表信息 | 核心变化及与 warping 的关系 | 边界 | 论文 / 作者资源 |
| --- | --- | --- | --- | --- |
| <a id="n19"></a>N19 | **Go-with-the-Flow**，CVPR 2025 | [应用/T9] 高效生成 warped noise 并微调视频模型，把运动模式作为噪声先验，用于运动迁移及相机/物体控制 | 需要相应模型适配；普通 pretrained 模型不必然直接支持相同控制 | [作者论文、代码与演示](https://eyeline-labs.github.io/Go-with-the-Flow/) |
| <a id="n20"></a>N20 | **MEMFOF**，ICCV 2025 | [估计/T4] 精简相关表示并引入多帧估计与高分辨率训练，推进原生 FullHD 光流的显存效率 | 不是新的采样核；资源数据应按作者指定硬件、精度和分辨率复测 | [论文](https://arxiv.org/abs/2506.23151) · [代码](https://github.com/msu-video-group/memfof) |
| <a id="n21"></a>N21 | **LookingGlass / Laplacian Pyramid Warping (LPW)**，CVPR 2025 | [算子/应用/T7,T9] 用 Laplacian 金字塔进行频率感知的图像 warp 与视图聚合，支持多视角生成式 anamorphosis | 主要针对多变换生成与频率保真，不直接保证随机噪声统计 | [作者项目、论文](https://lookingglass-lpw.github.io/) |
| <a id="n22"></a>N22 | **WAVE: Warp-Based View Guidance**，ICCV 2025 | [应用/T6,T9] 用视图 warping 引导自适应 attention 与噪声重新初始化，提高单图新视角一致性，无需额外训练 | 依赖基础新视角模型与几何估计；与其他同名 WAVE 工作应区分 | [会议论文](https://openaccess.thecvf.com/content/ICCV2025/html/Park_WAVE_Warp-Based_View_Guidance_for_Consistent_Novel_View_Synthesis_Using_ICCV_2025_paper.html) |
| <a id="n23"></a>N23 | **SplatDiff: High-Fidelity Novel View Synthesis via Splatting-Guided Diffusion**，SIGGRAPH 2025 | [应用/T6,T7,T9] 以 pixel splatting 约束目标视角，结合对齐合成与 texture bridge，平衡几何一致性和纹理保真 | 深度和 splat 错误仍可能传播；生成细节需要单独核验真实性 | [论文](https://arxiv.org/abs/2502.12752) · [作者页](https://studios.disneyresearch.com/2025/07/16/splatdiff/) |

### 3.5 2026：几何到噪声、生成式对齐与空间资源重分配

| ID | 工作 / 核实状态 | 核心变化及与 warping 的关系 | 边界 | 原始来源 |
| --- | --- | --- | --- | --- |
| <a id="n24"></a>N24 | **CameraNoise**，**ICML 2026，PMLR 正式论文** | [模型/算子/应用/T6,T9] 以 Geometry-guided Reprojection Flow 与噪声 warping 将相机运动编码到时序相关噪声中，同时关注 Gaussian 先验与轨迹控制 | 效果依赖场景几何和运动估计；不能据此推导任意非刚性运动均可精确控制 | [正式论文](https://proceedings.mlr.press/v306/zhao26l.html) · [作者代码](https://github.com/gulucaptain/CameraNoise) |
| <a id="n26"></a>N26 | **WarpI2I**，2026；arXiv 注明 **ECCV 2026** | [模型/应用/T2,T9] 在编码前用 saliency-guided warp 向显著区域分配更多空间表示，处理后 unwarp，改善紧凑 latent 模型的结构保留 | 用 warp 分配表示预算，不以运动估计为核心；逆映射受数值采样影响 | [论文及会议声明](https://arxiv.org/abs/2606.31018) |
| <a id="n27"></a>N27 | **Warp-as-History**，**2026 预印本** | [应用/T6,T9] 将相机诱导的 warp 作为对齐目标位置的伪历史，结合有效 token 选择利用冻结模型的历史输入通路；另探索单视频 LoRA | 截止本版仅按公开预印本收录；控制能力仍需跨数据与轨迹验证 | [论文](https://arxiv.org/abs/2605.15182) |

<a id="topics"></a>
## 四、按照 Topic 和领域分类

同一工作可以属于多个领域。点击编号跳转到完整记录；本节是同一文献集合的第二种组织方式。

| Topic / 领域 | 核心问题 | 2022 年之前的代表 | 2022–2026 的代表与变化 | 建议评估 |
| --- | --- | --- | --- | --- |
| **图像配准 / Image Registration** | 两幅图的空间对齐 | [C01 全局变换](#c01)、[C02 LK](#c02)、[C05 TPS](#c05)、[C07 B-spline](#c07) | [N08 UDIS++](#n08) 混合几何 | 对应误差、有效区域、遮挡鲁棒性；生成结果不能仅用几何误差概括 |
| **医学图像 / Computational Anatomy** | 三维器官、跨模态与跨个体配准 | [C26 LDDMM](#c26)、[C10 SyN](#c10)、[C11 Diffeomorphic Demons](#c11)、[C18 VoxelMorph](#c18) | [N05 TransMorph](#n05)、[N06 SynthMorph](#n06)、[N14 uniGradICON](#n14)：长程关系与跨域泛化 | Dice、地标 TRE、Jacobian、逆一致性、运行时间 |
| **拼接 / 全景 / 几何校正** | 对齐重叠区，同时控制非重叠区畸变 | [C01 Homography](#c01)、[C12 APAP](#c12) | [N08 UDIS++](#n08)：homography + TPS + 接缝合成 | 配准误差、直线/形状保持、重影、接缝、视差范围 |
| **视频稳像 / 在线视频拼接** | 抑制相机抖动和逐帧 warp 的时间不一致 | [C29 Content-Preserving Warps](#c29) | [N28 StabStitch](#n28)：联合空间对齐与时间稳定 | 稳定性、裁切比例、内容畸变、接缝、在线延迟 |
| **光流 / 运动估计 / 稠密对应** | 寻找跨帧像素对应，生成可供 warp 使用的 flow | [C02 LK](#c02)、[C03 HS](#c03)、[C27 Brox](#c27)、[C15 PWC-Net](#c15)、[C20 RAFT](#c20) | [N01 GMFlow](#n01)、[N02 FlowFormer](#n02)、[N09 UniMatch](#n09)、[N13 SEA-RAFT](#n13)、[N20 MEMFOF](#n20) | EPE、outlier rate、遮挡区域、大运动、跨域、显存与延迟 |
| **视频插帧 / 慢动作** | 构造中间时刻，对冲突和反遮挡进行处理 | [C19 Softmax Splatting](#c19) | [N04 FILM](#n04)：大运动、多尺度共享与图像合成 | PSNR/SSIM、感知质量、运动边界、反遮挡与时序一致性 |
| **视频复原 / 超分 / 去噪 / 补全** | 对齐并融合跨帧信息 | [C14 DCN](#c14)、[C15 PWC-Net](#c15)、[C20 RAFT](#c20) 为常用组件 | [N07 BasicVSR++](#n07) 光流引导可形变对齐；[N17 Warped Diffusion](#n17) 图像先验用于视频逆问题 | 复原质量、闪烁、纹理粘连、错误传播、推理成本 |
| **图像编辑 / Morphing / 形状操控** | 由点、线或网格控制局部形变 | [C04 FFD](#c04)、[C05 TPS](#c05)、[C06 Beier–Neely](#c06)、[C08 MLS](#c08)、[C09 ARAP](#c09) | [N21 LPW](#n21) 频率感知生成；[N26 WarpI2I](#n26) 空间表示预算分配 | 控制点误差、局部形状、折叠、高频与往返采样损失 |
| **人像 / 人体动画 / Motion Transfer** | 从 driving motion 驱动 source appearance | [C17 FOMM](#c17) | [N03 TPS Motion Model](#n03) 扩展非刚性运动；[N19 Go-with-the-Flow](#n19) 噪声运动先验 | 身份/外观保持、关键点运动、姿态泛化、遮挡与时序一致性 |
| **虚拟试衣 / Virtual Try-On** | 服装到人体的对齐，保持纹理与标识 | [C24 CP-VTON](#c24)：显式 TPS | [GP-VTON](../README.zh-CN.md#s035)：局部 flow 与全局 parsing 协同的显式服装 warping | 服装细节、文字/logo、身体结构、遮挡；显式与隐式对应分开比较 |
| **深度 / 双目 / 多视图几何** | 由几何约束建立跨视图对应 | [C01 Homography](#c01)、[C16 Monodepth2](#c16) 的深度重投影 | [N09 UniMatch](#n09) 统一对应表示 | 深度/视差误差、遮挡、尺度、标定与动态物体影响 |
| **新视角合成 / NVS** | 相机改变后的几何投影与内容补全 | [C28 DIBR](#c28)、[C16 Monodepth2](#c16) 提供重投影基础；[C21 D-NeRF](#c21)、[C22 Nerfies](#c22) 用于动态场景 | [N15 GenWarp](#n15)、[N22 WAVE](#n22)、[N23 SplatDiff](#n23)：几何引导与生成先验融合 | 相机遵循、几何与跨视图一致性、可见区细节、反遮挡质量 |
| **动态三维 / 4D 重建** | 将时间变化映射到 canonical representation | [C21 D-NeRF](#c21)、[C22 Nerfies](#c22)、[C23 HyperNeRF](#c23) | [N11 Deformable 3D Gaussians](#n11)、[N12 4D-GS](#n12)：显式可渲染基元与形变结合 | 渲染质量、运动/拓扑、训练成本、存储、渲染速度 |
| **视频扩散 / 相机与运动控制** | 将运动或几何约束传递给生成模型 | [C19 Softmax Splatting](#c19)、[C20 RAFT](#c20) 是相关基础组件，并非扩散控制方法 | [N16 ∫-noise](#n16)、[N19 Go-with-the-Flow](#n19)、[N24 CameraNoise](#n24)、[N27 Warp-as-History](#n27) | 噪声统计、运动/相机误差、内容质量、长时一致性和补全 |
| **计算成像 / 逆问题 / 优化** | 把 motion warp 纳入测量算子与梯度计算 | [C07 B-spline FFD](#c07)、[C13 STN](#c13) 为相关基础 | [N10 ImWIP](#n10) 离散伴随与导数；[N17 Warped Diffusion](#n17) 视频生成先验 | 伴随测试、梯度检查、测量一致性、收敛与重建误差 |
| **投影艺术 / Anamorphosis / 多视图幻象** | 通过镜面、透镜或视角变换产生不同解释 | [C06 特征 morphing](#c06)、[C25 EWA](#c25) 提供形变/采样背景 | [N21 LookingGlass](#n21)：Laplacian 金字塔 warp 联合同步生成 | 各视图语义、变换精度、频率细节与打印/成像条件 |

<a id="trends"></a>
## 五、技术演进与仍未解决的问题

以下是基于上述原始来源的**整理与归纳**，不是论文共同采用的一套官方分类。

### 5.1 近年的五条主要进展

1. **从局部残差搜索到全局对应，再到高效多帧估计。** [PWC-Net](#c15) 的逐层特征 warp、[RAFT](#c20) 的相关体与循环更新，发展为 [GMFlow](#n01) / [FlowFormer](#n02) 的全局或 attention 表示；[SEA-RAFT](#n13) / [MEMFOF](#n20) 进一步关注效率、高分辨率和多帧。进展主要发生在“如何估计对应”，并未淘汰传统采样。
2. **从二维位移到可渲染的三维、四维形变。** [D-NeRF](#c21) / [Nerfies](#c22) 的 canonical deformation 延伸到 [Deformable 3D Gaussians](#n11) / [4D-GS](#n12)。改变的是表示和渲染效率；真实运动恢复、拓扑与遮挡仍需单独分析。
3. **从先 warp 后补洞到几何与生成联合设计。** [GenWarp](#n15)、[WAVE](#n22)、[SplatDiff](#n23) 让几何引导、attention 和生成先验互相配合。生成内容的视觉真实性不等于可验证的空间对应。
4. **从输运颜色到输运随机场。** [∫-noise](#n16) 将噪声统计纳入算子设计，[Go-with-the-Flow](#n19) 把 warped noise 用作可控视频先验，[CameraNoise](#n24) 进一步结合相机重投影几何。对噪声而言，“看起来平滑”通常不是目标。
5. **从只关心对齐到关心离散算子、频率和表示预算。** [ImWIP](#n10) 关注伴随和导数，[LookingGlass](#n21) 关注多频带 warp，[WarpI2I](#n26) 通过 warp–unwarp 分配 latent 表示资源。这些方向优化的是不同性质，不能只用同一个像素误差指标排序。

### 5.2 为什么普通图像 warp 不能直接等同于 noise warp？

假设源噪声 `ε_i` 相互独立且服从标准高斯，普通线性插值得到：

```text
z(y) = Σ_i w_i(y) ε_i
Var[z(y)] = Σ_i w_i(y)^2
Cov[z(y), z(y')] = Σ_i w_i(y) w_i(y')
```

因此，即使权重之和为 1，方差也不一定为 1；相邻输出共享输入噪声时，还会产生空间相关。仅做逐像素方差归一化通常不能同时消除这些相关性。应分别检查**每帧的分布/空间统计**和**跨帧随运动变化的相关性**。[∫-noise 的原文与推导](https://openreview.net/pdf?id=pzElnMrgSD) 是这一方向的起点。

上述公式针对已知、确定的线性插值权重；当权重本身依赖随机信号或使用非线性算子时，不能直接照搬结论。

### 5.3 仍然需要解决的问题

- **遮挡与反遮挡**：不存在源观测的区域不能靠纯坐标变换恢复；需要多视图信息、历史缓存或生成补全。
- **拓扑、折叠与可逆性**：平滑不等于一一映射；连续模型的性质也可能被离散采样破坏。
- **抗混叠与累积损失**：强缩放需要匹配足迹的滤波；反复 warp/unwarp 会损失高频细节。
- **几何可信度与生成自由度**：生成模型可以隐藏几何错误，必须分别评估可见区域的忠实度和不可见区域的合理性。
- **长期时序一致性**：单步对齐良好不等于长期无漂移；运动估计、补全和历史误差会累积。
- **跨域与算力**：医学/自然图像、静态/动态场景和不同分辨率之间的效果不能直接外推。

<a id="practice"></a>
## 六、实现与选型

### 6.1 常用实现入口

| 需求 | 实现入口 | 使用提醒 |
| --- | --- | --- |
| 仿射、透视、稠密坐标重映射 | [OpenCV Geometric Image Transformations](https://docs.opencv.org/4.x/da/d54/group__imgproc__transform.html) | 明确矩阵方向、`WARP_INVERSE_MAP`、插值和边界模式 |
| 神经网络中的 backward sampling | [PyTorch grid_sample](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.grid_sample.html) / [affine_grid](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.affine_grid.html) | 像素坐标与归一化坐标不同；统一 `align_corners`，检查越界与精度 |
| 经典图像变换 / TPS | [scikit-image transform](https://scikit-image.org/docs/stable/api/skimage.transform.html) / [TPS 示例](https://scikit-image.org/docs/stable/auto_examples/transform/plot_tps_deformation.html) | 区分正向模型与 inverse map；固定库版本与坐标顺序 |
| 可微 forward warp | [Softmax Splatting 作者实现](https://github.com/sniklaus/softmax-splatting) | 聚合权重、遮挡与空洞处理需要单独设计 |
| 网格 ARAP | [libigl 教程](https://libigl.github.io/libigl/tutorial/) | 准备正确拓扑、控制点与约束，检查自交 |
| 逆问题中的 warp / 伴随 / 导数 | [ImWIP](https://imwip.readthedocs.io/en/latest/) | `inverse`、`adjoint` 与 `derivative` 是不同对象 |
| 学习式三维医学配准 | [VoxelMorph](https://github.com/voxelmorph/voxelmorph) / [uniGradICON](https://github.com/uncbiag/uniGradICON) | 明确体素间距、方向、空间单位和形变场约定 |

### 6.2 快速选型

| 已知条件 / 目标 | 可作为起点的路线 | 需要额外处理 |
| --- | --- | --- |
| 平面、扫描件、透视校正或近似纯旋转 | Homography + backward sampling | 错误匹配、插值与边界 |
| 少量可交互控制点，需要平滑二维形变 | TPS / MLS | 控制点离群、外推与折叠 |
| 需要尽量保形的网格编辑 | ARAP | 网格质量、约束与自交 |
| 两帧自然视频，需要稠密运动 | RAFT / GMFlow / SEA-RAFT；高分辨率多帧可考察 MEMFOF | 遮挡、置信度和领域偏移 |
| 已有源深度与目标相机 | 三维重投影 + z-buffer / splatting | 深度边界、多对一、反遮挡补全 |
| 三维解剖图像，需要形变正则与拓扑检查 | SyN / Diffeomorphic Demons / 适配的学习式配准 | 物理坐标、Jacobian 与解剖约束 |
| 视频复原，需要跨帧特征融合 | Flow-guided deformable alignment，如 BasicVSR++ | 错误 flow 传播与时序闪烁 |
| 单图新视角、较大相机变化 | 几何 warp + diffusion，如 GenWarp / SplatDiff | 内容幻觉、跨视图一致性和几何误差 |
| 将运动编码到扩散噪声 | 从 ∫-noise 理解统计要求，再考察 Go-with-the-Flow / CameraNoise | 空间白噪声统计、跨帧相关、补洞及模型适配 |

这些是阅读和原型实现的起点，不构成统一最优推荐；实际选型应在相同数据、硬件和误差约束下比较。

<a id="contributing"></a>
## 贡献方式与核验原则

欢迎补充、纠错和提交 PR。建议新增记录包含：

- 完整论文名、作者、正式发表年份/venue，以及不同于正式发表的首次预印本年份。
- 原论文 / 会议 / 作者项目链接；代码标注官方或第三方，避免把第三方复现写成官方实现。
- **技术族 T1–T9**、应用 Topic、角色标签，以及一句可核实的贡献和主要局限。
- 如声称性能提升，注明数据集、指标、分辨率、硬件、训练数据与比较协议。
- 预印本在有正式发表证据前继续标注预印本；新版本更新状态时保留可追溯来源。

本仓库链接原始资源，不转载论文全文。论文、代码和模型权利及使用条件以各自来源为准。
