SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3

import sys


def sublist(list_one, list_two):
    if not list_one and not list_two:
        return EQUAL
    if not list_one:
        return SUBLIST
    if not list_two:
        return SUPERLIST
    
    if len(list_one) == len(list_two) and list_one == list_two:
        return EQUAL
    
    if len(list_one) < len(list_two):
        compressed_two = encode(list_two)
        #if is_sparse(compressed_two, list_two):
        if True:
            #if _check_sublist2(list_one, list_two, encode(list_one), compressed_two):
            if kmp_search(list_two, list_one):
                return SUBLIST
        else:
            if _check_sublist(list_one, list_two):
                return SUBLIST
    
    if len(list_two) < len(list_one):
        compressed_one = encode(list_one)
        #if is_sparse(compressed_one, list_one):
        if True:
            print("is sparse")
            #if _check_sublist2(list_two, list_one, encode(list_two), compressed_one):
            if kmp_search(list_one, list_two):
                return SUPERLIST
        else:
            print("Not sparse")
            if _check_sublist(list_two, list_one):
                return SUPERLIST
    
    #if len(list_one) < len(list_two) and _check_sublist(list_one, list_two):
    #    return SUBLIST
    #if len(list_one) > len(list_two) and _check_sublist(list_two, list_one):
    #    return SUPERLIST
    return UNEQUAL
    
def _check_sublist(list_one, list_two):
    table = bad_char_table(list_one)
    table2 = good_suffix_table(list_one)
    i = len(list_one) - 1
    j = len(list_one) - 1
    while i < len(list_two):
        j = len(list_one) - 1
        while j >= 0 and list_one[j] == list_two[i]:
            j -= 1
            i -= 1
        if j < 0:
            return True
        i += max(table2[j], table.get(list_two[j], len(list_one)))
    return False
    
def bad_char_table(list_one):
    last = len(list_one) - 1
    m = {}
    m[list_one[-1]] = len(list_one)
    for i, v in enumerate(list_one):
        if i == last:
            break
        m[v] = last - i
    print(f"bc table: {m}")
    return m
    
def bad_char_table2(list_compressed):
    print(f"the list: {list_compressed}")
    last = len(list_compressed) - 1
    real_last = list_compressed[-1][1]
    m = {}
    m[list_compressed[-1][2]] = real_last + 1
    for i, t in enumerate(list_compressed):
        if i == last:
            if t[3] > 1:
                m[t[2]] = real_last - 1
            break
        m[t[2]] = real_last - t[1]
    #m = {
    #    t[2]: list_compressed[-1][3] - t[1]
    #    for t in list_compressed
    #}
    #m[list_compressed[-1][2]] = list_compressed[-1][3] + 1
    print(f"bc table: {m}")
    return m
    
def good_suffix_table(list_one):
    table = [0] * len(list_one)
    last = len(list_one) - 1
    last_prefix = last
    print("first pass")
    for i in range(last, -1, -1):
        #if has_prefix(list_one, list_one[i+1:]):
        if has_prefix2(list_one, list_one, i+1):
            last_prefix = i + 1
        # lastPrefix is the shift, and (last-i) is len(suffix).
        print(f"i={i}, value: {last_prefix + last - i}")
        table[i] = last_prefix + last - i

    # Second pass: find repeats of pattern's suffix starting from the front.
    print("Second pass")
    for i in range(0, last):
        #len_suffix = longest_common_suffix(list_one, list_one[1:i+1])
        len_suffix = longest_common_suffix2(list_one, list_one, i+1)
        print(f"i={i}, len_suffix={len_suffix}, list_one_index={i-len_suffix}, list_one_index_2={last-len_suffix}")
        if list_one[i-len_suffix] != list_one[last-len_suffix]:
            # (last-i) is the shift, and lenSuffix is len(suffix).
            table[last-len_suffix] = len_suffix + last - i
            print(f"i={i}, table index={last-len_suffix}, table value={len_suffix + last - i}, len_suffix={len_suffix}")
            
    print(f"gs table: {table}")
    return table

def has_prefix2(a, prefix, idx):
    print(f"has_prefix2. a: {a}, prefix: {prefix}, idx: {idx}")
    if len(a) < len(prefix) - idx:
        print("Too small, so return false")
        return False
    i = 0
    while i < len(prefix) - idx:
        if a[i] != prefix[idx]:
            print(f"mismatch: i={i}, idx={idx}, a={a[i]}, prefix={prefix[idx]}")
            return False
        idx += 1
        i += 1
    return True
    
