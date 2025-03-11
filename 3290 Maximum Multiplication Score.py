"""
You are given an integer array a of size 4 and another integer array b of size at least 4.

You need to choose 4 indices i0, i1, i2, and i3 from the array b such that i0 < i1 < i2 < i3. Your score will be equal to the value a[0] * b[i0] + a[1] * b[i1] + a[2] * b[i2] + a[3] * b[i3].

Return the maximum score you can achieve.

 

Example 1:

Input: a = [3,2,5,6], b = [2,-6,4,-5,-3,2,-7]

Output: 26

Explanation:
We can choose the indices 0, 1, 2, and 5. The score will be 3 * 2 + 2 * (-6) + 5 * 4 + 6 * 2 = 26.

Example 2:

Input: a = [-1,4,5,-2], b = [-5,-1,-3,-2,-4]

Output: -1

Explanation:
We can choose the indices 0, 1, 3, and 4. The score will be (-1) * (-5) + 4 * (-1) + 5 * (-2) + (-2) * (-4) = -1.

 

Constraints:

a.length == 4
4 <= b.length <= 10^5
-10^5 <= a[i], b[i] <= 10^5
"""
import sys


class Solution:
    def maxScore_error(self, a: List[int], b: List[int]) -> int:
        """
        Greedy: max times max
        """
        a.sort(reverse=True)
        b.sort(reverse=True)
        ret = 0
        for i in range(4):
            ret += a[i] *b[i]
        
        return ret

    def maxScore_TLE(self, a: List[int], b: List[int]) -> int:
        """
        backtracking 
        permutation to the depth of 4
        """
        maxa = [-sys.maxsize-1]
        self.backtrack(a, b, 0, [], maxa)
        return maxa[0]
    
    def backtrack(self, a, b, cur, ret, maxa):
        if len(ret) == 4:
            cur_maxa = 0
            for i in range(4):
                cur_maxa += a[i] * ret[i]
            maxa[0] = max(maxa[0], cur_maxa)
            return
        
        for i in range(cur, len(b)):
            # not choose i
            self.backtrack(a, b, i+1, ret, maxa)
            # choose i
            ret.append(b[i])
            self.backtrack(a, b, i+1, ret, maxa)
            ret.pop()
    
    def maxScore_error(self, a: List[int], b: List[int]) -> int:
        """
        Let F[i][j] be the max score for a[:i] and b[:j] and choosing a[i-1] but may not b[j-1]
        F[i][j] = a[i-1] * b[j-1] + F[i-1][j-1]
        """
        F = [
            [0 for _ in range(len(b)+1)]  # cannot initialize with 0
            for _ in range(len(a)+1)
        ]
        
        for i in range(1, len(a)+1):
            for j in range(1, len(b)+1):
                F[i][j] = max(a[i-1] * b[j-1] + F[i-1][j-1], F[i][j-1])
        
        return max(F[4][j] for j in range(4, len(b) + 1))
    
    def maxScore2(self, a: List[int], b: List[int]) -> int:
        """
        Let F[i][j] be the max score for a[:i] and b[:j] and choosing a[i] but may or may not b[j]
        F[i][j] = max(a[i] * b[j] + F[i-1][j-1], F[i][j-1])

        Because of complication of negative number and calculation, we cannot augment a dummy row and a column for F
        """
        MIN = -sys.maxsize-1
        F = [
            [MIN for _ in range(len(b))]
            for _ in range(len(a))
        ]
        
        for i in range(len(a)):
            for j in range(i, len(b)):  # cannot start with 0
                F[i][j] = max(a[i] * b[j] + (F[i-1][j-1] if i > 0 and j > 0 else 0), F[i][j-1] if j > 0 else MIN)

        return F[3][~0]
    
    def maxScore(self, a: List[int], b: List[int]) -> int:
        """
        Let F[i][j] be the max score for a[:i] and b[:j] and choosing a[i-1] but may or may not b[j-1]
        F[i][j] = max(a[i] * b[j] + F[i-1][j-1], F[i][j-1])
        """
        MIN = -sys.maxsize-1
        F = [
            [MIN for _ in range(len(b)+1)]
            for _ in range(len(a)+1)
        ]
        for j in range(len(b)+1):
            F[0][j] = 0

        for i in range(1, len(a)+1):
            for j in range(i, len(b)+1):  # cannot start with 1
                F[i][j] = max(
                    a[i-1] * b[j-1] + F[i-1][j-1], 
                    F[i][j-1])

        return F[4][~0]
        
        


        