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

    def preorderTraversal(self, root):
        lst = []
        self.preTraverse(root, lst)
        return lst



    def preTraverse(self, node, lst):
        if node==None:
            return
        lst.append(node.val)
        if node.left:
            self.preTraverse(node.left, lst)
        if node.right:
            self.preTraverse(node.right, lst)



if __name__=="__main__":
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    print Solution().preorderTraversal(t1)