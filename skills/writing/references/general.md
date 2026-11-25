**全文主线：具体问题 → 现有解释或做法留下的缺口 → 核心洞察 → 由洞察导出的设计 → 关键证据 → 新的认识或能力。** 章节内部的因果与依赖关系优先于套句、模块数量和形式上的整齐。

**1. 故事、novelty 与 insight**

- 先用一句话说清“本文发现了什么，因此能怎样解决什么问题”。全篇围绕这一中心判断展开；Abstract 压缩它，Introduction 建立理由，Method 实现它，Experiments 检验它，Conclusion 提炼它。
- **Novelty 是具体差别及其意义：** 相比最接近的工作，改变了哪项问题设定、信息需求、机制、性质或解释，因此新增什么能力。仅更换名称、拼接组件或提升一个分数，不足以解释新意；用具体比较让读者看见贡献。
- **Insight 是设计背后的认识：** 哪个观察、关系或结构解释了困难，并使某个设计成为合理选择。先讲认识，再讲操作；“我们提出一种新框架”只是贡献声明。观察可以来自数据、例子或理论，不强制另做动机实验。
- **对照示例：**
  - Insight。✗ `We propose a novel framework that combines retrieval and reranking.`（只是贡献声明）✓ `Our key insight is that most retrieval failures come from a granularity mismatch between queries and documents, not from ranking noise; aligning granularity before ranking removes the dominant error source.`
  - Novelty。✗ `Unlike prior work, our method achieves better performance.` ✓ `Unlike X, which calibrates with labeled target data, our method calibrates with unlabeled model outputs alone, so it applies to domains without annotations.`
- 挑战、设计与验证相互对应即可，不机械凑成三组。分析论文围绕研究问题与发现组织，理论论文围绕对象、性质与推论组织，数据集论文围绕能力缺口、构建原则与验证组织。

**2. 章节顺序与篇幅**

新稿默认：**Abstract → Introduction → Problem Formulation → Method → Experiments → Related Work → Conclusion → Limitations（可选）→ Ethical Considerations（可选）→ Appendix**。参考文献按模板放置。已有稿件保持原有章节顺序与标题，各节按对应章节文件的组织链承担职责；用户明确要求重组时才调整顺序。下表是经验型方法论文的起始预算，按正文占用空间估算，含归属各节的图表，不含参考文献、附录及单独计页的可选章节。

| 章节 | 起始占比 | 篇幅主要用于 |
|---|---:|---|
| Abstract | 3% | 一条完整贡献链，通常 150–250 英文词 |
| Introduction | 16% | 问题、相关工作、挑战、洞察与方法、结果，5 段加贡献列表 |
| Problem Formulation | 8% | 输入输出、可用信息与目标，通常 2–4 段 |
| Method | 28% | 核心机制、设计理由与完整使用流程 |
| Experiments | 36% | 主效果、设计验证及有价值的进一步发现 |
| Related Work | 6% | 最接近路线的定位，通常 2–3 个主题段 |
| Conclusion | 3% | 核心认识与成果，通常 1 段 |

占比合计 100%，是编辑起点，不是文献统计或会议规定。短摘要服从目标字数；理论贡献突出时增加 Method 中的分析，发现型论文增加 Experiments，数据集论文将 Method 用于构建与验证设计。优先压缩重复背景、次要变体和报数，再将长证明、配置与完整分项结果移入附录；保住解释核心设计和核心发现的空间。不要用小字号和挤间距替代内容取舍，也不覆盖官方模板的间距、字号与版式。用户给定页数时，正文最后一页接近写满；Conclusion 是正文最后一节，Limitations 等可选章节放在其后。

**3. 数字密度与信息分层**

摘要通常留 2–3 个关键结果数值；引言留 1–2 组比较；实验每个结果段留 1–2 组能说明发现的比较；结论通常不报数，必要时保留一组。参考范围（同领域已发表论文的实测，不必凑满）：8 页正文的结果值（小数、百分数）约 10–25 个；结果段一般不超过 4 个数字，含 6 个以上数字的段落全文至多一两段；贯穿全文的小例子中的算术不计入。正文说趋势、差别与意义，图表给完整值，附录给完整设置及扩展结果。正文的每个结果数字都能在正文图表中找到，或指向附录的具体表格；摘要、图、表的汇总口径一致。删减数字时保留推理步骤、定义与条件。方法中的公式参数和定义常数不按“结果数字”计数。比较须说清对象、指标与关键条件，区分百分点、相对提升和绝对差值。

**报数写法**（依据同领域 59 篇论文的正文统计）：

- 两个数的比较写 `from X to Y`（同一方法改动前后）或 `X vs. Y`，不写 `X against Y`；能用结论加图表指向说清的，句中不报数。
- `in k of N settings` 式计数只补充平均结果，实验部分用一两次；摘要和引言用平均指标，不用计数。
- 不做配对检验，也不列配对差异表；确有必要（如审稿人要求）时，附录用一段话、正文用一句话带过，不单独成表。
- 置信区间不写进正文句子，需要时放在图的误差条或阴影中。
- 机制验证、子集对比等次要诊断的数值放附录，正文只写结论并指向对应表格。

**4. 正文可读性与理论密度**

