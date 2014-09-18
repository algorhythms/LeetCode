"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed)
parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""
__author__ = 'Danyang'
class Solution:
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
        stack = []  # hold unpaired bracket, either ( or )
        longest = 0
        for ind, char in enumerate(s):
            if char==")" and stack and s[stack[-1]]=="(":  # ), and non-empty stack
                stack.pop()
                if not stack:
                    longest = ind+1
                else:
                    longest = max(longest, ind-stack[-1])
            else:
                stack.append(ind)

        return longest

if __name__=="__main__":
    assert Solution().longestValidParentheses("(()()")==4
    assert Solution().longestValidParentheses("()(()")==2
    assert Solution().longestValidParentheses("(()")==2
    assert Solution().longestValidParentheses(")()())")==4