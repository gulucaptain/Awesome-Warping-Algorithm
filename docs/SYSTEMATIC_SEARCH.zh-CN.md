# 全 Topic 系统检索记录 · 2026-10-24

[English](SYSTEMATIC_SEARCH.md) · [中文目录](../README.zh-CN.md) · [上一轮扩充记录](EXPANSION_AUDIT.md)

以提交 `c3327b8` 的 128 篇论文为基线，本轮新增 **84 篇**，当前共 **212 篇**。原有论文记录、ID、链接与描述，以及原先的检索记录均保留。6 个研究板块和 16 个 Topic 的名称及范围保持不变。

## 检索与判断方式

- 先按“应用任务 × 空间机制 × 被变换对象”开展发现检索，再核验论文标题和元数据。目录分类用于最终归属，不作为检索边界。检索包含无年份限制的经典工作与 2025–2026 近期工作。
- 对 16 个 Topic 分别执行开放任务/机制检索、近期方向检索及相关工作追踪；从原文中的方法和参考文献继续扩展，再回到会议、出版社与作者原文核验。引用追踪不声称覆盖了全部前向引用。
- 记录了 117 条 Web 查询、1355 个不同结果 URL，并对 86 个候选进行全文核查；URL 包含镜像、文档和非论文，不能作为“发现论文数”或“逐篇筛查数”。其他搜索结果仍是发现线索。
- 最终新增 84 篇。每条明确说明主 Topic、实际机制、被变换对象、贡献与局限；区分显式形变、对应估计、采样算子、流条件引导和空间记忆，不能把后几者统一称为 Warping 算子。
- 质量判断结合原文贡献、正式发表或预印本状态、方法影响力和引用证据。OpenAlex 在本轮返回 HTTP 429，串行重试后仍限流即停止；仅取得 19 篇新增论文的可靠匹配记录。其他引用数保持缺失，不写成零、不据此淘汰，不声称完成了同领域引用排名。
- 这是有记录的系统检索批次，不是完整文献普查。仍待核查的扩展稿和未筛查线索明确保留，不以 Topic 非空或固定篇数宣称检索饱和。

## 可追溯记录

| 记录 | 内容 |
| --- | --- |
| [检索词与结果 URL](../data/research/2026-10-24-systematic/searches.json) | 发现检索、机制追踪、版本核查分阶段记录；仅保留结果标题与链接 |
| [候选核查计划](../data/research/2026-10-24-systematic/verification-plan.json) | 进入核查时的标题、出处和来源提议；这些是待核实输入，以筛选结果为准 |
| [收录、排除与版本判断](../data/research/2026-10-24-systematic/screening.json) | 99 项判断、双语理由、原文来源与文件哈希、失败访问和资源核验 |
| [元数据与引用查询](../data/research/2026-10-24-systematic/metadata-lookups.json) | OpenAlex 与 HF 查询、匹配状态及候选记录 |
| [原文标题关联](../data/research/2026-10-24-systematic/reference-mentions.json) | 自动检测的完整标题提及，用于参考文献/相关工作追踪，不冒充人工确认的引用边 |

## 版本和相关性处理

- FGDVI 撤回旧稿不入正文，以作者指向的 FloED 为代表；FloED 内部改名只计一次。
- FIA-VTON 的预印本题名与 ICCV 2025 题名合并；EquiVDM 的两种标题合并到同一 arXiv 记录，并保守标为预印本。
- 服装动画 FloAt 与音频人像 FLOAT 是不同论文；ECCV 2024 的视频编辑 WAVE 与已有 ICCV 2025 的新视角合成 WAVE 也不同。不能只按简称去重。
- PDC-Net+ 记录对 PDC-Net 的扩展关系；本轮只新增期刊代表条目。StabStitch++ 与已有记录的独立贡献重叠仍待逐项比较，暂不追加计数。
- Fast Forward 的初稿题名、MIDL 2025 会议年和 PMLR 2026 出版年均保留，按正式论文集年份排序。
- GeoWorld 的双曲潜在几何、概率 flow matching 与行人轨迹预测，不因名称中出现 geometry/flow 就当作空间 Warping 方法。
- FlowVid 作者仓库明确没有公开代码与权重，保留项目和论文链接，隐藏 GitHub Code 徽章。其他代码链接须有论文或作者项目的关联证据。

## Topic 覆盖

| Topic | 原有 | 新增 | 当前 |
| --- | ---: | ---: | ---: |
| 1.1 几何变换与形变编辑 | 10 | 5 | 15 |
| 1.2 可微采样与 Splatting | 6 | 8 | 14 |
| 2.1 光流与稠密对应 | 20 | 5 | 25 |
| 2.2 图像配准、拼接与视频稳像 | 9 | 4 | 13 |
| 2.3 医学图像配准与可逆形变 | 12 | 5 | 17 |
| 3.1 视频插帧与复原 | 11 | 7 | 18 |
| 3.2 人物动画、运动迁移与虚拟试衣 | 8 | 8 | 16 |
| 4.1 噪声 Warping 与时序一致性 | 4 | 7 | 11 |
| 4.2 相机、轨迹与运动可控生成 | 7 | 6 | 13 |
| 5.1 空间感知、深度与三维重建 | 7 | 5 | 12 |
| 5.2 重投影与新视角合成 | 9 | 5 | 14 |
| 5.3 动态三维与 4D 场景 | 9 | 4 | 13 |
| 5.4 空间推理与场景记忆 | 4 | 6 | 10 |
| 6.1 世界模型与环境预测 | 5 | 2 | 7 |
| 6.2 交互式环境与模拟 | 3 | 3 | 6 |
| 6.3 具身智能体、规划与控制 | 4 | 4 | 8 |

