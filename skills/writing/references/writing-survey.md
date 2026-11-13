# 写作架构文献调查

调查日期：2026-11-13。选取 **27 篇已发表论文**：ICLR 7、ICML 6、NeurIPS 6、ACL 主会 6；另加 EMNLP 2 篇，与语言模型不确定性和表示学习直接相关，单独标注。优先选择已有影响力的工作，再补充与当前写作需求紧密相关的论文；没有把预印本、Findings 或其他会议混计为四个主会样本。

本次读取正文结构与关键段落，重点对照问题、洞察、方法定义、实验展开和正文／附录分工。ICML、NeurIPS、ACL、EMNLP 及 confidence elicitation 的全文来自官方论文集；6 篇 OpenReview PDF 受访问限制的 ICLR 论文改读作者 arXiv 全文，发表身份另以会议／作者出版记录核实。表中链接指向发表记录，文末列出所读作者版本；不将作者版本一概称为 camera-ready。

引用数为 **OpenAlex 单条匹配记录的 cited_by_count 快照**，查询日期同上；链接可追到对应记录。未合并不同版本，也不等同于 Google Scholar。它只辅助挑选，不衡量写作质量；与主题直接相关的少引用论文仍保留。没有精确匹配的记录留空。表内“观察”来自原文，“采用方式”是此次编辑判断；本调查未统计会议全体论文的词数、页数或公式数。

## 逐篇结构依据

