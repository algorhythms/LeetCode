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

Note: Recursive solution is trivial, could you do it iteratively? - see postTraverse_itr
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
        Recursive post-order traversal is trivial. What is the iteration version for this
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

        double stacks

        :param root:
        :param lst:
        :return:
        """
        if not root:
            return
        stk = [root]
        while stk:
            cur = stk.pop()
            lst.insert(0, cur.val)  # reversely insert
            if cur.left:
                stk.append(cur.left)

            if cur.right:
                stk.append(cur.right)






if __name__=="__main__":
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    print Solution().postorderTraversal(t1)