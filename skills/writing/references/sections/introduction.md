# Introduction

**组织链：问题 → 相关工作及其缺口 → 挑战 → 洞察与方法 → 实验结果 → 贡献。**

必须为 5 个自然段加贡献列表：每个论证块恰好一段，按下表顺序排列；不合并相邻块，也不把一个块拆成多段。篇幅用于让读者理解“问题为什么成立、为什么难、改变为什么有价值”。只读各段首句，也应能重建主线。

## 段落结构

| 论证块 | 段落内部逻辑 | 默认衔接框架 | 参考占比 |
|---|---|---|---:|
| 问题，第 1 段 | 研究背景 → 研究对象的用途 → 现有主流做法（一句）→ 现实约束 → 现有做法因此无法解决（一句）→ 本文研究的问题 | `[研究对象] ... . However, ... , so ... cannot ... . Hence, in this paper, we study/focus on ... .` | 10% |
| 相关工作，第 2 段 | 首句给出现有方法的分类 → 逐类介绍代表做法 → 末句以 However 指出这些方法没有解决的问题 | `Existing approaches to ... fall into [N] categories: ... and ... .` / `Although many approaches have been proposed for ... , they fall into ... .`；末句 `However, these methods ... .` | 20% |
| 挑战，第 3 段 | 解决上述缺口要克服什么 → 困难从何而来 → 为什么直接扩展现有方法不够 | `Addressing ... is challenging because ... .` / `The key challenge is that ... .` | 15% |
| 洞察与方法，第 4 段 | 以洞察引出方法 → 必要的例子或定义讲清洞察 → 按挑战逐一给出设计 → 必要的理论保证及其条件 | `Motivated by our key insight that ... , we propose ... , a framework that ... . [洞察的例子或定义] ... . First, ... . Second, to address ... , ... .` | 30% |
| 实验结果，第 5 段 | 评估覆盖什么 → 主要结果及关键数值 → 按重要性递进的补充结果 | `We extensively evaluate ... on ... .`；补充用 `Moreover, ... .`，最重要的补充用 `More importantly, ... .` | 15% |
| 贡献列表 | 概念新意 → 技术新意 → 实验效果 | 固定起首词见下文“贡献列表” | 10% |

## 各段要求

- **问题段收束到研究问题：** 先交代背景和研究对象为何有用，再用一句概括现有主流做法，接 `However` 说明现实约束，然后用一句说明现有做法为何因此无法解决（如它依赖的信息或资源在该场景中不可得），最后以 `Hence, in this paper, we study/focus on/investigate ...` 点明本文问题，使研究这个问题成为前文的直接推论，而不是突然转到本文。不用 `We ask whether ...` 引出问题。
- **相关工作段要有分类：** 首句用一句话给出最相关路线的分类，随后每类用一两句介绍代表做法并就近引用，末句用 `However, these methods ...` 点明它们共同没有解决的问题。末句的缺口必须对每一类都成立；某类本来就不存在该问题时，按类分别写出不足，不把一项不足笼统地套到所有类别上。说清现有方法为何留下这个问题，不写“很少有人研究”或笼统的“现有方法均不足”；互补或新任务也能构成贡献，不能虚构前人失败。对比最接近的工作即可，不提前写一篇 Related Work；分类与 Related Work 保持一致。
- **挑战与缺口分工：** 第 2 段末句说“还没解决什么”，第 3 段说“为什么难解决”，后者不复述前者。挑战来自问题设定本身，是任何方法都要面对的障碍，不写本方法自己的实现细节；写成具体的技术或信息障碍，每项挑战用一个例子或一句原因讲清，使第 4 段能写明各设计与它的对应关系。只有一个挑战时用单数 `challenge`，多个时写 `the above challenges`。
- **洞察与方法合为一段，突出新意：** 洞察不单独成段，以 `Motivated by our key insight that ... , we propose ...` 开头，让洞察直接成为方法新意的一部分。洞察是一句可理解的判断，把“挑战为何存在”连到“新做法为何可行”，例如先区分所需信息与表面信号；不能把组件组合本身称为洞察。需要时紧接一两句例子或定义讲清洞察。随后用一句说明方法是什么框架，再按挑战逐一给出设计（`First, ... Second, to address ... , ...`）：每个设计说明利用了洞察的哪一部分、解决哪项挑战。设计数与挑战数不必相等；不一一对应时（如两个设计分担同一挑战的不同部分，或一个设计应对两项挑战），必须明确写出每个设计应对哪项挑战的哪一部分，以及多个设计之间的关系（互补、替代或先后），不让读者自行拼对。设计名称与总览图及 Method 小节的模块名相同。有理论保证时，用一句写明结论及成立条件。这一段是引言中篇幅最大的段落，要让读者看出技术新意，不能写成组件的简单拼接；公式推导、完整模块配置与算法步骤留到 Method。
- **Teaser 的引用：** 有 Teaser 时必须在引言中引用。默认在问题段点明约束处写 `As illustrated in Figure~X, ...`；Teaser 主要展示洞察时，改在第 4 段讲清洞察的例子处引用；按子图分别讲问题和机制时，可在这两处分别引用对应子图。
- **结果段有层次：** 有方法性能比较时，用 `We extensively evaluate ... on ...` 如实交代评估范围，给出主结果的关键数值，再用 `Moreover` 补充、用 `More importantly` 标出最能说明价值的结果，让读者看出主次。没有此类比较时，本段写主要发现或性质及其意义。报数数量见[数字](../style/numbers.md)。

