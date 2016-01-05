"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed)
parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""
__author__ = 'Danyang'


class Solution(object):
    def longestValidParentheses(self, s):
        """
        Stack holds the index of unpaired brackets

        case 1:
        ()())), length is last_paired_index+1
        case 2:
        ))()(), length is last_paired_index - stack[-1]
        case 3:
        (())), length is last_paired_index+1
        case 4:
        ((())(, length is last_paired_index - stack[-1]
        :param s: a string
        :return: an integer
        """
        stk = []  # hold the INDEX of UNPAIRED bracket, either ( or )
        maxa = 0
        for idx, val in enumerate(s):
            if val == ")" and stk and s[stk[-1]] == "(":
                stk.pop()
                if not stk:
                    maxa = max(maxa, idx+1)
                else:
                    maxa = max(maxa, idx-stk[-1])
            else:
                stk.append(idx)

        return maxa


if __name__ == "__main__":
    assert Solution().longestValidParentheses("(()()") == 4
    assert Solution().longestValidParentheses("()(()") == 2
    assert Solution().longestValidParentheses("(()") == 2
    assert Solution().longestValidParentheses(")()())") == 4