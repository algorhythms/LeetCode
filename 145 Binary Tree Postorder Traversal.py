__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers

    def postorderTraversal(self, root):
        lst = []
        self.postTraverse(root, lst)
        return lst



    def postTraverse(self, node, lst):
        if node==None:
            return

        if node.left:
            self.postTraverse(node.left, lst)
        if node.right:
            self.postTraverse(node.right, lst)

        lst.append(node.val)

if __name__=="__main__":
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    print Solution().postorderTraversal(t1)