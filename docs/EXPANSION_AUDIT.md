# 论文扩充核验记录 · 2026-10-24

本轮在原有 56 篇具体论文基础上新增 72 篇，当前共 128 篇论文；6 个研究板块与 16 个 Topic 的名称和范围保持不变。原有论文及其 ID、资源、描述全部保留。原目录另含一个通用概念条目 C01（刚体、相似、仿射与单应性变换），现移至中英文研究指南的基础概念部分，原始记录保留在文献数据的 `background_references` 中，不列入论文正文与统计。

新增条目中，71 篇匹配到 OpenAlex 引用记录，59 篇的单条匹配记录引用数不少于 100，15 篇不少于 1,000。DIAMOND 未找到可准确匹配的记录，标记为未取得数据，没有写成零引用。

## 筛选口径

- 首先要求论文的核心贡献符合主 Topic，之后综合引用记录、正式发表信息、方法代表性与技术链覆盖。引用数没有用于改变 README 中的年份倒序。
- 引用数为 OpenAlex 在核验日返回的单条记录快照，不等同于 Google Scholar 总引用；预印本与正式版本不相加，不据此建立跨领域统一排名。较新的代表性论文可以低于上述引用阈值。
- 论文内容依据会议原文、作者论文或作者项目核对；HF 仅在页面确实存在时提供徽章。HF 自动关联的 GitHub 仓库不自动视为作者实现。
- Deep Image Homography Estimation、DragNUWA、GAIA-1 仅按公开预印本或技术报告收录；EDVR 明确标为 CVPR Workshops。CoRL 工作在标题中同时保留会议年与 PMLR 出版年，并按 PMLR 出版年排序。
- PlaNet、DreamerV3 与 NeRF 标为相关基础，不声称它们是显式空间 Warping 算子。LoFTR 是半稠密匹配，不能当作完整时序光流；PYoCo、FreeNoise、ConsistI2V 的噪声相关或初始化也不直接等同于坐标输运。
- 所有新增论文保留中英文贡献、局限、主 Topic、关联 Topic、来源及引用快照，见 [文献数据](../data/catalog.json)。以下“归属依据”为编辑归纳。

## 各 Topic 覆盖

| Topic | 原有 | 新增 | 当前 |
| --- | ---: | ---: | ---: |
| 1.1 几何变换与形变编辑 | 7 | 3 | 10 |
| 1.2 可微采样与 Splatting | 3 | 3 | 6 |
| 2.1 光流与稠密对应 | 10 | 10 | 20 |
| 2.2 图像配准、拼接与视频稳像 | 5 | 4 | 9 |
| 2.3 医学图像配准与可逆形变 | 8 | 4 | 12 |
| 3.1 视频插帧与复原 | 5 | 6 | 11 |
| 3.2 人物动画、运动迁移与虚拟试衣 | 4 | 4 | 8 |
| 4.1 噪声 Warping 与时序一致性 | 1 | 3 | 4 |
| 4.2 相机、轨迹与运动可控生成 | 3 | 4 | 7 |
| 5.1 空间感知、深度与三维重建 | 1 | 6 | 7 |
| 5.2 重投影与新视角合成 | 4 | 5 | 9 |
| 5.3 动态三维与 4D 场景 | 5 | 4 | 9 |
| 5.4 空间推理与场景记忆 | 0 | 4 | 4 |
| 6.1 世界模型与环境预测 | 0 | 5 | 5 |
| 6.2 交互式环境与模拟 | 0 | 3 | 3 |
| 6.3 具身智能体、规划与控制 | 0 | 4 | 4 |

## 新增条目与一手来源

引用数列链接到对应 OpenAlex 记录。代码和项目只在内容核对且地址可访问时收录；访问受限的原出版页优先使用作者原文镜像。

### 1.1 几何变换与形变编辑

