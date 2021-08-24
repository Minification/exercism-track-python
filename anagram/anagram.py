from typing import List

def find_anagrams(word: str, candidates: List[str]) -> List[str]:
    word_sorted = sorted(word.upper())
    return [
    	candidate for candidate in candidates
    	if word_sorted == sorted(candidate.upper()) and word.upper() != candidate.upper()
    ]
