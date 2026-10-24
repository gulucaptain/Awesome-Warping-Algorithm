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

{{STATS}}

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

Entries follow **research area → topic**, with papers listed newest year first within each topic. Each topic opens with a scope and paper-count block. Papers follow a consistent sequence: full paper title (venue and year), one row of resource badges followed by technique tags, and a contribution summary. Full publication histories, code provenance and limitations remain in the bilingual catalog and research guides. Horizontal rules separate methods; classical and recent work appear together without year navigation or year groups. Published work uses its representative publication year, and preprints use their preprint year; publication histories are retained. Entries combining foundational methods use the publication year of the linked representative paper. Undated foundations appear last within their topic. Entries from the same year retain catalog order. Coverage ends on {{DATE}}. Descriptions are grounded in papers and author resources; the collection does not claim a unified reproduction of all methods.

Each work has one primary topic, with related tags and reading links for other directions. Spatial reasoning, world models, interactive simulation and embodied agents are reserved for future work directly connected to warping.

[Definitions, mapping conventions and evidence policy →](docs/RESEARCH_GUIDE.md#scope)

</details>

<a id="topics"></a>
## 🗂️ Topic navigation

{{AREA_COUNT}} research areas and {{TOPIC_COUNT}} topics, including {{RESERVED_COUNT}} reserved topics. Counts include primary entries only; related reading is not counted twice.

{{TOPICS}}

{{CATALOG}}

<a id="technology"></a>
## 🧩 Technique cross-index

Methods can belong to multiple families. Follow a method name to its primary entry; `T1–T9` tags link back to this map. Works are listed newest year first.

<details>
<summary><b>Browse all {{TECH_COUNT}} technique families</b></summary>

{{TECHNOLOGIES}}

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

<a id="contributing"></a>
## 🤝 Contributing

Suggestions, corrections and verified links are welcome through [Issues](https://github.com/gulucaptain/Awesome-Warping-Algorithm/issues) and [Pull Requests](https://github.com/gulucaptain/Awesome-Warping-Algorithm/pulls).

Please include the **paper title, publication year/status, Paper, Project, GitHub, technique family, primary topic and related topic tags**. Leave unavailable links empty, and distinguish author implementations, third-party reimplementations and shared frameworks.

Edit [the bilingual catalog](data/catalog.json) and run `python3 scripts/build_readme.py` to update both READMEs. Counts and indexes use the same data; check consistency with `python3 scripts/build_readme.py --check`. Set each work's unique home with `primary_topic`; `topics` contains that home and related directions. When adding papers to a reserved topic, set its `reserved` flag to `false`.

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