def has_prefix(a, prefix):
    print(f"{a} vs {prefix}")
    if len(a) < len(prefix):
        print("special case")
        return False
    i = 0
    print(f"prefix size: {len(prefix)}")
    print("Start")
    while i < len(prefix):
        print(f"Iteration {i}")
        print(f"Comparing: {a[i]}, {prefix[i]}")
        if a[i] != prefix[i]:
            print("mismatch")
            return False
        print("was equal")
        i += 1
    print("completely equal")
    return True
    #return len(a) >= len(prefix) and a[:len(prefix)] == prefix
    
def has_prefix_compressed(string, start):
    print(f"start: {start}, string: {string}")
    #print(f"Start: {start}")
    ret = binsearch(string, start)
    if ret is None:
        print("Ret is none")
        return True
    prefix_part, prefix_idx = ret
    print(f"prefix_part: {prefix_part}")
    #print(f"binsearch_res: {prefix_part}, {prefix_idx}")
    prefix_len = string[-1][1] - start + 1
    print(f"prefix_len: {prefix_len}")
    full_index = start
    real_index_from_start = 0
    i = 0
    while real_index_from_start < prefix_len:
        string_part = string[i]
        prefix_part = string[prefix_idx]
        prefix_part_length = min(prefix_part[1] - start + 1, prefix_part[3])
        print(f"string_part: {string_part}")
        print(f"prefix_part: {prefix_part}")
        print(f"prefix_part_length: {prefix_part_length}")
        #The parts need to have the same char and length
        if string_part[2] != prefix_part[2] or string_part[3] != prefix_part_length:
            print(f"Mismatch found at: {full_index}")
            return False
        print("no mismatch yet")
        full_index += prefix_part_length
        real_index_from_start += prefix_part_length
        prefix_idx += 1
        i += 1
    print("Done iterating")
    return True

def longest_common_suffix2(list_one, list_two, end):
    i = 0
    m = end - 1
    while i < min(len(list_one), m):
        if list_one[len(list_one)-1-i] != list_two[m-i]:
            return i
        i += 1
    return i
    
def longest_common_suffix(list_one, list_two):
    i = 0
    while i < min(len(list_one), len(list_two)):
        if list_one[len(list_one)-1-i] != list_two[len(list_two)-1-i]:
            return i
        i += 1
    return i
    
def longest_common_suffix_compressed(list_one, end):
    full_length = list_one[-1][1] + 1
    i = 0
    string_part = list_one[-1]
    str_idx = len(list_one) - 1
    suffix_part, suffix_idx = binsearch(list_one, end - 1)
    full_len_list_2 = end - 1
    while i < full_len_list_2:
        suffix_part = list_one[suffix_idx]
        string_part = list_one[str_idx]
        suffix_part_length = suffix_part[1] - suffix_part[0] + 1
        print(f"string_part: {string_part}")
        print(f"suffix_part: {suffix_part}")
        print(f"suffix_part_length: {suffix_part_length}")
        print("-------------------------")
        
        if suffix_part[0] == 0:
            # In this case, we have to disregard the very first element
            if string_part[2] != suffix_part[2] or string_part[3] != suffix_part_length - 1:
                print("Returning case 1")
                print(f"chars: {string_part[2]} vs {suffix_part[2]}, lengths: {string_part[3]} vs {suffix_part_length - 1}")
                return i
            str_idx -= 1
            suffix_idx -= 1
            i += suffix_part_length - 1
        else:
            # In this case, we have to regard all elements of the parts
            if string_part[2] != suffix_part[2] or string_part[3] != suffix_part_length:
                print("Returning case 2")
                print(f"chars: {string_part[2]} vs {suffix_part[2]}, lengths: {string_part[3]} vs {suffix_part_length}")
                return i
            str_idx -= 1
            suffix_idx -= 1
            i += suffix_part_length
        # loop end
    return full_len_list_2
    
def encode(_list):
    # o = []
    o = [[0, 0, _list[0], 1]]
    # (start, end, element), all inclusive
    # current = [0, 0, _list[0], 1]
    i = 1
    while i < len(_list):
        if o[-1][2] != _list[i]:
            o.append([i, i, _list[i], 1])
            #current = [i, i, _list[i], 1]
        else:
            o[-1][1] += 1
            o[-1][3] += 1
        i += 1
    
    #print(o)
    return o
    
