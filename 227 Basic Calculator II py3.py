#!/usr/bin/python3
"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators
and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""


class Solution:
    def calculate(self, s: str) -> int:
        """
        No brackets. Look at previous operand and operator, when finishing
        scanning current operand.
        """
        operand = 0
        stk = []
        prev_op = "+"
        for i, c in enumerate(s):
            if c.isdigit():
                operand = operand * 10 + int(c)

            #  i == len(s) - 1
            delimited = c in ("+", "-", "*", "/") or i == len(s) - 1
            if delimited:
                if prev_op == "+":
                    cur = operand
                elif prev_op == "-":
                    cur = -operand
                elif prev_op == "*":
                    cur = stk.pop() * operand
                else:
                    assert prev_op == "/"
                    # instead of op1 // op2 due to negative handling, -3 // 2 == -2
                    cur = int(stk.pop() / operand)

                stk.append(cur)
                prev_op = c
                operand = 0

        return sum(stk)

    def calculate_error(self, s: str) -> int:
        """
        cannot use dictionary, since it is eager evaluation
        """
        operand = 0
        stk = []
        prev_op = "+"
        for i, c in enumerate(s):
            if c.isdigit():
                operand = operand * 10 + int(c)

            #  i == len(s) - 1
            delimited = c in ("+", "-", "*", "/") or i == len(s) - 1
            if delimited:
                cur = {
                    "+": operand,
                    "-": -operand,
                    "*": stk.pop() * operand,
                    "/": int(stk.pop() / operand),  # instead of op1 // op2 due to negative handling, -3 // 2 == -2
                }[prev_op]
                stk.append(cur)

                prev_op = c
                operand = 0

        return sum(stk)


if __name__ == "__main__":
    assert Solution().calculate("3+2*2") == 7
