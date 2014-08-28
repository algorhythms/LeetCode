__author__ = 'Danyang'
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        Algorithm: Hash table, two pointers
        Given a string, find the length of the longest substring without repeating characters.
        :param s: String
        :return: Integer
        """
        # last visited index in the string
        visited_last_index = [-1 for _ in range(256)]  # ascii


        longest = 0
        start = 0
        for ind, val in enumerate(s):
            if visited_last_index[ord(val)]==-1:
                longest = max(longest, (ind)-start+1)
            else:
                longest = max(longest, (ind-1)-start+1)

                # unmark
                for i in range(start, visited_last_index[ord(val)]):
                    visited_last_index[ord(s[i])] = -1

                start = visited_last_index[ord(val)]+1

            visited_last_index[ord(val)] = ind  # update last visited index
        return longest