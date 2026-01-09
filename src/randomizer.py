import random


def get_random_quote(quotes: list[str]) -> str:
    if not quotes:
        raise ValueError("No quotes available")
    return random.choice(quotes)
