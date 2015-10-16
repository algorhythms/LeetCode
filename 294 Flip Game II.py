"""
Premium Question
Game, Winner, Backtracking
"""
__author__ = 'Daniel'


class Solution(object):
    def canWin(self, s):
        return any(not self.canWin(s[:i]+"--"+s[i+2:]) for i in xrange(len(s)-1) if s[i:i+2] == "++")

    def canWin_trivial(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in xrange(len(s)-1):
            if s[i:i+2] == "++":
                if not self.canWin(s[:i]+"--"+s[i+2:]):
                    return True

        return False


if __name__ == "__main__":
    assert Solution().canWin("+++++") == False