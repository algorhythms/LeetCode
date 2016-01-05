"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
__author__ = 'Danyang'


class Solution:
    def isValid(self, s):
        """
        Algorithm: Stack
        :param s: string
        :return: boolean
        """
        put_set = ("(", "[", "{")
        pop_set = (")", "]", "}")
        pair = dict(zip(put_set, pop_set))

        stack = []
        for element in s:
            if element in put_set:
                stack.append(pair[element])
            elif element in pop_set:
                if not stack or element != stack.pop():  # check NullPointer, otherwise, IndexError: pop from empty list
                    return False

        return True if not stack else False


if __name__ == "__main__":
    assert Solution().isValid("()")