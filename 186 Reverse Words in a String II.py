"""
Premium Question
"""
__author__ = 'Daniel'


class Solution(object):
    def reverseWords(self, s):
        """
        in-place without allocating extra space

        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        self.reverse(s, 0, len(s))
        i = 0
        while i < len(s):
            j = i+1
            while j < len(s) and s[j] != " ":
                j += 1

            self.reverse(s, i, j)
            i = j+1

    def reverse(self, s, start, end):
        i = start
        j = end
        while i < j-1:
            s[i], s[j-1] = s[j-1], s[i]
            i += 1
            j -= 1

if __name__ == "__main__":
    lst = list("the sky is blue")
    Solution().reverseWords(lst)
    assert "".join(lst) == "blue is sky the"