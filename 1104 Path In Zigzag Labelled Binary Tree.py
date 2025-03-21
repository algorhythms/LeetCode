"""
In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.

Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

Example 1:

Input: label = 14
Output: [1,3,4,14]
Example 2:

Input: label = 26
Output: [1,2,6,10,26]
 

Constraints:

1 <= label <= 10^6
"""
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        """
        Brute force, construct the tree 

        If not zig zag, pi = x // 2
        If zig zag,
           complement of pi = x // 2, for every level by observation 
        """
        stk = [label]
        while stk[-1] > 1:
            cur = stk[-1] >> 1
            # 2^lo <= val < 2^hi
            msb = 0
            while cur >> msb > 0:
                msb += 1
            delta = cur - (1 << msb - 1)
            t = (1 << msb) - 1 - delta
            stk.append(t)
        
        return stk[::-1]
        