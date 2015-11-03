"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively? - see preTraverse_itr
"""
__author__ = 'Danyang'


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """Morris"""
        ret = []
        cur = root
        while cur:
            if not cur.left:
                ret.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right

                if not pre.right:
                    pre.right = cur
                    ret.append(cur.val)
                    cur = cur.left
                else:
                    pre.right = None
                    cur = cur.right

        return ret

    def preorderTraversal_memory(self, root):
        """
        dfs
        :param root:
        :return:
        """
        lst = []
        self.preTraverse_itr(root, lst)
        return lst


    def preTraverse(self, node, lst):
        if not node:
            return
        lst.append(node.val)

        self.preTraverse(node.left, lst)
        self.preTraverse(node.right, lst)

    def preTraverse_itr(self, root, lst):
        """
        stack = [R, L, cur]

        Pretty simple using stack
        double stacks

        :param root:
        :param lst:
        :return:
        """
        if not root:
            return
        stk = [root]
        while stk:
            node = stk.pop()
            lst.append(node.val)
            if node.right:  # right first
                stk.append(node.right)

            if node.left:
                stk.append(node.left)



if __name__=="__main__":
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    print Solution().preorderTraversal(t1)