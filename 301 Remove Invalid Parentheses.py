"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]

"""
__author__ = 'Daniel'


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        Algorithm focuses on left parentheses
        Backtracking/DFS with pruning
        :type s: str
        :rtype: List[str]
        """
        rmcnt = self.minrm(s)
        ret = []
        self.dfs(s, "", 0, None, 0, rmcnt, ret)
        return ret

    def minrm(self, s):
        """
        returns minimal number of removals
        """
        rmcnt = 0
        l = 0
        for c in s:
            if c == "(":
                l += 1
            elif c == ")":
                l -= 1
                if l < 0:
                    l = 0
                    rmcnt += 1

        rmcnt += l
        return rmcnt

    def dfs(self, s, cur, l, last_rm, i, rmcnt, ret):
        """
        Remove parenthesis
        backtracking, post-check
        :param s: original string
        :param cur: current string builder
        :param l: number of remaining left parentheses in s[0..i]
        :param last_rm: last removed char
        :param rmcnt: number of remaining removals needed
        :param ret: results
        """
        if l < 0 or rmcnt < 0 or i > len(s):
            return
        if i == len(s):
            if rmcnt == 0 and l == 0:
                ret.append(cur)
            return

        if s[i] not in ("(", ")"):  # skip non-parenthesis
            self.dfs(s, cur+s[i], l, None, i+1, rmcnt, ret)
        else:
            if last_rm == s[i]:  # jump, if rm, rm them all to avoid duplication
                while i < len(s) and last_rm and last_rm == s[i]: i, rmcnt = i+1, rmcnt-1
                self.dfs(s, cur, l, last_rm, i, rmcnt, ret)
            else:
                self.dfs(s, cur, l, s[i], i+1, rmcnt-1, ret)
                L = l+1 if s[i] == "(" else l-1  # consume "("
                self.dfs(s, cur+s[i], L, None, i+1, rmcnt, ret)  # put


if __name__ == "__main__":
    assert Solution().removeInvalidParentheses("(a)())()") == ['(a())()', '(a)()()']




