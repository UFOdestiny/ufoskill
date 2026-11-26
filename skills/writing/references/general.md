# 全文规范

本文件管全文主线、章节分工与内容取舍。章节内部如何组织见各章节文件，句子与表达见 style。

## 全文主线

**具体问题 → 现有解释或做法留下的缺口 → 核心洞察 → 由洞察导出的设计 → 关键证据 → 新的认识或能力。**

- 必须能用一句话说清“本文发现了什么，因此能怎样解决什么问题”。全篇围绕这一中心判断展开：Abstract 压缩它，Introduction 建立理由，Method 实现它，Experiments 检验它，Conclusion 提炼它。
- 章节内部的因果与依赖关系优先于套句、模块数量和形式上的整齐。
- 挑战、设计与验证相互对应，数量随实际内容决定，不为凑成三组而拆分或合并。数量不必一一相等：一个设计可同时应对多项挑战，多个设计也可分担同一挑战的不同部分；不一一对应时，必须写明哪个设计应对哪项挑战的哪一部分。章节文件另有数量规定的（如 Introduction 的 5 段与三条贡献、Teaser 与 Experimental Results 图默认三个面板），按其规定执行。
- 论文类型决定主线的落点：方法论文围绕挑战、设计与验证；分析论文围绕研究问题与发现；理论论文围绕对象、性质与推论；数据集论文围绕能力缺口、构建原则与验证。

## Novelty 与 insight

- **Novelty 是具体差别及其意义：** 相比最接近的工作，改变了哪项问题设定、信息需求、机制、性质或解释，因此新增什么能力。仅更换名称、拼接组件或提升一个分数，不足以说明新意；用具体比较让读者看见贡献。
- **Insight 是设计背后的认识：** 哪个观察、关系或结构解释了困难，并使某个设计成为合理选择。先讲认识，再讲操作；“我们提出一种新框架”只是贡献声明。观察可以来自数据、例子或理论，不强制另做动机实验。

| | ✗ | ✓ |
|---|---|---|
| Insight | `We propose a novel framework that combines retrieval and reranking.`（只是贡献声明） | `Our key insight is that most retrieval failures come from a granularity mismatch between queries and documents, not from ranking noise; aligning granularity before ranking removes the dominant error source.` |
| Novelty | `Unlike prior work, our method achieves better performance.` | `Unlike X, which ranks fixed-length chunks, GAR re-segments each document to match the query's granularity before ranking, so it retrieves evidence that fixed chunking splits apart.` |

## 章节顺序与篇幅

新稿默认顺序：**Abstract → Introduction → Problem Formulation → Method → Experiments → Related Work → Conclusion → Limitations（可选）→ Ethical Considerations（可选）→ Appendix**。参考文献按模板放置。Conclusion 是正文最后一节，可选章节放在其后。

下表是经验型方法论文的参考起始预算，按正文占用空间估算，含归属各节的图表，不含参考文献、附录及单独计页的可选章节。

| 章节 | 参考占比 | 篇幅主要用于 |
|---|---:|---|
| Abstract | 3% | 一条完整贡献链，参考 150–250 英文词 |
| Introduction | 16% | 问题、相关工作、挑战、洞察与方法、结果，5 段加贡献列表 |
| Problem Formulation | 8% | 输入输出、可用信息与目标，参考 2–4 段 |
| Method | 28% | 核心机制、设计理由与完整使用流程 |
| Experiments | 36% | 主效果、设计验证及有价值的进一步发现 |
| Related Work | 6% | 最接近路线的定位，参考 2–3 个主题段 |
| Conclusion | 3% | 核心认识与成果，默认 1 段 |

- 预算是编辑起点，不是文献统计或会议规定。短摘要服从目标字数。理论贡献突出时增加 Method 中的分析，发现型论文增加 Experiments，数据集论文将 Method 用于构建与验证设计。
- **压缩顺序：** 先压缩重复背景、次要变体和报数，再将长证明、配置与完整分项结果移入附录；保住解释核心设计和核心发现的空间。
- 不能用小字号和挤间距替代内容取舍，也不能覆盖官方模板的间距、字号与版式。
- 用户给定页数时，正文默认写到最后一页接近写满。

## 正文与附录分工

正文必须能独立成立：读者不看附录也能理解方法、核心性质及主结果。长证明、工程设置、完整分项结果与次要分析放附录；决定结论成立范围的条件随正文结论出现，附录负责展开。

## 内容取舍

- **直接写：** 直接写发现、操作和收益。删去无信息的自我辩护、反复让步、预演审稿人质疑和“虽然简单／有限，但仍然……”式开场。
- **不利内容：** 修改时不新增限定、弱化或不利说法；已有的不利说法删除。为与数据一致所做的准确改写（如 all 改为 most）不算新增限定。有解释价值的补充材料按需移入附录，不要求每项结果后附弱点。
- **主张跟随证据：** 保留会改变结论含义的事实与条件，并自然融入对应陈述；删掉弱结果后若“所有任务均改善”已不成立，就改写这个主张。数值、实验、引用与定理条件沿用证据。
- **只呈现最终版本：** 不写版本演变（v1、v2）、旧实现或旧稿的问题与修复、开发中的试错经过；实验设置只描述最终采用的协议。
- **信息前进：** 写完检查每段是否带来新信息，删除同一贡献在相邻段落中的重复铺陈。

## 阅读路径

- 每节先回答一个读者问题，每段推进一个中心判断。段首给判断或目的，随后解释或举证，段末交代其作用或自然引出下一步；不要求每段都补总结句。
- 首次阅读应能沿着文字读通“为什么、做什么、得到什么”。先给直觉、例子或总览，再引入必要符号。方法类论文默认用一个贯穿全文的小例子，串联定义、性质与结果。
- Abstract、Introduction、Conclusion 默认使用各自章节文件中的衔接框架；其余章节的连接词只是可选建议，按语义选用，没有配额。
