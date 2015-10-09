"""
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?
"""
__author__ = 'Daniel'


class Solution(object):
    def hIndex(self, citations):
        """
        Given sorted -> binary search
        From linear search into bin search
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        s = 0
        e = n
        while s < e:
            m = (s+e)/2
            if citations[m] >= n-m:
                e = m
            else:
                s = m+1

        return n-s


if __name__ == "__main__":
    assert Solution().hIndex([0, 1, 3, 5, 6]) == 3