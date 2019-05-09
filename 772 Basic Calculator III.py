#!/usr/bin/python3
"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus +
or minus sign -, non-negative integers and empty spaces .

The expression string contains only non-negative integers, +, -, *, / operators
, open ( and closing parentheses ) and empty spaces . The integer division
should truncate toward zero.

You may assume that the given expression is always valid. All intermediate
results will be in the range of [-2147483648, 2147483647].

Some examples:
"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12

Note: Do not use the eval built-in library function.
"""


class Solution:
    def calculate(self, s: str) -> int:
        """
        recursively handle bracket
        """
        s = s + "\0"  # signal the end
        ret, _ = self.eval(s, 0, [])
        print(ret)
        return ret

    def eval(self, s, i, stk):
        operand = 0
        prev_op = "+"
        while i < len(s):
            c = s[i]
            if c == " ":
                i += 1
            elif c.isdigit():
                operand = operand * 10 + int(c)
                i += 1
            elif c in ("+", "-", "*", "/", ")", "\0"):   # delimited
                if prev_op == "+":
                    stk.append(operand)
                elif prev_op == "-":
                    stk.append(-operand)
                elif prev_op == "*":
                    prev_operand = stk.pop()
                    stk.append(prev_operand * operand)
                elif prev_op == "/":
                    prev_operand = stk.pop()
                    stk.append(int(prev_operand / operand))

                operand = 0
                prev_op = c
                i += 1

                if c == ")":
                    return sum(stk), i

            elif c == "(":
                operand, i = self.eval(s, i + 1, [])
            # elif c == ")":
            #     return sum(stk), i + 1
            else:
                raise

        return sum(stk), i
        

if __name__ == "__main__":
    assert Solution().calculate("(2+6* 3+5- (3*14/7+2)*5)+3") == -12
