"""
You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.

We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.

Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.

Return the largest possible overlap.

 

Example 1:


Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We translate img1 to right by 1 unit and down by 1 unit.

The number of positions that have a 1 in both images is 3 (shown in red).

Example 2:

Input: img1 = [[1]], img2 = [[1]]
Output: 1
Example 3:

Input: img1 = [[0]], img2 = [[0]]
Output: 0
 

Constraints:

n == img1.length == img1[i].length
n == img2.length == img2[i].length
1 <= n <= 30
img1[i][j] is either 0 or 1.
img2[i][j] is either 0 or 1.
"""
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        """
        sliding - 4 dirs any offset
        sliding outside - the relative position doesn't change 

        brute force: starting from any position of img1, and img2, dfs 
        O(N^2 * N^2 * N)

        better brute force:
        Chekc Overlap O(N^2)
        Offset - sliding 2N horizontailly, 2N vertically
        """
        M = len(img1)
        N = len(img1[0])
        maxa = 0
        for di in range(-M+1, M):
            for dj in range(-N+1, N):
                cur = 0
                for i in range(M):
                    for j in range(N):
                        I = i + di
                        J = j + dj
                        if 0 <= I < M and 0 <= J < N:
                            if img1[I][J] == img2[i][j] and img1[I][J] == 1:
                                cur += 1
                maxa = max(maxa, cur)
        
        return maxa