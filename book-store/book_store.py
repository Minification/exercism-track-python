from typing import List
from collections import Counter, defaultdict

# First index is a dummy index.
# The calculations are done in cents, probably because we're dealing
# with currency. From index 1 including and onwards, we have
# 800 cents, then 800*0.95, *0.9, *0.8, *0.75.
DISCOUNTED_PRICES = [0, 800, 760, 720, 640, 600]

# Explanation of the algorithm (I would almost call this dynamic programming?):
# The rationale here is that if the basket has been aggregated to equip each
# book with its copy count, then the while-loop goes over the group sizes in
# decreasing order, i.e., we obtain a partial order of group sizes. It is now
# very easy and efficient to implement the rule that two groups of four
# different books lead to a larger discount than one group of three and one
# group of five. That is because when we encounter the groups of size 3, we will
# already be done with groups of size 5. So we don't even note groups of size 3
# as long as we still have groups of size 5, remove the group of size 5, and
# instead note down that we now have two more groups of size 4. In all other
# cases, we just note down that we note down that we have encountered another
# group of a certain size. Of course, we subtract 1 from each book in the
# aggregate, and remove the zero count ones.
# At the very end, we just calculate how many books of a certain discounted 
# price we have, and sum all of that up.
# The advantage of this algorithm is that it uses NO `in` except once, and that
# one use runs in O(1) because the size is bounded by 6. Also, we never have to
# call `remove()`, all is done by arithmetic.
def total(basket: List[int]) -> int:
    counter = Counter(basket)
    
    groups = [0] * 6
    
    # "Work horse" of the discount optimization.
    # For the explanation, see above.
    while len(counter):
        group_size = len(counter)
        if group_size == 3 and groups[5] > 0:
            groups[4] += 2
            groups[5] -= 1
        else:
            groups[group_size] += 1
        # decrement each book count by one
        counter.subtract(counter.keys())
        # Remove the zero ones
        counter = +counter
    
    # Now we just sum up the discounted prices for each book
    return sum(count * size * DISCOUNTED_PRICES[size] for size, count in enumerate(groups))
