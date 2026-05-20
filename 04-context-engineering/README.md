# 04 · Context Engineering

## 这一课要回答的问题

> **怎么让 Agent 跑得又便宜又好?为什么 200K 上下文窗口"不够用"?**

## 核心判断

> Prompt Engineering 关心"怎么说一句话"。
> **Context Engineering 关心"在每一刻,让 LLM 看到正确的信息"。**
>
> 这是两件难度完全不同的事。

## 为什么 Agent 翻车 80% 是 Context 管理稀烂

三个真实问题:

1. **Lost in the Middle** —— 长 context 里中间信息检索准确率显著下降
2. **成本爆炸** —— 20 轮循环累计输入 token 可达 45 万,单次跑十几美元
3. **注意力稀释** —— context 越长决策质量越差,而不是越好

## 关键认知: Context Window ≠ Memory

```
Context Window  ← LLM 这一次能看到的所有 token (有限)
Memory         ← Agent 跨越多次调用持有的总信息 (可以很大)
```

Context Engineering 的核心: **从 Memory 这个大池子里,精准捞出最该被 LLM 看到的那一小撮。**

## Context 的四种成分(必须分开管理)

| 成分 | 例子 | 管理策略 |
|------|------|---------|
| **System Context** | 角色、规则 | 一次性放好 |
| **Task Context** | 用户目标 | 每轮重复或固定位置 |
| **Working Memory** | 中间结果 | **核心管理对象** |
| **Retrieved Context** | RAG 知识 | 按需检索 + 排序 |

新手最大错误: **把所有东西塞同一个 messages 列表**。

## 四种核心管理模式

1. **Compression** —— 历史长了就压成摘要(用便宜模型压)
2. **Scratchpad** —— 给 Agent 独立"工作笔记本",重要事实写这里
3. **Retrieval** —— 知识/工具用向量库存,按需检索注入
4. **Isolation** —— 不同子任务用独立 context (Plan-Execute 已经在做了)

## Prompt Caching: 被低估的杀器

- 缓存命中的 token = **原价的 10%**
- 多轮 Agent 可以再省 50%+
- 跟前面四种模式叠加 → 总成本能压到 1/5

## 状态

🚧 待自己实现。建议路径:

1. 给前面的 Agent 加 token 估算和打印,看实际消耗
2. 实现 `Scratchpad` 类
3. 实现 `compress_history` 函数,**人工对比**压缩前后丢了什么
4. 启用 Prompt Caching,对比成本
5. **综合实验**: 同任务用三种配置跑,对比 token/费用/质量

## 行业现状(别被框架骗)

LangChain、LangGraph、CrewAI 这些**默认都是把所有历史塞 context**。
它们的"memory 模块"大多就是简单截断或滑动窗口。
真正做好 Context Engineering 需要你**绕过框架的默认行为**手动管理。

这就是为什么这门课强调"先理解原理再用框架"。
