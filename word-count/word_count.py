from typing import Dict
from collections import Counter
import re

def count_words(sentence: str) -> Dict[str, int]:
    return Counter(re.findall(r"[a-z0-9]+(?:'[a-z]+)?", sentence.lower()))
