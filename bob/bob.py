import re

def response(hey_bob):
	hey_bob = re.sub(r"\s+", "", hey_bob)
	if not hey_bob:
		return "Fine. Be that way!"
	all_caps = hey_bob == hey_bob.upper()
	only_symbols_or_numbers = re.sub(r"[A-Za-z]", "", hey_bob) == hey_bob
	is_question = hey_bob[-1] == "?"
	has_fullstop = hey_bob[-1] == "." or re.compile(r"[A-Za-z0-9]").match(hey_bob[-1])
	is_exclamation = hey_bob[-1] == "!"
	if all_caps and not only_symbols_or_numbers:
		if not is_question:
			return "Whoa, chill out!"
		else:
			return "Calm down, I know what I'm doing!"
	if is_question:
		return "Sure."
	if has_fullstop or is_exclamation:
		return "Whatever."
	return "End"
	
