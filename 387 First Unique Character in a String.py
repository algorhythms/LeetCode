"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.


"""
__author__ = 'Daniel'


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1

        first = {}
        for i, v in enumerate(list(s)):
            if v not in first:
                first[v] = i
            else:
                first[v] = -1

        lst = filter(lambda x: x != -1, first.values())
        return min(lst) if lst else -1


if __name__ == "__main__":
    assert Solution().firstUniqChar("leetcode") == 0