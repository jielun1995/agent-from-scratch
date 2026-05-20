# 心智模型 3：ReAct 范式

## 来源

2022 年 Yao 等人提出 **ReAct = Reasoning + Acting**。
到今天所有主流 Agent 框架的底层都是它的变种。

## 核心循环

每一轮 LLM 输出三样东西：

```
Thought:     我现在应该做什么？为什么？
Action:      调用哪个工具，参数是什么？
Observation: (由系统填入工具执行结果)
```

然后把 Observation 喂回 LLM，进入下一轮，直到 LLM 输出 `Final Answer`。

## 一个真实例子

> **问题**：苹果公司现任 CEO 的太太是谁？

```
Thought: 我不知道这个信息，但可以分两步：先查 CEO，再查他的配偶。
Action: web_search("Apple CEO 2026")
Observation: Tim Cook is the CEO of Apple.

Thought: 现在我知道 CEO 是 Tim Cook，下一步查他配偶。
Action: web_search("Tim Cook spouse")
Observation: Tim Cook 公开身份是单身。

Thought: 我得到了答案。
Final Answer: 苹果现任 CEO Tim Cook 公开身份是单身。
```

**这就是 Agent 的全部秘密。** 其余架构都是在这个基础上做加法。

## 现代演进

| 阶段 | 关键升级 |
|------|---------|
| 2022 | 原始 ReAct：用文本格式输出 Thought/Action，要正则解析 |
| 2023 | Function Calling：LLM 直接输出结构化 JSON，可靠性从 70% → 95%+ |
| 2024 | 多 Agent：把任务拆给多个专家 Agent |
| 2024+ | 状态机化：LangGraph 把循环显式建模成图 |
| 2025+ | MCP 协议：工具定义标准化，跨平台复用 |

## 经常被忽视的点

1. **Function Calling 是真正的转折点**——不是框架的功劳，是模型能力的功劳
2. **`description` 字段决定一切**——工具选择准确率主要看你怎么描述它
3. **stop_reason 是循环的退出条件**——不是文本匹配
4. **失败必须有兜底**——max_iterations、token budget、超时
5. **工具数量超过 20，准确率显著下降**——这是 Tool RAG 存在的原因

---

## 我的补充

<!-- TODO: 写下你第一次跑通 ReAct 时最意外的地方 -->

---

## 30 天后回看
