# A practical guide to spatial warping

[← English collection](../README.md) · [中文研究指南](RESEARCH_GUIDE.zh-CN.md)

This guide explains the collection's organizing concepts. Method-specific contributions and limitations appear in both READMEs. Coverage is representative, with a review cutoff of **2026-10-24**.

<a id="scope"></a>
## Scope and mapping conventions

Warping has three complementary layers:

1. **The map and its estimation:** affine/projective transforms, TPS, meshes, optical flow, depth reprojection and 3D deformation determine where coordinates move.
2. **The sampling operator:** interpolation, forward splatting, reconstruction footprints and antialiasing determine how values reach a discrete target grid.
3. **The application:** registration, stitching, interpolation, reconstruction and generation determine the objective and how unobserved content is handled.

An optical-flow network estimates correspondence; it is not itself an interpolation kernel. NeRF and 3DGS are representation and rendering systems; their deformation and reprojection components are relevant here. Attention can support implicit alignment without defining an invertible geometric map.

- **Backward / pull:** for target position `y`, sample at source position `φ(y)`: `I_target(y) = sample(I_source, φ(y))`. This fills a target grid conveniently but cannot recover unobserved content.
- **Forward / push / splat:** move source position `x` to `ψ(x)` and aggregate contributions. Collisions, holes and visibility need explicit treatment.
- **Flow:** `ψ(x) = x + f(x)`. Backward flow generally cannot be obtained by simply negating forward flow at the same coordinates.
- **Depth reprojection:** back-project using depth and intrinsics, transform 3D points and project into a target camera. Distinguish camera-induced motion from independently moving objects.

See the [OpenCV transformation documentation](https://docs.opencv.org/4.x/da/d54/group__imgproc__transform.html) for inverse sampling and [Softmax Splatting](https://arxiv.org/abs/2003.05534) for differentiable forward aggregation.

## Publication and evidence policy

Classics end in 2021. The recent section uses representative formal publication years and notes earlier preprints. Preprints and author-reported acceptance are distinguished from formal proceedings.

Primary papers and author resources support the entries. HF Paper links identify verified paper pages, not necessarily models or demos. Code provenance is labeled; shared-framework counts describe the entire repository. This collection does not independently reproduce every performance claim.

<a id="trends"></a>
## Major developments

The following is an editorial synthesis of the linked work.

- **Correspondence estimation:** [PWC-Net](../README.md#c15), [RAFT](../README.md#c20), [GMFlow](../README.md#n01) and [FlowFormer](../README.md#n02) develop different ways to estimate dense maps. [SEA-RAFT](../README.md#n13) and [MEMFOF](../README.md#n20) emphasize accuracy, efficiency and resolution. Careful resampling remains necessary.
- **Renderable 3D and 4D deformation:** canonical deformation in [D-NeRF](../README.md#c21) and [Nerfies](../README.md#c22) extends to [Deformable 3D Gaussians](../README.md#n11) and [4D-GS](../README.md#n12). Rendering efficiency and true motion recovery are distinct questions.
- **Geometry coupled to generation:** [GenWarp](../README.md#n15), [WAVE](../README.md#n22) and [SplatDiff](../README.md#n23) combine geometric guidance with generative priors. [DMAligner](../README.md#n25) explores generative alignment. Plausible synthesis does not necessarily recover true correspondence.
- **Transporting random fields:** [∫-noise](../README.md#n16) incorporates noise statistics into transport; [Go-with-the-Flow](../README.md#n19) uses warped noise for motion control; [CameraNoise](../README.md#n24) connects camera reprojection to noise conditioning.
- **Operators, frequencies and capacity:** [ImWIP](../README.md#n10) studies adjoints and derivatives, [LookingGlass](../README.md#n21) uses frequency-aware warping, and [WarpI2I](../README.md#n26) redistributes latent representation capacity. Their objectives require different evaluation criteria.

<a id="noise"></a>
## Why interpolation changes Gaussian noise

For independent standard Gaussian samples `ε_i` and deterministic linear weights:

```text
z(y) = Σ_i w_i(y) ε_i
Var[z(y)] = Σ_i w_i(y)^2
Cov[z(y), z(y')] = Σ_i w_i(y) w_i(y')
```

Weights summing to one do not imply unit variance. Neighboring outputs sharing source samples can become spatially correlated. Per-pixel variance normalization generally does not remove these correlations. Evaluate within-frame statistics separately from motion-induced cross-frame correlation. The formulas do not directly cover signal-dependent random weights or arbitrary nonlinear operators. See the [∫-noise paper](https://openreview.net/pdf?id=pzElnMrgSD).

## Open problems and evaluation

- **Occlusion:** pure coordinate transforms cannot recover absent observations; multiview evidence, history or synthesis is needed.
- **Topology:** smoothness does not imply invertibility; inspect folds, self-intersections and discrete Jacobians.
- **Resampling:** strong minification needs footprint-aware filtering; repeated warp–unwarp can lose high-frequency detail.
- **Generative faithfulness:** evaluate visible-region fidelity, geometry and disoccluded-region plausibility separately.
- **Long-term drift:** good single-step alignment does not ensure stable long sequences.
- **Generalization and resources:** compare matched datasets, resolutions, precision and hardware.

Useful metrics include flow endpoint error and outlier rate; landmark error, Dice and Jacobians for registration; seams and distortion for stitching; and camera adherence, temporal consistency, texture fidelity and noise statistics for generative applications.

<a id="practice"></a>
## Tools and starting points

| Need | Starting point | Check |
| --- | --- | --- |
| Affine, projective or dense remapping | [OpenCV](https://docs.opencv.org/4.x/da/d54/group__imgproc__transform.html) | Direction, interpolation and boundaries |
| Differentiable backward sampling | [PyTorch grid_sample](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.grid_sample.html) | Normalized coordinates and `align_corners` |
| Landmark deformation | TPS / MLS; [scikit-image TPS](https://scikit-image.org/docs/stable/auto_examples/transform/plot_tps_deformation.html) | Outliers, extrapolation and folding |
| Shape-preserving mesh editing | ARAP; [libigl](https://libigl.github.io/libigl/tutorial/) | Mesh quality, constraints and self-intersection |
| Differentiable forward warping | [Softmax Splatting](https://github.com/sniklaus/softmax-splatting) | Weights, collisions and empty pixels |
| Known depth and camera trajectory | Reprojection with visibility handling | Depth boundaries, calibration and disocclusion |
| Dense video motion | RAFT / GMFlow / SEA-RAFT; MEMFOF for high-resolution multiframe use | Occlusion, confidence and domain shift |
| Anatomical registration | SyN / Diffeomorphic Demons / suitable learned methods | Physical coordinates, spacing and Jacobians |
| Warping in inverse problems | [ImWIP](https://imwip.readthedocs.io/en/latest/) | Inverse, adjoint and derivative differ |
| Motion-conditioned diffusion noise | ∫-noise, then Go-with-the-Flow / CameraNoise | Statistics, temporal correlation and model adaptation |

These are reading and prototyping starting points, not universal optimal choices. Select methods under the application's geometry, data, resource and error constraints.
