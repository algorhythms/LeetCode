"""
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the
researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h
citations each, and the other N - h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had
received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the
remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.
"""
__author__ = 'Daniel'


class Solution(object):
    def hIndex(self, citations):
        """
        Reverse mapping & DP
        Determine the range of h-index
        Chunk by n
        Let F[i] be the #paper with i citations (later transform F[i] to #paoer with >= i citations
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        F = [0 for _ in xrange(n+1)]
        for elt in citations:
            if elt >= n:  # chunk
                F[n] += 1
            else:
                F[elt] += 1

        if F[n] >= n:
            return n

        for i in xrange(n-1, -1, -1):
            F[i] += F[i+1]
            if F[i] >= i:
                return i

        return 0

    def hIndex_sort(self, citations):
        """
        Algorithm forward sort
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        citations.sort()
        for i in xrange(n):
            if citations[i] >= n-i:
                return n-i

        return 0

    def hIndex_reverse_sort(self, citations):
        """
        Algorithm sort
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        citations.append(0)
        h = 0
        for i in xrange(len(citations)-1):
            if citations[i] >= i+1 >= citations[i+1]:
                h = i+1
            elif h:
                break

        return h

if __name__ == "__main__":
    assert Solution().hIndex([3, 0, 6, 1, 5]) == 3