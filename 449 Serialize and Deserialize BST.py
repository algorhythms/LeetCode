"""
Serialization is the process of converting a data structure or object into a
sequence of bits so that it can be stored in a file or memory buffer, or
transmitted across a network connection link to be reconstructed later in the
same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is
no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary search tree can be serialized to a string
and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.
"""


# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
      self.val = x
      self.left = None
      self.right = None


class Codec:
    DELIMITER = ","

    def serialize(self, root):
        """Encodes a tree to a single string.
        Basic binary tree serialize (BFS), see Serialize and Deserialize
        Binary Tree

        The main difference is as compact as possible. No need "null", since
        insertion order is specfied.

            3 (1)
        2 (2)  5 (2)
                 6 (3)  # bracket () is the insertion order

        pre-order traversal keeps the insertion order
        :type root: TreeNode
        :rtype: str
        """
        def traverse(root, ret):
            if not root:
                return

            ret.append(root.val)
            traverse(root.left, ret)
            traverse(root.right, ret)

        ret = []
        traverse(root, ret)
        return self.DELIMITER.join(map(str, ret))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        Normal BST insert
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
            
        lst = list(map(int, data.split(self.DELIMITER)))
        root = TreeNode(lst[0])
        def insert(root, val):
            # need to keep the parent
            if val < root.val:
                if not root.left:
                    root.left = TreeNode(val)
                else:
                    insert(root.left, val)
            else:
                if not root.right:
                    root.right = TreeNode(val)
                else:
                    insert(root.right, val)

        for a in lst[1:]:
            insert(root, a)

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
