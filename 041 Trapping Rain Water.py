__author__ = 'Danyang'
class Solution:
    def trap(self, A):
        """
        Simplified version of Palantir Technology Online Test 2013

        Algorithm: forward scanning & backward scanning

        :param A: a list of integers
        :return: an integer
        """
        left_maxs = [0 for _ in A]  # on the left including itself
        right_maxs = [0 for _ in A]  # on the right including itself

        left_max = 0
        for ind, val in enumerate(A):
            left_max = max(left_max, val)
            left_maxs[ind] = left_max

        right_max = 0
        # for ind, val in enumerate(reversed(A)):  # ind incorrect
        for ind, val in reversed(list(enumerate(A))):
            right_max = max(right_max, val)
            right_maxs[ind] = right_max

        # calculate the volume
        volume = 0
        for ind, val in enumerate(A):
            volume += max(0, min(left_maxs[ind], right_maxs[ind]) - val)

        return volume


if __name__=="__main__":
    print Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])




