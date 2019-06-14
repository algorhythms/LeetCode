#!/usr/bin/python3
"""
You are given coins of different denominations and a total amount of money.
Write a function to compute the number of combinations that make up that amount.
You may assume that you have infinite number of each kind of coin.



Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1
"""
from collections import defaultdict


class Solution:
    def change(self, amount, coins):
        """
        let F[amount][l] = # ways ending (but not necesserily) using coins[l-1]
        (i.e. coins[:l])
        Two options: use coin[l-1] or not
        F[amount][l] = F[amount][l-1] + F[amount - coin[l-1]][l]

        Similar to 0-1 knapsack

        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        F = defaultdict(lambda: defaultdict(int))
        n = len(coins)
        for l in range(n + 1):
            F[0][l] = 1   # trivial case
             # why not start from 0, because we need to handle trivial case F[0][0]

        for a in range(1, amount + 1):
            for l in range(1, n + 1):
                F[a][l] = F[a][l-1] + F[a - coins[l-1]][l]

        return F[amount][n]


    def change_TLE(self, amount, coins):
        """
        Like the take the step for the stairs dp

        let F[amount][i] = # ways ending using coin[i]
        F[amount][i] += F[amount - coin[i]][j] for j in range(i)

        O(n^3)
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount == 0:
            return 1

        coins.sort()
        n = len(coins)
        F = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            F[coins[i]][i] = 1

        for a in range(1, amount + 1):
            for i in range(n):
                for j in range(i + 1):
                    F[a][i] += F[a - coins[i]][j]

        return sum(F[amount].values())

    def change_error(self, amount, coins):
        """
        Like the take the step for the stairs dp

        let F[amount] = # ways
        F[amount] += F[amount - v] for v in coins
        error: count repeated: 1 + 2, 2 + 1

        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        F = {0: 1}
        for a in range(1, amount + 1):
            F[a] = 0
            for c in coins:
                if a - c in F:
                    F[a] += F[a - c]

        return F[amount]


if __name__ == "__main__":
    assert Solution().change(5, [1, 2, 5]) == 4
