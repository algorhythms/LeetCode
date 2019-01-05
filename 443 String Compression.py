#!/usr/bin/python3
"""
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?
"""


class Solution:
    def compress(self, chars):
        """
        tedious pointer manipulation
        :type chars: List[str]
        :rtype: int
        """
        ret = 1
        s = 0  # start index of current char
        for i in range(1, len(chars) + 1):
            if i < len(chars) and chars[i] == chars[s]:
                continue
            l = i - s
            if l > 1:
                for digit in str(l):
                    chars[ret] = digit
                    ret += 1
            if i < len(chars):
                chars[ret] = chars[i]
                ret += 1
                s = i
                
        return ret

    def compress_error(self, chars):
        """
        tedious pointer manipulation
        :type chars: List[str]
        :rtype: int
        """
        s = 0
        for idx in range(1, len(chars) + 1):
            if idx < len(chars) and chars[idx] == chars[s]:
                continue
            l = idx - s
            if l == 1:
                s = min(s + 1, len(chars) - 1)
            else:
                for digit in str(l):
                    s += 1
                    chars[s] = digit
                if idx < len(chars):
                    s += 1
                    chars[s] = chars[idx]
        return s + 1


if __name__ == "__main__":
    assert Solution().compress(["a"]) == 1
    assert Solution().compress(["a","a","b","b","c","c","c"]) == 6
    assert Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]) == 4