- 每节先回答一个读者问题，每段推进一个中心判断。段首给判断或目的，随后解释或举证，段末交代其作用或自然引出下一步；不要求每段都补总结句。
- 首次阅读应能沿着文字读通“为什么、做什么、得到什么”。先给直觉、例子或总览，再引入必要符号。方法类论文默认用一个贯穿全文的小例子，串联定义、性质与结果。
- **定义先于使用：** 术语、符号和图表标签在首次出现处或之前定义；靠前的 Teaser 和表格在原位置就能读懂，结果表不早于其基线和指标的定义。正文指向附录参考约 8–14 处，每处说明附录里有什么；一段通常只引用一组图表。
- **交叉引用写进句子：** 引用图、表、章节和附录时，让引用成为句子成分，不在句末加括号。✗ `We ask whether labels from other models can suffice to score its responses (Figure~\ref{fig:teaser}).` ✓ `As shown in Figure~\ref{fig:teaser}, we ask whether ...`；也可写 `Table~\ref{tab:main} reports ...`、`Section~\ref{sec:method} describes ...`、`Appendix~\ref{app:setup} lists the full configuration.`。Abstract 不含任何交叉引用；Introduction 只引用 Teaser 和一个主结果图或表，不引用 Section 与 Appendix。
- **术语、缩写与符号：** 使用领域通用术语，用词对照 baseline 与最接近的工作，不自造词，不给普通操作层层命名；同一对象保持同一名称。缩写在摘要和正文中各自第一次出现时必须展开，AUROC 等常见指标名及数据集、模型名除外；自造缩写尽量少，参考 3–5 个以内；方法名第一次出现写成 `Judge-Imitating Probe (JIP)` 的形式。一个符号只表示一个对象。
- **方法名：** 方法名指向真实机制，可读、易记，不与正文中描述其他动作的常用词同形，也不与同领域已有方法重名，命名前检索一次。正文在需要指代方法时使用方法名，不把它当作每句的主语反复出现。
- **问题名称准确：** 先检索领域是否已有通用说法，有则沿用。借用的说法若在文献中另有含义，加限定词使其准确，并在首次出现时定义该设定下哪些信息可用、哪些不可用。
- **术语字面义与实际操作一致：** 选词让读者按日常含义就能猜对操作，不用暗示排序、比较或因果的词指称并无此关系的对象。描述关键现象的词在首次使用处给出可操作的定义。
- **保留理论骨架，压缩推导负担。** 正文保留定义方法的公式、核心性质及条件，并解释它为何改变设计或结论。长证明、辅助引理、代数展开放附录。正文的定理、命题等形式化结论参考 3 个以内，其余写成非形式表述并指向附录中的正式版本，条件与附录一致；每个形式化结论前一句说明它回答的问题，后一句说明它对方法或结论意味着什么。经验型论文不为显得严谨堆定理；理论型论文保留核心证明思路，不照搬经验论文的低理论密度。
- 连续出现定义、公式、定理时，检查读者是否知道每一步的用途；需要解释就插入解释，关系简单就并入行内，避免形式化结论连续堆叠。编号公式参考每页 0–1 个。图与算法用于缩短理解路径，不能替代关键机制的文字说明。

**5. 直接、有取舍的写作**

直接写发现、操作和收益。删去无信息的自我辩护、反复让步、预演审稿人质疑和“虽然简单／有限，但仍然……”式开场。修改时不新增限定、弱化或不利说法，已有的不利说法删除；为与数据一致所做的准确改写（如 all 改为 most）不算新增限定。有解释价值的补充材料按需移入附录，不要求每项结果后附弱点。

正文只呈现最终版本：不写版本演变（v1、v2）、旧实现或旧稿的问题与修复、开发中的试错经过；实验设置只描述最终采用的协议。

保留会改变结论含义的事实与条件，并自然融入对应陈述；删掉弱结果后若“所有任务均改善”已不成立，就改写这个主张。数值、实验、引用与定理条件沿用证据。`show` 用于直接发现，`suggest` 用于解释性推断，不靠层层 `may / potentially / to some extent` 表达严谨，也不以夸大的确定性替代证据。

Abstract、Introduction、Conclusion 使用对应文件中的衔接框架；其余章节只建议语义合适的连接，不规定连接词配额。写完检查信息是否前进，删除同一贡献在相邻段落中的重复铺陈。

**6. 去除 LLM 文风**

英文正文应像领域研究者写的，而不是模型生成的。章节文件中的衔接框架不受本节限制。

- **替换空泛用词：** `delve into`、`crucial / pivotal / paramount`、`intricate`、`realm`、`landscape`、`tapestry`、`myriad`、`showcase`、`underscore`、`shed light on`、`pave the way`、`groundbreaking`、`seamless(ly)`、`it is worth noting that`、`plays a crucial role in` 改为具体陈述；`leverage / utilize` 一般写 `use`；`novel` 不反复自称；`robust`、`comprehensive`、`significantly` 只在有对应证据或统计检验时使用。
- **不用模板句式：** 不用 em dash（—）插入语，改用括号或拆句；不用 `not only ... but also`、`It is not X, but Y` 式反转；不凑三项排比或三连形容词；不在段末加 `This demonstrates the effectiveness of ...` 一类总结句；不连续用 `Moreover / Furthermore / Additionally` 开头。
- **写法朴素具体：** 主语明确，多用主动语态和 `we`；方法与结论用一般现在时，具体实验过程可用过去时。一个概念始终用同一术语，不为避免重复换同义词。一句话不要断成很多截，少用连续逗号插入语，例如写 `could not see in principle`，不写 `could not, in principle, see`。
- **少用 `let` 一类短词：** `lets X do` 改为 `allows X to do` 或 `enables X to do`，例如 ✗ `A confidence score for each response lets a system abstain` ✓ `A confidence score for each response allows a system to abstain`。数学定义中的 `Let $x$ denote ...` 不受此限。
- **连接副词不夹在句中：** `therefore`、`thus`、`hence` 不放在主语与谓语之间。确为因果推进时移到句首，✗ `We therefore ask whether ...` ✓ `Therefore, we ask whether ...`；上文已说清因果时直接删去，写 `We ask whether ...`。
