LETTERS_SCORES = {
	k: v
	for keys, v in zip(["AEIOULNRST", "DG", "BCMP", "FHVWY", "K", "JX", "QZ"], [1, 2, 3, 4, 5, 8, 10])
	for k in keys
}

def score(word: str) -> int:
    return sum(LETTERS_SCORES[letter] for letter in word.upper())
