__author__ = 'Danyang'
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        ops = ["+", "-", "*", "/"]

        def arith(a, b, op):
            if (op=="+"):
                return a + b
            if (op=="-"):
                return a - b
            if (op=="/"):
                # return a/b # python treat differently for division 6/-132 is -1
                return int(float(a) / b) # round towards 0
            if (op=="*"):
                return a * b

        # stack
        stack = []
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = arith(arg1, arg2, token)
                stack.append(result)
        return stack.pop()


if __name__=="__main__":
    Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])