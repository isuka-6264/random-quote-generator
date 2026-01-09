def load_quotes(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]
