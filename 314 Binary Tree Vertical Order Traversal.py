"""
Premium Question
"""
__author__ = 'Daniel'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def verticalOrder(self, root):
        """
        O(N)
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        l = self.leftmost(root, 0)
        r = self.rightmost(root, 0)

        ret = [[] for _ in xrange(r-l-1)]
        self.bfs(root, -l-1, ret)
        return ret

    def bfs(self, cur, col, ret):
        q = []
        if cur:
            q.append((cur, col))

        while q:
            l = len(q)
            for i in xrange(l):  # avoid non-stop access as in `for elt in q`
                v, c = q[i]
                ret[c].append(v.val)
                if v.left: q.append((v.left, c-1))
                if v.right: q.append((v.right, c+1))

            q = q[l:]

    def leftmost(self, cur, l):
        if not cur: return l
        return min(self.leftmost(cur.left, l-1), self.leftmost(cur.right, l+1))

    def rightmost(self, cur, r):
        if not cur: return r
        return max(self.rightmost(cur.left, r-1), self.rightmost(cur.right, r+1))

    def sidemost(self, cur, p, f):
        if not cur: return p
        return f(self.sidemost(cur.left, p-1, f), self.sidemost(cur.right, p+1, f))