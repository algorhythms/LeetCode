"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        dfs
        :param root: TreeNode
        :return: a list of int
        """
        lst = []
        self.postTraverse_itr(root, lst)
        return lst



    def postTraverse(self, node, lst):
        if not node:
            return
        self.postTraverse(node.left, lst)
        self.postTraverse(node.right, lst)

        lst.append(node.val)

    def postTraverse_itr(self, root, lst):
        """
        stack = [L, R, cur]

        :param root:
        :param lst:
        :return:
        """
        if not root:
            return
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.left:
                stack.append(cur.left)

            if cur.right:
                stack.append(cur.right)

            lst.insert(0, cur.val)  # reverse insert




if __name__=="__main__":
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    print Solution().postorderTraversal(t1)