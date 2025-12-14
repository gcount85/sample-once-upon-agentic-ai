"""Example showing use of the built-in http_request tool with a Strands Agent.

The tool lets the agent fetch data from web resources. After initialization we
ask it to look up the designers of Dungeons & Dragons from Wikipedia.
"""

from strands import Agent
from strands_tools import http_request  # Built-in tool import


def main() -> None:
    agent = Agent(
        tools=[http_request],
    )

    question = (
        "Using the website https://en.wikipedia.org/wiki/Dungeons_%26_Dragons "
        "tell me the name of the designers of Dungeons and Dragons."
    )

    response = agent(question)
    print("=== Agent Response ===")
    print(response)


if __name__ == "__main__":
    main()
