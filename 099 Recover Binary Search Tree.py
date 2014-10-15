"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.val)

class Solution:
    def __init__(self):
        self.swapped_pair = []
        self.current = None
        self.pre = None

    def recoverTree(self, root):
        """
        In-order traversal
        binary tree: {1, 2, 3, 4, 5, 6}
        swap 3 and 6: {1, 2, 6, 4, 5, 3}
        when comparing (6, 4) error, record the 1st item
        when comparing (5, 3) error, record the 2nd item
        In-order traverse, keep the previous tree node,
        Find first misplaced node by
        if ( current.val < prev.val )
           Node first = prev;

        Find second by
        if ( current.val < prev.val )
           Node second = current;

        Other solutions:
        http://fisherlei.blogspot.sg/2012/12/leetcode-recover-binary-search-tree.html
        Traverse without stack: Threaded Binary Tree

        :param root: TreeNode
        :return: TreeNode
        """
        self.in_order(root)
        if len(self.swapped_pair)==2:
            self.swapped_pair[0][0].val, self.swapped_pair[1][1].val = self.swapped_pair[1][1].val, self.swapped_pair[0][0].val
        else: # neighboring
            self.swapped_pair[0][0].val, self.swapped_pair[0][1].val = self.swapped_pair[0][1].val, self.swapped_pair[0][0].val
        return root

    def in_order(self, current):
        if not current:
            return

        self.in_order(current.left)
        # update global
        self.pre = self.current
        self.current = current
        if self.pre and not self.pre.val<self.current.val:
            if not self.swapped_pair:
                self.swapped_pair.append((self.pre, self.current))  # pre is wrong
            else:
                self.swapped_pair.append((self.pre, self.current))  # current is wrong
        self.in_order(current.right)

    # def __get_smallest(self, root):
    #     if not root.left and not root.right:
    #         return root.val
    #     if root.left:
    #         return self.__get_smallest(root.left)
    #     else:
    #         return self.__get_smallest(root.right)
    #
    # def __get_largest(self, root):
    #     if not root.left and not root.right:
    #         return root.val
    #     if root.right:
    #         return self.__get_largest(root.right)
    #     else:
    #         return self.__get_largest(root.left)
    #
    # def __is_bst(self, root):
    #     if not root:
    #         return True
    #     if root.left and self.__get_largest(root.left)>root.val:
    #         return False
    #     if root.right and self.__get_smallest(root.right)<root.val:
    #         return False
    #     return True
    #
    # def __find(self, root, result):
    #     if self.__is_bst(root.left) and self.__is_bst(root.right) and not self.__is_bst(root):
    #         result.append(root)
    #     if root.left: self.__find(root.left, result)
    #     if root.right: self.__find(root.right, result)

if __name__=="__main__":
    node1 = TreeNode(2)
    node2 = TreeNode(1)
    node1.right = node2
    print Solution().recoverTree(node1)