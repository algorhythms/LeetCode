"""
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two's complement method is
used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero
character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1

Output:
"ffffffff"
"""
__author__ = 'Daniel'


class Solution(object):
    def toHex(self, num):
        """
        All use bit manipulation
        :type num: int
        :rtype: str
        """
        ret = []
        while len(ret) < 8 and num:
            ret.append(self.encode(num & 0xf))
            num >>= 4

        return ''.join(ret[::-1]) or '0'

    def toHexNormal(self, num):
        """
        Python arithmetic handles the negative number very well
        :type num: int
        :rtype: str
        """
        ret = []
        while len(ret) < 8 and num:
            ret.append(self.encode(num % 16))
            num /= 16

        return ''.join(ret[::-1]) or '0'

    def encode(self, d):
        if 0 <= d < 10:
            return str(d)

        return chr(ord('a') + d - 10)


if __name__ == "__main__":
    assert Solution().toHex(-1) == 'ffffffff'
