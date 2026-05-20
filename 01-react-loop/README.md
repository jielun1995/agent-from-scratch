# 01 · ReAct 循环

## 这一课要回答的问题

> **Agent 到底是什么？跟普通 LLM 调用有什么本质区别？**

## 核心洞察

1. Agent 的灵魂是**循环**，不是工具
2. 用 Function Calling 而不是文本解析
3. 工具就是普通 Python 函数——LLM 不会执行任何东西，是你的代码在执行
4. `description` 字段决定 LLM 选不选这个工具
5. `stop_reason` 是循环退出条件

## 文件说明

```
01-react-loop/
├── README.md            ← 你正在读
├── notes.md             ← 我的笔记(用自己的话重写)
├── code/
│   ├── tools.py         ← 工具定义(web_search、calculator)
│   ├── minimal_agent.py ← 最小 ReAct Agent (~100 行)
│   └── run.py           ← 运行入口
└── exercises/
    └── README.md        ← 练习清单
```

## 快速开始

```bash
cd code/
export ANTHROPIC_API_KEY="sk-ant-..."
python run.py
```

你会看到 Agent 自主完成"苹果股价 × 100"这种需要两步的任务。

## 关键代码片段

完整代码见 [`code/minimal_agent.py`](./code/minimal_agent.py)，核心循环只有这点：

```python
for iteration in range(max_iterations):
    response = client.messages.create(
        model="claude-opus-4-7",
        tools=TOOLS_SCHEMA,
        messages=messages,
    )
    messages.append({"role": "assistant", "content": response.content})

    if response.stop_reason == "end_turn":
        return extract_final_text(response)

    if response.stop_reason == "tool_use":
        tool_results = execute_tools(response.content)
        messages.append({"role": "user", "content": tool_results})
```

记住这 10 行。**这就是 Agent 的本体。**

## 练习

见 [`exercises/`](./exercises/)。

## 我的笔记

见 [`notes.md`](./notes.md)。
