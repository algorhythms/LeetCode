"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division
should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.


"""
__author__ = 'Daniel'


class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = self.parse(s)
        post = self.infix2postfix(lst)
        return self.eval_postfix(post)

    def parse(self, s):
        """
        return tokens
        """
        i = 0
        ret = []
        while i < len(s):
            if s[i] == " ":
                i += 1

            elif s[i] in ("(", ")", "+", "-", "*", "/"):
                ret.append(s[i])
                i += 1

            else:
                b = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                ret.append(s[b:i])

        return ret

    def infix2postfix(self, lst):
        # operator stacks rather than operand
        stk = []  # stk only stores operators in strictly increasing precedence
        ret = []
        for elt in lst:
            if elt.isdigit():
                ret.append(elt)
            elif elt == "(":
                stk.append(elt)
            elif elt == ")":
                while stk[-1] != "(":
                    ret.append(stk.pop())
                stk.pop()
            else:  # generalized to include * and /
                while stk and self.precendece(elt) <= self.precendece(stk[-1]):
                    ret.append(stk.pop())

                stk.append(elt)

        while stk:
            ret.append(stk.pop())

        return ret

    def precendece(self, op):
        if op in ("(", ")"):
            return 0
        if op in ("+", "-"):
            return 1
        if op in ("*", "/"):
            return 2
        return 3

    def eval_postfix(self, post):
        stk = []
        for elt in post:
            if elt in ("+", "-", "*", "/"):
                b = int(stk.pop())
                a = int(stk.pop())
                if elt == "+":
                    stk.append(a+b)
                elif elt == "-":
                    stk.append(a-b)
                elif elt == "*":
                    stk.append(a*b)
                else:
                    stk.append(a/b)
            else:
                stk.append(elt)

        assert len(stk) == 1
        return int(stk[-1])


if __name__ == "__main__":
    assert Solution().calculate("3+2*2") == 7
