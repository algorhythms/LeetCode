"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        Queue
        BFS
        :param root: Tree node
        :return: a list of lists of integers
        """
        result = []
        q = []
        if root:
            q.append(root)

        while q:
            length = len(q)
            cur_level = []
            for i in range(length):
                cur = q[i]
                cur_level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            q = q[length:]  # no need to create a new list
            result.append(cur_level)
        return result

if __name__=="__main__":
    nodes = [TreeNode(i) for i in range(3)]
    nodes[0].left = nodes[1]
    nodes[1].left = nodes[2]
    print Solution().levelOrder(nodes[0])


