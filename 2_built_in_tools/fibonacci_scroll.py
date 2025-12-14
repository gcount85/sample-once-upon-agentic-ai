#!/usr/bin/env python3
"""
🔮 The Fibonacci Scroll of Kiro the Grey Hat 🔮
A mystical incantation to summon the sacred sequence
where each number emerges from the harmony of its ancestors.
"""


def fibonacci_spell(n):
    """
    Cast the Fibonacci enchantment to generate the first n numbers
    of the legendary sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

    Args:
        n (int): Number of Fibonacci numbers to conjure

    Returns:
        list: The sacred sequence of Fibonacci numbers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    # Begin the ritual with the first two sacred numbers
    fibonacci_sequence = [0, 1]

    # Cast the spell to generate the remaining numbers
    for i in range(2, n):
        next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence


def display_sequence_with_magic(sequence):
    """
    Display the Fibonacci sequence with mystical formatting
    """
    print("✨" * 50)
    print("🔮 BEHOLD! The Fibonacci Sequence Emerges! 🔮")
    print("✨" * 50)

    for i, num in enumerate(sequence):
        if i == 0:
            print(f"F({i}) = {num} ← The Void, where all begins")
        elif i == 1:
            print(f"F({i}) = {num} ← The Unity, the first light")
        else:
            prev1 = sequence[i - 1]
            prev2 = sequence[i - 2]
            print(f"F({i}) = {num} ← Born from {prev2} + {prev1}")

    print("✨" * 50)
    print(f"The sequence: {' → '.join(map(str, sequence))}")
    print("✨" * 50)


if __name__ == "__main__":
    print("🧙‍♂️ Kiro the Grey Hat casts the Fibonacci Spell! 🧙‍♂️")
    print()

    # Generate the first 10 Fibonacci numbers
    magical_sequence = fibonacci_spell(10)

    # Display with mystical flourish
    display_sequence_with_magic(magical_sequence)

    print("\n🌟 The spell is complete! The ancient sequence has been revealed! 🌟")