## 新增论文与归属依据

### 1.1 几何变换与形变编辑

| 论文 | 出处 | 机制 / 归属依据 |
| --- | --- | --- |
| [Inpaint4Drag: Repurposing Inpainting Models for Drag-Based Image Editing via Bidirectional Warping](../README.zh-CN.md#s003) · [原文](https://openaccess.thecvf.com/content/ICCV2025/html/Lu_Inpaint4Drag_Repurposing_Inpainting_Models_for_Drag-Based_Image_Editing_via_Bidirectional_ICCV_2025_paper.html) | ICCV 2025 | **显式空间形变** · 将拖拽编辑分解为像素空间双向 Warping 与图像修复，先建立几何对应，再补全显露区域。 |
| [FlowDrag: 3D-aware Drag-based Image Editing with Mesh-guided Deformation Vector Flow Fields](../README.zh-CN.md#s004) · [原文](https://proceedings.mlr.press/v267/koo25a.html) | ICML 2025 | **显式空间形变** · 由单图构建三维网格，用控制点驱动网格变形，再将位移投影为二维流场引导扩散编辑。 |
| [DragDiffusion: Harnessing Diffusion Models for Interactive Point-based Image Editing](../README.zh-CN.md#s005) · [原文](https://openaccess.thecvf.com/content/CVPR2024/html/Shi_DragDiffusion_Harnessing_Diffusion_Models_for_Interactive_Point-based_Image_Editing_CVPR_2024_paper.html) | CVPR 2024 | **空间编辑** · 通过 UNet 特征上的运动监督优化扩散潜变量，实现交互式点拖拽和形状编辑。 |
| [Green Coordinates](../README.zh-CN.md#s002) · [原文](https://www.wisdom.weizmann.ac.il/~ylipman/GC/gc_techrep.pdf) | SIGGRAPH / TOG 2008 | **显式空间形变** · 以笼体顶点与面法向共同定义 Green 坐标，构造二维保角及三维近似保角的形变映射。 |
| [Harmonic Coordinates for Character Articulation](../README.zh-CN.md#s001) · [原文](https://www.cs.jhu.edu/~misha/ReadingSeminar/Papers/Joshi07.pdf) | SIGGRAPH / TOG 2007 | **显式空间形变** · 通过求解笼体内部的调和权重控制体积形变，在凹形区域保持非负权重与内部局部性。 |

### 1.2 可微采样与 Splatting

| 论文 | 出处 | 机制 / 归属依据 |
| --- | --- | --- |
| [gsplat: An Open-Source Library for Gaussian Splatting](../README.zh-CN.md#s010) · [原文](https://jmlr.org/papers/v26/24-1476.html) | JMLR 2025 | **采样 / Splatting 算子** · 以可微高斯投影与光栅化核心实现高效训练和渲染，并提供公开的高斯 Splatting 软件论文。 |
| [Mip-Splatting: Alias-free 3D Gaussian Splatting](../README.zh-CN.md#s008) · [原文](https://openaccess.thecvf.com/content/CVPR2024/html/Yu_Mip-Splatting_Alias-free_3D_Gaussian_Splatting_CVPR_2024_paper.html) | CVPR 2024 | **采样 / Splatting 算子** · 结合三维平滑滤波和二维 Mip 滤波，减轻高斯 Splatting 在缩放与采样率变化下的混叠。 |
| [Towards Progressive Multi-Frequency Representation for Image Warping](../README.zh-CN.md#s079) · [原文](https://openaccess.thecvf.com/content/CVPR2024/html/Xiao_Towards_Progressive_Multi-Frequency_Representation_for_Image_Warping_CVPR_2024_paper.html) | CVPR 2024 | **采样 / Splatting 算子** · 通过渐进频带表示和可学习 Gabor 滤波器捕获局部空间频率，提高非规则网格变换中的图像细节。 |
| [Kernel Aware Resampler](../README.zh-CN.md#s006) · [原文](https://openaccess.thecvf.com/content/CVPR2023/html/Bernasconi_Kernel_Aware_Resampler_CVPR_2023_paper.html) | CVPR 2023 | **采样 / Splatting 算子** · 联合建模重建核、局部几何畸变和抗混叠核，以空间变化的退化信息控制通用图像重采样。 |
| [Learning Local Implicit Fourier Representation for Image Warping](../README.zh-CN.md#s085) · [原文](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136780179.pdf) | ECCV 2022 | **采样 / Splatting 算子** · 利用局部纹理估计和坐标变换的 Jacobian 调整傅里叶响应，在连续表示中重采样非规则图像形状。 |
| [SRWarp: Generalized Image Super-Resolution under Arbitrary Transformation](../README.zh-CN.md#s086) · [原文](https://openaccess.thecvf.com/content/CVPR2021/html/Son_SRWarp_Generalized_Image_Super-Resolution_under_Arbitrary_Transformation_CVPR_2021_paper.html) | CVPR 2021 | **采样 / Splatting 算子** · 将图像超分推广到任意空间变换，通过多尺度特征和自适应 Warping 支持非规则输出形状。 |
| [Modular Primitives for High-Performance Differentiable Rendering](../README.zh-CN.md#s009) · [原文](https://research.nvidia.com/publication/2020-11_modular-primitives-high-performance-differentiable-rendering) | SIGGRAPH Asia / TOG 2020 | **采样 / Splatting 算子** · 将光栅化、属性插值、纹理采样和抗混叠拆为可微模块，支持硬件加速的逆渲染。 |
| [Linearized Multi-Sampling for Differentiable Image Transformation](../README.zh-CN.md#s007) · [原文](https://research.google/pubs/linearized-multi-sampling-for-differentiable-image-transformation/) | ICCV 2019 | **采样 / Splatting 算子** · 在采样点邻域生成辅助样本并建立局部线性近似，改善可微图像变换的梯度传播。 |

### 2.1 光流与稠密对应

| 论文 | 出处 | 机制 / 归属依据 |
| --- | --- | --- |
| [UFM: A Simple Path towards Unified Dense Correspondence with Flow](../README.zh-CN.md#s015) · [原文](https://proceedings.neurips.cc/paper_files/paper/2025/hash/9d89448b63ce1e2e8dc7af72c984c196-Abstract-Conference.html) | NeurIPS 2025 | **对应关系估计** · 以统一的可共视训练数据和 Transformer 直接回归二维位移，将光流与宽基线稠密匹配合并建模。 |
| [PDC-Net+: Enhanced Probabilistic Dense Correspondence Network](../README.zh-CN.md#s012) · [原文](https://arxiv.org/abs/2109.13912) | TPAMI 2023 | **对应关系估计** · 联合预测稠密对应与概率置信度，为大位移、遮挡和跨视角匹配提供不确定性信息。 |
| [CroCo v2: Improved Cross-view Completion Pre-training for Stereo Matching and Optical Flow](../README.zh-CN.md#s014) · [原文](https://openaccess.thecvf.com/content/ICCV2023/html/Weinzaepfel_CroCo_v2_Improved_Cross-view_Completion_Pre-training_for_Stereo_Matching_and_ICCV_2023_paper.html) | ICCV 2023 | **对应关系估计** · 通过跨视图补全预训练与相对位置编码学习光流和双目匹配，不依赖显式图像 Warping 组件。 |
| [COTR: Correspondence Transformer for Matching Across Images](../README.zh-CN.md#s011) · [原文](https://openaccess.thecvf.com/content/ICCV2021/html/Jiang_COTR_Correspondence_Transformer_for_Matching_Across_Images_ICCV_2021_paper.html) | ICCV 2021 | **对应关系估计** · 用跨图像 Transformer 为连续坐标查询预测对应点，并通过局部细化实现精确匹配。 |
| [GLU-Net: Global-Local Universal Network for Dense Flow and Correspondences](../README.zh-CN.md#s013) · [原文](https://openaccess.thecvf.com/content_CVPR_2020/html/Truong_GLU-Net_Global-Local_Universal_Network_for_Dense_Flow_and_Correspondences_CVPR_2020_paper.html) | CVPR 2020 | **对应关系估计** · 结合全局与局部相关层以及自适应分辨率，统一几何匹配、光流与语义对应估计。 |

### 2.2 图像配准、拼接与视频稳像

| 论文 | 出处 | 机制 / 归属依据 |
| --- | --- | --- |
| [PixelStitch: Structure-Preserving Pixel-Wise Bidirectional Warps for Unsupervised Image Stitching](../README.zh-CN.md#s018) · [原文](https://openaccess.thecvf.com/content/ICCV2025/html/Jin_PixelStitch_Structure-Preserving_Pixel-Wise_Bidirectional_Warps_for_Unsupervised_Image_Stitching_ICCV_2025_paper.html) | ICCV 2025 | **显式空间形变** · 通过单应性分解建立中间投影平面，再学习双向逐像素残差形变以兼顾对齐与结构保持。 |
| [DUT: Learning Video Stabilization by Simply Watching Unstable Videos](../README.zh-CN.md#s019) · [原文](https://arxiv.org/abs/2011.14574) | IEEE TIP 2022 | **显式空间形变** · 从不稳定视频中无监督学习网格轨迹估计与动态平滑，再用平滑后的网格路径完成视频稳像。 |
| [Shape-Preserving Half-Projective Warps for Image Stitching](../README.zh-CN.md#s016) · [原文](https://openaccess.thecvf.com/content_cvpr_2014/html/Chang_Shape-Preserving_Half-Projective_Warps_2014_CVPR_paper.html) | CVPR 2014 | **显式空间形变** · 在重叠区域保留投影对齐，向非重叠区域平滑过渡到相似变换，以降低全景拼接畸变。 |
| [Parallax-tolerant Image Stitching](../README.zh-CN.md#s017) · [原文](https://openaccess.thecvf.com/content_cvpr_2014/html/Zhang_Parallax-tolerant_Image_Stitching_2014_CVPR_paper.html) | CVPR 2014 | **显式空间形变** · 结合单应性、保内容局部形变与接缝选择，在存在较大视差的图像间寻找可自然融合的区域。 |

### 2.3 医学图像配准与可逆形变

| 论文 | 出处 | 机制 / 归属依据 |
| --- | --- | --- |
| [Learning Diffeomorphism for Medical Image Registration with Time-Embedded Architectures Using Semigroup Regularization](../README.zh-CN.md#s023) · [原文](https://openaccess.thecvf.com/content/CVPR2026/html/Matinkia_Learning_Diffeomorphism_for_Medical_Image_Registration_with_Time-Embedded_Architectures_Using_CVPR_2026_paper.html) | CVPR 2026 | **显式空间形变** · 以时间嵌入网络表示连续形变，并通过半群正则学习具有逆一致性与周期一致性的配准映射。 |
| [Fast forward: Rephrasing 3D deformable image registration through density alignment and splatting](../README.zh-CN.md#s084) · [原文](https://proceedings.mlr.press/v301/heinrich26a.html) | MIDL 2025 / PMLR 2026 | **采样 / Splatting 算子** · 将医学形变配准重述为点云前向 Splatting 得到的密度体对齐，用可微光栅化替代仅依赖反向插值的流程。 |
| [GradICON: Approximate Diffeomorphisms via Gradient Inverse Consistency](../README.zh-CN.md#s020) · [原文](https://openaccess.thecvf.com/content/CVPR2023/html/Tian_GradICON_Approximate_Diffeomorphisms_via_Gradient_Inverse_Consistency_CVPR_2023_paper.html) | CVPR 2023 | **显式空间形变** · 对双向变换复合的 Jacobian 与单位矩阵的偏差施加正则，学习更规则的医学配准映射。 |
| [Fourier-Net: Fast Image Registration with Band-limited Deformation](../README.zh-CN.md#s022) · [原文](https://ojs.aaai.org/index.php/AAAI/article/view/25182) | AAAI 2023 | **显式空间形变** · 预测带限傅里叶域中的低维形变表示，再通过零填充和逆变换还原高分辨率位移场。 |
| [Large Deformation Diffeomorphic Image Registration with Laplacian Pyramid Networks](../README.zh-CN.md#s021) · [原文](https://arxiv.org/abs/2006.16148) | MICCAI 2020 | **显式空间形变** · 在拉普拉斯金字塔中由粗到细估计形变，并在微分同胚映射空间逐级完成医学图像配准。 |

### 3.1 视频插帧与复原

| 论文 | 出处 | 机制 / 归属依据 |
| --- | --- | --- |
| [HomoGen: Enhanced Video Inpainting via Homography Propagation and Diffusion](../README.zh-CN.md#s028) · [原文](https://openaccess.thecvf.com/content/CVPR2025/html/Ding_HomoGen_Enhanced_Video_Inpainting_via_Homography_Propagation_and_Diffusion_CVPR_2025_paper.html) | CVPR 2025 | **显式空间形变** · 通过单应性配准传播上下文像素，将所得结构先验以自适应强度注入视频扩散修复过程。 |
| [BiM-VFI: Bidirectional Motion Field-Guided Frame Interpolation for Video with Non-uniform Motions](../README.zh-CN.md#s029) · [原文](https://openaccess.thecvf.com/content/CVPR2025/html/Seo_BiM-VFI_Bidirectional_Motion_Field-Guided_Frame_Interpolation_for_Video_with_Non-uniform_CVPR_2025_paper.html) | CVPR 2025 | **对应关系估计** · 用双向运动场描述非匀速运动，结合流估计、内容自适应上采样和蒸馏来生成中间帧。 |
| [Coherent Video Inpainting Using Optical Flow-Guided Efficient Diffusion](../README.zh-CN.md#s027) · [原文](https://arxiv.org/abs/2412.00857) | arXiv 2024 | **特征 / 潜变量 / 注意力对齐** · 以光流补全分支和多尺度流适配器引导视频修复，并用流 Warping 的潜变量插值加速去噪。 |
| [Upscale-A-Video: Temporal-Consistent Diffusion Model for Real-World Video Super-Resolution](../README.zh-CN.md#s030) · [原文](https://openaccess.thecvf.com/content/CVPR2024/html/Zhou_Upscale-A-Video_Temporal-Consistent_Diffusion_Model_for_Real-World_Video_Super-Resolution_CVPR_2024_paper.html) | CVPR 2024 | **特征 / 潜变量 / 注意力对齐** · 结合局部时序层与全局光流引导的循环潜变量传播，在扩散视频超分中保持跨帧一致性。 |
| [ProPainter: Improving Propagation and Transformer for Video Inpainting](../README.zh-CN.md#s024) · [原文](https://openaccess.thecvf.com/content/ICCV2023/html/Zhou_ProPainter_Improving_Propagation_and_Transformer_for_Video_Inpainting_ICCV_2023_paper.html) | ICCV 2023 | **特征 / 潜变量 / 注意力对齐** · 结合循环光流补全、图像与特征双域 Warping，以及稀疏视频 Transformer，实现视频内容修复。 |
| [Towards An End-to-End Framework for Flow-Guided Video Inpainting](../README.zh-CN.md#s025) · [原文](https://arxiv.org/abs/2204.02663) | CVPR 2022 | **特征 / 潜变量 / 注意力对齐** · 联合训练光流补全、对齐特征传播和内容补全模块，构成端到端的流引导视频修复框架。 |
| [Deep Flow-Guided Video Inpainting](../README.zh-CN.md#s026) · [原文](https://arxiv.org/abs/1905.02884) | CVPR 2019 | **特征 / 潜变量 / 注意力对齐** · 先补全时空连续的光流，再沿完整流场传播可见像素，修复视频中被遮罩的内容。 |

### 3.2 人物动画、运动迁移与虚拟试衣

| 论文 | 出处 | 机制 / 归属依据 |
| --- | --- | --- |
| [Learning Implicit Features with Flow-Infused Transformations for Realistic Virtual Try-On](../README.zh-CN.md#s032) · [原文](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_Learning_Implicit_Features_with_Flow-Infused_Transformations_for_Realistic_Virtual_Try-On_ICCV_2025_paper.html) | ICCV 2025 | **流场 / 轨迹条件引导** · 将稠密 warp flow 与服装特征注入 Flow Infused Attention，以隐式空间引导替代对变形服装图像的完全依赖。 |
| [FloAt: Flow Warping of Self-Attention for Clothing Animation Generation](../README.zh-CN.md#s033) · [原文](https://arxiv.org/abs/2411.15028) | arXiv 2024 | **特征 / 潜变量 / 注意力对齐** · 从连续法线图估计光流，Warp 前一帧的自注意力特征并与当前帧融合，以生成一致的服装动画。 |
| [D4-VTON: Dynamic Semantics Disentangling for Differential Diffusion based Virtual Try-On](../README.zh-CN.md#s036) · [原文](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6231_ECCV_2024_paper.php) | ECCV 2024 | **显式空间形变** · 自发现服装语义层并预测分层局部流，再以差分信息跟踪改善扩散试衣中的服装细节。 |
| [Taming the Power of Diffusion Models for High-Quality Virtual Try-On with Appearance Flow](../README.zh-CN.md#s031) · [原文](https://arxiv.org/abs/2308.06101) | ACM MM 2023 | **显式空间形变** · 用外观流显式变形服装图像，将对齐后的服装作为输入和局部条件引导扩散试衣。 |
| [GP-VTON: Towards General Purpose Virtual Try-on via Collaborative Local-Flow Global-Parsing Learning](../README.zh-CN.md#s035) · [原文](https://arxiv.org/abs/2303.13756) | CVPR 2023 | **显式空间形变** · 以局部流与全局解析协同学习服装部件对齐，并通过动态梯度截断减轻边界处纹理挤压。 |
| [High-Resolution Virtual Try-On with Misalignment and Occlusion-Handled Conditions](../README.zh-CN.md#s034) · [原文](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/6403_ECCV_2022_paper.php) | ECCV 2022 | **显式空间形变** · 在同一条件生成器中交互学习服装变形与人体分割，缓解错位和遮挡处的纹理挤压。 |
| [ClothFormer: Taming Video Virtual Try-On in All Module](../README.zh-CN.md#s078) · [原文](https://openaccess.thecvf.com/content/CVPR2022/html/Jiang_ClothFormer_Taming_Video_Virtual_Try-On_in_All_Module_CVPR_2022_paper.html) | CVPR 2022 | **显式空间形变** · 通过抗遮挡外观流 Warping、流序列平滑与双流 Transformer，生成时空一致的视频试衣结果。 |
| [One-Shot Free-View Neural Talking-Head Synthesis for Video Conferencing](../README.zh-CN.md#s037) · [原文](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_One-Shot_Free-View_Neural_Talking-Head_Synthesis_for_Video_Conferencing_CVPR_2021_paper.html) | CVPR 2021 | **显式空间形变** · 分解身份与运动关键点，用三维运动表示构造稠密形变并搬运源图像特征，生成可控人像视频。 |

### 4.1 噪声 Warping 与时序一致性

| 论文 | 出处 | 机制 / 归属依据 |
| --- | --- | --- |
| [Infinite-Resolution Integral Noise Warping for Diffusion Models](../README.zh-CN.md#s043) · [原文](https://proceedings.iclr.cc/paper_files/paper/2025/hash/7feb98f84ee34f697944333d4faec0bd-Abstract-Conference.html) | ICLR 2025 | **噪声输运** · 分析积分噪声 Warping 的无限分辨率极限，以 Brownian bridge 增量构造高效、分布保持的噪声输运。 |
| [On Equivariance and Fast Sampling in Video Diffusion Models Trained with Warped Noise](../README.zh-CN.md#s044) · [原文](https://arxiv.org/abs/2504.09789) | arXiv 2025 | **噪声输运** · 分析相关 Warping 噪声训练如何促进空间等变性，并将该性质用于高效视频生成与采样蒸馏。 |
| [FlowVid: Taming Imperfect Optical Flows for Consistent Video-to-Video Synthesis](../README.zh-CN.md#s038) · [原文](https://openaccess.thecvf.com/content/CVPR2024/html/Liang_FlowVid_Taming_Imperfect_Optical_Flows_for_Consistent_Video-to-Video_Synthesis_CVPR_2024_paper.html) | CVPR 2024 | **显式空间形变** · 用光流将编辑首帧 Warp 到后续帧，联合深度等空间条件引导扩散模型传播视频编辑。 |
| [FLATTEN: optical FLow-guided ATTENtion for consistent text-to-video editing](../README.zh-CN.md#s039) · [原文](https://openreview.net/forum?id=JgqftqZQZ7) | ICLR 2024 | **流场 / 轨迹条件引导** · 让视频中同一光流轨迹上的图像块在注意力模块中相互关联，改善文本引导编辑的跨帧一致性。 |
| [WAVE: Warping DDIM Inversion Features for Zero-shot Text-to-Video Editing](../README.zh-CN.md#s042) · [原文](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9682_ECCV_2024_paper.php) | ECCV 2024 | **特征 / 潜变量 / 注意力对齐** · 在 DDIM 反演过程中利用光流传播关键帧特征，以获得更一致的反演潜变量并支持视频编辑。 |
| [LatentWarp: Consistent Diffusion Latents for Zero-Shot Video-to-Video Translation](../README.zh-CN.md#s040) · [原文](https://arxiv.org/abs/2311.00353) | arXiv 2023 | **特征 / 潜变量 / 注意力对齐** · 用光流在扩散潜空间中执行 Warping，约束跨帧 query token，以改善零样本视频翻译。 |
| [Rerender A Video: Zero-Shot Text-Guided Video-to-Video Translation](../README.zh-CN.md#s041) · [原文](https://arxiv.org/abs/2306.07954) | SIGGRAPH Asia / TOG 2023 | **特征 / 潜变量 / 注意力对齐** · 对关键帧施加跨帧形状和纹理约束，再通过时序感知的匹配与混合传播完整视频编辑。 |

### 4.2 相机、轨迹与运动可控生成

| 论文 | 出处 | 机制 / 归属依据 |
| --- | --- | --- |
| [FloVD: Optical Flow Meets Video Diffusion Model for Enhanced Camera-Controlled Video Synthesis](../README.zh-CN.md#s047) · [原文](https://arxiv.org/abs/2502.08244) | CVPR 2025 | **流场 / 轨迹条件引导** · 将相机与物体运动表示为光流，先生成流场，再以流条件视频扩散实现相机控制与动态合成。 |
| [TrajectoryCrafter: Redirecting Camera Trajectory for Monocular Videos via Diffusion Models](../README.zh-CN.md#s048) · [原文](https://www.openaccess.thecvf.com/content/ICCV2025/html/Yu_TrajectoryCrafter_Redirecting_Camera_Trajectory_for_Monocular_Videos_via_Diffusion_Models_ICCV_2025_paper.html) | ICCV 2025 | **重投影与渲染** · 将源视频与按目标轨迹渲染的点云共同作为扩散条件，并以双重重投影构建训练数据。 |
| [Latent-Reframe: Enabling Camera Control for Video Diffusion Models without Training](../README.zh-CN.md#s049) · [原文](https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_Latent-Reframe_Enabling_Camera_Control_for_Video_Diffusion_Models_without_Training_ICCV_2025_paper.html) | ICCV 2025 | **重投影与渲染** · 通过时间感知点云将视频潜变量重构到目标相机轨迹，再用潜空间修复与协调完成视频生成。 |
| [MotionPro: A Precise Motion Controller for Image-to-Video Generation](../README.zh-CN.md#s050) · [原文](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_MotionPro_A_Precise_Motion_Controller_for_Image-to-Video_Generation_CVPR_2025_paper.html) | CVPR 2025 | **流场 / 轨迹条件引导** · 以局部区域轨迹和运动掩码区分物体与相机运动，为视频生成提供精细的运动条件。 |
| [Motion-I2V: Consistent and Controllable Image-to-Video Generation with Explicit Motion Modeling](../README.zh-CN.md#s045) · [原文](https://arxiv.org/abs/2401.15977) | SIGGRAPH 2024 | **流场 / 轨迹条件引导** · 先预测参考图像像素的运动轨迹，再通过运动增强时序注意力传播特征，并支持稀疏轨迹控制。 |
| [MotionCraft: Physics-Based Zero-Shot Video Generation](../README.zh-CN.md#s046) · [原文](https://proceedings.neurips.cc/paper_files/paper/2024/hash/ded49449e9239a47057c33ef8d42c26e-Abstract-Conference.html) | NeurIPS 2024 | **噪声输运** · 将物理模拟得到的光流作用于扩散噪声潜空间，以零样本方式控制视频中的物理运动。 |

### 5.1 空间感知、深度与三维重建

| 论文 | 出处 | 机制 / 归属依据 |
| --- | --- | --- |
| [VGGT: Visual Geometry Grounded Transformer](../README.zh-CN.md#s054) · [原文](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.html) | CVPR 2025 | **几何估计** · 从单幅或多幅图像联合预测相机、深度、三维点与点轨迹，为几何重建和后续重投影提供基础。 |
| [FoundationStereo: Zero-Shot Stereo Matching](../README.zh-CN.md#s055) · [原文](https://openaccess.thecvf.com/content/CVPR2025/html/Wen_FoundationStereo_Zero-Shot_Stereo_Matching_CVPR_2025_paper.html) | CVPR 2025 | **对应关系估计** · 利用大规模合成双目数据、单目先验与长程代价体推理，学习跨域泛化的双目深度匹配。 |
| [RAFT-Stereo: Multilevel Recurrent Field Transforms for Stereo Matching](../README.zh-CN.md#s053) · [原文](https://arxiv.org/abs/2109.07547) | 3DV 2021 | **对应关系估计** · 在校正后的双目图像上构建相关金字塔，用多层循环更新预测稠密视差。 |
| [Cascade Cost Volume for High-Resolution Multi-View Stereo and Stereo Matching](../README.zh-CN.md#s051) · [原文](https://openaccess.thecvf.com/content_CVPR_2020/html/Gu_Cascade_Cost_Volume_for_High-Resolution_Multi-View_Stereo_and_Stereo_Matching_CVPR_2020_paper.html) | CVPR 2020 | **几何估计** · 利用前一级深度缩小后续假设范围，通过金字塔级联代价体进行高分辨率多视图与双目匹配。 |
| [DPSNet: End-to-end Deep Plane Sweep Stereo](../README.zh-CN.md#s052) · [原文](https://arxiv.org/abs/1905.00538) | ICLR 2019 | **重投影与渲染** · 通过可微平面扫描 Warping 构建跨视图特征代价体，再聚合并回归场景深度。 |

### 5.2 重投影与新视角合成

| 论文 | 出处 | 机制 / 归属依据 |
| --- | --- | --- |
| [DepthSplat: Connecting Gaussian Splatting and Depth](../README.zh-CN.md#s059) · [原文](https://openaccess.thecvf.com/content/CVPR2025/html/Xu_DepthSplat_Connecting_Gaussian_Splatting_and_Depth_CVPR_2025_paper.html) | CVPR 2025 | **重投影与渲染** · 结合预训练单目特征与多视图深度估计来构建高斯场景，并用渲染监督促进深度学习。 |
| [MVSplat: Efficient 3D Gaussian Splatting from Sparse Multi-View Images](../README.zh-CN.md#s058) · [原文](https://arxiv.org/abs/2403.14627) | ECCV 2024 | **重投影与渲染** · 以平面扫描代价体估计几何并预测三维高斯，从稀疏多视图实现前馈式新视角渲染。 |
| [MultiDiff: Consistent Novel View Synthesis from a Single Image](../README.zh-CN.md#s060) · [原文](https://openaccess.thecvf.com/content/CVPR2024/html/Muller_MultiDiff_Consistent_Novel_View_Synthesis_from_a_Single_Image_CVPR_2024_paper.html) | CVPR 2024 | **重投影与渲染** · 用单目深度将参考图像 Warp 到目标视角，再以视频扩散先验联合生成一致的多视图序列。 |
| [SynSin: End-to-End View Synthesis From a Single Image](../README.zh-CN.md#s056) · [原文](https://openaccess.thecvf.com/content_CVPR_2020/html/Wiles_SynSin_End-to-End_View_Synthesis_From_a_Single_Image_CVPR_2020_paper.html) | CVPR 2020 | **重投影与渲染** · 将源图像特征提升为三维点云并可微投影到目标视角，再通过细化网络补全缺失区域。 |
| [3D Photography Using Context-Aware Layered Depth Inpainting](../README.zh-CN.md#s083) · [原文](https://openaccess.thecvf.com/content_CVPR_2020/html/Shih_3D_Photography_Using_Context-Aware_Layered_Depth_Inpainting_CVPR_2020_paper.html) | CVPR 2020 | **重投影与渲染** · 将单幅 RGB-D 图像转为带显式像素连接的分层深度表示，并补全遮挡区域的颜色与深度来渲染运动视差。 |

### 5.3 动态三维与 4D 场景

| 论文 | 出处 | 机制 / 归属依据 |
| --- | --- | --- |
| [MoSca: Dynamic Gaussian Fusion from Casual Videos via 4D Motion Scaffolds](../README.zh-CN.md#s063) · [原文](https://openaccess.thecvf.com/content/CVPR2025/html/Lei_MoSca_Dynamic_Gaussian_Fusion_from_Casual_Videos_via_4D_Motion_CVPR_2025_paper.html) | CVPR 2025 | **显式空间形变** · 将视频先验提升为四维运动支架，并融合附着其上的高斯，以分离场景外观和动态形变。 |
| [SC-GS: Sparse-Controlled Gaussian Splatting for Editable Dynamic Scenes](../README.zh-CN.md#s061) · [原文](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_SC-GS_Sparse-Controlled_Gaussian_Splatting_for_Editable_Dynamic_Scenes_CVPR_2024_paper.html) | CVPR 2024 | **显式空间形变** · 以稀疏控制点的时变六自由度变换，经局部插值驱动稠密三维高斯，实现动态重建与编辑。 |
| [SceNeRFlow: Time-Consistent Reconstruction of General Dynamic Scenes](../README.zh-CN.md#s062) · [原文](https://arxiv.org/abs/2308.08258) | 3DV 2024 | **显式空间形变** · 通过反向形变将动态观测映射到固定规范场景，恢复长期、较大运动下的跨时刻对应。 |
| [Non-Rigid Neural Radiance Fields: Reconstruction and Novel View Synthesis of a Dynamic Scene From Monocular Video](../README.zh-CN.md#s064) · [原文](https://openaccess.thecvf.com/content/ICCV2021/html/Tretschk_Non-Rigid_Neural_Radiance_Fields_Reconstruction_and_Novel_View_Synthesis_of_ICCV_2021_paper.html) | ICCV 2021 | **显式空间形变** · 通过射线弯曲和刚性约束分离规范辐射场与场景形变，从单目动态视频建立时空表示。 |

### 5.4 空间推理与场景记忆

| 论文 | 出处 | 机制 / 归属依据 |
| --- | --- | --- |
| [3D-Mem: 3D Scene Memory for Embodied Exploration and Reasoning](../README.zh-CN.md#s066) · [原文](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_3D-Mem_3D_Scene_Memory_for_Embodied_Exploration_and_Reasoning_CVPR_2025_paper.html) | CVPR 2025 | **空间记忆** · 结合三维场景表示、信息丰富的多视图记忆快照与前沿快照，支持具身探索和问答。 |
| [GraphEQA: Using 3D Semantic Scene Graphs for Real-time Embodied Question Answering](../README.zh-CN.md#s067) · [原文](https://proceedings.mlr.press/v305/saxena25a.html) | CoRL 2025 / PMLR 2025 | **空间记忆** · 将在线三维度量语义场景图与相关图像组成多模态记忆，用于结构化探索和具身问答。 |
| [Trans4Map: Revisiting Holistic Bird's-Eye-View Mapping From Egocentric Images to Allocentric Semantics With Vision Transformers](../README.zh-CN.md#s082) · [原文](https://openaccess.thecvf.com/content/WACV2023/html/Chen_Trans4Map_Revisiting_Holistic_Birds-Eye-View_Mapping_From_Egocentric_Images_to_Allocentric_WACV_2023_paper.html) | WACV 2023 | **空间记忆** · 用 Transformer 提取自我视角特征，将其投影并累积到双向世界坐标记忆，预测俯视语义地图。 |
| [EgoMap: Projective mapping and structured egocentric memory for Deep RL](../README.zh-CN.md#s080) · [原文](https://arxiv.org/abs/2002.02286) | ECML PKDD 2020 | **空间记忆** · 将图像特征可微反投影到俯视记忆地图，并依据自运动通过仿射变换更新记忆坐标。 |
| [Neural Map: Structured Memory for Deep Reinforcement Learning](../README.zh-CN.md#s065) · [原文](https://arxiv.org/abs/1702.08360) | ICLR 2018 | **空间记忆** · 以空间结构化的二维神经记忆存储环境信息，通过位置相关的读写支持长期导航推理。 |
| [MapNet: An Allocentric Spatial Memory for Mapping Environments](../README.zh-CN.md#s081) · [原文](https://openaccess.thecvf.com/content_cvpr_2018/html/Henriques_MapNet_An_Allocentric_CVPR_2018_paper.html) | CVPR 2018 | **空间记忆** · 将 RGB-D 感知注册到可学习的世界坐标记忆中，以卷积与反卷积形式实现定位和地图更新。 |

### 6.1 世界模型与环境预测

| 论文 | 出处 | 机制 / 归属依据 |
| --- | --- | --- |
| [Stochastic Variational Video Prediction](../README.zh-CN.md#s070) · [原文](https://openreview.net/forum?id=rk49Mg-CW) | ICLR 2018 | **运动变换与预测** · 在 CDNA 运动变换式视频预测器中引入随机潜变量，为同一动作与观测生成多个可能未来。 |
| [Unsupervised Learning for Physical Interaction through Video Prediction](../README.zh-CN.md#s068) · [原文](https://papers.nips.cc/paper_files/paper/2016/hash/d9d4f495e875a2e075a1a4a6e1b9770f-Abstract.html) | NeurIPS 2016 | **运动变换与预测** · 通过 DNA、CDNA 与空间变换预测器建模像素运动，将前帧内容变换和融合为动作条件的未来图像。 |

### 6.2 交互式环境与模拟

| 论文 | 出处 | 机制 / 归属依据 |
| --- | --- | --- |
| [WorldMem: Long-term Consistent World Simulation with Memory](../README.zh-CN.md#s072) · [原文](https://proceedings.neurips.cc/paper_files/paper/2025/hash/470629a47e2d65ce0606c40055df5d26-Abstract-Conference.html) | NeurIPS 2025 | **空间记忆** · 保存历史帧、相机位姿与时间状态，通过记忆检索和注意力提高交互式世界模拟的长期一致性。 |
| [Video World Models with Long-term Spatial Memory](../README.zh-CN.md#s073) · [原文](https://proceedings.neurips.cc/paper_files/paper/2025/hash/467655d26fcc207bca08915dc91964c6-Abstract-Conference.html) | NeurIPS 2025 | **重投影与渲染** · 将生成帧累积为几何空间记忆，再按目标相机视角检索和渲染，维持动作条件世界生成中的场景一致性。 |
| [Gibson Env: Real-World Perception for Embodied Agents](../README.zh-CN.md#s071) · [原文](https://openaccess.thecvf.com/content_cvpr_2018/html/Xia_Gibson_Env_Real-World_CVPR_2018_paper.html) | CVPR 2018 | **重投影与渲染** · 将真实扫描场景中的观测重投影到新视角并进行神经修复，构建用于具身感知与控制的模拟环境。 |

### 6.3 具身智能体、规划与控制

| 论文 | 出处 | 机制 / 归属依据 |
| --- | --- | --- |
| [Autonomous Functional Play with Correspondence-Driven Trajectory Warping](../README.zh-CN.md#s077) · [原文](https://proceedings.iclr.cc/paper_files/paper/2026/hash/b52ffc1e3ab14f7b423acbb14cdbfe8e-Abstract-Conference.html) | ICLR 2026 | **动作轨迹形变** · 以语义关键点对应将少量示范的动作轨迹 Warp 到目标场景，并通过自主任务交互持续收集经验。 |
| [RVT: Robotic View Transformer for 3D Object Manipulation](../README.zh-CN.md#s075) · [原文](https://proceedings.mlr.press/v229/goyal23a.html) | CoRL 2023 / PMLR 2023 | **重投影与渲染** · 将 RGB-D 点云重渲染为多个虚拟视图，融合跨视图特征并反投影来预测三维机器人动作。 |
| [FlowBot3D: Learning 3D Articulation Flow to Manipulate Articulated Objects](../README.zh-CN.md#s076) · [原文](https://www.roboticsproceedings.org/rss18/p018.html) | RSS 2022 | **运动变换与预测** · 预测关节物体点云上各点的潜在三维运动方向，再用该稠密向量场引导解析运动规划。 |
| [Dense Object Nets: Learning Dense Visual Object Descriptors By and For Robotic Manipulation](../README.zh-CN.md#s074) · [原文](https://proceedings.mlr.press/v87/florence18a.html) | CoRL 2018 / PMLR 2018 | **对应关系估计** · 利用多视图三维重建自动构造对应监督，学习支持跨姿态与跨物体操作的稠密视觉描述子。 |
