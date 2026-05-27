# agent-from-scratch

> 从零手写 AI Agent，理解循环、规划、评估、上下文四大支柱。不靠框架，先懂原理。

这是我学习 AI Agent 工程的笔记和代码仓库。所有 Agent 实现都不依赖 LangChain / CrewAI / AutoGen 等框架，**全程用原生 SDK 手写**，目的是真正理解每一行在做什么。

---

## 为什么从零写

主流框架（LangChain、LangGraph、CrewAI、AutoGen）已经很成熟，但有两个问题：

1. **抽象太厚** —— 出问题时不知道底下发生了什么
2. **掩盖了原理** —— 学完会用框架，但理解不到本质

所以我的学习路径反过来：**先手写原理，再去看框架**。当你能用 100 行代码实现 ReAct 循环，再回头看 LangGraph，会发现它其实没什么神秘。

---

## 学习路线（四课）

| 课程 | 主题 | 核心问题 | 状态 |
|------|------|---------|------|
| [01](./01-react-loop/) | **ReAct 循环** | Agent 到底是什么？ 
| [02](./02-plan-execute/) | **Plan-Execute 多步骤任务** | 如何处理复杂任务？ 
| [03](./03-evaluation/) | **评估体系** | 如何知道 Agent 做得好不好？ 
| [04](./04-context-engineering/) | **上下文工程** | 如何让 Agent 跑得又便宜又好？

完成这四课，你会掌握 Agent 工程的**核心四元组**：

> **循环（Loop）+ 规划（Plan）+ 评估（Eval）+ 上下文（Context）**

行业里其他东西（多 Agent、各种花哨框架）都是这四元组之上的变奏。

---

## 仓库结构

```
agent-from-scratch/
├── 00-mental-models/        ← 核心心智模型(贯穿所有课程)
├── 01-react-loop/           ← 第一课
├── 02-plan-execute/         ← 第二课
├── 03-evaluation/           ← 第三课
├── 04-context-engineering/  ← 第四课
├── insights/                ← 我自己的洞察、踩过的坑
├── patterns/                ← 可复用的代码模式
├── reading-list.md          ← 后续阅读清单
└── changelog.md             ← 学习日志
```

每个课程目录都有自己的 README，包含：
- 这一课的核心问题
- 我的笔记（用自己的话重写，不照抄）
- 可运行的代码
- 我做的练习与踩坑记录

---


## 环境

- Python 3.10+
- `anthropic` SDK
- `ANTHROPIC_API_KEY` 环境变量

```bash
pip install anthropic
export ANTHROPIC_API_KEY="sk-ant-..."
```

---

## 学习原则（贴在显眼处，时刻提醒自己）

1. **先理解，再实现，最后才用框架**
2. **写不下来 = 没真懂**
3. **能跑 ≠ 真的工作**——必须有 Eval
4. **简单单 Agent 优先**，别一上来就多 Agent
5. **每个失败案例都加进 Eval 集**

---

## License

MIT —— 随便用。但如果有帮助，欢迎给个 star。
