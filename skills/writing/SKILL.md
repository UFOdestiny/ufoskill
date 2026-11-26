---
name: writing
description: Draft, restructure, polish, and compress English AI, ML, and NLP research papers by following per-section organization logic, with focus on the overall story, novelty, insight, and readability; also diagnose manuscripts and apply requested revisions. Use for paper writing, rewriting, polishing, tightening, page-limit compression, sections such as abstract, introduction, problem formulation, method, experiments, related work, conclusion, and appendix, and the figures, tables, and citations that support the text. 撰写、重组、润色和压缩 AI、ML、NLP 英文研究论文，按章节内部逻辑组织，突出整体故事、novelty、insight 与可读性；也按用户要求诊断稿件并落实修改，涵盖配套的图、表与引用。
---

# Writing

论文正文必须用英文撰写；说明、诊断与修改理由跟随用户使用的语言。

**章节组织逻辑是本 skill 的核心约束：** 写、改、润色或诊断任一章节，都按章节文件的组织链、内容块顺序和段落内部逻辑落笔。

## 规则强度

| 用词 | 含义 |
|---|---|
| **必须**、**不能**，以及未加强度词的直接要求（含“不……”句） | 硬性要求，交付前逐项核对 |
| **默认**、**优先** | 没有其他指示时采用；用户要求、目标会议或模板规定可以改变，论文实际内容明显不适合时也可调整 |
| **参考** | 经验数值或比例，是编辑起点；按论文实际内容浮动，不为凑数改写 |
| **可**、**可选** | 允许的做法，按需要选用 |

- “不必”“无需”“不要求”“不强制”表示允许省略，不是禁止。
- 衔接框架表中标为“默认”的句式，在正文要求中再次出现时仍按默认处理。
- 硬性要求只因用户明确要求或会议硬性规定（如页数、匿名、必需章节）而改变；规则自身写明的例外按该条执行。
- 各文件的英文示例默认围绕一个虚构方法 Granularity-Aligned Retrieval（GAR）：它在排序前把文档切成与查询粒度匹配的段落。示例只演示写法，不代表要求的内容。

## 文件分工

| 位置 | 负责什么 |
|---|---|
| [general](references/general.md) | 全文主线、novelty 与 insight、章节顺序与篇幅、内容取舍 |
| `references/sections/` | 各章节的行文逻辑：组织链、段落职责与顺序、衔接框架。章节内部如何组织以章节文件为准 |
| `references/style/` | 跨章节的表达规范：句子、术语、数字、交叉引用、公式与理论 |
| `references/presentation/` | 图、表、文献引用本身的内容与格式。正文如何提及图表属于 style 的交叉引用 |

**章节文件**

| 章节 | 文件 |
|---|---|
| Abstract | [摘要](references/sections/abstract.md) |
| Introduction | [引言](references/sections/introduction.md) |
| Problem Formulation | [问题定义](references/sections/problem-formulation.md) |
| Method | [方法](references/sections/method.md) |
| Experiments | [实验](references/sections/experiments.md) |
| Related Work | [相关工作](references/sections/related-work.md) |
| Conclusion | [结论](references/sections/conclusion.md) |
| Limitations，可选 | [局限](references/sections/limitations.md) |
| Ethical Considerations，可选 | [伦理考量](references/sections/ethical-considerations.md) |
| Appendix | [附录](references/sections/appendix.md) |

**表达与呈现文件**

| 文件 | 内容 |
|---|---|
| [语言](references/style/language.md) | 句子写法、主张措辞、去除 LLM 文风 |
| [术语](references/style/terminology.md) | 术语、方法名、缩写、符号、定义先于使用 |
| [数字](references/style/numbers.md) | 各位置的报数数量、报数写法、统计表述 |
| [交叉引用](references/style/cross-references.md) | 图、表、章节、附录的引用写法与各章节限制 |
| [公式与理论](references/style/math.md) | 公式、定理与理论密度 |
| [图](references/presentation/figures.md) | Teaser、Framework、结果图的内容、面板与图注 |
| [绘图规格](references/presentation/figure-drawing.md) | 字体、线条、坐标、配色与箭头 |
| [表格](references/presentation/tables.md) | 表格组织、表注与版式 |
| [引用](references/presentation/citations.md) | 文献引用与 BibTeX 核验 |

## 读取范围

