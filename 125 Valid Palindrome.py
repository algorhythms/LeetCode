"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""
__author__ = 'Danyang'


class Solution(object):
    def isPalindrome(self, s):
        """

        :param s: a string
        :return: a boolean
        """
        s = s.lower()
        # import re  # not supported
        # s = re.sub('[^a-zA-Z0-9]', '', s)  # not supported
        s = ''.join(e for e in s if e.isalnum())
        if not s:
            return True

        return s == s[::-1]