"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to
group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
"""
import re

__author__ = 'Daniel'


class Solution:
    def diffWaysToCompute(self, input):
        """
        Looping + Divide & Conquer

        :type: input
        :rtype: list[]
        """
        input_lst = re.split(r"(\D)", input)  # capturing parentheses
        nums = map(int, filter(lambda x: re.match(r"\d+", x), input_lst))
        ops = filter(lambda x: re.match(r"\D", x), input_lst)
        ret = self.dfs_eval(nums, ops)
        return ret

    def dfs_eval(self, nums, ops):
        ret = []
        if not ops:
            assert len(nums) == 1
            return nums

        for i, op in enumerate(ops):
            left_vals = self.dfs_eval(nums[:i+1], ops[:i])
            right_vals = self.dfs_eval(nums[i+1:], ops[i+1:])
            for l in left_vals:
                for r in right_vals:
                    ret.append(self._eval(l, r, op))

        return ret

    def _eval(self, a, b, op):
        return {
            "+": lambda a, b: a+b,
            "-": lambda a, b: a-b,
            "*": lambda a, b: a*b,
        }[op](a, b)


if __name__ == "__main__":
    assert Solution().diffWaysToCompute("1+1") == [2]