| 工作 | 出处 | OpenAlex 引用快照 | 原始来源 | 归属依据 |
| --- | --- | ---: | --- | --- |
| [Laplacian Surface Editing](../README.zh-CN.md#p01) | SGP 2004 | [1,169](https://openalex.org/W1631674738) | [原文](https://diglib.eg.org/items/ee43c2c6-4956-4ff0-9db1-c946306a5b99) | 通过局部拉普拉斯坐标与控制柄约束实现保留几何细节的网格编辑，是局部形变表示的重要基础。 |
| [Embedded Deformation](../README.zh-CN.md#p02) | SIGGRAPH / TOG 2007 | [459](https://openalex.org/W2047947369) | [原文](https://cgl.ethz.ch/~sumnerb/research/embdef/Sumner2007EDF.pdf) | 用稀疏形变图及节点局部仿射变换驱动复杂形状，为非刚性重建和形状操控提供通用模型。 |
| [Bounded Biharmonic Weights (BBW)](../README.zh-CN.md#p03) | SIGGRAPH / TOG 2011 | [336](https://openalex.org/W3137158176) | [原文](https://igl.ethz.ch/projects/bbw/bounded-biharmonic-weights-siggraph-2011-jacobson-et-al.pdf) | 通过带边界约束的双调和能量求解形状感知混合权重，统一点、骨骼和笼式控制下的二维与三维形变。 |

### 1.2 可微采样与 Splatting

| 工作 | 出处 | OpenAlex 引用快照 | 原始来源 | 归属依据 |
| --- | --- | ---: | --- | --- |
| Neural 3D Mesh Renderer（2026-10-24 范围审校后移除） | CVPR 2018 | [939](https://openalex.org/W2769112042) | [原文](https://arxiv.org/abs/1711.07566) | 为三角形光栅化设计近似梯度，使二维图像损失能够优化三维网格形状与相机参数。 |
| [Surface Splatting](../README.zh-CN.md#p04) | SIGGRAPH 2001 | [674](https://openalex.org/W2293372129) | [原文](https://www.cs.umd.edu/~zwicker/publications/SurfaceSplatting-SIG01.pdf) | 将屏幕空间 EWA 滤波推广到不规则表面点采样，结合可见性处理实现抗混叠点基元渲染。 |
| Soft Rasterizer (SoftRas)（2026-10-24 范围审校后移除） | ICCV 2019 | [642](https://openalex.org/W2990173985) | [原文](https://arxiv.org/abs/1904.01786) | 以概率覆盖和软聚合替代硬光栅化，将轮廓和颜色误差传播到网格几何与相机参数。 |

### 2.1 光流与稠密对应

| 工作 | 出处 | OpenAlex 引用快照 | 原始来源 | 归属依据 |
| --- | --- | ---: | --- | --- |
| [FlowNet](../README.zh-CN.md#p07) | ICCV 2015 | [4,310](https://openalex.org/W764651262) | [原文](https://openaccess.thecvf.com/content_iccv_2015/html/Dosovitskiy_FlowNet_Learning_Optical_ICCV_2015_paper.html) | 将稠密光流估计引入端到端卷积网络，并以相关层和 Flying Chairs 合成数据建立学习式光流的重要基线。 |
| [FlowNet 2.0](../README.zh-CN.md#p08) | CVPR 2017 | [3,154](https://openalex.org/W2560474170) | [原文](https://openaccess.thecvf.com/content_cvpr_2017/html/Ilg_FlowNet_2.0_Evolution_CVPR_2017_paper.html) | 通过级联网络、基于中间光流的图像 Warping 和专门的小位移分支，改进学习式光流估计。 |
| [LoFTR](../README.zh-CN.md#p69) | CVPR 2021 | [1,788](https://openalex.org/W3166285241) | [原文](https://openaccess.thecvf.com/content/CVPR2021/html/Sun_LoFTR_Detector-Free_Local_Feature_Matching_With_Transformers_CVPR_2021_paper.html) | 用图像对条件化 Transformer 特征进行粗到细匹配，在低纹理区域建立无需关键点检测的稠密候选对应。 |
| [SIFT Flow](../README.zh-CN.md#p72) | TPAMI 2011 | [1,589](https://openalex.org/W2090518410) | [原文](https://people.csail.mit.edu/celiu/SIFTflow/) | 在稠密 SIFT 描述子上优化保边空间匹配，将光流式对应推广到不同场景和不同外观的图像对齐。 |
| [SPyNet](../README.zh-CN.md#p09) | CVPR 2017 | [1,378](https://openalex.org/W2548527721) | [原文](https://openaccess.thecvf.com/content_cvpr_2017/html/Ranjan_Optical_Flow_Estimation_CVPR_2017_paper.html) | 在经典空间金字塔中用小型卷积网络逐层估计残差光流，以粗到细 Warping 处理大运动。 |
| [LiteFlowNet](../README.zh-CN.md#p10) | CVPR 2018 | [814](https://openalex.org/W2964156315) | [原文](https://arxiv.org/abs/1805.07036) | 结合特征金字塔、特征 Warping、匹配和局部正则，以紧凑网络估计光流。 |
| [Global Motion Aggregation (GMA)](../README.zh-CN.md#p11) | ICCV 2021 | [380](https://openalex.org/W3147597595) | [原文](https://openaccess.thecvf.com/content/ICCV2021/html/Jiang_Learning_To_Estimate_Hidden_Motions_With_Global_Motion_Aggregation_ICCV_2021_paper.html) | 用全局运动聚合将可见区域的运动信息传递到遮挡区域，增强基于 RAFT 的光流估计。 |
| [Robust Dense Matching (RoMa)](../README.zh-CN.md#p71) | CVPR 2024 | [285](https://openalex.org/W4402772491) | [原文](https://openaccess.thecvf.com/content/CVPR2024/html/Edstedt_RoMa_Robust_Dense_Feature_Matching_CVPR_2024_paper.html) | 结合冻结的基础模型特征、局部卷积特征和匹配解码器，预测对视角与外观变化更稳健的稠密坐标映射。 |
| [Dense Kernelized Matching (DKM)](../README.zh-CN.md#p70) | CVPR 2023 | [189](https://openalex.org/W4386075582) | [原文](https://openaccess.thecvf.com/content/CVPR2023/html/Edstedt_DKM_Dense_Kernelized_Feature_Matching_for_Geometry_Estimation_CVPR_2023_paper.html) | 通过全局核化回归和局部细化预测稠密匹配及置信度，服务于相机几何估计。 |
| [FlowFormer++](../README.zh-CN.md#p12) | CVPR 2023 | [123](https://openalex.org/W4386047772) | [原文](https://arxiv.org/abs/2303.01237) | 通过遮蔽代价体自编码预训练学习对应表示，增强光流网络对匹配结构的建模。 |

### 2.2 图像配准、拼接与视频稳像

| 工作 | 出处 | OpenAlex 引用快照 | 原始来源 | 归属依据 |
| --- | --- | ---: | --- | --- |
| [Deep Image Homography Estimation](../README.zh-CN.md#p13) | arXiv 2016 | [367](https://openalex.org/W2439114332) | [原文](https://arxiv.org/abs/1606.03798) | 直接从图像对预测四角点参数化单应性，为学习式平面配准提供早期代表方法。 |
| [Bundled Camera Paths](../README.zh-CN.md#p15) | SIGGRAPH / TOG 2013 | [361](https://openalex.org/W2057412674) | [原文](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/Stabilization_SIGGRAPH13.pdf) | 以网格顶点对应的多条相机路径描述空间变化运动，并联合时空平滑与几何约束完成视频稳像。 |
| [Unsupervised Deep Image Stitching (UDIS)](../README.zh-CN.md#p14) | IEEE TIP 2021 | [310](https://openalex.org/W3175249881) | [原文](https://arxiv.org/abs/2106.12859) | 在无真实单应性标注下学习图像对齐，并通过特征到图像重建完成拼接。 |
| [MeshFlow](../README.zh-CN.md#p16) | ECCV 2016 | [160](https://openalex.org/W2519006193) | [原文](https://doi.org/10.1007/978-3-319-46466-4_48) | 将特征运动传播到网格顶点，以顶点轨迹自适应平滑实现低延迟在线视频稳像。 |

### 2.3 医学图像配准与可逆形变

| 工作 | 出处 | OpenAlex 引用快照 | 原始来源 | 归属依据 |
| --- | --- | ---: | --- | --- |
| [Demons Registration](../README.zh-CN.md#p17) | Medical Image Analysis 1998 | [2,445](https://openalex.org/W2158167845) | [原文](https://doi.org/10.1016/s1361-8415(98)80022-4) | 以扩散过程类比构造稠密图像匹配更新，为医学图像非刚性配准提供经典迭代方法。 |
| [Deep Learning Image Registration (DLIR)](../README.zh-CN.md#p18) | Medical Image Analysis 2019 | [816](https://openalex.org/W2891590469) | [原文](https://arxiv.org/abs/1809.06130) | 结合全局仿射与局部非刚性网络，以图像相似性训练无监督医学配准框架。 |
| [Symmetric Diffeomorphic Registration (SYMNet)](../README.zh-CN.md#p19) | CVPR 2020 | [279](https://openalex.org/W3012775984) | [原文](https://arxiv.org/abs/2003.09514) | 在对称微分同胚空间中同时估计前向与反向变换，以无监督方式实现快速医学配准。 |
| [ICON](../README.zh-CN.md#p20) | ICCV 2021 | [25](https://openalex.org/W3160225309) | [原文](https://arxiv.org/abs/2105.04459) | 利用逆一致性损失与随机离网格插值促进空间映射正则化，学习近似微分同胚配准。 |

### 3.1 视频插帧与复原

| 工作 | 出处 | OpenAlex 引用快照 | 原始来源 | 归属依据 |
| --- | --- | ---: | --- | --- |
| [Task-Oriented Flow (TOFlow)](../README.zh-CN.md#p26) | IJCV 2019 | [1,399](https://openalex.org/W2769654144) | [原文](https://arxiv.org/abs/1711.09078) | 针对复原目标联合学习运动表示与视频处理网络，使跨帧 Warping 服务于插帧、去噪和超分任务。 |
| [EDVR](../README.zh-CN.md#p24) | CVPR Workshops 2019 | [1,271](https://openalex.org/W2965669158) | [原文](https://openaccess.thecvf.com/content_CVPRW_2019/html/NTIRE/Wang_EDVR_Video_Restoration_With_Enhanced_Deformable_Convolutional_Networks_CVPRW_2019_paper.html) | 以金字塔级联可形变对齐处理跨帧大运动，再用时空注意力融合实现视频复原。 |
| [Super SloMo](../README.zh-CN.md#p21) | CVPR 2018 | [848](https://openalex.org/W2963093735) | [原文](https://arxiv.org/abs/1712.00080) | 联合估计双向光流、任意中间时刻光流和软可见性，通过 Warping 与融合生成多帧慢动作。 |
| [BasicVSR](../README.zh-CN.md#p25) | CVPR 2021 | [626](https://openalex.org/W3107955907) | [原文](https://openaccess.thecvf.com/content/CVPR2021/html/Chan_BasicVSR_The_Search_for_Essential_Components_in_Video_Super-Resolution_and_CVPR_2021_paper.html) | 系统分析传播、对齐、聚合与上采样，以双向特征传播和光流 Warping 构建视频超分基线。 |
| [Depth-Aware Interpolation (DAIN)](../README.zh-CN.md#p22) | CVPR 2019 | [570](https://openalex.org/W2949258649) | [原文](https://arxiv.org/abs/1904.00830) | 在光流投影时利用深度优先处理近处物体，并融合 Warping 后的图像与上下文特征生成中间帧。 |
| [RIFE](../README.zh-CN.md#p23) | ECCV 2022 | [340](https://openalex.org/W4312623579) | [原文](https://arxiv.org/abs/2011.06294) | 直接估计任意中间时刻的光流，结合特权蒸馏和时间编码实现高效视频插帧。 |

### 3.2 人物动画、运动迁移与虚拟试衣

| 工作 | 出处 | OpenAlex 引用快照 | 原始来源 | 归属依据 |
| --- | --- | ---: | --- | --- |
| [VITON](../README.zh-CN.md#p27) | CVPR 2018 | [676](https://openalex.org/W2964050021) | [原文](https://arxiv.org/abs/1711.08447) | 利用粗到细生成、服装形变与融合，将服装图像迁移到目标人物并保留纹理细节。 |
| [X2Face](../README.zh-CN.md#p30) | ECCV 2018 | [435](https://openalex.org/W2884460600) | [原文](https://arxiv.org/abs/1807.10550) | 学习源人脸的嵌入表示及驱动采样场，通过空间重采样实现图像、姿态或音频驱动的人脸动画。 |
| [Adaptive Content Generation and Preservation (ACGPN)](../README.zh-CN.md#p28) | CVPR 2020 | [310](https://openalex.org/W3013135579) | [原文](https://arxiv.org/abs/2003.05863) | 根据试衣后的语义布局选择生成或保留内容，并用服装 Warping 与融合处理姿态和遮挡变化。 |
| [Parser-Free Appearance Flow (PF-AFN)](../README.zh-CN.md#p29) | CVPR 2021 | [225](https://openalex.org/W3175714707) | [原文](https://openaccess.thecvf.com/content/CVPR2021/html/Ge_Parser-Free_Virtual_Try-On_via_Distilling_Appearance_Flows_CVPR_2021_paper.html) | 通过教师—辅导—学生蒸馏学习服装与人体的外观流，使推理阶段不再依赖人体解析。 |

### 4.1 噪声 Warping 与时序一致性

| 工作 | 出处 | OpenAlex 引用快照 | 原始来源 | 归属依据 |
| --- | --- | ---: | --- | --- |
| Preserve Your Own Correlation (PYoCo)（2026-10-24 范围审校后移除） | ICCV 2023 | [136](https://openalex.org/W4390872681) | [原文](https://arxiv.org/abs/2305.10474) | 设计混合与渐进式时序相关噪声先验，将图像扩散模型适配到视频生成。 |
| FreeNoise（2026-10-24 范围审校后移除） | ICLR 2024 | [9](https://openalex.org/W4387929853) | [原文](https://proceedings.iclr.cc/paper_files/paper/2024/hash/15ce8e7afe5ee95bad56e3b9be28d3d1-Abstract-Conference.html) | 通过重调度初始噪声形成长程相关，并结合窗口时序注意力扩展预训练视频扩散模型的生成长度。 |
| ConsistI2V（2026-10-24 范围审校后移除） | TMLR 2024 | [4](https://openalex.org/W4391670749) | [原文](https://openreview.net/forum?id=vqniLmUDvj) | 结合首帧时空注意力与低频噪声初始化，改善图生视频中的布局、外观和时序一致性。 |

### 4.2 相机、轨迹与运动可控生成

| 工作 | 出处 | OpenAlex 引用快照 | 原始来源 | 归属依据 |
| --- | --- | ---: | --- | --- |
| MotionCtrl（2026-10-24 范围审校后移除） | SIGGRAPH 2024 | [134](https://openalex.org/W4400573519) | [原文](https://arxiv.org/abs/2312.03641) | 以相机位姿和物体轨迹分别建模相机与物体运动，支持视频生成中的独立控制与组合。 |
| DragAnything（2026-10-24 范围审校后移除） | ECCV 2024 | [29](https://openalex.org/W4402961675) | [原文](https://arxiv.org/abs/2403.07420) | 利用实体表示将用户绘制的轨迹关联到对象，支持多个对象及背景的运动控制。 |
| DragNUWA（2026-10-24 范围审校后移除） | arXiv 2023 | [13](https://openalex.org/W4385965594) | [原文](https://arxiv.org/abs/2308.08089) | 融合文本、图像与轨迹条件，通过轨迹采样和多尺度控制实现开放域运动引导。 |
| CameraCtrl（2026-10-24 范围审校后移除） | ECCV 2024 | [4](https://openalex.org/W4393967358) | [原文](https://arxiv.org/abs/2404.02101) | 将相机轨迹编码到可插拔相机模块，在尽量保留基础视频模型的同时实现位姿控制。 |

### 5.1 空间感知、深度与三维重建

| 工作 | 出处 | OpenAlex 引用快照 | 原始来源 | 归属依据 |
| --- | --- | ---: | --- | --- |
| COLMAP / Structure-from-Motion Revisited（2026-10-24 范围审校后移除） | CVPR 2016 | [6,417](https://openalex.org/W2471962767) | [原文](https://openaccess.thecvf.com/content_cvpr_2016/html/Schonberger_Structure-From-Motion_Revisited_CVPR_2016_paper.html) | 改进增量式运动恢复结构流程，从无序图像估计相机和稀疏几何，为跨视图重投影提供基础。 |
| [SfMLearner](../README.zh-CN.md#p43) | CVPR 2017 | [2,908](https://openalex.org/W2609883120) | [原文](https://openaccess.thecvf.com/content_cvpr_2017/html/Zhou_Unsupervised_Learning_of_CVPR_2017_paper.html) | 用可微视图重建连接单目深度与相机运动网络，以无监督光度误差学习几何。 |
| [MVSNet](../README.zh-CN.md#p39) | ECCV 2018 | [1,526](https://openalex.org/W2962793285) | [原文](https://arxiv.org/abs/1804.02505) | 用可微单应性 Warping 构建多视图代价体，并通过三维正则化推断参考视图深度。 |
| DUSt3R（2026-10-24 范围审校后移除） | CVPR 2024 | [594](https://openalex.org/W4402816534) | [原文](https://arxiv.org/abs/2312.14132) | 将无标定多视图重建转化为成对点图回归，再通过全局对齐建立统一三维坐标系。 |
| [DROID-SLAM](../README.zh-CN.md#p40) | NeurIPS 2021 | [345](https://openalex.org/W3193551877) | [原文](https://arxiv.org/abs/2108.10869) | 通过循环更新和稠密束调整联合优化相机位姿与逐像素深度，统一单目、双目及 RGB-D SLAM。 |
| MASt3R（2026-10-24 范围审校后移除） | ECCV 2024 | [308](https://openalex.org/W4404002617) | [原文](https://arxiv.org/abs/2406.09756) | 在 DUSt3R 三维点图基础上加入局部描述子与高效匹配，使图像对应与场景几何联合建模。 |

### 5.2 重投影与新视角合成

| 工作 | 出处 | OpenAlex 引用快照 | 原始来源 | 归属依据 |
| --- | --- | ---: | --- | --- |
| 3D Gaussian Splatting (3DGS)（2026-10-24 范围审校后移除） | SIGGRAPH / TOG 2023 | [5,979](https://openalex.org/W4385318467) | [原文](https://arxiv.org/abs/2308.04079) | 优化各向异性三维高斯及其密度，通过可见性感知 Splatting 实现高效新视角渲染。 |
| NeRF（2026-10-24 范围审校后移除） | ECCV 2020 | [5,335](https://openalex.org/W3109585842) | [原文](https://arxiv.org/abs/2003.08934) | 用连续辐射场与可微体渲染表示场景，从已知相机图像优化新视角合成。 |
| [pixelNeRF](../README.zh-CN.md#p47) | CVPR 2021 | [1,600](https://openalex.org/W3176368002) | [原文](https://openaccess.thecvf.com/content/CVPR2021/html/Yu_pixelNeRF_Neural_Radiance_Fields_From_One_or_Few_Images_CVPR_2021_paper.html) | 将三维采样点投影到源图像特征，以一幅或少量图像条件化辐射场并生成新视角。 |
| [IBRNet](../README.zh-CN.md#p46) | CVPR 2021 | [757](https://openalex.org/W3186630079) | [原文](https://arxiv.org/abs/2102.13090) | 将邻近源视图投影特征与射线聚合结合，学习可跨场景泛化的图像式新视角渲染。 |
| [Stereo Magnification / Multiplane Images](../README.zh-CN.md#p48) | SIGGRAPH / TOG 2018 | [149](https://openalex.org/W2804091141) | [原文](https://arxiv.org/abs/1805.09817) | 从窄基线双目图像预测多平面图像，以深度平面的单应性 Warping 合成更大基线的新视角。 |

### 5.3 动态三维与 4D 场景

| 工作 | 出处 | OpenAlex 引用快照 | 原始来源 | 归属依据 |
| --- | --- | ---: | --- | --- |
| [DynamicFusion](../README.zh-CN.md#p50) | CVPR 2015 | [952](https://openalex.org/W1938204631) | [原文](https://openaccess.thecvf.com/content_cvpr_2015/html/Newcombe_DynamicFusion_Reconstruction_and_2015_CVPR_paper.html) | 在规范空间中融合 RGB-D 观测，并估计将几何映射到当前帧的非刚性形变场，实现在线动态重建。 |
| [Neural Scene Flow Fields (NSFF)](../README.zh-CN.md#p49) | CVPR 2021 | [697](https://openalex.org/W3174752334) | [原文](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Neural_Scene_Flow_Fields_for_Space-Time_View_Synthesis_of_Dynamic_CVPR_2021_paper.html) | 联合建模外观、几何和三维场景流，以单目视频约束动态场景的时间与视角合成。 |
| [Dynamic 3D Gaussians](../README.zh-CN.md#p51) | 3DV 2024 | [473](https://openalex.org/W4399574574) | [原文](https://arxiv.org/abs/2308.09713) | 以随时间运动旋转、外观持久的三维高斯及局部刚性约束，联合实现动态视角合成与稠密跟踪。 |
| [TiNeuVox](../README.zh-CN.md#p52) | SIGGRAPH Asia 2022 | [287](https://openalex.org/W4281651265) | [原文](https://arxiv.org/abs/2205.15285) | 将时感知体素特征、小型坐标形变网络与多距离插值结合，加速动态辐射场优化。 |

### 5.4 空间推理与场景记忆

| 工作 | 出处 | OpenAlex 引用快照 | 原始来源 | 归属依据 |
| --- | --- | ---: | --- | --- |
| Visual Language Maps (VLMaps)（2026-10-24 范围审校后移除） | ICRA 2023 | [375](https://openalex.org/W4383108296) | [原文](https://arxiv.org/abs/2210.05714) | 将预训练视觉语言特征融合到三维地图，支持开放词汇目标定位与空间关系驱动的导航。 |
| ConceptGraphs（2026-10-24 范围审校后移除） | ICRA 2024 | [285](https://openalex.org/W4401414715) | [原文](https://arxiv.org/abs/2309.16650) | 将二维基础模型输出经跨视图关联融合为开放词汇三维场景图，用对象及关系支撑空间推理与规划。 |
| ConceptFusion（2026-10-24 范围审校后移除） | RSS 2023 | [227](https://openalex.org/W4385431115) | [原文](https://arxiv.org/abs/2302.07241) | 通过像素对齐开放集特征与多视图三维融合建立可用语言、图像或音频查询的空间地图。 |
| [Semantic MapNet (SMNet)](../README.zh-CN.md#p53) | AAAI 2021 | [68](https://openalex.org/W3091259027) | [原文](https://ojs.aaai.org/index.php/AAAI/article/view/16180) | 把第一视角 RGB-D 特征投影到俯视坐标，并用空间记忆积累多帧信息，形成可供导航和问答使用的语义地图。 |

### 6.1 世界模型与环境预测

| 工作 | 出处 | OpenAlex 引用快照 | 原始来源 | 归属依据 |
| --- | --- | ---: | --- | --- |
| PlaNet（2026-10-24 范围审校后移除） | ICML 2019 | [707](https://openalex.org/W2900152462) | [原文](https://proceedings.mlr.press/v97/hafner19a.html) | 从像素学习含确定性与随机成分的潜在状态动力学，并通过多步预测在潜在空间中搜索动作。 |
| DreamerV3（2026-10-24 范围审校后移除） | Nature 2025 | [179](https://openalex.org/W4409147637) | [原文](https://www.nature.com/articles/s41586-025-08744-2) | 从观测学习环境动力学、奖励与继续概率，在潜在想象轨迹中训练策略，并用归一化等机制提升跨任务稳定性。 |
| Drive-WM（2026-10-24 范围审校后移除） | CVPR 2024 | [119](https://openalex.org/W4402778069) | [原文](https://arxiv.org/abs/2311.17918) | 联合建模多视角和时间维度，生成不同驾驶动作对应的未来视频，并以图像奖励评估规划轨迹。 |
| GAIA-1（2026-10-24 范围审校后移除） | arXiv 2023 | [28](https://openalex.org/W4387294122) | [原文](https://arxiv.org/abs/2309.17080) | 将视频、文本与动作离散化并预测后续序列，用于驾驶场景的动作条件未来生成。 |
| DIAMOND（2026-10-24 范围审校后移除） | NeurIPS 2024 | 未取得数据 | [原文](https://proceedings.neurips.cc/paper_files/paper/2024/hash/6bdde0373d53d4a501249547084bed43-Abstract-Conference.html) | 在像素空间扩散世界模型中预测视觉动态，并利用模型想象训练强化学习策略。 |

### 6.2 交互式环境与模拟

| 工作 | 出处 | OpenAlex 引用快照 | 原始来源 | 归属依据 |
| --- | --- | ---: | --- | --- |
| Genie（2026-10-24 范围审校后移除） | ICML 2024 | [23](https://openalex.org/W4392182423) | [原文](https://proceedings.mlr.press/v235/bruce24a.html) | 从无动作标注的视频学习潜在动作与时空动态，生成可逐帧交互的虚拟环境。 |
| UniSim（2026-10-24 范围审校后移除） | ICLR 2024 | [20](https://openalex.org/W4387560742) | [原文](https://proceedings.iclr.cc/paper_files/paper/2024/hash/c4d66eae503694424123b93ac0fbaf17-Abstract-Conference.html) | 从异质视频与交互数据学习动作条件模拟器，生成指令或低层动作引起的视觉变化，并用于智能体训练。 |
| GameNGen（2026-10-24 范围审校后移除） | ICLR 2025 | [7](https://openalex.org/W4402704721) | [原文](https://proceedings.iclr.cc/paper_files/paper/2025/hash/b71ecea210f7159f31e46631fe5c838f-Abstract-Conference.html) | 用历史帧和动作条件化扩散模型，结合噪声增强训练生成可交互的 DOOM 画面序列。 |

### 6.3 具身智能体、规划与控制

| 工作 | 出处 | OpenAlex 引用快照 | 原始来源 | 归属依据 |
| --- | --- | ---: | --- | --- |
| [Active Neural SLAM](../README.zh-CN.md#p63) | ICLR 2020 | [318](https://openalex.org/W3011144238) | [原文](https://arxiv.org/abs/2004.05155) | 结合可学习空间映射、全局探索策略与局部规划，将几何地图用于具身环境中的主动探索。 |
| [CLIPort](../README.zh-CN.md#p66) | CoRL 2021 / PMLR 2022 | [223](https://openalex.org/W3203511201) | [原文](https://proceedings.mlr.press/v164/shridhar22a.html) | 将 CLIP 的语言语义与 Transporter 的空间对应结合，学习语言条件下的精确抓取放置操作。 |
| [Transporter Networks](../README.zh-CN.md#p65) | CoRL 2020 / PMLR 2021 | [200](https://openalex.org/W3096099141) | [原文](https://proceedings.mlr.press/v155/zeng21a.html) | 通过平移与旋转视觉特征并进行相关匹配，预测抓取和放置的空间位移，将对应建模用于机器人操作。 |
| Goal-Oriented Semantic Exploration (SemExp)（2026-10-24 范围审校后移除） | NeurIPS 2020 | [44](https://openalex.org/W3102804550) | [原文](https://proceedings.neurips.cc/paper/2020/hash/2c75cf2681788adaca63aa95ae028b22-Abstract.html) | 建立情景语义地图并利用目标类别相关的空间先验规划探索，完成未知环境中的对象目标导航。 |

## 链接与归属的排除记录

- Genie 的 HF 页面关联了 `1x-technologies/1xgpt`；它不是本篇 Genie 的作者实现，因此没有作为 Genie 的代码链接。
- ACGPN 的 HF 页面关联了第三方实现；没有据此标为官方代码。
- 部分旧项目页或候选仓库返回空内容、404、连接失败或无法核对身份，没有生成对应徽章；没有使用 “Unverified” 占位。
- 非刚性动态重建保留在 5.3，静态 NeRF / 3DGS 放在 5.2；空间地图与场景记忆放在 5.4，使用地图执行闭环导航与操作的系统放在 6.3。
- DIAMOND 的主要贡献是可用于策略学习的预测世界模型，主归 6.1；其可交互引擎作为 6.2 的关联阅读。UniSim、Genie、GameNGen 的主入口是可交互模拟环境，归 6.2。

本轮核验只扩充文献集合，没有统一复现论文性能，也没有收录与空间、视觉或环境交互无关的通用办公或编程智能体。
