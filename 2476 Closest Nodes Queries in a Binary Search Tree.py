"""
You are given the root of a binary search tree and an array queries of size n consisting of positive integers.

Find a 2D array answer of size n where answer[i] = [mini, maxi]:

mini is the largest value in the tree that is smaller than or equal to queries[i]. If a such value does not exist, add -1 instead.
maxi is the smallest value in the tree that is greater than or equal to queries[i]. If a such value does not exist, add -1 instead.
Return the array answer.

 

Example 1:


Input: root = [6,2,13,1,4,9,15,null,null,null,null,null,null,14], queries = [2,5,16]
Output: [[2,2],[4,6],[15,-1]]
Explanation: We answer the queries in the following way:
- The largest number that is smaller or equal than 2 in the tree is 2, and the smallest number that is greater or equal than 2 is still 2. So the answer for the first query is [2,2].
- The largest number that is smaller or equal than 5 in the tree is 4, and the smallest number that is greater or equal than 5 is 6. So the answer for the second query is [4,6].
- The largest number that is smaller or equal than 16 in the tree is 15, and the smallest number that is greater or equal than 16 does not exist. So the answer for the third query is [15,-1].
Example 2:


Input: root = [4,null,9], queries = [3]
Output: [[-1,4]]
Explanation: The largest number that is smaller or equal to 3 in the tree does not exist, and the smallest number that is greater or equal to 3 is 4. So the answer for the query is [-1,4].
 

Constraints:

The number of nodes in the tree is in the range [2, 10^5].
1 <= Node.val <= 10^6
n == queries.length
1 <= n <= 10^5
1 <= queries[i] <= 10^6
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class SolutionUnbalancedTLE:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        ret = []
        for t in queries:
            ret.append([self.find_lo(root, t), self.find_hi(root, t)])
        
        return ret

    def find_lo(self, cur, target):
        if not cur:
            return -1

        if target < cur.val:
            return self.find_lo(cur.left, target)
        elif target > cur.val:
            ret = self.find_lo(cur.right, target)
            if ret == -1:
                return cur.val
            return ret 
        else:
            return cur.val
    
    def find_hi(self, cur, target):
        if not cur:
            return -1
        if target < cur.val:
            ret = self.find_hi(cur.left, target)
            if ret == -1:
                return cur.val
            return ret 
        elif target > cur.val:
            return self.find_hi(cur.right, target)
        else:
            return cur.val


import bisect 


class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        A = []
        self.inorder(root, A)
        ret = []
        for q in queries:
            idx = bisect.bisect_left(A, q)
            if idx < len(A) and A[idx] == q:
                lo = A[idx]
            else:
                lo = A[idx-1] if idx > 0 else -1

            idx = bisect.bisect_right(A, q)
            if idx > 0 and A[idx-1] == q:
                hi = A[idx-1]
            else:
                hi = A[idx] if idx < len(A) else -1

            ret.append([lo, hi])
        
        return ret

    def inorder(self, cur, A):
        if not cur:
            return 
        
        self.inorder(cur.left, A)
        A.append(cur.val)
        self.inorder(cur.right, A)