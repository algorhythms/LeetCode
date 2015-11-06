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
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        # solve min count of removal
        cnt = 0
        l = 0
        for c in s:
            if c == "(":
                l += 1
            elif c == ")":
                l -= 1
                if l < 0:
                    l = 0
                    cnt += 1

        cnt += l
        ret = []
        self.dfs(s, "", 0, None, 0, cnt, ret)
        return ret

    def dfs(self, s, cur, l, removed, i, cnt, ret):
        """backtracking, post-check"""
        if l < 0 or cnt < 0 or i > len(s):
            return
        if i == len(s):
            if cnt == 0 and l == 0:
                ret.append(cur)
            return

        if s[i] in ("(", ")"):
            # jump
            C = cnt
            while i < len(s) and removed and removed == s[i]:
                i += 1
                C -= 1

            if C != cnt:
                self.dfs(s, cur, l, removed, i, C, ret)
            else:
                self.dfs(s, cur, l, s[i], i+1, cnt-1, ret)

                L = l+1 if s[i] == "(" else l-1
                self.dfs(s, cur+s[i], L, None, i+1, cnt, ret)  # put
        else:
            self.dfs(s, cur+s[i], l, None, i+1, cnt, ret)


if __name__ == "__main__":
    assert Solution().removeInvalidParentheses("(a)())()") == ['(a())()', '(a)()()']




