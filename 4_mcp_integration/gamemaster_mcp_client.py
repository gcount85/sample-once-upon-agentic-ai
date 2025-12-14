from strands import Agent
from strands.tools.mcp.mcp_client import MCPClient
from mcp.client.streamable_http import streamablehttp_client


def main():
    # Connect to the dice roll MCP server
    print("\nConnecting to D&D Dice Roll MCP Server...")
    # Create a streamable http MCPClient connecting to MCP endpoint
    mcp_endpoint = "http://localhost:8080/mcp"
    mcp_client = MCPClient(lambda: streamablehttp_client(mcp_endpoint))

    try:
        # Keep MCP client session open for the entire interactive loop
        with mcp_client:
            # Get available tools from MCP server (optional display)
            mcp_tools = mcp_client.list_tools_sync()
            print(f"Available tools: {[tool.tool_name for tool in mcp_tools]}")

            # Create the gamemaster agent with the MCP client as a tool
            gamemaster = Agent(
                system_prompt=(
                    "You are Lady Luck, mystical keeper of dice and fortune. "
                    "Speak with theatrical flair. Announce dice rolls. "
                    "Use proper tools; never invent results. 한국말로 대답해라."
                ),
                tools=mcp_tools,
            )

            # Start interactive session
            print("\n🎲 Lady Luck - D&D Gamemaster with MCP Dice Rolling")
            print("=" * 60)
            print("\n🎯 Try: 'Roll a d20' or 'Roll a d6' or 'Roll a d100'")

            while True:
                user_input = input("\n🎲 Your request: ")
                if user_input.lower() in ["exit", "quit", "bye"]:
                    print("🎭 May fortune favor your future adventures!")
                    break

                print("\n🎲 Rolling the dice of fate...\n")
                response = gamemaster(user_input)
                print(response)

    except Exception as e:
        print(f"❌ Connection failed: {e}")
        print(
            "💡 Ensure dice service is running: python "
            "4_mcp_integration/dice_roll_mcp_server.py"
        )


if __name__ == "__main__":
    main()
