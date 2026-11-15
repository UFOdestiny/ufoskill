# MySKILL

一个自包含的 **writing** skill，用于撰写、重组、润色和压缩 AI、ML、NLP 研究论文，同时支持 Codex 与 Claude Code。规范用中文；论文正文一律英文，说明与修改理由跟随用户语言。

核心约束是 `references/sections/` 中各章节的组织逻辑：写、改或诊断任一章节都按其组织链展开。在此之上统一整体故事、novelty、insight、篇幅、数字密度与可读性，并去除 LLM 文风。已有稿件保持原章节顺序，用户要求重组时才调整；引用不凭记忆生成，缺失内容统一留 `[TODO: ...]`。直接表达贡献与发现，删除空泛防御和偏离主线的内容。

## 使用

```text
$myskill:writing 重组引言，突出核心洞察和各段之间的推进关系。
$myskill:writing 调整方法：先解释直觉，再按依赖展开机制，最后交代推断。
$myskill:writing 压缩全文，保留核心设计与发现，将长推导和完整分项结果移入附录。
```

Claude Code 使用 `/myskill:writing`。局部修改保持局部；只需审阅时说明不改文件。

## 目录

```text
skills/writing/
  SKILL.md                   唯一入口，按需读取规范
  agents/openai.yaml         Codex 显示信息
  references/
    general.md               全局故事、篇幅、数字与理论密度
    sections/                十个章节的内部逻辑
    presentation/            figures、tables、citations
plugin.json                  Codex 插件声明
.agents/plugins/             Codex marketplace
.claude-plugin/              Claude 插件声明与 marketplace
scripts/manage.py            验证、更新版本、打包
tests/                      资源完整性与双客户端加载测试
.github/workflows/ci.yml     持续验证与标签发布
```

从 [writing 入口](skills/writing/SKILL.md) 阅读章节索引；[全局规范](skills/writing/references/general.md) 统一全文取舍。

章节顺序为 **Abstract → Introduction → Problem Formulation → Method → Experiments → Related Work → Conclusion → Limitations（可选）→ Ethical Considerations（可选）→ Appendix**。Abstract、Introduction、Conclusion 提供衔接框架，其他章节以逻辑关系为主。

所有写作依赖都在 `skills/writing/` 内；写作时无需 Python。插件安装使用完整仓库，以保留两种客户端的发现与安装信息。

## 安装

```bash
# Codex
codex plugin marketplace add UFOdestiny/MySKILL
codex plugin add myskill@myskill

# Claude Code
claude plugin marketplace add UFOdestiny/MySKILL
claude plugin install myskill@myskill
```

## 更新

从 GitHub 拉取最新发布版本：

```bash
# Codex
codex plugin marketplace upgrade myskill
codex plugin add myskill@myskill

# Claude Code
claude plugin marketplace update myskill
claude plugin update myskill@myskill
```

安装或更新后启动新会话，使用唯一的 `myskill:writing` 入口；远程安装不会包含尚未发布的本地修改。

## 验证与打包

```bash
python3 -m pip install -r requirements-dev.txt
python3 -B scripts/manage.py validate
python3 -B -m unittest discover -s tests -v
python3 -B scripts/manage.py build
```

Claude 安装测试需指定原生客户端：`MYSKILL_CLAUDE_BIN=/path/to/native/claude`；CI 已设置。账号包装器可能覆盖临时配置目录，所以未指定时跳过该项。测试检查自包含资源、唯一入口、元数据与链接、可重复归档，以及双客户端实际加载。

两种 manifest 的版本和公共元数据由验证脚本检查一致性。使用 `python3 -B scripts/manage.py bump <版本号>` 同步版本。构建默认输出 `dist/myskill-<version>.zip` 和校验和，也可用 `build --output <目录>` 指定位置。生成物不作为源文件维护；CI 在版本标签上发布验证过的归档。
