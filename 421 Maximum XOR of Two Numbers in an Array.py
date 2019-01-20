#!/usr/bin/python3
"""
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 2^31.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?
"""


class Solution:
    def findMaximumXOR(self, nums):
        """
        Brute force: O(n^2)
        constrinat: 32 bit
        check bit by bit rather than number by number
        build the bit from MSB to LSB, since be need the largest

        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for i in reversed(range(32)):
            prefixes = set(num >> i for num in nums)
            ret <<= 1
            # fixing the remaining bit, set the LSB
            cur = ret + 1
            for p in prefixes:
                # a ^ b ^ a = b
                if cur ^ p in prefixes:
                    ret = cur
                    break  # found one

        return ret


if __name__ == "__main__":
    assert Solution().findMaximumXOR([3, 10, 5, 25, 2, 8]) == 28
