import re

def decode(string):
    def repeat(matcher):
        return int(matcher.group(1)) * matcher.group(2)
    return re.sub(r"(\d+)(\D)", repeat, string)

def encode(string):
    def compress(matcher):
        return str(len(matcher.group(0))) + matcher.group(0)[0]
    return re.sub(r"([A-Za-z ])\1+", compress, string)
