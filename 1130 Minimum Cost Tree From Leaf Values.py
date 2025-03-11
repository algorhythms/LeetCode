"""
Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree, respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node. It is guaranteed this sum fits into a 32-bit integer.

A node is a leaf if and only if it has zero children.

 

Example 1:


Input: arr = [6,2,4]
Output: 32
Explanation: There are two possible trees shown.
The first has a non-leaf node sum 36, and the second has non-leaf node sum 32.
Example 2:


Input: arr = [4,11]
Output: 44
 

Constraints:

2 <= arr.length <= 40
1 <= arr[i] <= 15
It is guaranteed that the answer fits into a 32-bit signed integer (i.e., it is less than 2^31).
"""
import functools


class SolutionDP:
    def mctFromLeafValues(self, A: List[int]) -> int:
        """
        The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree, respectively.
        We cannot sort A
        We need to combine neighbor into 1 operation

        Smallest non-leaf sum

        Brute force?

        [6, 2, 4]

        Let F_{i, j} be the smallest in A[i:j]

        Then partion F_{i, j}
        F_{i, j} =  F_{i, k} + F{k, j} + max(A[i:k])*max(A[k:j]) 
                    min over k \in [i, j)

        How to build this DP? memoization 
        """
        return self.F(0, len(A), tuple(A))
    
    @functools.lru_cache(maxsize=None)
    def F(self, i, j, A):
        return min(
            (
                self.F(i, k, A) + self.F(k, j, A)
                + max(A[i:k]) * max(A[k:j])
                for k in range(i+1, j)
            ),
            default=0,
        )
    

class Solution:
    def mctFromLeafValues(self, A: List[int]) -> int:
        """
        Max leaf is used at each inner node => put big leaf nodes close to the root.
        => greedily start with the smallest leaf

        To remove any number a, it costs a * b, where b >= a.
        So `a` has to be removed by a bigger neighbor `b`.
        To minimize this cost, we need to minimize b.

        i = A.index(min(A))
        cost += A[i] * min(A[i-1], A[i+1])
        A.pop(i)
        O(N^2)

        How to efficiently find the min index
        We need to find i s.t. A[i-1] > A[i] < A[i+1]
        Keep a monotonic stack for A[:i], till the monotonicity break by A[i], then we need to pop and maintain the monotonicity 
        """
        cost = 0
        stk = []
        for a in A:
            while stk and stk[-1] <= a:
                mid = stk.pop()
                if stk:
                    left = stk[-1]
                    cost += mid * min(left, a)
                else:
                    cost += mid * a
                    
            stk.append(a)
        
        while len(stk) > 1:
            mid = stk.pop()
            left = stk[-1]
            cost += mid * left
        
        return cost
