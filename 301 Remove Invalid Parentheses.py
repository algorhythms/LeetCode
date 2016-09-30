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
        Brute force: BFS and then validate

        Algorithm focuses on left parentheses
        Backtracking/DFS with prune & jump

        :type s: str
        :rtype: List[str]
        """
        rmcnt = self.minrm(s)
        ret = []
        self.dfs(s, "", 0, None, 0, rmcnt, ret)
        return ret

    def minrm(self, s):
        """
        Find the minimal removal count to limit the search depth
        returns minimal number of removals
        """
        rmcnt = 0
        left = 0
        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                if left > 0:
                    left -= 1
                else:
                    rmcnt += 1

        rmcnt += left
        return rmcnt

    def dfs(self, s, cur, left, pi, i, rmcnt, ret):
        """
        Remove parenthesis
        backtracking, post-check
        :param s: original string
        :param cur: current string builder
        :param left: number of remaining left parentheses in s[0..i] not consumed by ")"
        :param pi: last removed char
        :param i: current index
        :param rmcnt: number of remaining removals needed
        :param ret: results
        """
        if left < 0 or rmcnt < 0 or i > len(s):
            return
        if i == len(s):
            if rmcnt == 0 and left == 0:
                ret.append(cur)
            return

        if s[i] not in ("(", ")"):  # skip non-parenthesis
            self.dfs(s, cur+s[i], left, None, i+1, rmcnt, ret)
        else:
            if pi == s[i]:  # jump, if rm, rm them all to avoid duplication
                while i < len(s) and pi and pi == s[i]: i, rmcnt = i+1, rmcnt-1
                self.dfs(s, cur, left, pi, i, rmcnt, ret)
            else:
                self.dfs(s, cur, left, s[i], i+1, rmcnt-1, ret)
                L = left+1 if s[i] == "(" else left-1  # consume "("
                self.dfs(s, cur+s[i], L, None, i+1, rmcnt, ret)  # put


if __name__ == "__main__":
    assert Solution().removeInvalidParentheses("(a)())()") == ['(a())()', '(a)()()']
