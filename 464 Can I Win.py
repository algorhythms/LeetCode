#!/usr/bin/python3
"""
In the "100 game," two players take turns adding, to a running total, any
integer from 1..10. The player who first causes the running total to reach or
exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers
of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine
if the first player to move can force a win, assuming both players play
optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and
desiredTotal will not be larger than 300.
"""


class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        can p win?
        F^p_{total, choice_set - i} = not any(
            F^p'_{total - A[j] - A[i], choice_set - j - i}
            for j
        )

        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        cache = {}
        # set is not hashable while frozenset is
        choices = frozenset([choice for choice in range(1, maxChoosableInteger + 1)])
        return self._can_win(desiredTotal, choices, sum(choices), cache)

    def _can_win(self, total, choices, gross,cache):
        if (total, choices) in cache:
            return cache[(total, choices)]

        ret = False
        if max(choices) >= total:
            ret = True

        elif gross < total:
            ret = False
        else:
            for choice in choices:
                if not self._can_win(
                        total - choice,
                        choices - set([choice]),
                        gross - choice,
                        cache
                ):
                    ret = True
                    break

        cache[(total, choices)] = ret
        return ret


if __name__ == "__main__":
    assert Solution().canIWin(10, 11) == False
    assert Solution().canIWin(10, 0) == True
    assert Solution().canIWin(13, 11) == True
