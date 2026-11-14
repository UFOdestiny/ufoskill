---
name: writing
description: Draft, restructure, polish, and compress English AI, ML, and NLP research papers by following per-section organization logic, with focus on the overall story, novelty, insight, and readability; also diagnose manuscripts and apply requested revisions. Use for paper writing, rewriting, polishing, tightening, page-limit compression, and sections such as abstract, introduction, problem formulation, method, experiments, related work, conclusion, and appendix. 撰写、重组、润色和压缩 AI、ML、NLP 英文研究论文，按章节内部逻辑组织，突出整体故事、novelty、insight 与可读性；也按用户要求诊断稿件并落实修改。
---

# Writing

论文正文一律用英文撰写；说明、诊断与修改理由跟随用户使用的语言。

**章节组织逻辑是本 skill 的核心约束。** 先读 [general](references/general.md)；写、改或诊断任一章节前，必须读取下表中该章节的文件，按其首行组织链、内容块顺序和段落内部逻辑落笔，并按语义选用其中的衔接框架。general 管全文主线与取舍，章节内部如何组织以章节文件为准。润色句子时也不能打乱所在章节的组织链。

| 章节 | 读取内容 |
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

处理对应内容时，再读 [引用](references/presentation/citations.md)、[表格](references/presentation/tables.md)、[图示](references/presentation/figures.md)。

**工作顺序**

1. 从已有材料确定核心问题、洞察、机制和主结果。
2. 对照章节文件，给每段确定它在组织链中的环节与职责：缺失的环节补上，越位的内容移到对应章节或附录，重复的环节合并。
3. 最后修改句子，并按 general 第 6 节清理 LLM 文风。

新稿按 general 中的默认章节顺序组织。已有稿件保持原有章节顺序和标题，只在章节内部按组织链调整；用户明确要求重组时才调整章节顺序。局部修改保持局部；审阅请求只给诊断，并对照章节组织链指出问题；审阅并修改则交付改稿。已有材料足够时无需另建计划文件或启动整篇审计。

缺少会改变研究含义、结果取值或主张范围的信息时，询问用户。工作稿中缺失的结果、引用或事实统一写作 `[TODO: <缺少什么>]`，例如 `[TODO: accuracy of X on Y]`、`[TODO: cite the original Z paper]`；方括号内避免 LaTeX 特殊字符，不用 `XX.X`、`??` 或编造的数值占位，修改说明中列出全部 TODO。

交付前检查：每个改动章节的段落能逐一对应其章节文件的组织链，顺序一致，没有缺失或越位的环节；故事连贯，核心设计讲清，数字与引用对应，正文能独立读懂。改动 LaTeX 后使用项目已有构建方式检查版面；无法构建时说明实际完成的检查。交付改稿和简短修改说明，不追加通用风险清单。
