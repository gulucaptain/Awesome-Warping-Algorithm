# Systematic search across all topics · 2026-10-24

[中文](SYSTEMATIC_SEARCH.zh-CN.md) · [English collection](../README.md) · [Previous expansion audit](EXPANSION_AUDIT.md)

Baseline: **128 papers** at commit `c3327b8`. This batch adds **84 papers**, bringing the collection to **212**. Existing entries, IDs, links, descriptions and earlier research records are preserved. The six research areas and 16 topic definitions are unchanged.

## Search and screening method

- Discover candidates across application tasks, spatial mechanisms and transformed representations before looking up exact-title metadata. Topics determine the final home rather than limiting discovery. Searches include foundational work without a year restriction and recent 2025–2026 directions.
- Each topic receives open task/mechanism queries, recent-work queries and related-work follow-up. Methods and references in original papers provide further leads, followed by conference, publisher and author-source verification. This is not a complete forward-citation crawl.
- The log contains 117 Web queries and 1355 distinct returned URLs. 86 candidates received full-text review. URLs include mirrors, documentation and non-papers; they are not a paper count or a claim of individually screening every result.
- 84 papers are accepted with an explicit topic, mechanism, transformed representation, contribution and limitation. Spatial deformation, correspondence estimation, sampling, flow conditioning and memory are distinguished; they are not all called warping operators.
- Selection considers methodological contribution, publication status, influence and citation evidence. OpenAlex returned HTTP 429; a serial retry stopped on another 429. Only 19 accepted additions have verified citation matches. Missing counts remain missing, are never zero-filled and are not exclusion thresholds. No complete citation ranking is claimed.
- This is a bounded systematic batch rather than an exhaustive census. Unreviewed discovery hits and unresolved extension overlaps remain explicit leads. Nonempty topics or fixed quotas are not evidence of search saturation.

## Research records

| Record | Contents |
| --- | --- |
| [Queries and returned URLs](../data/research/2026-10-24-systematic/searches.json) | Discovery, mechanism follow-up and publication checks, with titles and links only |
| [Verification plan](../data/research/2026-10-24-systematic/verification-plan.json) | Proposed metadata before verification; screening decisions are authoritative |
| [Screening and version decisions](../data/research/2026-10-24-systematic/screening.json) | 99 decisions with bilingual reasons, original-source hashes, access failures and resource checks |
| [Metadata lookups](../data/research/2026-10-24-systematic/metadata-lookups.json) | OpenAlex/HF queries, statuses and matching alternatives |
| [Full-title mentions](../data/research/2026-10-24-systematic/reference-mentions.json) | Machine-detected related-work/reference leads, not independently validated citation edges |

## Version and relevance decisions

- Withdrawn FGDVI is represented by its author-designated successor FloED; title revisions within FloED are counted once.
- FIA-VTON preprint/proceedings title changes are merged. EquiVDM titles belong to one arXiv record and are conservatively labeled as a preprint.
- Clothing-animation FloAt differs from audio-driven FLOAT. The ECCV 2024 editing WAVE differs from the existing ICCV 2025 novel-view WAVE. Acronyms alone are not deduplication keys.
- PDC-Net+ records its extension relationship to PDC-Net; only the journal representative is added here. StabStitch++ remains deferred pending a contribution-level overlap review.
- Fast Forward retains its earlier title, MIDL 2025 conference date and PMLR 2026 publication date; sorting uses the proceedings publication year.
- Hyperbolic latent geometry, probability-flow matching and human-trajectory prediction are not accepted as spatial warping merely because titles mention geometry or flow.
- FlowVid has no released code/checkpoints according to its author repository. Its paper/project remain linked, with no GitHub Code badge. Other code requires a link from the original paper or an author project.

## Topic coverage

| Topic | Before | Added | Current |
| --- | ---: | ---: | ---: |
| 1.1 Geometric Transformations & Deformation Editing | 10 | 5 | 15 |
| 1.2 Differentiable Sampling & Splatting | 6 | 8 | 14 |
| 2.1 Optical Flow & Dense Correspondence | 20 | 5 | 25 |
| 2.2 Image Registration, Stitching & Stabilization | 9 | 4 | 13 |
| 2.3 Medical Registration & Diffeomorphic Deformation | 12 | 5 | 17 |
| 3.1 Video Interpolation & Restoration | 11 | 7 | 18 |
| 3.2 Animation, Motion Transfer & Virtual Try-On | 8 | 8 | 16 |
| 4.1 Noise Warping & Temporal Consistency | 4 | 7 | 11 |
| 4.2 Camera-, Trajectory- & Motion-Controlled Generation | 7 | 6 | 13 |
| 5.1 Spatial Perception, Depth & 3D Reconstruction | 7 | 5 | 12 |
| 5.2 Reprojection & Novel View Synthesis | 9 | 5 | 14 |
| 5.3 Dynamic 3D & 4D Scenes | 9 | 4 | 13 |
| 5.4 Spatial Reasoning & Scene Memory | 4 | 6 | 10 |
| 6.1 World Models & Environment Prediction | 5 | 2 | 7 |
| 6.2 Interactive Environments & Simulation | 3 | 3 | 6 |
| 6.3 Embodied Agents, Planning & Control | 4 | 4 | 8 |

