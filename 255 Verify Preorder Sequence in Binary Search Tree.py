"""
Premium Question
"""
__author__ = 'Daniel'


class Solution:
    def verifyPreorder(self, preorder):
        """
        * Draw a valid BST, and swap a pair of nodes to get an invalid BST.
        * Get the preorder traversal of the 2 BSTs and compare and contrast them.
        * For tree traversal, a stack or a queue is normally involved.
        :type preorder:List[int]
        :rtype: bool
        """
        left_finished = None
        stk = []
        for num in preorder:
            if left_finished and num < left_finished:
                return False

            while stk and stk[-1] < num:
                left_finished = stk.pop()

            stk.append(num)

        return True


if __name__ == "__main__":
    preorder = [3, 5, 2, 1, 4, 7, 6, 9, 8, 10]
    assert Solution().verifyPreorder(preorder) == False
