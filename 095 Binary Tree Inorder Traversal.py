"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
"""
__author__ = 'Danyang'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        Morris Traversal
        """
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
                    cur = cur.left
                else:
                    pre.right = None
                    ret.append(cur.val)
                    cur = cur.right

        return ret

    def inorderTraversal_memory(self, root):
        """
        :type root: TreeNode
        :param root:
        :return: a list of integers
        """
        lst = []
        self.inorderTraverse_itr(root, lst)
        return lst

    def inorderTraverse(self, root, lst):
        """
        In order traverse
        """
        if not root:
            return
        self.inorderTraverse(root.left, lst)
        lst.append(root.val)
        self.inorderTraverse(root.right, lst)

    def inorderTraverse_itr(self, root, lst):
        """
        iterative version
        leftmost first in the lst
        double loop

        reference: http://fisherlei.blogspot.sg/2013/01/leetcode-binary-tree-inorder-traversal.html
        :type root: TreeNode
        :param root:
        :param lst:
        :return:
        """
        if not root:
            return

        cur = root
        stk = []
        while stk or cur:
            while cur:
                stk.append(cur)
                cur = cur.left
            cur = stk.pop()  # left_most
            lst.append(cur.val)
            cur = cur.right
            # if cur.right:  # should go to next iteration
            #     cur = cur.right
            #     stk.append(cur)

