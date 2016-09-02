"""
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the
node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a
null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary
tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as
"1,,3".

Example 1:
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true

Example 2:
"1,#"
Return false

Example 3:
"9,#,#,1"
Return false
"""
__author__ = 'Daniel'


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stk = preorder.split(',')
        child_cnt = 0
        while stk:
            if stk[-1] == '#':
                stk.pop()
                child_cnt += 1
            else:
                child_cnt -= 2
                if child_cnt < 0:
                    return False

                stk.pop()
                child_cnt += 1

        return not stk and child_cnt == 1

    def isValidSerializationSpace(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stk = preorder.split(',')
        child_stk = []
        while stk:
            if stk[-1] == '#':
                child_stk.append(stk.pop())  # a counter is enough
            else:
                try:
                    child_stk.pop()
                    child_stk.pop()
                    stk.pop()
                    child_stk.append('#')
                except IndexError:
                    return False

        return not stk and len(child_stk) == 1


if __name__ == "__main__":
    Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")






