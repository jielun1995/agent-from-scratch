# 02 · Plan-Execute 多步骤任务

## 这一课要回答的问题

> **复杂任务该怎么处理?为什么朴素 ReAct 在复杂任务上会崩?**

## 复杂任务下朴素 ReAct 的四种崩溃模式

1. **上下文爆炸** —— 每搜一次就塞几千 token,跑十几轮就满了
2. **路径迷失** —— 第 5 轮可能就忘了用户最初要什么
3. **无计划性** —— 走一步算一步,没有全局视野
4. **无法并行** —— 明明可以并发,非要串行

## 核心范式: Plan-and-Execute

```
用户目标
   ↓
[Planner]   ← 强模型,专门做任务分解
   ↓
任务列表
   ↓
[Executor] ← 对每个子任务跑一个小型 ReAct 循环
   ↓
中间结果池
   ↓
[Synthesizer] ← 汇总输出最终答案
```

**关键认知**: 这还是单 Agent 思维,只是把"思考"和"执行"在时间上分开。
**不是多 Agent。**

## 关键技巧

- 用**强模型**做规划,用**快模型**做执行 → 省 60-80% 成本
- 子任务用 `ThreadPoolExecutor` **并发**跑
- 显式定义 **State 对象**,不要把所有信息都塞 messages
- Synthesizer 只看子任务"最终结论",不看过程

## 状态

🚧 待自己实现。建议路径:

1. 先看 `00-mental-models/four-pillars.md` 理解为什么需要 Plan
2. 设计自己的 `AgentState` 和 `SubTask` 数据类
3. 实现 Planner / Executor / Synthesizer 三个阶段
4. 加上并发执行
5. 跑一个真实研究任务,对比 vs 朴素 ReAct

## 文件结构(待填充)

```
02-plan-execute/
├── README.md             ← 你正在读
├── notes.md              ← 待写
├── code/
│   ├── state.py          ← AgentState、SubTask 数据类
│   ├── planner.py        ← 任务分解
│   ├── executor.py       ← 子任务执行
│   ├── synthesizer.py    ← 结果汇总
│   └── research_agent.py ← 编排所有阶段
└── exercises/
    └── README.md         ← 待写
```
