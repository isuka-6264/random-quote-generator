from loader import load_quotes
from randomizer import get_random_quote

def main():
    quotes = load_quotes("quotes/quotes.txt")
    print(get_random_quote(quotes))

if __name__ == "__main__":
    main()
