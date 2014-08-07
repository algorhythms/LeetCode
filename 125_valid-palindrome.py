__author__ = 'Danyang'
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = s.lower()
        # import re  # not supported
        # s = re.sub('[^a-zA-Z0-9]', '', s)  # not supported
        s = ''.join(e for e in s if e.isalnum())
        if not s:
            return True

        s2 = s[::-1]
        return s2==s