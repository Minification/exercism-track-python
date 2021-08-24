def is_isogram(string: str) -> bool:
    letters = [s for s in string.casefold() if s.isalpha()]
    return len(letters) == len(set(letters))
