# 语言

英文正文应像领域研究者写的，而不是模型生成的。章节文件中的衔接框架不受本文件的用词限制。

## 句子

- **一句讲一件事：** 能独立成句的内容用句号分开；难懂的定义改写成直白的短句。
- **不用分号连接分句：** 两个独立分句不用分号相接，撰写、改写和润色时都不新增这类句子。按两部分的关系改写且不改变原意：关系松散时拆成两句；转折、因果或并列紧密时用 `but`、`so`、`and` 连接；一部分为另一部分提供背景时改成从句。分号只保留在三处：分隔本身含逗号的列表项，表注与图注中的缩写说明（如 `LP: log-probability; SC: self-consistency`），以及伪代码。
- **不打碎句子：** 一句话不断成很多截，默认不用连续的逗号插入语。
- **主语明确：** 默认用主动语态和 `we`。代词 `it`、`this` 必须有明确先行词；标题中不用 `it`；指代方法时直接写方法名（方法名用法见[术语](terminology.md)）。
- **时态：** 方法与结论用一般现在时，具体实验过程可用过去时。
- **同一概念同一术语：** 不为避免重复换同义词。

## 主张措辞

- `show` 用于直接发现，`suggest` 用于解释性推断。
- 不靠层层 `may / potentially / to some extent` 表达严谨，也不以夸大的确定性替代证据。
- `robust`、`comprehensive` 只在有对应证据时使用；`significantly` 只在有统计检验时使用（见[数字](numbers.md)）。

## 去除 LLM 文风

- **空泛用词改为具体陈述：** `delve into`、`crucial / pivotal / paramount`、`intricate`、`realm`、`landscape`、`tapestry`、`myriad`、`showcase`、`underscore`、`shed light on`、`pave the way`、`groundbreaking`、`seamless(ly)`、`it is worth noting that`、`plays a crucial role in`。`leverage / utilize` 默认写 `use`；`novel` 不反复自称。
- **不用模板句式：** 不用 em dash（—）插入语，改用括号或拆句；不用 `not only ... but also`、`It is not X, but Y` 式反转；不凑三项排比或三连形容词；不在段末加 `This demonstrates the effectiveness of ...` 一类总结句；不连续用 `Moreover / Furthermore / Additionally` 开头。
- **连接副词不夹在句中：** `therefore`、`thus`、`hence` 不放在主语与谓语之间。确为因果推进时移到句首；上文已说清因果时直接删去。
- **`let` 一类短词：** `lets X do` 默认改为 `allows X to do` 或 `enables X to do`。数学定义中的 `Let $x$ denote ...` 不受此限。

## 常见改写对照

| ✗ | ✓ |
|---|---|
| `GAR splits each document before ranking; the reranker then scores each passage.` | `GAR splits each document before ranking. The reranker then scores each passage.` |
| `Recall rises on long documents; it barely changes on short ones.` | `Recall rises on long documents but barely changes on short ones.` |
| `We therefore split each document before ranking.` | `Therefore, we split each document before ranking.`；因果已清楚时写 `We split each document before ranking.` |
| `A confidence score for each response lets a system abstain.` | `A confidence score for each response allows a system to abstain.` |
| `The retriever could not, in principle, see the answer.` | `The retriever could not see the answer in principle.` |
| `The aligner — which selects a passage length for each query — runs before ranking.` | `The aligner selects a passage length for each query. It runs before ranking.` |
| `We leverage a pivotal reranking step to seamlessly utilize ...` | `We use a reranking step to ...` |
| `This demonstrates the effectiveness of our method.` | 删去，或写出具体发现：`Alignment removes most granularity errors.` |
| `GAR not only improves recall but also reduces latency.` | `GAR improves recall and reduces latency.` |
