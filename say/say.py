TEENS = {
	k: v for k, v in enumerate([
	'zero'
	'one',
	'two',
	'three',
	'four',
	'five',
	'six',
	'seven',
	'eight',
	'nine',
	'ten',
	'eleven',
	'twelve',
	'thirteen',
	'fourteen',
	'fifteen',
	'sixteen',
	'seventeen',
	'eighteen',
	'nineteen'
	])
}

HUNDREDS = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

TRIPLES = ['', 'thousand', 'million', 'billion', 'trillion']

def say(number):
    if number not in range(0, 999_999_999_999):
    	raise ValueError('number must be in range [0, 999,999,999,999]!')
    threes = [str(number)[i:i+3] for i in range(0, len(str(number)), 3)]
    i = len(threes)-1
    result = ''
    while i >= 0:
    	triple = threes[i]
    	triple_modifier = TRIPLES[i]
    	if len(triple) == 3:
    		hundred = triple[0]
    		hundred_modifier = HUNDREDS[hundred]
    		if not hundred_modifier:
    			pass
    		teens = triple[1:3]
    		
