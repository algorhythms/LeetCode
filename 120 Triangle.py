"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row
below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""
__author__ = 'Danyang'
class Solution:
    def minimumTotal(self, triangle):
        """
        bottom-up dp
        :param triangle: a list of lists of integers
        :return: integer
        """
        dp = []
        length = len(triangle)

        # trivial
        dp.insert(0, [num for num in triangle[length-1]])
        # starting from penultimate row
        for row in xrange(length-1-1, -1, -1):
            dp.insert(0, [])
            for col in xrange(len(triangle[row])):
                dp[0].append(triangle[row][col]+min(dp[1][col], dp[1][col+1]))  # next level

        assert len(dp[0])==1

        return dp[0][0]


if __name__=="__main__":
    Solution().minimumTotal([[-1], [2, 3], [1, -1, -3]])