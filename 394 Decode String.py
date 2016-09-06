"""
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly
k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat
numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""
__author__ = 'Daniel'


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = [
            [1, []]
        ]  # with default
        i = 0
        while i < len(s):
            if s[i].isdigit():  # construct number from digit
                j = i+1
                while s[j] != '[': j += 1
                stk.append([
                    int(s[i:j]), []
                ])
                i = j+1
            elif s[i].islower():  # append alphabet
                stk[-1][1].append(s[i])
                i += 1
            elif s[i] == ']':  # pop
                cnt, partial = stk.pop()
                partial = ''.join(partial) * cnt
                stk[-1][1].append(partial)
                i += 1

        return ''.join(stk.pop()[1])


class SolutionVerbose(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = []
        i = 0
        ret = []
        while i < len(s):
            if s[i].isdigit():  # construct number from digit
                j = i+1
                while s[j] != '[': j += 1
                stk.append([
                    int(s[i:j]), []
                ])
                i = j+1
            elif s[i].islower():  # append alphabet
                if not stk:
                    ret.append(s[i])
                else:
                    stk[-1][1].append(s[i])
                i += 1
            elif s[i] == ']':  # pop
                cnt, partial = stk.pop()
                partial = ''.join(partial) * cnt
                if not stk:
                   ret.append(partial)
                else:
                    stk[-1][1].append(partial)

                i += 1

        return ''.join(ret)


class SolutionError(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = []
        i = 0
        ret = []
        while i < len(s):
            if s[i].isdigit():
                j = i + 1
                while s[j] != '[': j += 1
                prev = stk[-1] if stk else 1
                stk.append(prev * int(s[i:j]))
                i = j + 1
            elif s[i].islower():
                repeat = stk[-1] if stk else 1
                for _ in xrange(repeat): ret.append(s[i])
                i += 1
            elif s[i] == ']':
                stk.pop()
                i += 1

        return ''.join(ret)


if __name__ == "__main__":
    assert Solution().decodeString('2[abc]3[cd]ef') == 'abcabccdcdcdef'




