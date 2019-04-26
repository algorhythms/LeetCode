#!/usr/bin/python3
"""
Premium question
"""


class Solution:
    def parseTernary(self, expression: str) -> str:
        """
        stk from right to left parsing, including the operand and operator
        """
        stk = []
        for c in reversed(expression):
            if stk and stk[-1] == "?":
                stk.pop()  # ?
                first = stk.pop()
                stk.pop()  # :
                second = stk.pop()
                if c == "T":
                    stk.append(first)
                else:
                    stk.append(second)
            else:
                stk.append(c)

        return stk[0]

    def parseTernary_complex(self, expression: str) -> str:
        """
        tokenize + recursive (dfs)?

        stk from right to left, only include the operand

        can handle multiple digit (not required)
        """
        n = len(expression)
        stk = []
        i = n - 1
        while i >= 0:
            j = i
            while j >= 0 and expression[j] not in (":", "?"):
                j -= 1

            if j < i:
                stk.append(expression[j+1:i+1])

            if expression[j] == ":":
                i = j - 1
            else:  # "?"
                i = j - 1
                if expression[i] == "T":
                    a = stk.pop()
                    stk.pop()
                    stk.append(a)
                    i -= 1
                else:
                    stk.pop()
                    i -= 1

        return stk[0]



if __name__ == "__main__":
    assert Solution().parseTernary("F?1:T?4:5") == "4"
    assert Solution().parseTernary("T?T?F:5:3") == "F"
