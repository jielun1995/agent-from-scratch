"""
运行入口。

使用:
    export ANTHROPIC_API_KEY="sk-ant-..."
    python run.py
"""

from minimal_agent import run_agent


def main():
    # 示例 1: 需要两步的任务
    answer = run_agent("苹果当前股价乘以 100 是多少美元?")
    print(f"\n🎯 最终答案: {answer}\n")

    # 自己加更多测试 ↓
    # answer = run_agent("特斯拉股价加上英伟达股价是多少?")


if __name__ == "__main__":
    main()
