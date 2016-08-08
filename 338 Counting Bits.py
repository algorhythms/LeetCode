"""
Given a non negative integer number num. For every numbers i in the range 0 <= i <= num calculate the number of 1's in
their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /
possibly in a single pass?

Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other
language.
"""
__author__ = 'Daniel'


class Solution(object):
    def countBits(self, num):
        """
        Dynamic programming: make use of what you have produced already
          0 => 0
          1 => 1

         10 => 1+0
         11 => 1+1

        100 => 1+0
        101 => 1+1
        110 => 1+1
        111 => 1+2

        :type num: int
        :rtype: List[int]
        """
        ret = [0]
        i = 0
        hi = len(ret)
        while len(ret) < num + 1:
            if i == hi:
                i = 0
                hi = len(ret)

            ret.append(1+ret[i])
            i += 1

        return ret
