import re

def abbreviate(phrase: str) -> str:
    words = re.split(r"[^A-Z']+", phrase.upper())
    return ''.join(word[0] for word in words)