def good_size_reduction(_compressed, _uncompressed):
    print(f"{len(_compressed)} < {2 * len(_uncompressed) / 3}")
    return len(_compressed) < 2 * len(_uncompressed) / 3
    
def is_sparse(_compressed, _uncompressed):
    return good_size_reduction(_compressed, _uncompressed) and median_segment_length(_compressed) > len(_uncompressed) ** (1/3.)
    
def median_segment_length(_compressed):
    l = sorted(_compressed)[len(_compressed) // 2][3]
    print(f"median {l}")
    return l
    
def binsearch(lis, to_find):
    lo = 0
    hi = len(lis)
    while lo < hi:
        mid = (lo + hi) // 2
        if to_find < lis[mid][0]:
            hi = mid
        elif to_find > lis[mid][1]:
            lo = mid + 1
        else:
            return lis[mid], mid
    return None
    
def _check_sublist2(list_one, list_two, c_1, c_2):
    table = bad_char_table2(c_1)
    table2 = good_suffix_table2(list_one, c_1)
    i = len(list_one) - 1
    j = len(list_one) - 1
    while i < len(list_two):
        j = len(list_one) - 1
        p = c_1[-1]
        t, k = binsearch(c_2, i)
        l = len(c_1) - 1
        while l >= 0 and p[2] == t[2] and p[3] <= t[3]:
            l -= 1
            k -= 1
            j -= p[3]
            i -= p[3]
            p = c_1[l]
            if i >= 0:
                t, k = binsearch(c_2, i)
        if l < 0:
            return True
        i += max(table2[j], table.get(list_two[j], len(list_one)))
    return False
    
def z_based_good_suffix_table(_list):
    n = len(_list)
    N = algorithm_z(_list[::-1])[::-1]
    L = [0] * n
    j = 0
    while j < n - 1:
        i = n - N[j]
        L[i] = j
    return L
        
# Based on https://www.hackerearth.com/practice/algorithms/string-algorithm/z-algorithm/tutorial/
def algorithm_z(s):
    L = 0
    R = 0
    n = len(s)
    z = [0] * n
    for i in range(1, n): 
        if i > R:
            L = R = i
            while R < n and s[R-L] == s[R]:
                R += 1
            z[i] = R-L 
            R -= 1
        else:
            k = i-L
            if z[k] < R-i+1: 
                z[i] = z[k]
            else:
                L = i
                while R < n and s[R-L] == s[R]: 
                    R += 1
                z[i] = R-L 
                R -= 1
    return z
        

def good_suffix_table2(list_one, compressed_list):
    table = [0] * len(list_one)
    last = len(list_one) - 1
    last_prefix = last
    print("First pass")
    for i in range(last, -1, -1):
        #if has_prefix(list_one, list_one[i+1:]):
        if has_prefix_compressed(compressed_list, i+1):
            print(f"i={i}, has_prefix_compressed=True, so has_prefix={i+1}")
            last_prefix = i + 1
        else:
            print(f"i={i}, has_prefix_compressed=False")
        # lastPrefix is the shift, and (last-i) is len(suffix).
        print(f"i={i}, value={last_prefix + last - i}")
        table[i] = last_prefix + last - i

    print("second pass")
    # Second pass: find repeats of pattern's suffix starting from the front.
    for i in range(0, last):
        #len_suffix = longest_common_suffix(list_one, list_one[1:i+1])
        len_suffix = longest_common_suffix_compressed(compressed_list, i+1)
        print(f"i={i}, len_suffix={len_suffix}, list_one_index={i-len_suffix}, list_one_index_2={last-len_suffix}")
        if list_one[i-len_suffix] != list_one[last-len_suffix]:
            # (last-i) is the shift, and lenSuffix is len(suffix).
            table[last-len_suffix] = len_suffix + last - i
            print(f"i={i}, table index={last-len_suffix}, table value={len_suffix + last - i}, len_suffix={len_suffix}")
            
    print(f"gs table: {table}")
    return table
    
class Reverse:
    def __init__(self, source):
        self.source = source
    
    def __len__():
        return len(self.source)
        
    def __getitem__(self, key):
        return self.source[self.__len__() - 1 - key]
        
    def __setitem__(self, key, value):
        self.source[self.__len__() - 1 - key] = value
        
    def __delitem__(self, key):
        pass
    
import string


def z_array(s):
    """ Use Z algorithm (Gusfield theorem 1.4.1) to preprocess s """
    assert len(s) > 1
    z = [len(s)] + [0] * (len(s)-1)

    # Initial comparison of s[1:] with prefix
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            z[1] += 1
        else:
            break
    
    r, l = 0, 0
    if z[1] > 0:
        r, l = z[1], 1

    for k in range(2, len(s)):
        assert z[k] == 0
        if k > r:
            # Case 1
            for i in range(k, len(s)):
                if s[i] == s[i-k]:
                    z[k] += 1
                else:
                    break
            r, l = k + z[k] - 1, k
        else:
            # Case 2
            # Calculate length of beta
            nbeta = r - k + 1
            zkp = z[k - l]
            if nbeta > zkp:
                # Case 2a: zkp wins
                z[k] = zkp
            else:
                # Case 2b: Compare characters just past r
                nmatch = 0
                for i in range(r+1, len(s)):
                    if s[i] == s[i - k]:
                        nmatch += 1
                    else:
                        break
                l, r = k, r + nmatch
                z[k] = r - k + 1
    return z


def n_array(s):
    """ Compile the N array (Gusfield theorem 2.2.2) from the Z array """
    return z_array(s[::-1])[::-1]


def big_l_prime_array(p, n):
    """ Compile L' array (Gusfield theorem 2.2.2) using p and N array.
        L'[i] = largest index j less than n such that N[j] = |P[i:]| """
    lp = [0] * len(p)
    for j in range(len(p)-1):
        i = len(p) - n[j]
        if i < len(p):
            lp[i] = j + 1
    return lp


def big_l_array(p, lp):
    """ Compile L array (Gusfield theorem 2.2.2) using p and L' array.
        L[i] = largest index j less than n such that N[j] >= |P[i:]| """
    l = [0] * len(p)
    l[1] = lp[1]
    for i in range(2, len(p)):
        l[i] = max(l[i-1], lp[i])
    return l


def small_l_prime_array(n):
    """ Compile lp' array (Gusfield theorem 2.2.4) using N array. """
    small_lp = [0] * len(n)
    for i in range(len(n)):
        if n[i] == i+1:  # prefix matching a suffix
            small_lp[len(n)-i-1] = i+1
    for i in range(len(n)-2, -1, -1):  # "smear" them out to the left
        if small_lp[i] == 0:
            small_lp[i] = small_lp[i+1]
    return small_lp


def good_suffix_table3(p):
    """ Return tables needed to apply good suffix rule. """
    n = n_array(p)
    lp = big_l_prime_array(p, n)
    return lp, big_l_array(p, lp), small_l_prime_array(n)


def good_suffix_mismatch(i, big_l_prime, small_l_prime):
    """ Given a mismatch at offset i, and given L/L' and l' arrays,
        return amount to shift as determined by good suffix rule. """
    length = len(big_l_prime)
    assert i < length
    if i == length - 1:
        return 0
    i += 1  # i points to leftmost matching position of P
    if big_l_prime[i] > 0:
        return length - big_l_prime[i]
    return length - small_l_prime[i]


def good_suffix_match(small_l_prime):
    """ Given a full match of P to T, return amount to shift as
        determined by good suffix rule. """
    return len(small_l_prime) - small_l_prime[1]


def dense_bad_char_tab(p, amap):
    """ Given pattern string and list with ordered alphabet characters, create
        and return a dense bad character table.  Table is indexed by offset
        then by character. """
    tab = []
    nxt = [0] * len(amap)
    for i in range(0, len(p)):
        c = p[i]
        print(c)
        assert c in amap
        tab.append(nxt[:])
        nxt[amap[c]] = i+1
    return tab
    
class BoyerMoore(object):
    """ Encapsulates pattern and associated Boyer-Moore preprocessing. """

    def __init__(self, p, alphabet='ACGT'):
        # Create map from alphabet characters to integers
        self.amap = {alphabet[i]: i for i in range(len(alphabet))}
        # Make bad character rule table
        self.bad_char = dense_bad_char_tab(p, self.amap)
        # Create good suffix rule table
        _, self.big_l, self.small_l_prime = good_suffix_table3(p)

    def bad_character_rule(self, i, c):
        """ Return # skips given by bad character rule at offset i """
        assert c in self.amap
        assert i < len(self.bad_char)
        ci = self.amap[c]
        return i - (self.bad_char[i][ci]-1)

    def good_suffix_rule(self, i):
        """ Given a mismatch at offset i, return amount to shift
            as determined by (weak) good suffix rule. """
        length = len(self.big_l)
        assert i < length
        if i == length - 1:
            return 0
        i += 1  # i points to leftmost matching position of P
        if self.big_l[i] > 0:
            return length - self.big_l[i]
        return length - self.small_l_prime[i]

    def match_skip(self):
        """ Return amount to shift in case where P matches T """
        return len(self.small_l_prime) - self.small_l_prime[1]
        
def boyer_moore(p, p_bm, t):
    """ Do Boyer-Moore matching """
    i = 0
    occurrences = []
    while i < len(t) - len(p) + 1:
        shift = 1
        mismatched = False
        for j in range(len(p)-1, -1, -1):
            if p[j] != t[i+j]:
                skip_bc = p_bm.bad_character_rule(j, t[i+j])
                skip_gs = p_bm.good_suffix_rule(j)
                shift = max(shift, skip_bc, skip_gs)
                mismatched = True
                break
        if not mismatched:
            occurrences.append(i)
            skip_gs = p_bm.match_skip()
            shift = max(shift, skip_gs)
        i += shift
    return occurrences
    
def kmp_table(pattern):
    T = [-1] * len(pattern)
    pos = 1
    cnd = 0
    while pos < len(pattern):
        if pattern[pos] == pattern[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and pattern[pos] != pattern[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1
    return T
    
def kmp_search(text, pattern):
    j = 0
    k = 0
    table = kmp_table(pattern)
    while j < len(text):
        if text[j] == pattern[k]:
            j += 1
            k += 1
            if k == len(pattern):
                return True
        else:
            k = table[k]
            if k < 0:
                j += 1
                k += 1
    return False
    
def kmp_search_compressed(text, pattern):
    j = 0
    k = 0
    table = kmp_table(pattern)
    text_compressed = encode(text)
    pattern_compressed = encode(pattern)
    text_index = 0
    pattern_index = 0
    while j < len(text):
        text_part = text_compressed[text_index]
        pattern_part = pattern_compressed[pattern_index]
        text_part_length = text_part[1] - j + 1
        pattern_part_length = pattern_part[1] - k + 1
        if pattern_index == len(pattern_compressed) - 1:
            if text_part[2] == pattern_part[2] and pattern_part_length <= text_part_length:
                return True
            else:
                k = table[k]
                if k < 0:
                    j += 1
                    k += 1
                    if j >= len(text):
                        return False
                    text_part, text_index = binsearch(text_compressed, j)
                    pattern_index = 0
                else:
                    pattern_part, pattern_index = binsearch(pattern_compressed, k)
        else:
            if text_part[2] == pattern_part[2] and pattern_part_length == text_part_length:
                j += text_part_length
                k += pattern_part_length
                text_index += 1
                pattern_index += 1
                if j >= len(text):
                        return False
            else:
                k = table[k]
                if k < 0:
                    j += 1
                    k += 1
                    if j >= len(text):
                        return False
                    text_part, text_index = binsearch(text_compressed, j)
                    pattern_index = 0
                else:
                    pattern_part, pattern_index = binsearch(pattern_compressed, k)
    return False
    
    
if __name__ == "__main__":
    #string = "cabdabdab"[::-1]
    #z_table = algorithm_z(string)
    #print(z_table[::-1])
    
    #t = 'haystack needle haystack' # "text" - thing we search in
    #p = 'needle' # "pattern" - thing we search for
    #t = "".join([str(i) for i in list([0] * 1000000)]),
    #p = "".join([str(i) for i in list(([0] * 500000) + [1])]),
    #p_bm = BoyerMoore(p, alphabet='10')
    #print(boyer_moore(p, p_bm, t))
    print(kmp_search_compressed(t, p))
    
    #list_one = "abcxxxabc"
    #print("Starting normal")
    #normal = good_suffix_table(list_one)
    #print("end normal")
    #print("------------------------------")
    #print("Starting compressed")
    #compressed = good_suffix_table2(list_one, encode(list_one))
    #print("end compressed")
    #print("------------------------------")
    #print(f"normal: {normal}")
    #print(f"compressed: {compressed}")
    #expected = [14, 13, 12, 11, 10, 9, 11, 10, 1]
    #self.assertEqual(
    #    actual, expected
    #)
    
    #sublist("this is a test string", "aaaaaab")
    #m = sublist([1, 1, 2], [0, 1, 1, 1, 2, 1, 2])
    #print(f"output: {m}, expected: 0")
    #sublist(
    #            list([0] * 1000000),
    #            list(([0] * 500000) + [1]),
    #        )
