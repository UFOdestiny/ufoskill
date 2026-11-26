# 交叉引用

本文件管正文如何提及图、表、章节和附录，是这类规则的唯一来源。文献引用见[引用](../presentation/citations.md)。

## 写法

- **写进句子：** 引用图、表、章节和附录时，让引用成为句子成分，不在句末加括号。
  - ✗ `Most retrieval errors come from granularity mismatch (Figure~\ref{fig:teaser}).`
  - ✓ `As shown in Figure~\ref{fig:teaser}, most retrieval errors come from granularity mismatch.`
  - ✓ `Table~\ref{tab:main} reports ...`、`We describe ... in Section~\ref{sec:align}`、`Appendix~\ref{app:setup} lists the full configuration.`
- **Section 不作主语：** ✗ `Section~\ref{sec:align} aligns the query granularity ...` ✓ `We describe granularity alignment in Section~\ref{sec:align}.` 只在读者确需跳转时引用章节，删去不必要的 `Section~X`。
- **指向附录说明内容：** 每处说明附录里有什么，可按内容选用 `provides`、`presents`、`lists` 等。正文指向附录参考约 8–14 处。
- 一段默认只引用一组图表。

## 各章节的限制

| 章节 | 要求 |
|---|---|
| Abstract | 不含任何图、表、章节或附录引用 |
| Introduction | 只引用 Teaser 和一个主结果图或表；不引用 Section 与 Appendix；贡献列表后不加逐节导航段。Teaser 的引用位置见[引言](../sections/introduction.md) |
| Problem Formulation | 不出现 `built in Section~X` 式的前向章节引用 |
| Method 总领段 | 例外：模块名后用括号标注小节，见[方法](../sections/method.md)总领段。指向附录的完整算法或例子时用 `provides`、`presents`，不用 `gives` |
| Experiments Setup | 各类的附录指向见[实验](../sections/experiments.md) Setup |
