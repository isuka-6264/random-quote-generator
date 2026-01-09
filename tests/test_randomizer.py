from src.randomizer import get_random_quote

def test_random_quote():
    quotes = ["a", "b", "c"]
    assert get_random_quote(quotes) in quotes
