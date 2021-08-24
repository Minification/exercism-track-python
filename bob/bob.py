import re

def is_true_upper(string: str) -> bool:
    return string.lower() != string and string.upper() == string
    
def is_question(string: str) -> bool:
    return string.strip().endswith("?")

def response(hey_bob: str) -> str:
	if is_true_upper(hey_bob) and is_question(hey_bob):
	    return "Calm down, I know what I'm doing!"
	elif is_true_upper(hey_bob):
	    return "Whoa, chill out!"
	elif is_question(hey_bob):
	    return "Sure."
	elif not hey_bob.strip():
	    return "Fine. Be that way!"
	return "Whatever."
