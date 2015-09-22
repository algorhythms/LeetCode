"""
Given a string, find the length of the longest substring without repeating characters. For example, the longest
substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring
is "b", with the length of 1.
"""
__author__ = 'Danyang'


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        Algorithm: Hash Map, two pointers
        Hash Map: array visited = [] for all ascii, notice the algorithm of updating this array
        Two pointers: start - start of the string; ind - scanning

        Given a string, find the length of the longest substring without repeating characters.
        :param s: String
        :return: Integer
        """
        # last visited index in the string
        visited_last_index = [-1 for _ in range(256)]  # ascii
        longest = 0  # record result

        start = 0  # pointer
        for ind, val in enumerate(s):
            if visited_last_index[ord(val)] == -1:
                longest = max(longest, (ind)-start+1)
            else:
                longest = max(longest, (ind-1)-start+1)

                # unmark
                for i in range(start, visited_last_index[ord(val)]):
                    visited_last_index[ord(s[i])] = -1

                start = visited_last_index[ord(val)]+1

            visited_last_index[ord(val)] = ind  # update last visited index

        return longest