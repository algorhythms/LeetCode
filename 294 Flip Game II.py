"""
Premium Question
Game, Winner, Backtracking
"""
__author__ = 'Daniel'


class Solution(object):
    def __init__(self):
        self.d = {}

    def canWin(self, s):
        """
        memoization
        110ms
        """
        if s not in self.d:
            flag = False
            for i in xrange(len(s)-1):
                if s[i:i+2] == "++":
                    if not self.canWin(s[:i]+"--"+s[i+2:]):
                        flag = True
                        break
            self.d[s] = flag

        return self.d[s]

    def canWin_oneline(self, s):
        return any(not self.canWin_oneline(s[:i]+"--"+s[i+2:]) for i in xrange(len(s)-1) if s[i:i+2] == "++")

    def canWin_trivial(self, s):
        """
        3200 ms
        :type s: str
        :rtype: bool
        """
        for i in xrange(len(s)-1):
            if s[i:i+2] == "++":
                if not self.canWin_trivial(s[:i]+"--"+s[i+2:]):
                    return True

        return False


if __name__ == "__main__":
    assert Solution().canWin("+++++") == False