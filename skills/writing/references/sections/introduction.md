**引言组织：问题 → 相关工作及其缺口 → 挑战 → 洞察 → 方法 → 实验结果 → 贡献。**

固定为 6 个自然段加贡献列表，每个论证块恰好一段，按下表顺序排列；不合并相邻块，也不把一个块拆成多段。篇幅用于让读者理解“问题为什么成立、为什么难、改变为什么有价值”。

| 论证块 | 段落内部逻辑 | 优先衔接框架 | 参考占比 |
|---|---|---|---:|
| 问题，第 1 段 | 研究对象与用途 → 具体困难 → 解决后的价值 | `[研究对象] ... . However, ... .`；只有确有后果才接 `Consequently, ... .` | 10% |
| 相关工作，第 2 段 | 首句给出现有方法的分类 → 逐类介绍代表做法 → 末句以 However 指出这些方法没有解决的问题 | `Existing approaches to ... fall into [N] categories: ... and ... . [类别 A] ... . [类别 B] ... . However, these methods do not ... .` | 20% |
| 挑战，第 3 段 | 解决上述缺口要克服什么 → 困难从何而来 → 为什么直接扩展现有方法不够 | `Addressing ... is challenging because ... .` / `The key challenge is that ... .` | 15% |
| 洞察，第 4 段，宜短 | 观察或例子 → 对挑战的新解释 → 由此出现的机会 | `Our key insight is that ... .` / `We observe that ... . This offers an opportunity to ... .` | 10% |
| 方法，第 5 段 | 提出方法 → 关键操作如何利用洞察 → 各自应对哪项挑战 | `Motivated by this insight, we propose ... . Specifically, ... .` / `To address the above challenges and advance existing research, we propose ... .` | 20% |
| 实验结果，第 6 段 | 评估覆盖什么 → 主要结果 → 为什么支持核心主张 | `Experiments on ... show that ... .`；另一维度用 `Moreover, ... .` | 15% |
| 贡献，必须三条 | 概念新意 → 技术新意 → 实验效果 | `Conceptually, ...`；`Technically, ...`；`Empirically, ...` | 10% |

**衔接规范：** 问题与缺口用 `However`，原因用 `because`，例子用 `For example`，洞察到机会用 `This offers an opportunity / This suggests`，洞察到方法用 `Motivated by`，方法展开用 `Specifically`，证据用 `Experiments ... show`。每个连接只承担其真实逻辑，不在各段重复“挑战很大，因此我们提出”。只有一个挑战时使用单数（`challenge`），多个时写 `the above challenges`。

- **相关工作段要有分类：** 首句用一句话给出最相关路线的分类，随后每类用一两句介绍代表做法并就近引用，末句用 `However, these methods ...` 点明它们共同没有解决的问题。对比最接近的工作即可，不提前写一篇 Related Work。说清现有方法为何留下这个问题，避免“很少有人研究”或笼统“现有方法均不足”；互补或新任务也能构成贡献，不必虚构前人失败。
- **挑战与缺口分工：** 第 2 段末句说“还没解决什么”，第 3 段说“为什么难解决”，后者不复述前者。挑战写成具体的技术或信息障碍，使第 5 段的设计能与之逐一对应。
- **洞察要短而形成转折：** 通常 2–4 句，用一句可理解的判断将“挑战为何存在”连到“新做法为何可行”。例如先区分所需信息与表面信号，再说明它带来的机会；不要把组件组合本身称为洞察。有 Teaser 时，引言必须引用它，放在帮助理解这一转折的位置。
- **方法要讲因果：** 以 `Motivated by` 或 `To address the above challenges` 开头，选一到两个关键操作，分别解释它们如何利用洞察、应对哪项挑战。公式推导、完整模块配置与算法步骤留到 Method。
- **贡献要分工：** 贡献列表必须为三条，分别以 `Conceptually,`、`Technically,`、`Empirically,` 开头。
  - Conceptually 是高层的概念归类：从概念上说明本文的问题或方法新在哪里，例如从一个新的角度切入问题、重新界定任务或所需信息；不写具体模块。
  - Technically 说明方法层面的 novelty：新增的机制、设计或性质，以及它与已有方法在做法上的区别。
  - Empirically 说明方法效果好：在哪些数据和设置上，相比哪些基线取得什么主要提升。
  - 三条不能把同一方法换说法写三次；保留原有方法名。分析、理论、数据集论文同样使用这三条，Empirically 写证据揭示的主要发现，按实际贡献填写，不编造；某类确无内容时询问用户。
- **交叉引用要少：** 引言只引用 Teaser 和一个主结果图或表，不引用 Section 与 Appendix，读者会自行往后读；引用写进句子，不放在句末括号里（见 general 第 4 节）。贡献结束后直接进入下一节，无需另加逐节导航段。
- **数字与重复：** 引言通常 1–2 组关键比较即可，用平均指标表述，不用 `in k of N settings` 式计数；结果段与贡献列表避免重复报数。只读各段首句，也应能重建主线。
