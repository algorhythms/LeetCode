"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the
number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n >= 1, find out how much money you need to have to guarantee a win.
"""
__author__ = 'Daniel'


class Solution(object):
    def getMoneyAmount(self, n):
        """
        Let F[i][j] be the min cost of guessing [i, j)
        F[i][j] = min(
          k + max(F[i][k], F[k+1][j]) for k in [i, j)
        )
        Draw a matrix to show the population direction
        [ ] -> [ ]
                ^
                |
               [ ]
        O(n^3)

        Edge cases:
          F[i][i+1] = 0
        :type n: int
        :rtype: int
        """
        N = n + 1  # guessing [1, N), where N = n + 1
        F = [[0 for _ in xrange(N+1)] for _ in xrange(N+1)]
        for i in xrange(n, 0, -1):
            for j in xrange(i+2, N+1):
                F[i][j] = min(
                    k + max(F[i][k], F[k+1][j])
                    for k in xrange(i, j)
                )

        return F[1][N]

    def getMoneyAmountError(self, n):
        """
        Cost for number. Guarantee a win.
        Let C[i] be the min requirement of the number of wrong guesses
        Let F[i] be the min requirement of money

        C[i] = min(C[k-1] + 1 + C[i-k] for k in [1, i])
        F[i] = min(F[k-1] + k + k*C[i-k] + F[i-k] for k in [1, i])
        O(n^2)

        Still one-directional guess
        Error: F[i] does not correspond to C[i]
        :type n: int
        :rtype: int
        """
        C = [0 for _ in xrange(n+1)]
        F = [0 for _ in xrange(n+1)]
        for i in xrange(2, n+1):
            C[i] = min(1 + max(C[k-1], C[i-k]) for k in xrange(1, i+1))
            F[i] = min(k + max(F[k-1], k*C[i-k] + F[i-k]) for k in xrange(1, i+1))

        return F[n]


if __name__ == "__main__":
    print Solution().getMoneyAmount(100)