| 论文／会议 | 引用快照 | 原文定位与结构观察 | 本次采用方式 |
|---|---:|---|---|
| [LoRA: Low-Rank Adaptation of Large Language Models](https://openreview.net/forum?id=nZeVKeeFYf9) · ICLR 2022 | [14,504](https://openalex.org/W3168867926) | §2、§4、§5、§7：问题定义后展开低秩更新及在 Transformer 中的使用，主效果与秩的分析分开。 | 机制先完整讲清；性质与设计分析提供额外解释，不塞进背景。 |
| [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://openreview.net/forum?id=1PL1NIMMrw) · ICLR 2023 | [5,574](https://openalex.org/W4221161695) | §2、§3.2–3.5、§5、附录 A：用多条推理路径汇合到答案的直觉引出采样与聚合；主结果之后比较其他解码路线并分析稳健性。 | 方法可短而完整，实验顺序应围绕主张而非照抄任务清单。 |
| [ReAct: Synergizing Reasoning and Acting in Language Models](https://openreview.net/forum?id=WE_vluYUL-X) · ICLR 2023 | [5,870](https://openalex.org/W4304195432) | §2、§3–4、§6：先定义智能体交互再引入推理动作；知识任务与决策任务分别给设置和发现。 | 先解释信息与行为的关系，异质任务可分组展开，不强求一套统一 Setup。 |
| [Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation](https://openreview.net/forum?id=VD-AYtP0dve) · ICLR 2023 | [725](https://openalex.org/W4321594373) | §3、§4、§4.1、附录 A：先分解语义等价、采样空间、长度带来的困难，再介绍采样、聚类与熵估计，并回扣挑战。 | 洞察先解释错位在哪里，方法逐步改变处理对象；挑战与设计要能互相追溯。 |
| [Conformal Language Modeling](https://openreview.net/forum?id=pzUhfQ74c5) · ICLR 2024 | [118](https://openalex.org/W4381551003) | §3–4、§5–6、附录 A–F：方法总览先给采样、拒绝与停止过程，再形式化设置及校准；主要保证与算法相邻。 | 让读者先理解流程，理论紧接其支持的设计，保留条件与实际含义。 |
| [Calibrating Sequence likelihood Improves Conditional Language Generation](https://openreview.net/forum?id=0qSOodKmJaN) · ICLR 2023 | [79](https://openalex.org/W4302010020) | §2、§3.3 及后续实验：先说明训练后的校准阶段，再展开相似性、校准损失、正则化与候选生成；实验较早安排消融。 | 步骤依赖要可读；当设计解释是核心时，消融可以先于完整主表。 |
| [Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/hash/6733cf15e10e2cd1d59af033c3bb8507-Abstract-Conference.html) · ICLR 2024 | 未精确匹配 | §3、§5.1–5.4、附录 A/B/E/F：用提示、采样、聚合三个维度组织方法空间；分析小节标题直接陈述发现；证明、结果、设置、提示词分附录。 | 发现型论文可用发现式标题；正文理论密度按贡献决定，附录按用途拆分。 |
| [On Calibration of Modern Neural Networks](https://proceedings.mlr.press/v70/guo17a.html) · ICML 2017 | [4,171](https://openalex.org/W2626967530) | §2–5、§6：先定义校准，再观察失校准及影响因素，之后讨论校准方法和比较结果。 | 现象→解释→处理的故事可替代常规算法先行；先说清评价对象。 |
| [Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning](https://proceedings.mlr.press/v48/gal16.html) · ICML 2016 | [7,187](https://openalex.org/W582134693) | §3–4、§5.1–5.4、§6：先建立 dropout 的概率解释，再推导如何取得预测不确定性，实验从行为展示走向预测与决策使用。 | 理论须接到可用计算与实际作用，不能只展示等式；结论收束解释及用途。 |
| [A Simple Framework for Contrastive Learning of Visual Representations](https://proceedings.mlr.press/v119/chen20j.html) · ICML 2020 | [11,960](https://openalex.org/W3005680577) | §2、§3–6、§8：框架先建立；后续以增强、编码器／投影头、损失与训练规模逐项研究设计作用。 | 机制分析可以成为主要叙事，篇幅给改变理解的设计因素。 |
| [Learning Transferable Visual Models From Natural Language Supervision](https://proceedings.mlr.press/v139/radford21a.html) · ICML 2021 | [19,258](https://openalex.org/W3135367836) | §2.1–2.5、§3：依次说明数据、预训练目标、模型、训练与使用，分析区分零样本迁移及表示能力。 | Method 必须闭合到使用方式；不同能力分开定义和验证。 |
| [Parameter-Efficient Transfer Learning for NLP](https://proceedings.mlr.press/v97/houlsby19a.html) · ICML 2019 | [2,643](https://openalex.org/W2913946806) | §2–3：先介绍适配模块与训练，再比较参数／性能关系并分析模块位置和容量。 | 资源收益需要与质量共同呈现；新增模块获得主要解释篇幅。 |
| [Calibrate Before Use: Improving Few-shot Performance of Language Models](https://proceedings.mlr.press/v139/zhao21c.html) · ICML 2021 | [711](https://openalex.org/W3132736064) | §2–5：先展示少样本提示的不稳定性，再分析偏置来源，随后用无内容输入估计偏置并进行校准。 | 让观察解释设计，不把 motivation 写成领域背景；相似术语需定义准确。 |
| [Attention is All you Need](https://papers.nips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html) · NeurIPS 2017 | [136,318](https://openalex.org/W2626778328) | §3、§4、§5–6、§7：架构从整体到注意力等子结构；另节比较自注意力的性质，再给训练与结果。 | 总览先于细节，解释为什么选择机制；不照搬其每个标准组件的篇幅。 |
| [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://papers.nips.cc/paper_files/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html) · NeurIPS 2020 | [6,197](https://openalex.org/W3027879771) | §2.1–2.5、§3–4、§5：总览检索与生成后定义两个模型，再补训练和解码；任务实验之后给相关工作。 | 按计算依赖展开方法，最终输出流程明确；Related Work 放后部也能成立。 |
| [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://papers.nips.cc/paper_files/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html) · NeurIPS 2022 | [14,051](https://openalex.org/W7133224126) | §2–5、§6：用实例界定思维链，再按算术、常识和符号任务展示能力，另节讨论相关研究。 | 具体例子可以承担方法直觉，任务族应服务能力主张。 |
| [Training language models to follow instructions with human feedback](https://papers.nips.cc/paper_files/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract-Conference.html) · NeurIPS 2022 | [8,088](https://openalex.org/W4226278401) | §3.1–3.5、§4、§5：先给总体训练过程，再说明数据、人类反馈、模型和评价；结果用发现领起段落。 | 训练信号的来源属于理解方法的必要信息；结果段以发现而非表号为中心。 |
| [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://papers.nips.cc/paper_files/paper/2023/hash/a85b405ed65c6477a4fe8302b5e06ce7-Abstract-Conference.html) · NeurIPS 2023 | [3,139](https://openalex.org/W7133208539) | §3–5、§6.1–6.3、§7：预备知识引出目标重参数化，理论分析解释方法；实验明确询问目标优化、真实偏好数据及迁移。 | 关键推导解释机制，研究问题形成证据链；不要强制所有论文低理论密度。 |
| [QLoRA: Efficient Finetuning of Quantized LLMs](https://papers.nips.cc/paper_files/paper/2023/hash/1feb87871436031bdc0f2beaa62a049b-Abstract-Conference.html) · NeurIPS 2023 | [4,064](https://openalex.org/W7133233472) | §2–3、§4–5、§6–7、附录：先交代量化与低秩基础，再解释关键技术；先验证低比特微调，再研究聊天模型。 | 验证前提后再扩展应用；多项技术要连到同一个资源与质量目标。 |
| [Prefix-Tuning: Optimizing Continuous Prompts for Generation](https://aclanthology.org/2021.acl-long.353/) · ACL 2021 | [4,645](https://openalex.org/W3174770825) | §3、§4.1–4.3、§5–7：Problem Statement 定义任务与模型；Method 明确先 Intuition 再 Method 与参数化；实验覆盖主结果及分析。 | 问题定义与解决方案分工明确，直觉→形式化→训练安排可直接复用。 |
| [BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://aclanthology.org/2020.acl-main.703/) · ACL 2020 | [11,472](https://openalex.org/W2982399380) | §2–3、§4–5：先介绍模型及去噪目标，再说明各类任务如何使用；先比较预训练目标，再呈现规模化结果。 | 方法必须解释训练目标与实际使用的关系，实验回答具体设计问题。 |
| [TruthfulQA: Measuring How Models Mimic Human Falsehoods](https://aclanthology.org/2022.acl-long.229/) · ACL 2022 | [2,812](https://openalex.org/W3201174429) | §2.1–2.3、§3、附录：先定义何为真实，再说明数据构建和独立验证；实验区分模型、提示、任务与评价。 | 数据集论文的 Method 重点是定义、构建和验证，不强行编出算法模块。 |
| [Large Language Models Are Reasoning Teachers](https://aclanthology.org/2023.acl-long.830/) · ACL 2023 | [403](https://openalex.org/W4385571219) | §3、§4.1–4.2、§5–8、附录 A–G：先给教师生成与学生训练流程；实验沿多种规模轴分析，再讨论使用与取舍，附录按材料类型展开。 | 效率与规模分析围绕同一问题，不机械套固定数量的研究问题。 |
| [Universal Language Model Fine-tuning for Text Classification](https://aclanthology.org/P18-1031/) · ACL 2018 | [5,169](https://openalex.org/W2798812533) | §3.1–3.3、§4–5、§7：方法按通用预训练、目标任务语言模型适配、分类器训练推进，再用实验与分析解释效果。 | 按阶段依赖写方法，每一步说明前一步输出如何继续使用。 |
| [Get To The Point: Summarization with Pointer-Generator Networks](https://aclanthology.org/P17-1099/) · ACL 2017 | [3,985](https://openalex.org/W2606974598) | §2.1–2.3、§6–7、§8：从基础模型到指针生成、覆盖机制，分别针对内容复制和重复问题；结果之外分析摘要行为。 | 每个新设计对应明确困难；结果还可以回答模型究竟改变了什么行为。 |
| [SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models](https://aclanthology.org/2023.emnlp-main.557/) · EMNLP 2023 | [1,479](https://openalex.org/W4389520749) | §3–5、§6–7、附录：先区分模型访问条件，再介绍一致性评估变体；句子检测与段落排序分开评价。 | 信息条件先讲清，方法变体与评价目标分层；这是 EMNLP 补充样本。 |
| [SimCSE: Simple Contrastive Learning of Sentence Embeddings](https://aclanthology.org/2021.emnlp-main.552/) · EMNLP 2021 | [3,892](https://openalex.org/W3156636935) | §2–5、§6–9、附录 A–G：背景后依次给无监督／监督方案，再用表示几何解释，实验、分析与相关工作职责分开。 | 主要方法、解释与证据互相承接；这是 EMNLP 补充样本。 |

## 落入写作规范的取舍

- **General：** 用问题—洞察—设计—证据的关系统领文章，而非堆“贡献点”。各论文的理论与实验比重差异很大，故当前 3/16/8/28/36/6/3 的预算是可调整的编辑起点，不能说成顶会统计均值。
- **Abstract 与 Introduction：** 提取“缺口为何出现、认识如何改变设计”的推进关系；部分优秀摘要方法先行、部分观察先行，故保留功能顺序而允许合句合段。`Conceptually / Technically / Empirically` 是本项目偏好，不是这些论文共同使用的模板。
- **Problem Formulation：** 以 Prefix-Tuning、校准研究中的任务定义为依据，把原 Preliminary 的背景重心改成对象、信息、目标。基础知识只保留理解目标和方法所需部分。
- **Method：** Prefix-Tuning 的直觉先行、RAG／ULMFiT 的流程依赖、DPO／Conformal LM 的理论连接共同支持“全貌→设计→求解→使用”。保留关键推理，完整证明与辅助推导移附录；不设统一公式上限。
- **Experiments：** DPO 的问题式实验、confidence elicitation 的发现式标题、SimCLR 的机制分析均可成立。统一的是“问题→发现→证据→解释”，不统一标题形式与实验数量。每段 1–2 组数字是阅读负担上的建议，并非对样本逐段统计的结果。
- **Related Work：** 优先综合与定位，可以写继承、互补与新设定；不要求每段找前人缺陷。论文中的位置并不一致，本项目采用用户指定的实验之后顺序。
- **Conclusion 与可选章节：** 结论收束核心认识、机制和发现，不重复贡献列表。局限与伦理按研究和目标要求设置，不因为某篇范例有一节就套用其内容。
- **Appendix：** 从提示词、设置、证明和额外结果的实际分工提炼导航原则，不把某一篇的附录字母顺序推广为通用标准。

**未照搬的写法：** 夸张优先权声明、领域热度开场、组件名称堆叠、逐表报数、重复自我让步，以及与主线无关的局限。论文被录用或引用高，只说明它适合作为研究样本，不使其中每种表达都成为推荐写法。去防御性通过删冗余、直述条件实现；实验记录与结论含义保持一致。

## 作者全文与发表身份补充

- lora：[本次读取的作者全文](https://arxiv.org/pdf/2106.09685)。发表身份见 [Microsoft Research 的 ICLR 2022 记录](https://www.microsoft.com/en-us/research/publication/lora-low-rank-adaptation-of-large-language-models/)。
- self-consistency：[本次读取的作者全文](https://arxiv.org/pdf/2203.11171)。所读全文首页标注对应 ICLR 会议年份。
- react：[本次读取的作者全文](https://arxiv.org/pdf/2210.03629)。所读全文首页标注对应 ICLR 会议年份。
- semantic：[本次读取的作者全文](https://arxiv.org/pdf/2302.09664)。所读全文首页标注对应 ICLR 会议年份。
- conformal：[本次读取的作者全文](https://arxiv.org/pdf/2306.10193)。所读全文首页标注对应 ICLR 会议年份。
- slic：[本次读取的作者全文](https://arxiv.org/pdf/2210.00045)。发表身份见 [ICLR 2023 论文记录](https://openreview.net/pdf?id=0qSOodKmJaN)；作者版未标注正式会议页眉。
