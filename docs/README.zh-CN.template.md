<!-- Generated from data/catalog.json by scripts/build_readme.py. -->
<a id="top"></a>

<div align="center">

<img src="assets/warping-banner-v2.png" alt="Luminous coordinate grids deform into a continuous three-dimensional flow surface" width="100%">

# Awesome Warping Algorithms · 中文版

*空间 Warping 算法与研究资源图谱。*

[English](README.md) · **简体中文**

<p align="justify">
Warping 将像素、特征与噪声在空间和时间中建立映射，是图像对齐、三维重建与可控生成的重要基础。本仓库连接经典方法与前沿进展，按基础技术和应用领域整理论文与代码，帮助研究者梳理技术脉络、比较不同思路，并在已有工作上继续探索。
</p>

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

“经典”指截至 2021 年的工作；2022–2026 按代表性正式发表年份整理，并保留早期预印本说明。2026 年覆盖截至 {{DATE}} 的公开资料。方法贡献和局限来自原论文、作者资料与原版调研；本合集未对所有实现做统一复现。

[完整定义、Forward / Backward 与核验原则 →](docs/RESEARCH_GUIDE.zh-CN.md#scope)

</details>

<a id="technology"></a>
## 🧩 基础技术

一种方法可以跨多个技术族；点击方法名直达条目，条目的 `T1–T9` 标签可返回本表。

<details>
<summary><b>展开 9 类基础技术与文献索引</b></summary>

{{TECHNOLOGIES}}

</details>

<a id="topics"></a>
## 🗂️ 应用领域

<details>
<summary><b>展开 16 个应用领域与文献索引</b></summary>

{{TOPICS}}

</details>

<a id="recent"></a>
## 🚀 近期进展 · 2022–2026

**[2026](#year-2026)** · **[2025](#year-2025)** · **[2024](#year-2024)** · **[2023](#year-2023)** · **[2022](#year-2022)**

由近及远浏览。每条保留原始来源、技术标签和一句贡献；详细边界与选型见 [研究指南](docs/RESEARCH_GUIDE.zh-CN.md#recent)。

{{RECENT}}

<a id="classics"></a>
## 🏛️ 经典方法 · 2022 年之前

{{CLASSICS}}

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

每条建议包含 **论文名、发表年份/状态、Paper、Project、GitHub、技术族和应用领域**。未公开的资源留空；第三方复现、共享框架与作者实现请明确区分。

维护者可编辑 [中英文文献数据](data/catalog.json)，再运行 `python3 scripts/build_readme.py` 同时更新中英文页面；计数与索引由同一份数据生成。详细原理与旧版逐项备注保留在 [研究指南](docs/RESEARCH_GUIDE.zh-CN.md)。

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
