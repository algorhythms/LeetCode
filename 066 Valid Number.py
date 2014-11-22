"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before
implementing one.
"""
__author__ = 'Danyang'
class Solution:
    def isNumber_builtin(self, s):
        """
        using built-in function
        :param s: a string
        :return: boolean
        """
        try:
            float(s)
            return True
        except ValueError:
            return False

    def isNumber(self, s):
        """
        D-FSA: Deterministic Finite State Automata
        Transition table T, which is constructed from FSA

        state = T[state, token]

        Draw the diagram for FSA
        :param s:
        :return:
        """
        INVALID = 0
        SPACE = 1
        SIGN = 2
        DIGIT = 3
        DOT = 4
        E = 5
        T = [
            [-1, 0, 3, 1, 2,-1],
            [-1, 8,-1, 1, 4, 5],
            [-1,-1,-1, 4,-1,-1],
            [-1,-1,-1, 1, 2,-1],
            [-1, 8,-1, 4,-1, 5],
            [-1,-1, 6, 7,-1,-1],
            [-1,-1,-1, 7,-1,-1],
            [-1, 8,-1, 7,-1,-1],
            [-1, 8,-1,-1,-1,-1], # 9
        ]
        state = 0
        for char in s:
            if state==-1:
                return False
            if char==" ":
                token = SPACE
            elif char in ("-", "+"):
                token = SIGN
            elif char in map(str, range(10)):
                token = DIGIT
            elif char==".":
                token = DOT
            elif char in ("e", "E"):
                token = E
            else:
                token = INVALID

            state = T[state][token]
        if state in (1, 4, 7, 8):  # accept state
            return True
        else:
            return False

if __name__=="__main__":
    assert Solution().isNumber(".2e81")==True
    assert Solution().isNumber("6+1")==False
    assert Solution().isNumber("1 a")==False
    assert Solution().isNumber("1e10")==True
    assert Solution().isNumber(" 0.1")==True
    assert Solution().isNumber("abc")==False


