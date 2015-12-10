"""
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you
take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn
to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win
the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove
, the last stone will always be removed by your friend.
"""
__author__ = 'Daniel'


class Solution(object):
    def canWinNim(self, n):
        """
        Enumerate example and find the pattern
        """
        return n % 4 != 0

    def canWinNim_TLE(self, n):
        """
        dp

        Let F[i] be the whether act & win when there is i stones left
        :type n: int
        :rtype: bool
        """
        if n < 3:
            return True

        F = [False for _ in xrange(3)]
        F[1] = F[2] = F[0] = True
        for i in xrange(4, n+1):
            F[i%3] = any(not F[(i-k)%3] for k in xrange(1, 4))

        return F[n%3]

    def canWinNim_MLE(self, n):
        """
        dp

        Let F[i] be the whether act & win when there is i stones left
        :type n: int
        :rtype: bool
        """
        if n < 3:
            return True

        F = [False for _ in xrange(n+1)]
        F[1] = F[2] = F[3] = True
        for i in xrange(4, n+1):
            F[i] = any(not F[i-k] for k in xrange(1, 4))

        return F[n]


if __name__ == "__main__":
    assert Solution().canWinNim(5)