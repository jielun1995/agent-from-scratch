"""
最小 ReAct Agent —— Agent 的本质就在这一个文件里。

核心循环 (10 行):
    for iteration in range(max_iterations):
        response = LLM(messages)
        messages.append(response)
        if response.stop_reason == "end_turn":
            return final_answer
        if response.stop_reason == "tool_use":
            tool_results = execute_tools(response)
            messages.append(tool_results)

任何 Agent 框架(LangGraph、CrewAI、AutoGen)的底层都是这个循环。
框架做的只是: 给循环装上更多功能(状态、可观测性、并发、人工介入)。
"""

import anthropic
from tools import TOOLS_REGISTRY, TOOLS_SCHEMA

client = anthropic.Anthropic()


def run_agent(user_question: str, max_iterations: int = 10) -> str:
    """
    跑一个 ReAct 循环直到完成或达到最大轮次。

    Args:
        user_question: 用户问题
        max_iterations: 最大循环轮次(防死循环)

    Returns:
        Agent 的最终回答
    """
    messages = [{"role": "user", "content": user_question}]

    print(f"\n🧑 用户提问: {user_question}")
    print("=" * 60)

    for iteration in range(max_iterations):
        print(f"\n🔄 第 {iteration + 1} 轮循环")
        print("-" * 40)

        # 1) 思考: 调用 LLM
        response = client.messages.create(
            model="claude-opus-4-7",
            max_tokens=1024,
            tools=TOOLS_SCHEMA,
            messages=messages,
        )

        # 2) 把 LLM 的回复加入历史(否则它会"失忆")
        messages.append({
            "role": "assistant",
            "content": response.content
        })

        # 3) 打印 LLM 的思考
        for block in response.content:
            if block.type == "text" and block.text.strip():
                print(f"💭 思考: {block.text}")

        # 4) 终止条件: 没有工具调用 = 任务完成
        if response.stop_reason == "end_turn":
            print("\n" + "=" * 60)
            print("✅ Agent 完成任务")
            final_text = next(
                (b.text for b in response.content if b.type == "text"),
                "(无文本回复)"
            )
            return final_text

        # 5) 行动: 执行所有工具调用
        if response.stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    tool_name = block.name
                    tool_input = block.input
                    print(f"🔧 调用工具: {tool_name}({tool_input})")

                    # 真正执行函数(LLM 自己不会执行任何东西!)
                    if tool_name in TOOLS_REGISTRY:
                        try:
                            result = TOOLS_REGISTRY[tool_name](**tool_input)
                        except Exception as e:
                            result = f"工具执行出错: {e}"
                    else:
                        result = f"未知工具: {tool_name}"

                    print(f"📋 工具返回: {result}")

                    # 工具结果必须用 tool_result 格式回填
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result
                    })

            # 6) 把工具结果作为新的 user 消息加入历史
            messages.append({
                "role": "user",
                "content": tool_results
            })

    print("\n⚠️  达到最大循环次数,强制终止")
    return "(任务未在限定步数内完成)"
