"""
Agent 可用工具的定义。

两个核心要点:
1. 工具就是普通 Python 函数,没有任何魔法
2. TOOLS_SCHEMA 里的 description 字段决定 LLM 选不选这个工具——写好它!
"""


def web_search(query: str) -> str:
    """模拟搜索。生产环境替换为 Tavily / Serper / Brave Search API。"""
    fake_db = {
        "apple stock price": "Apple (AAPL) 当前股价约 $228.50",
        "tesla stock price": "Tesla (TSLA) 当前股价约 $342.10",
        "nvidia stock price": "NVIDIA (NVDA) 当前股价约 $135.20",
    }
    query_lower = query.lower()
    for key, value in fake_db.items():
        if key in query_lower:
            return value
    return f"未找到关于 '{query}' 的结果"


def calculator(expression: str) -> str:
    """安全地求值数学表达式。

    注意: 生产环境不要用 eval, 改用 ast.literal_eval 或 sympy。
    这里用受限 eval 仅供学习。
    """
    try:
        # 禁用 builtins, 不允许导入和调用任何东西
        result = eval(expression, {"__builtins__": {}}, {})
        return f"结果是 {result}"
    except Exception as e:
        return f"计算错误: {e}"


# 工具函数注册表 —— 名字到函数的映射
TOOLS_REGISTRY = {
    "web_search": web_search,
    "calculator": calculator,
}

# 工具的 JSON Schema —— 这是给 LLM 看的"工具说明书"
# description 一定要写得清晰具体,这决定了 LLM 选工具的准确率
TOOLS_SCHEMA = [
    {
        "name": "web_search",
        "description": "搜索网络获取实时信息,比如股价、新闻、人物等。当你不确定某个事实时使用。",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "搜索关键词,简洁明确,不要带多余的话"
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "calculator",
        "description": "计算数学表达式,比如 '228.5 * 100' 或 '(3 + 4) * 2'。涉及任何数学运算时必须用这个工具,不要心算。",
        "input_schema": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "合法的 Python 数学表达式"
                }
            },
            "required": ["expression"]
        }
    }
]