- 每个任务必须先读 general。
- **整节任务**（撰写、重写、润色或诊断整节）：读取该章节文件和 style 下全部文件。
- **局部任务**（改写、润色或诊断部分段落）：读取所在章节文件、语言和术语；本次处理的内容含结果数字、图表／章节／附录的提及、公式或定理时，再分别读取数字、交叉引用、公式与理论。
- **全文任务**（整篇撰写、修改、压缩或诊断）：读取 general、稿件涉及的全部章节文件、style 下全部文件，以及图、表格、引用。
- **presentation：** 撰写、修改或核对图表内容、图注或表注，或新增、修改、核验文献引用时，读取对应文件；正文只是提及图表时按交叉引用处理。只有生成或修改图像本身时才读绘图规格。
- 读取被截断时必须补读缺失部分。
- 章节表外的非标准章节（如 Data-Driven Findings、Discussion）按其实际内容组织，对照 general 与 style。

## 工作流程

1. 从已有材料确定核心问题、洞察、机制和主结果。
2. 对照章节文件，给每段确定它在组织链中的环节与职责：缺失的环节补上，越位的内容移到对应章节或附录，重复的环节合并。
3. 最后按 style 修改句子。

- **章节顺序：** 新稿按 general 中的默认顺序组织。已有稿件保持原有章节顺序和标题，只在章节内部按组织链调整；用户明确要求重组时才调整章节顺序。
- **局部保持局部：** 只改用户指定的范围。润色只改句子，同时落实所改段落涉及的章节硬性要求；不移动、合并或拆分段落，不打乱所在章节的组织链。需要移动、合并或拆分段落才能落实的硬性要求（含润色时发现的缺失或越位环节），以及范围外发现的问题，在修改说明中列出，不擅自修改。
- **审阅与交付：** 审阅请求只给诊断，对照章节组织链指出问题；审阅并修改则交付改稿。默认只交付一版，用户要求时才给多个候选。已有材料足够时，无需另建计划文件或启动整篇审计。
- **篇幅：** 用户未说明时，改后篇幅与原文相近，且不能超出原有页数限制。用户要求按篇幅调整时，先按用户要求和模板确定哪些部分计入限额，满足页数后再参照 general 的章节预算逐节调整；每轮编译后按同一口径计页，交付时说明实际计入的页数。

## 证据与缺失信息

- 缺少会改变研究含义、结果取值或主张范围的信息时，询问用户。
- 工作稿中缺失的结果、引用或事实必须写作 `[TODO: <缺少什么>]`，例如 `[TODO: accuracy of X on Y]`、`[TODO: cite the original Z paper]`。方括号内不用 LaTeX 特殊字符；不能用 `XX.X`、`??` 或编造的数值占位。修改说明中列出全部 TODO。
- **结果数字核对：** 新增或改写正文中的结果数字时，必须能追溯到结果文件、生成代码或稿中已有的结果表；相对提升可由同一口径的表值复算。新增或修改表中数值，或用户要求核验结果时，必须对照结果文件或生成代码。用户仅要求核验时，在核验说明中列出错误及无法追溯的数值，保留原稿；任务包含改稿时，在授权范围内改正错误值，删除无法追溯的数值。纯语言润色保留原值；发现与稿中表格不一致时，在修改说明中列出。当前改动依赖的结果无法确定、又未提供结果文件或代码时，询问用户。

## 交付核对

- **按改动范围核对：** 全文或整节任务逐节核对，每个改动章节对照 general、其章节文件及本次读取的 style 与 presentation 文件复核（表外章节对照 general 与 style）：段落能逐一对应组织链，顺序一致，没有缺失或越位的环节，硬性要求均已落实。局部任务核对本次处理的段落在组织链中的职责及其与相邻段落的衔接。未完成核对，不能声称已按本 skill 完成。
- 同时确认故事连贯，核心设计讲清，数字与引用对应，正文能独立读懂。
- 改动 LaTeX 后，使用项目已有的构建方式检查版面；无法构建时说明实际完成了哪些检查。
- 交付改稿和简短修改说明，不追加通用风险清单。

## 可选模块

仅在用户明确要求时使用。

- **独立 A/B 盲评：** 由独立 agent 只阅读同一段落修改前后的文本，随机标为 A、B；不提供修改意图、对话历史或倾向性描述，用中立提示判断哪版作为研究论文文本更好，并简述理由。修改版胜出才保留，否则调整后再评，可迭代数轮；仍不胜出则保留原文。数字更正与用户指定的改动不受盲评否决。
- **首次阅读者评审：** 由独立 agent 只阅读编译后的 PDF，不看源码和对话历史，按首次阅读的顺序回答“第一次读在哪里卡住”：逐处给出页码、位置和原因（如未定义的术语、符号或图表标签，跳过的推理，过密的数字）。按反馈修改后可再评。
