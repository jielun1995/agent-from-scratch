# Patterns · 可复用的代码模式

> 在课程中沉淀出的、可以直接抄到新项目里的代码片段。
>
> 不是"完整项目",是"模块/技巧/模板"。

## 当前模式

(随学随加。建议每个文件配一段使用说明。)

## 候选模式(等学到了再补)

- `tool_definition_template.py` —— 工具定义的标准模板
- `react_loop.py` —— 最小 ReAct 循环(从 01 提炼)
- `trajectory_logger.py` —— 结构化轨迹日志(从 03 提炼)
- `llm_judge.py` —— LLM-as-Judge 的标准实现(从 03 提炼)
- `scratchpad.py` —— Scratchpad 数据类(从 04 提炼)
- `compress_history.py` —— 历史压缩(从 04 提炼)
- `prompt_caching.py` —— Prompt Caching 标准用法

## 使用约定

- 每个文件**独立可用**,不依赖仓库其他文件
- 文件开头写清: 用途、输入输出、依赖
- 包含一个 `__main__` 示例,跑一下就能看到效果
