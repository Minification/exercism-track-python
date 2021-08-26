from typing import List
from collections import Counter

# First index is a dummy index.
# The calculations are done in cents, probably because we're dealing
# with currency. From index 1 including and onwards, we have
# 800 cents, then 800*0.95, *0.9, *0.8, *0.75.
DISCOUNTED_PRICES = [0, 800, 760, 720, 640, 600]

def total(basket: List[int]) -> int:
    counter = Counter(basket)
    groups = []
    
    while len(counter):
        groups.append(len(counter))
        # decrement each book count by one
        counter.subtract(counter.keys())
        # Remove the zero ones
        counter = +counter
    
    # Pair up groups of 3 and 5 and replace them with
    # two groups of 4, because this yields a larger discount.
    # This operation is rather expensive...
    while 3 in groups and 5 in groups:
        groups.remove(3)
        groups.remove(5)
        groups.extend([4, 4])
    
    # Now we just sum up the discounted prices for each book
    return sum(size * DISCOUNTED_PRICES[size] for size in groups)
