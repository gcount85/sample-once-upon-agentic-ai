from strands import Agent, tool


@tool
def roll_dice(faces: int = 6) -> int:
    """Roll a die with a specified number of faces.

    Args:
        faces: Number of faces on the die (must be >= 1). Defaults to 6.

    Returns:
        A random integer result between 1 and `faces` inclusive.

    Raises:
        ValueError: If `faces` is less than 1.
    """

    import random

    if faces < 1:
        raise ValueError("Dice must have at least 1 face")

    return random.randint(1, faces)


@tool
def roll_4d6_drop_lowest() -> int:
    """Roll 4d6, drop the lowest die, and sum the highest three.

    Returns:
        The sum of the top three dice from four six-sided dice rolls.
    """
    import random

    rolls = [random.randint(1, 6) for _ in range(4)]
    return sum(sorted(rolls, reverse=True)[:3])


dice_master = Agent(
    tools=[roll_dice, roll_4d6_drop_lowest],
    system_prompt=(
        """You are Lady Luck, the mystical keeper of dice and fortune in D&D "
        "adventures. You speak with theatrical flair and always announce dice "
        "rolls with appropriate drama. You know all about D&D mechanics, "
        "ability scores, and can help players with character creation. When "
        "rolling ability scores, remember the traditional method: roll 4d6, "
        "drop the lowest die. 한국말로 대답하세요!!"""
    ),
)

# Test your dice master's abilities
dice_master(
    "Help me create a new D&D character! Roll the strength, wisdom, charisma "
    "and intelligence abilities scores using 4d6 drop lowest method. 한국말로 대답해라."
)