## Accepted additions and topic fit

### 1.1 Geometric Transformations & Deformation Editing

| Paper | Publication | Mechanism / topic fit |
| --- | --- | --- |
| [Inpaint4Drag: Repurposing Inpainting Models for Drag-Based Image Editing via Bidirectional Warping](../README.md#s003) · [Source](https://openaccess.thecvf.com/content/ICCV2025/html/Lu_Inpaint4Drag_Repurposing_Inpainting_Models_for_Drag-Based_Image_Editing_via_Bidirectional_ICCV_2025_paper.html) | ICCV 2025 | **Explicit spatial deformation** · Separates pixel-space bidirectional warping from inpainting to deform selected regions and fill newly exposed content. |
| [FlowDrag: 3D-aware Drag-based Image Editing with Mesh-guided Deformation Vector Flow Fields](../README.md#s004) · [Source](https://proceedings.mlr.press/v267/koo25a.html) | ICML 2025 | **Explicit spatial deformation** · Deforms a reconstructed mesh with user handles and projects its displacement into a 2D flow field for diffusion editing. |
| DragDiffusion: Harnessing Diffusion Models for Interactive Point-based Image Editing (removed in the 2026-10-24 scope review) · [Source](https://openaccess.thecvf.com/content/CVPR2024/html/Shi_DragDiffusion_Harnessing_Diffusion_Models_for_Interactive_Point-based_Image_Editing_CVPR_2024_paper.html) | CVPR 2024 | **Spatial editing** · Optimizes diffusion latents with motion supervision on UNet features for interactive point-based shape editing. |
| [Green Coordinates](../README.md#s002) · [Source](https://www.wisdom.weizmann.ac.il/~ylipman/GC/gc_techrep.pdf) | SIGGRAPH / TOG 2008 | **Explicit spatial deformation** · Combines cage vertices and face orientations through Green coordinates for shape-preserving space deformation. |
| [Harmonic Coordinates for Character Articulation](../README.md#s001) · [Source](https://www.cs.jhu.edu/~misha/ReadingSeminar/Papers/Joshi07.pdf) | SIGGRAPH / TOG 2007 | **Explicit spatial deformation** · Uses harmonic cage weights to drive volumetric deformation with nonnegative influence and interior locality. |

### 1.2 Differentiable Sampling & Splatting

| Paper | Publication | Mechanism / topic fit |
| --- | --- | --- |
| gsplat: An Open-Source Library for Gaussian Splatting (removed in the 2026-10-24 scope review) · [Source](https://jmlr.org/papers/v26/24-1476.html) | JMLR 2025 | **Sampling / splatting operator** · Provides optimized differentiable Gaussian projection and rasterization for training and rendering splatting models. |
| Mip-Splatting: Alias-free 3D Gaussian Splatting (removed in the 2026-10-24 scope review) · [Source](https://openaccess.thecvf.com/content/CVPR2024/html/Yu_Mip-Splatting_Alias-free_3D_Gaussian_Splatting_CVPR_2024_paper.html) | CVPR 2024 | **Sampling / splatting operator** · Combines 3D smoothing and a 2D Mip filter to reduce Gaussian-splatting artifacts across sampling rates. |
| [Towards Progressive Multi-Frequency Representation for Image Warping](../README.md#s079) · [Source](https://openaccess.thecvf.com/content/CVPR2024/html/Xiao_Towards_Progressive_Multi-Frequency_Representation_for_Image_Warping_CVPR_2024_paper.html) | CVPR 2024 | **Sampling / splatting operator** · Uses progressive frequency representations and learnable Gabor filters to preserve local detail during image warping. |
| [Kernel Aware Resampler](../README.md#s006) · [Source](https://openaccess.thecvf.com/content/CVPR2023/html/Bernasconi_Kernel_Aware_Resampler_CVPR_2023_paper.html) | CVPR 2023 | **Sampling / splatting operator** · Conditions image resampling on spatially varying degradation that accounts for reconstruction kernels, geometric distortion and antialiasing. |
| [Learning Local Implicit Fourier Representation for Image Warping](../README.md#s085) · [Source](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136780179.pdf) | ECCV 2022 | **Sampling / splatting operator** · Uses local texture estimates and transformation Jacobians to predict Fourier responses for continuous image warping. |
| [SRWarp: Generalized Image Super-Resolution under Arbitrary Transformation](../README.md#s086) · [Source](https://openaccess.thecvf.com/content/CVPR2021/html/Son_SRWarp_Generalized_Image_Super-Resolution_under_Arbitrary_Transformation_CVPR_2021_paper.html) | CVPR 2021 | **Sampling / splatting operator** · Generalizes super-resolution to arbitrary spatial transforms using multiscale features and adaptive warping. |
| Modular Primitives for High-Performance Differentiable Rendering (removed in the 2026-10-24 scope review) · [Source](https://research.nvidia.com/publication/2020-11_modular-primitives-high-performance-differentiable-rendering) | SIGGRAPH Asia / TOG 2020 | **Sampling / splatting operator** · Exposes rasterization, interpolation, texture sampling and antialiasing as modular differentiable rendering primitives. |
| [Linearized Multi-Sampling for Differentiable Image Transformation](../README.md#s007) · [Source](https://research.google/pubs/linearized-multi-sampling-for-differentiable-image-transformation/) | ICCV 2019 | **Sampling / splatting operator** · Uses auxiliary neighboring samples and local linearization to improve gradients through differentiable image transformations. |

### 2.1 Optical Flow & Dense Correspondence

| Paper | Publication | Mechanism / topic fit |
| --- | --- | --- |
| [UFM: A Simple Path towards Unified Dense Correspondence with Flow](../README.md#s015) · [Source](https://proceedings.neurips.cc/paper_files/paper/2025/hash/9d89448b63ce1e2e8dc7af72c984c196-Abstract-Conference.html) | NeurIPS 2025 | **Correspondence estimation** · Directly regresses 2D displacement from unified covisible training pairs for optical flow and wide-baseline matching. |
| [PDC-Net+: Enhanced Probabilistic Dense Correspondence Network](../README.md#s012) · [Source](https://arxiv.org/abs/2109.13912) | TPAMI 2023 | **Correspondence estimation** · Jointly predicts dense correspondences and probabilistic confidence for large-displacement and wide-baseline matching. |
| CroCo v2: Improved Cross-view Completion Pre-training for Stereo Matching and Optical Flow (removed in the 2026-10-24 scope review) · [Source](https://openaccess.thecvf.com/content/ICCV2023/html/Weinzaepfel_CroCo_v2_Improved_Cross-view_Completion_Pre-training_for_Stereo_Matching_and_ICCV_2023_paper.html) | ICCV 2023 | **Correspondence estimation** · Uses cross-view completion pretraining and relative positions for flow and stereo without an explicit image-warping component. |
| [COTR: Correspondence Transformer for Matching Across Images](../README.md#s011) · [Source](https://openaccess.thecvf.com/content/ICCV2021/html/Jiang_COTR_Correspondence_Transformer_for_Matching_Across_Images_ICCV_2021_paper.html) | ICCV 2021 | **Correspondence estimation** · Predicts correspondences for continuous coordinate queries with a cross-image transformer and local refinement. |
| [GLU-Net: Global-Local Universal Network for Dense Flow and Correspondences](../README.md#s013) · [Source](https://openaccess.thecvf.com/content_CVPR_2020/html/Truong_GLU-Net_Global-Local_Universal_Network_for_Dense_Flow_and_Correspondences_CVPR_2020_paper.html) | CVPR 2020 | **Correspondence estimation** · Combines global and local correlations with adaptive resolution for geometric, optical-flow and semantic matching. |

### 2.2 Image Registration, Stitching & Stabilization

| Paper | Publication | Mechanism / topic fit |
| --- | --- | --- |
| [PixelStitch: Structure-Preserving Pixel-Wise Bidirectional Warps for Unsupervised Image Stitching](../README.md#s018) · [Source](https://openaccess.thecvf.com/content/ICCV2025/html/Jin_PixelStitch_Structure-Preserving_Pixel-Wise_Bidirectional_Warps_for_Unsupervised_Image_Stitching_ICCV_2025_paper.html) | ICCV 2025 | **Explicit spatial deformation** · Uses an intermediate projection plane and bidirectional pixel-wise residual warps to align images while preserving structure. |
| [DUT: Learning Video Stabilization by Simply Watching Unstable Videos](../README.md#s019) · [Source](https://arxiv.org/abs/2011.14574) | IEEE TIP 2022 | **Explicit spatial deformation** · Learns grid trajectories and adaptive smoothing from unstable videos to drive mesh-based stabilization. |
| [Shape-Preserving Half-Projective Warps for Image Stitching](../README.md#s016) · [Source](https://openaccess.thecvf.com/content_cvpr_2014/html/Chang_Shape-Preserving_Half-Projective_Warps_2014_CVPR_paper.html) | CVPR 2014 | **Explicit spatial deformation** · Transitions smoothly from projective alignment to similarity transforms to reduce distortion outside image overlaps. |
| [Parallax-tolerant Image Stitching](../README.md#s017) · [Source](https://openaccess.thecvf.com/content_cvpr_2014/html/Zhang_Parallax-tolerant_Image_Stitching_2014_CVPR_paper.html) | CVPR 2014 | **Explicit spatial deformation** · Combines homography, content-preserving local warps and seam selection for parallax-tolerant stitching. |

### 2.3 Medical Registration & Diffeomorphic Deformation

| Paper | Publication | Mechanism / topic fit |
| --- | --- | --- |
| [Learning Diffeomorphism for Medical Image Registration with Time-Embedded Architectures Using Semigroup Regularization](../README.md#s023) · [Source](https://openaccess.thecvf.com/content/CVPR2026/html/Matinkia_Learning_Diffeomorphism_for_Medical_Image_Registration_with_Time-Embedded_Architectures_Using_CVPR_2026_paper.html) | CVPR 2026 | **Explicit spatial deformation** · Models continuous-time registration with time-embedded networks and semigroup regularization instead of explicit integration. |
| [Fast forward: Rephrasing 3D deformable image registration through density alignment and splatting](../README.md#s084) · [Source](https://proceedings.mlr.press/v301/heinrich26a.html) | MIDL 2025 / PMLR 2026 | **Sampling / splatting operator** · Recasts medical registration as density alignment of forward-splatted point clouds using differentiable rasterization. |
| [GradICON: Approximate Diffeomorphisms via Gradient Inverse Consistency](../README.md#s020) · [Source](https://openaccess.thecvf.com/content/CVPR2023/html/Tian_GradICON_Approximate_Diffeomorphisms_via_Gradient_Inverse_Consistency_CVPR_2023_paper.html) | CVPR 2023 | **Explicit spatial deformation** · Regularizes the Jacobian of composed forward and reverse maps to learn smoother medical registration transforms. |
| [Fourier-Net: Fast Image Registration with Band-limited Deformation](../README.md#s022) · [Source](https://ojs.aaai.org/index.php/AAAI/article/view/25182) | AAAI 2023 | **Explicit spatial deformation** · Predicts band-limited Fourier deformation coefficients and decodes them into full-resolution displacement fields. |
| [Large Deformation Diffeomorphic Image Registration with Laplacian Pyramid Networks](../README.md#s021) · [Source](https://arxiv.org/abs/2006.16148) | MICCAI 2020 | **Explicit spatial deformation** · Estimates deformations coarse to fine in a Laplacian pyramid within a diffeomorphic registration framework. |

### 3.1 Video Interpolation & Restoration

| Paper | Publication | Mechanism / topic fit |
| --- | --- | --- |
| [HomoGen: Enhanced Video Inpainting via Homography Propagation and Diffusion](../README.md#s028) · [Source](https://openaccess.thecvf.com/content/CVPR2025/html/Ding_HomoGen_Enhanced_Video_Inpainting_via_Homography_Propagation_and_Diffusion_CVPR_2025_paper.html) | CVPR 2025 | **Explicit spatial deformation** · Propagates context through homography registration and injects the resulting priors into video diffusion inpainting. |
| [BiM-VFI: Bidirectional Motion Field-Guided Frame Interpolation for Video with Non-uniform Motions](../README.md#s029) · [Source](https://openaccess.thecvf.com/content/CVPR2025/html/Seo_BiM-VFI_Bidirectional_Motion_Field-Guided_Frame_Interpolation_for_Video_with_Non-uniform_CVPR_2025_paper.html) | CVPR 2025 | **Correspondence estimation** · Models nonuniform motion with bidirectional fields and combines flow estimation, adaptive upsampling and distillation for interpolation. |
| [Coherent Video Inpainting Using Optical Flow-Guided Efficient Diffusion](../README.md#s027) · [Source](https://arxiv.org/abs/2412.00857) | arXiv 2024 | **Feature / latent / attention alignment** · Guides video inpainting with completed flow and multiscale adapters, using flow-warped latent interpolation to accelerate denoising. |
| [Upscale-A-Video: Temporal-Consistent Diffusion Model for Real-World Video Super-Resolution](../README.md#s030) · [Source](https://openaccess.thecvf.com/content/CVPR2024/html/Zhou_Upscale-A-Video_Temporal-Consistent_Diffusion_Model_for_Real-World_Video_Super-Resolution_CVPR_2024_paper.html) | CVPR 2024 | **Feature / latent / attention alignment** · Combines temporal layers with global flow-guided recurrent latent propagation for diffusion-based video super-resolution. |
| [ProPainter: Improving Propagation and Transformer for Video Inpainting](../README.md#s024) · [Source](https://openaccess.thecvf.com/content/ICCV2023/html/Zhou_ProPainter_Improving_Propagation_and_Transformer_for_Video_Inpainting_ICCV_2023_paper.html) | ICCV 2023 | **Feature / latent / attention alignment** · Combines recurrent flow completion, image-and-feature propagation and a sparse video transformer for inpainting. |
| [Towards An End-to-End Framework for Flow-Guided Video Inpainting](../README.md#s025) · [Source](https://arxiv.org/abs/2204.02663) | CVPR 2022 | **Feature / latent / attention alignment** · Jointly trains flow completion, aligned feature propagation and content hallucination for end-to-end video inpainting. |
| [Deep Flow-Guided Video Inpainting](../README.md#s026) · [Source](https://arxiv.org/abs/1905.02884) | CVPR 2019 | **Feature / latent / attention alignment** · Completes spatiotemporal flow fields and propagates visible pixels along them to repair masked video regions. |

### 3.2 Animation, Motion Transfer & Virtual Try-On

| Paper | Publication | Mechanism / topic fit |
| --- | --- | --- |
| [Learning Implicit Features with Flow-Infused Transformations for Realistic Virtual Try-On](../README.md#s032) · [Source](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_Learning_Implicit_Features_with_Flow-Infused_Transformations_for_Realistic_Virtual_Try-On_ICCV_2025_paper.html) | ICCV 2025 | **Flow / trajectory conditioning** · Injects dense warp flow and garment features into attention for implicit alignment guidance in diffusion try-on. |
| [FloAt: Flow Warping of Self-Attention for Clothing Animation Generation](../README.md#s033) · [Source](https://arxiv.org/abs/2411.15028) | arXiv 2024 | **Feature / latent / attention alignment** · Warps previous-frame self-attention features using flow from normal maps and blends them into clothing-animation generation. |
| [D4-VTON: Dynamic Semantics Disentangling for Differential Diffusion based Virtual Try-On](../README.md#s036) · [Source](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6231_ECCV_2024_paper.php) | ECCV 2024 | **Explicit spatial deformation** · Discovers garment semantics for local-flow warping and uses differential information tracking in diffusion try-on. |
| [Taming the Power of Diffusion Models for High-Quality Virtual Try-On with Appearance Flow](../README.md#s031) · [Source](https://arxiv.org/abs/2308.06101) | ACM MM 2023 | **Explicit spatial deformation** · Explicitly warps garments with appearance flow and uses the aligned clothing to condition diffusion-based virtual try-on. |
| [GP-VTON: Towards General Purpose Virtual Try-on via Collaborative Local-Flow Global-Parsing Learning](../README.md#s035) · [Source](https://arxiv.org/abs/2303.13756) | CVPR 2023 | **Explicit spatial deformation** · Combines local garment flows and global parsing with dynamic gradient truncation to reduce boundary-related texture distortion. |
| [High-Resolution Virtual Try-On with Misalignment and Occlusion-Handled Conditions](../README.md#s034) · [Source](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/6403_ECCV_2022_paper.php) | ECCV 2022 | **Explicit spatial deformation** · Jointly exchanges information between garment warping and segmentation to reduce misalignment and occlusion-related texture squeezing. |
| [ClothFormer: Taming Video Virtual Try-On in All Module](../README.md#s078) · [Source](https://openaccess.thecvf.com/content/CVPR2022/html/Jiang_ClothFormer_Taming_Video_Virtual_Try-On_in_All_Module_CVPR_2022_paper.html) | CVPR 2022 | **Explicit spatial deformation** · Combines occlusion-aware garment warping, appearance-flow smoothing and a dual-stream transformer for consistent video try-on. |
| [One-Shot Free-View Neural Talking-Head Synthesis for Video Conferencing](../README.md#s037) · [Source](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_One-Shot_Free-View_Neural_Talking-Head_Synthesis_for_Video_Conferencing_CVPR_2021_paper.html) | CVPR 2021 | **Explicit spatial deformation** · Disentangles identity and motion keypoints to drive dense deformation and source-feature warping for talking-head synthesis. |

### 4.1 Noise Warping & Temporal Consistency

| Paper | Publication | Mechanism / topic fit |
| --- | --- | --- |
| [Infinite-Resolution Integral Noise Warping for Diffusion Models](../README.md#s043) · [Source](https://proceedings.iclr.cc/paper_files/paper/2025/hash/7feb98f84ee34f697944333d4faec0bd-Abstract-Conference.html) | ICLR 2025 | **Noise transport** · Uses Brownian-bridge increments to compute the infinite-resolution limit of integral noise warping efficiently. |
| [On Equivariance and Fast Sampling in Video Diffusion Models Trained with Warped Noise](../README.md#s044) · [Source](https://arxiv.org/abs/2504.09789) | arXiv 2025 | **Noise transport** · Studies how warped-noise training encourages spatial equivariance and applies it to efficient video generation and distillation. |
| [FlowVid: Taming Imperfect Optical Flows for Consistent Video-to-Video Synthesis](../README.md#s038) · [Source](https://openaccess.thecvf.com/content/CVPR2024/html/Liang_FlowVid_Taming_Imperfect_Optical_Flows_for_Consistent_Video-to-Video_Synthesis_CVPR_2024_paper.html) | CVPR 2024 | **Explicit spatial deformation** · Warps an edited first frame into later frames and combines these references with spatial conditions for video editing. |
| FLATTEN: optical FLow-guided ATTENtion for consistent text-to-video editing (removed in the 2026-10-24 scope review) · [Source](https://openreview.net/forum?id=JgqftqZQZ7) | ICLR 2024 | **Flow / trajectory conditioning** · Restricts attention along optical-flow trajectories to improve temporal consistency in text-guided video editing. |
| [WAVE: Warping DDIM Inversion Features for Zero-shot Text-to-Video Editing](../README.md#s042) · [Source](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9682_ECCV_2024_paper.php) | ECCV 2024 | **Feature / latent / attention alignment** · Propagates key-frame features with flow during DDIM inversion to improve latent consistency for video editing. |
| [LatentWarp: Consistent Diffusion Latents for Zero-Shot Video-to-Video Translation](../README.md#s040) · [Source](https://arxiv.org/abs/2311.00353) | arXiv 2023 | **Feature / latent / attention alignment** · Warps diffusion latents with optical flow to constrain query tokens for consistent zero-shot video translation. |
| [Rerender A Video: Zero-Shot Text-Guided Video-to-Video Translation](../README.md#s041) · [Source](https://arxiv.org/abs/2306.07954) | SIGGRAPH Asia / TOG 2023 | **Feature / latent / attention alignment** · Constrains key-frame shape and texture with cross-frame alignment, then propagates edits through temporal matching and blending. |

### 4.2 Camera-, Trajectory- & Motion-Controlled Generation

| Paper | Publication | Mechanism / topic fit |
| --- | --- | --- |
| [FloVD: Optical Flow Meets Video Diffusion Model for Enhanced Camera-Controlled Video Synthesis](../README.md#s047) · [Source](https://arxiv.org/abs/2502.08244) | CVPR 2025 | **Flow / trajectory conditioning** · Represents camera and object motion with flow, using flow generation followed by flow-conditioned video synthesis. |
| [TrajectoryCrafter: Redirecting Camera Trajectory for Monocular Videos via Diffusion Models](../README.md#s048) · [Source](https://www.openaccess.thecvf.com/content/ICCV2025/html/Yu_TrajectoryCrafter_Redirecting_Camera_Trajectory_for_Monocular_Videos_via_Diffusion_Models_ICCV_2025_paper.html) | ICCV 2025 | **Reprojection and rendering** · Conditions diffusion on source video and target-trajectory point-cloud renders, using double reprojection for training data. |
| [Latent-Reframe: Enabling Camera Control for Video Diffusion Models without Training](../README.md#s049) · [Source](https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_Latent-Reframe_Enabling_Camera_Control_for_Video_Diffusion_Models_without_Training_ICCV_2025_paper.html) | ICCV 2025 | **Reprojection and rendering** · Reframes video latents through time-aware point clouds and refines them with latent inpainting and harmonization. |
| MotionPro: A Precise Motion Controller for Image-to-Video Generation (removed in the 2026-10-24 scope review) · [Source](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_MotionPro_A_Precise_Motion_Controller_for_Image-to-Video_Generation_CVPR_2025_paper.html) | CVPR 2025 | **Flow / trajectory conditioning** · Uses region-wise trajectories and motion masks for fine-grained object and camera motion conditioning. |
| [Motion-I2V: Consistent and Controllable Image-to-Video Generation with Explicit Motion Modeling](../README.md#s045) · [Source](https://arxiv.org/abs/2401.15977) | SIGGRAPH 2024 | **Flow / trajectory conditioning** · Predicts pixel trajectories and uses motion-augmented temporal attention to propagate features under sparse trajectory control. |
| [MotionCraft: Physics-Based Zero-Shot Video Generation](../README.md#s046) · [Source](https://proceedings.neurips.cc/paper_files/paper/2024/hash/ded49449e9239a47057c33ef8d42c26e-Abstract-Conference.html) | NeurIPS 2024 | **Noise transport** · Warps diffusion noise latents with optical flow from a physics simulation for zero-shot motion control. |

### 5.1 Spatial Perception, Depth & 3D Reconstruction

| Paper | Publication | Mechanism / topic fit |
| --- | --- | --- |
| VGGT: Visual Geometry Grounded Transformer (removed in the 2026-10-24 scope review) · [Source](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.html) | CVPR 2025 | **Geometry estimation** · Jointly predicts cameras, depth, point maps and tracks for geometric reconstruction and downstream reprojection. |
| FoundationStereo: Zero-Shot Stereo Matching (removed in the 2026-10-24 scope review) · [Source](https://openaccess.thecvf.com/content/CVPR2025/html/Wen_FoundationStereo_Zero-Shot_Stereo_Matching_CVPR_2025_paper.html) | CVPR 2025 | **Correspondence estimation** · Combines synthetic stereo data, monocular priors and cost-volume reasoning for generalizable stereo depth matching. |
| RAFT-Stereo: Multilevel Recurrent Field Transforms for Stereo Matching (removed in the 2026-10-24 scope review) · [Source](https://arxiv.org/abs/2109.07547) | 3DV 2021 | **Correspondence estimation** · Uses correlation pyramids and multilevel recurrent updates to estimate dense disparity from rectified stereo pairs. |
| [Cascade Cost Volume for High-Resolution Multi-View Stereo and Stereo Matching](../README.md#s051) · [Source](https://openaccess.thecvf.com/content_CVPR_2020/html/Gu_Cascade_Cost_Volume_for_High-Resolution_Multi-View_Stereo_and_Stereo_Matching_CVPR_2020_paper.html) | CVPR 2020 | **Geometry estimation** · Narrows depth hypotheses across cascaded feature cost volumes for high-resolution stereo and multiview depth estimation. |
| [DPSNet: End-to-end Deep Plane Sweep Stereo](../README.md#s052) · [Source](https://arxiv.org/abs/1905.00538) | ICLR 2019 | **Reprojection and rendering** · Builds feature cost volumes with differentiable plane-sweep warping, then aggregates them to regress scene depth. |

### 5.2 Reprojection & Novel View Synthesis

| Paper | Publication | Mechanism / topic fit |
| --- | --- | --- |
| [DepthSplat: Connecting Gaussian Splatting and Depth](../README.md#s059) · [Source](https://openaccess.thecvf.com/content/CVPR2025/html/Xu_DepthSplat_Connecting_Gaussian_Splatting_and_Depth_CVPR_2025_paper.html) | CVPR 2025 | **Reprojection and rendering** · Connects multiview depth estimation and Gaussian reconstruction, using rendering supervision to improve depth representations. |
| [MVSplat: Efficient 3D Gaussian Splatting from Sparse Multi-View Images](../README.md#s058) · [Source](https://arxiv.org/abs/2403.14627) | ECCV 2024 | **Reprojection and rendering** · Uses plane-sweep feature cost volumes to predict 3D Gaussians for feed-forward novel-view rendering from sparse views. |
| [MultiDiff: Consistent Novel View Synthesis from a Single Image](../README.md#s060) · [Source](https://openaccess.thecvf.com/content/CVPR2024/html/Muller_MultiDiff_Consistent_Novel_View_Synthesis_from_a_Single_Image_CVPR_2024_paper.html) | CVPR 2024 | **Reprojection and rendering** · Warps a reference image with monocular depth and jointly synthesizes target views using a video-diffusion prior. |
| [SynSin: End-to-End View Synthesis From a Single Image](../README.md#s056) · [Source](https://openaccess.thecvf.com/content_CVPR_2020/html/Wiles_SynSin_End-to-End_View_Synthesis_From_a_Single_Image_CVPR_2020_paper.html) | CVPR 2020 | **Reprojection and rendering** · Lifts image features into a point cloud, differentiably projects them to target views and refines disoccluded regions. |
| [3D Photography Using Context-Aware Layered Depth Inpainting](../README.md#s083) · [Source](https://openaccess.thecvf.com/content_CVPR_2020/html/Shih_3D_Photography_Using_Context-Aware_Layered_Depth_Inpainting_CVPR_2020_paper.html) | CVPR 2020 | **Reprojection and rendering** · Builds a layered depth image with explicit pixel connectivity and inpaints hidden color and depth for parallax rendering. |

### 5.3 Dynamic 3D & 4D Scenes

| Paper | Publication | Mechanism / topic fit |
| --- | --- | --- |
| [MoSca: Dynamic Gaussian Fusion from Casual Videos via 4D Motion Scaffolds](../README.md#s063) · [Source](https://openaccess.thecvf.com/content/CVPR2025/html/Lei_MoSca_Dynamic_Gaussian_Fusion_from_Casual_Videos_via_4D_Motion_CVPR_2025_paper.html) | CVPR 2025 | **Explicit spatial deformation** · Lifts video priors into a 4D motion scaffold and fuses attached Gaussians to separate appearance from deformation. |
| [SC-GS: Sparse-Controlled Gaussian Splatting for Editable Dynamic Scenes](../README.md#s061) · [Source](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_SC-GS_Sparse-Controlled_Gaussian_Splatting_for_Editable_Dynamic_Scenes_CVPR_2024_paper.html) | CVPR 2024 | **Explicit spatial deformation** · Interpolates time-varying 6-DoF transforms of sparse control points to deform dense Gaussians for dynamic reconstruction and editing. |
| [SceNeRFlow: Time-Consistent Reconstruction of General Dynamic Scenes](../README.md#s062) · [Source](https://arxiv.org/abs/2308.08258) | 3DV 2024 | **Explicit spatial deformation** · Uses backward deformation into a canonical scene to recover time-consistent correspondences over large motions. |
| [Non-Rigid Neural Radiance Fields: Reconstruction and Novel View Synthesis of a Dynamic Scene From Monocular Video](../README.md#s064) · [Source](https://openaccess.thecvf.com/content/ICCV2021/html/Tretschk_Non-Rigid_Neural_Radiance_Fields_Reconstruction_and_Novel_View_Synthesis_of_ICCV_2021_paper.html) | ICCV 2021 | **Explicit spatial deformation** · Uses ray bending and rigidity constraints to separate canonical radiance from deformation in monocular dynamic reconstruction. |

### 5.4 Spatial Reasoning & Scene Memory

| Paper | Publication | Mechanism / topic fit |
| --- | --- | --- |
| 3D-Mem: 3D Scene Memory for Embodied Exploration and Reasoning (removed in the 2026-10-24 scope review) · [Source](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_3D-Mem_3D_Scene_Memory_for_Embodied_Exploration_and_Reasoning_CVPR_2025_paper.html) | CVPR 2025 | **Spatial memory** · Combines 3D scene representations with informative memory and frontier snapshots for embodied exploration and reasoning. |
| GraphEQA: Using 3D Semantic Scene Graphs for Real-time Embodied Question Answering (removed in the 2026-10-24 scope review) · [Source](https://proceedings.mlr.press/v305/saxena25a.html) | CoRL 2025 / PMLR 2025 | **Spatial memory** · Uses online metric-semantic 3D scene graphs and images as multimodal memory for structured exploration and question answering. |
| [Trans4Map: Revisiting Holistic Bird's-Eye-View Mapping From Egocentric Images to Allocentric Semantics With Vision Transformers](../README.md#s082) · [Source](https://openaccess.thecvf.com/content/WACV2023/html/Chen_Trans4Map_Revisiting_Holistic_Birds-Eye-View_Mapping_From_Egocentric_Images_to_Allocentric_WACV_2023_paper.html) | WACV 2023 | **Spatial memory** · Projects transformer features from egocentric images into bidirectional allocentric memory for top-down semantic mapping. |
| [EgoMap: Projective mapping and structured egocentric memory for Deep RL](../README.md#s080) · [Source](https://arxiv.org/abs/2002.02286) | ECML PKDD 2020 | **Spatial memory** · Inverse-projects image features into a top-down memory map and updates its coordinates with ego-motion-driven affine transforms. |
| Neural Map: Structured Memory for Deep Reinforcement Learning (removed in the 2026-10-24 scope review) · [Source](https://arxiv.org/abs/1702.08360) | ICLR 2018 | **Spatial memory** · Stores environment information in spatially structured neural memory with location-dependent reads and writes. |
| [MapNet: An Allocentric Spatial Memory for Mapping Environments](../README.md#s081) · [Source](https://openaccess.thecvf.com/content_cvpr_2018/html/Henriques_MapNet_An_Allocentric_CVPR_2018_paper.html) | CVPR 2018 | **Spatial memory** · Registers RGB-D observations into learned allocentric memory using paired convolutional localization and registration operations. |

### 6.1 World Models & Environment Prediction

| Paper | Publication | Mechanism / topic fit |
| --- | --- | --- |
| [Stochastic Variational Video Prediction](../README.md#s070) · [Source](https://openreview.net/forum?id=rk49Mg-CW) | ICLR 2018 | **Motion transformation and prediction** · Adds stochastic latents to a CDNA motion-transforming predictor to model multiple possible visual futures. |
| [Unsupervised Learning for Physical Interaction through Video Prediction](../README.md#s068) · [Source](https://papers.nips.cc/paper_files/paper/2016/hash/d9d4f495e875a2e075a1a4a6e1b9770f-Abstract.html) | NeurIPS 2016 | **Motion transformation and prediction** · Predicts pixel motion with DNA, CDNA and spatial-transformer predictors, transforming and compositing prior frames into action-conditioned futures. |

### 6.2 Interactive Environments & Simulation

| Paper | Publication | Mechanism / topic fit |
| --- | --- | --- |
| WorldMem: Long-term Consistent World Simulation with Memory (removed in the 2026-10-24 scope review) · [Source](https://proceedings.neurips.cc/paper_files/paper/2025/hash/470629a47e2d65ce0606c40055df5d26-Abstract-Conference.html) | NeurIPS 2025 | **Spatial memory** · Retrieves historical frames using pose and time states to improve long-term consistency in interactive world simulation. |
| [Video World Models with Long-term Spatial Memory](../README.md#s073) · [Source](https://proceedings.neurips.cc/paper_files/paper/2025/hash/467655d26fcc207bca08915dc91964c6-Abstract-Conference.html) | NeurIPS 2025 | **Reprojection and rendering** · Accumulates generated frames into geometric spatial memory for camera-conditioned retrieval and rendering in persistent world generation. |
| [Gibson Env: Real-World Perception for Embodied Agents](../README.md#s071) · [Source](https://openaccess.thecvf.com/content_cvpr_2018/html/Xia_Gibson_Env_Real-World_CVPR_2018_paper.html) | CVPR 2018 | **Reprojection and rendering** · Reprojects observations from scanned real spaces and uses neural rendering to support embodied perception and control in simulation. |

### 6.3 Embodied Agents, Planning & Control

| Paper | Publication | Mechanism / topic fit |
| --- | --- | --- |
| [Autonomous Functional Play with Correspondence-Driven Trajectory Warping](../README.md#s077) · [Source](https://proceedings.iclr.cc/paper_files/paper/2026/hash/b52ffc1e3ab14f7b423acbb14cdbfe8e-Abstract-Conference.html) | ICLR 2026 | **Action-trajectory warping** · Warps demonstration action trajectories through semantic keypoint correspondences and collects experience through autonomous functional play. |
| [RVT: Robotic View Transformer for 3D Object Manipulation](../README.md#s075) · [Source](https://proceedings.mlr.press/v229/goyal23a.html) | CoRL 2023 / PMLR 2023 | **Reprojection and rendering** · Renders RGB-D point clouds into virtual views, fuses their features and back-projects predictions into 3D robot actions. |
| FlowBot3D: Learning 3D Articulation Flow to Manipulate Articulated Objects (removed in the 2026-10-24 scope review) · [Source](https://www.roboticsproceedings.org/rss18/p018.html) | RSS 2022 | **Motion transformation and prediction** · Predicts point-wise 3D articulation directions and uses the resulting vector field to guide analytical manipulation planning. |
| Dense Object Nets: Learning Dense Visual Object Descriptors By and For Robotic Manipulation (removed in the 2026-10-24 scope review) · [Source](https://proceedings.mlr.press/v87/florence18a.html) | CoRL 2018 / PMLR 2018 | **Correspondence estimation** · Uses multiview 3D reconstruction to supervise dense descriptors for correspondence-based robotic manipulation. |
