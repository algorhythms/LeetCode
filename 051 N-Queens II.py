"""
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
"""
__author__ = 'Danyang'
INVALID = -1
QUEEN = 1
DEFAULT = 0
class Solution:
    def totalNQueens(self, n):
        """
        backtracking
        :param n: integer
        :return: a list of lists of string
        """
        result = []
        current = [[0 for _ in xrange(n)] for _ in xrange(n)]
        self.backtrack(0, current, result)
        return len(result)

    def backtrack(self, queen_index, current, result):
        """

        :param queen_index:
        :param current: 2D matrix
        :param result: list of 2D matrix
        :return: Nothing
        """
        n = len(current)
        if queen_index==n:
            result.append(current)
            return

        for i in xrange(n):
            if current[queen_index][i]==INVALID:
                continue

            # place the queen
            new_config = [list(element) for element in current]  # new copy
            new_config[queen_index][i] = QUEEN

            # config
            for m in xrange(n):
                # col
                if new_config[m][i]==DEFAULT:
                    new_config[m][i] = INVALID
                    # row
                if new_config[queen_index][m]==DEFAULT:
                    new_config[queen_index][m] = INVALID

                # diagonal
                row = queen_index+m
                col = i+m
                if 0<=row<n and 0<=col<n and new_config[row][col]==DEFAULT: new_config[row][col] = INVALID

                row = queen_index-m
                col = i-m
                if 0<=row<n and 0<=col<n and new_config[row][col]==DEFAULT: new_config[row][col] = INVALID

                row = queen_index-m
                col = i+m
                if 0<=row<n and 0<=col<n and new_config[row][col]==DEFAULT: new_config[row][col] = INVALID

                row = queen_index+m
                col = i-m
                if 0<=row<n and 0<=col<n and new_config[row][col]==DEFAULT: new_config[row][col] = INVALID

            self.backtrack(queen_index+1, new_config, result)


if __name__=="__main__":
    print Solution().totalNQueens(4)