## 贡献列表

必须为三条，分别以 `Conceptually,`、`Technically,`、`Empirically,` 开头。

- **Conceptually** 是高层的概念归类：从概念上说明本文的问题或方法新在哪里，例如从一个新的角度切入问题、重新界定任务或所需信息；不写具体模块。可写成 `whereas most existing work ... , we ...`。类比：别人都用 GPS 定位，我们用蓝牙定位。示例：`Conceptually, whereas most existing work treats retrieval granularity as a fixed property of the corpus, we treat it as a property of each query.`实验中观察到的现象属于 Technically 或 Empirically，不放在这一条。
- **Technically** 说明方法层面的 novelty：明确写出一两项技术新意，各自用读者能直接理解的动作描述“方法做了什么”，并点出与已有做法的关键区别（如 `without ...`、`instead of ...`）；理论保证用通俗的条件表述其结论。不堆叠名词短语、未定义术语和插入语式的拗口结构。示例：`Technically, GAR selects a passage length for each query before ranking, instead of ranking fixed-length chunks.`
- **Empirically** 用数值说明方法效果：给出相对最强基线的总体提升，可覆盖 2–3 个方面（如主设置、泛化或迁移、效率或决策收益），每个方面一个数，报数写法见[数字](../style/numbers.md)。在真实且公平的比较中选最有说服力的角度，例如“不用某种信息却胜过使用该信息的强基线”。比较对象必须确为同类条件下最强者，限定词写清（如 `the strongest baseline at the same cost`），不能以弱基线冒充最强。
- 三条篇幅大致均衡，每条一句，参考 30–45 个英文词。不复述方法段和结果段的细节；三条不能把同一方法换说法写三次；保留原有方法名。
- 分析、理论、数据集论文同样使用这三条，Empirically 写证据揭示的主要发现。按实际贡献填写，不编造；某类确无内容时询问用户。

## 衔接

问题与缺口用 `However`，原因用 `because`，例子用 `For example`，约束到本文问题用 `Hence / Therefore`（置于句首），洞察与方法合写为 `Motivated by our key insight that ... , we propose ...`，方法展开用 `Specifically`，证据用 `Experiments ... show`。每个连接只承担其真实逻辑，不在各段重复“挑战很大，因此我们提出”。

引言的交叉引用限制见[交叉引用](../style/cross-references.md)：读者应一遍读懂引言，不为理解某句而跳到后文的复杂图表。贡献列表结束后直接进入下一节。
