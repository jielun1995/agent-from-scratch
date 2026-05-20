# 第一课练习

> 做完每一个练习,把过程和踩坑记录在对应的 .md 文件里。
> 不只记录"成功的方案",更要记录"失败的尝试"——后者价值更高。

## Level 1: 跑通基础版

把 `code/run.py` 跑起来,试 3-5 个不同问题。观察:
- Agent 在哪些问题上表现好?
- 哪些问题会失败?为什么?

→ 笔记: [`level1_observations.md`](./level1_observations.md)

## Level 2: 加一个新工具

实现一个新工具(比如 `get_current_time()` 或 `read_file(path)`)
注册到 `TOOLS_REGISTRY` 和 `TOOLS_SCHEMA`,看 LLM 能不能正确选择它。

→ 笔记: [`level2_new_tool.md`](./level2_new_tool.md)

## Level 3: 让 Agent 在闲聊时不要乱调工具

故意问 Agent 一个不该用工具的问题,比如:
- "你好,介绍下自己"
- "讲个笑话"

观察它会不会乱调工具。如果会,你怎么改 system prompt 让它不调?

→ 笔记: [`level3_no_tool_when_chatting.md`](./level3_no_tool_when_chatting.md)

## Level 4 (进阶): 显式 ReAct

加一个 `system` 参数,在 system prompt 里加上:
"在调用工具前,先用一句话说明你的计划。"

看输出会不会变得更像真正的 ReAct(显式 Thought + Action)。

→ 笔记: [`level4_explicit_react.md`](./level4_explicit_react.md)

## Level 5 (硬核): 故意搞坏然后修

把 `description` 字段故意写得很含糊(比如改成"这是一个工具"),
看 Agent 的行为会怎样变化。

这个练习能让你深刻理解 description 的重要性。

→ 笔记: [`level5_bad_description.md`](./level5_bad_description.md)
