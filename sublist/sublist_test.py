import unittest

from sublist import sublist, SUBLIST, SUPERLIST, EQUAL, UNEQUAL, binsearch, encode, has_prefix, has_prefix_compressed, bad_char_table, good_suffix_table, bad_char_table2, good_suffix_table2

# Tests adapted from `problem-specifications//canonical-data.json`


class SublistTest(unittest.TestCase):
    #@unittest.skip("demonstrating skipping")
    def test_empty_lists(self):
        self.assertEqual(sublist([], []), EQUAL)

    #@unittest.skip("demonstrating skipping")
    def test_empty_list_within_non_empty_list(self):
        self.assertEqual(sublist([], [1, 2, 3]), SUBLIST)

    #@unittest.skip("demonstrating skipping")
    def test_non_empty_list_contains_empty_list(self):
        self.assertEqual(sublist([1, 2, 3], []), SUPERLIST)

    #@unittest.skip("demonstrating skipping")
    def test_list_equals_itself(self):
        self.assertEqual(sublist([1, 2, 3], [1, 2, 3]), EQUAL)

    #@unittest.skip("demonstrating skipping")
    def test_different_lists(self):
        self.assertEqual(sublist([1, 2, 3], [2, 3, 4]), UNEQUAL)

    #@unittest.skip("demonstrating skipping")
    def test_false_start(self):
        self.assertEqual(sublist([1, 2, 5], [0, 1, 2, 3, 1, 2, 5, 6]), SUBLIST)

    #@unittest.skip("demonstrating skipping")
    def test_consecutive(self):
        self.assertEqual(sublist([1, 1, 2], [0, 1, 1, 1, 2, 1, 2]), SUBLIST)

    #@unittest.skip("demonstrating skipping")
    def test_sublist_at_start(self):
        self.assertEqual(sublist([0, 1, 2], [0, 1, 2, 3, 4, 5]), SUBLIST)

    #@unittest.skip("demonstrating skipping")
    def test_sublist_in_middle(self):
        self.assertEqual(sublist([2, 3, 4], [0, 1, 2, 3, 4, 5]), SUBLIST)

    #@unittest.skip("demonstrating skipping")
    def test_sublist_at_end(self):
        self.assertEqual(sublist([3, 4, 5], [0, 1, 2, 3, 4, 5]), SUBLIST)

    #@unittest.skip("demonstrating skipping")
    def test_at_start_of_superlist(self):
        self.assertEqual(sublist([0, 1, 2, 3, 4, 5], [0, 1, 2]), SUPERLIST)

    #@unittest.skip("demonstrating skipping")
    def test_in_middle_of_superlist(self):
        self.assertEqual(sublist([0, 1, 2, 3, 4, 5], [2, 3]), SUPERLIST)

    #@unittest.skip("demonstrating skipping")
    def test_at_end_of_superlist(self):
        self.assertEqual(sublist([0, 1, 2, 3, 4, 5], [3, 4, 5]), SUPERLIST)

    #@unittest.skip("demonstrating skipping")
    def test_first_list_missing_element_from_second_list(self):
        self.assertEqual(sublist([1, 3], [1, 2, 3]), UNEQUAL)

    #@unittest.skip("demonstrating skipping")
    def test_second_list_missing_element_from_first_list(self):
        self.assertEqual(sublist([1, 2, 3], [1, 3]), UNEQUAL)

    #@unittest.skip("demonstrating skipping")
    def test_order_matters_to_a_list(self):
        self.assertEqual(sublist([1, 2, 3], [3, 2, 1]), UNEQUAL)

    #@unittest.skip("demonstrating skipping")
    def test_same_digits_but_different_numbers(self):
        self.assertEqual(sublist([1, 0, 1], [10, 1]), UNEQUAL)

    #@unittest.skip("demonstrating skipping")
    # Additional tests for this track
    def test_unique_return_values(self):
        self.assertEqual(len(set([SUBLIST, SUPERLIST, EQUAL, UNEQUAL])), 4)
    
    #@unittest.skip("demonstrating skipping")
    def test_inner_spaces(self):
        self.assertEqual(sublist(["a c"], ["a", "c"]), UNEQUAL)
    
    #@unittest.skip("demonstrating skipping")
    def test_large_lists(self):
        self.assertEqual(
            sublist(
                list(range(1000)) * 1000 + list(range(1000, 1100)),
                list(range(900, 1050)),
            ),
            SUPERLIST,
        )

    #@unittest.skip("demonstrating skipping")
    def test_spread_sublist(self):
        self.assertEqual(
            sublist(list(range(3, 200, 3)), list(range(15, 200, 15))), UNEQUAL
        )
        
    @unittest.skip("demonstrating skipping")
    def test_large_lists2(self):
        self.assertEqual(
            sublist(
                list([0] * 1000000),
                list(([0] * 500000) + [1]),
            ),
            UNEQUAL,
        )
        
    # binsearch
    
    def test_binsearch_zero(self):
        self.assertEqual(
            binsearch([[0, 0, 0, 1], [1, 1, 1, 1], [2, 2, 2, 1], [3, 3, 3, 1], [4, 4, 4, 1], [5, 5, 5, 1]], 0), ([0, 0, 0, 1], 0)
        )
        
    def test_binsearch_one(self):
        self.assertEqual(
            binsearch([[0, 0, 0, 1], [1, 1, 1, 1], [2, 2, 2, 1], [3, 3, 3, 1], [4, 4, 4, 1], [5, 5, 5, 1]], 1), ([1, 1, 1, 1], 1)
        )
        
    def test_binsearch_two(self):
        self.assertEqual(
            binsearch([[0, 0, 0, 1], [1, 1, 1, 1], [2, 2, 2, 1], [3, 3, 3, 1], [4, 4, 4, 1], [5, 5, 5, 1]], 2), ([2, 2, 2, 1], 2)
        )

    def test_binsearch_three(self):
        self.assertEqual(
            binsearch([[0, 0, 0, 1], [1, 1, 1, 1], [2, 2, 2, 1], [3, 3, 3, 1], [4, 4, 4, 1], [5, 5, 5, 1]], 3), ([3, 3, 3, 1], 3)
        )
        
    def test_binsearch_four(self):
        self.assertEqual(
            binsearch([[0, 0, 0, 1], [1, 1, 1, 1], [2, 2, 2, 1], [3, 3, 3, 1], [4, 4, 4, 1], [5, 5, 5, 1]], 4), ([4, 4, 4, 1], 4)
        )
        
    def test_binsearch_five(self):
        self.assertEqual(
            binsearch([[0, 0, 0, 1], [1, 1, 1, 1], [2, 2, 2, 1], [3, 3, 3, 1], [4, 4, 4, 1], [5, 5, 5, 1]], 5), ([5, 5, 5, 1], 5)
        )
        
    # prefix finding:
    
    def test_has_prefix_6(self):
        list_one = "aaaaaab"
        self.assertEqual(
            has_prefix(list_one, list_one[6+1:]), True
        )
        
    def test_has_prefix_compressed_6(self):
        list_one = "aaaaaab"
        self.assertEqual(
            has_prefix_compressed(encode(list_one), 6+1), True
        )
        
    def test_has_prefix_5(self):
        list_one = "aaaaaab"
        self.assertEqual(
            has_prefix(list_one, list_one[5+1:]), False
        )
        
    def test_has_prefix_compressed_5(self):
        list_one = "aaaaaab"
        self.assertEqual(
            has_prefix_compressed(encode(list_one), 5+1), False
        )
        
    def test_has_prefix_4(self):
        list_one = "aaaaaab"
        self.assertEqual(
            has_prefix(list_one, list_one[4+1:]), False
        )
        
    def test_has_prefix_compressed_4(self):
        list_one = "aaaaaab"
        self.assertEqual(
            has_prefix_compressed(encode(list_one), 4+1), False
        )
        
    def test_has_prefix_3(self):
        list_one = "aaaaaab"
        self.assertEqual(
            has_prefix(list_one, list_one[3+1:]), False
        )
        
    def test_has_prefix_compressed_3(self):
        list_one = "aaaaaab"
        self.assertEqual(
            has_prefix_compressed(encode(list_one), 3+1), False
        )
        
    def test_has_prefix_2(self):
        list_one = "aaaaaab"
        self.assertEqual(
            has_prefix(list_one, list_one[2+1:]), False
        )
        
    def test_has_prefix_compressed_2(self):
        list_one = "aaaaaab"
        self.assertEqual(
            has_prefix_compressed(encode(list_one), 2+1), False
        )
        
    def test_has_prefix_1(self):
        list_one = "aaaaaab"
        self.assertEqual(
            has_prefix(list_one, list_one[1+1:]), False
        )
        
    def test_has_prefix_compressed_1(self):
        list_one = "aaaaaab"
        self.assertEqual(
            has_prefix_compressed(encode(list_one), 1+1), False
        )
        
    def test_has_prefix_0(self):
        list_one = "aaaaaab"
        self.assertEqual(
            has_prefix(list_one, list_one[0+1:]), False
        )
        
    def test_has_prefix_compressed_0(self):
        list_one = "aaaaaab"
        self.assertEqual(
            has_prefix_compressed(encode(list_one), 0+1), False
        )
        
    def longest_common_suffix_0(self):
        list_one = "aaaaaab"
        self.assertEqual(
            longest_common_suffix(list_one, list_one[1:0+1]), 0
        )
        
    def longest_common_suffix_1(self):
        list_one = "aaaaaab"
        self.assertEqual(
            longest_common_suffix(list_one, list_one[1:1+1]), 0
        )
        
    def longest_common_suffix_2(self):
        list_one = "aaaaaab"
        self.assertEqual(
            longest_common_suffix(list_one, list_one[1:2+1]), 0
        )
        
    def longest_common_suffix_3(self):
        list_one = "aaaaaab"
        self.assertEqual(
            longest_common_suffix(list_one, list_one[1:3+1]), 0
        )
        
    def longest_common_suffix_4(self):
        list_one = "aaaaaab"
        self.assertEqual(
            longest_common_suffix(list_one, list_one[1:4+1]), 0
        )
        
    def longest_common_suffix_5(self):
        list_one = "aaaaaab"
        self.assertEqual(
            longest_common_suffix(list_one, list_one[1:5+1]), 0
        )
        
    def test_bad_char_table_abc(self):
        list_one = "abc"
        actual = bad_char_table(list_one)
        expected = {
            'a': 2, 'b': 1, 'c': 3
        }
        self.assertEqual(
            actual, expected
        )
        
    def test_good_suffix_table_abc(self):
        list_one = "abc"
        actual = good_suffix_table(list_one)
        expected = [5, 4, 1]
        self.assertEqual(
            actual, expected
        )
    
    def test_bad_char_table_mississi(self):
        list_one = "mississi"
        actual = bad_char_table(list_one)
        expected = {
            'i': 3, 'm': 7, 's': 1
        }
        self.assertEqual(
            actual, expected
        )
        
    def test_good_suffix_table_mississi(self):
        list_one = "mississi"
        actual = good_suffix_table(list_one)
        expected = [15, 14, 13, 7, 11, 10, 7, 1]
        self.assertEqual(
            actual, expected
        )
        
    def test_bad_char_table_abcxxxabc(self):
        list_one = "abcxxxabc"
        actual = bad_char_table(list_one)
        expected = {
            'a': 2, 'b': 1, 'c': 6, 'x': 3
        }
        self.assertEqual(
            actual, expected
        )
        
    def test_good_suffix_table_abcxxxabc(self):
        list_one = "abcxxxabc"
        actual = good_suffix_table(list_one)
        expected = [14, 13, 12, 11, 10, 9, 11, 10, 1]
        self.assertEqual(
            actual, expected
        )
        
    def test_bad_char_table_abyxcdeyx(self):
        list_one = "abyxcdeyx"
        actual = bad_char_table(list_one)
        expected = {
            'a': 8, 'b': 7, 'c': 4, 'd': 3, 'e': 2, 'y': 1, 'x': 5
        }
        self.assertEqual(
            actual, expected
        )
        
    def test_good_suffix_table_abyxcdeyx(self):
        list_one = "abyxcdeyx"
        actual = good_suffix_table(list_one)
        expected = [17, 16, 15, 14, 13, 12, 7, 10, 1]
        self.assertEqual(
            actual, expected
        )
        
    # own
    
    def test_bad_char_table2_abc(self):
        list_one = "abc"
        actual = bad_char_table2(encode(list_one))
        expected = {
            'a': 2, 'b': 1, 'c': 3
        }
        self.assertEqual(
            actual, expected
        )
        
    def test_good_suffix_table2_abc(self):
        list_one = "abc"
        actual = good_suffix_table2(list_one, encode(list_one))
        expected = [5, 4, 1]
        self.assertEqual(
            actual, expected
        )
    
    def test_bad_char_table2_mississi(self):
        list_one = "mississi"
        actual = bad_char_table2(encode(list_one))
        expected = {
            'i': 3, 'm': 7, 's': 1
        }
        self.assertEqual(
            actual, expected
        )
        
    def test_good_suffix_table2_mississi(self):
        list_one = "mississi"
        actual = good_suffix_table2(list_one, encode(list_one))
        expected = [15, 14, 13, 7, 11, 10, 7, 1]
        self.assertEqual(
            actual, expected
        )
        
    def test_bad_char_table2_abcxxxabc(self):
        list_one = "abcxxxabc"
        actual = bad_char_table2(encode(list_one))
        expected = {
            'a': 2, 'b': 1, 'c': 6, 'x': 3
        }
        self.assertEqual(
            actual, expected
        )
        
    def test_good_suffix_table2_abcxxxabc(self):
        list_one = "abcxxxabc"
        actual = good_suffix_table2(list_one, encode(list_one))
        expected = [14, 13, 12, 11, 10, 9, 11, 10, 1]
        self.assertEqual(
            actual, expected
        )
        
    def test_bad_char_table2_abyxcdeyx(self):
        list_one = "abyxcdeyx"
        actual = bad_char_table2(encode(list_one))
        expected = {
            'a': 8, 'b': 7, 'c': 4, 'd': 3, 'e': 2, 'y': 1, 'x': 5
        }
        self.assertEqual(
            actual, expected
        )
        
    def test_good_suffix_table2_abyxcdeyx(self):
        list_one = "abyxcdeyx"
        actual = good_suffix_table2(list_one, encode(list_one))
        expected = [17, 16, 15, 14, 13, 12, 7, 10, 1]
        self.assertEqual(
            actual, expected
        )

if __name__ == "__main__":
    unittest.main()
