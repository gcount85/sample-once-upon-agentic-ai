"""Minimal Strands Agent example.

Run:
    python 1_strands_basics/simple_agent.py

Steps:
1. Configure debug logging.
2. Create an Agent (D&D game master persona).
3. Send an initial incantation and print the response.
"""

import logging
from strands import Agent


def main() -> None:
    """Create and invoke the D&D game master agent."""
    # 1. Debug logging configuration (set to INFO if too noisy).
    logging.basicConfig(
        level=logging.WARNING,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    logger = logging.getLogger(__name__)

    # 2. Instantiate the Agent with the required system prompt.
    system_prompt = "You are a game master for a Dungeon & Dragon game"
    agent = Agent(system_prompt=system_prompt)
    logger.debug("Agent instantiated with system prompt: %s", system_prompt)

    # 3. Summon / invoke the agent with an initial incantation.
    incantation = "Hi, I am an adventurer ready for adventure!"
    logger.debug("Sending incantation: %s", incantation)

    # Try common invocation patterns.
    try:
        response = agent(incantation)
    except TypeError:
        if hasattr(agent, "run"):
            response = agent.run(incantation)
        elif hasattr(agent, "summon"):
            response = agent.summon(incantation)
        else:
            raise RuntimeError("Unable to invoke agent. Check strands.Agent API.")

    logger.debug("Raw agent response: %r", response)

    print("=== Agent Response ===")
    print(response)


if __name__ == "__main__":
    main()
