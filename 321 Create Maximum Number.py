"""
Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <=
m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array
of the k digits. You should try to optimize your time and space complexity.

Example 1:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

Example 2:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

Example 3:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9]
"""
__author__ = 'Daniel'


class SolutionTLE(object):
    def maxNumber(self, nums1, nums2, k):
        """
        http://algobox.org/2015/12/24/create-maximum-number/
        O(kN(N+M))
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        maxa = []
        n1, n2 = len(nums1), len(nums2)
        for l1 in xrange(min(n1, k)+1):
            l2 = k - l1
            assert l2 >= 0
            A1, A2 = self.maxNumberSingle(nums1, l1), self.maxNumberSingle(nums2, l2)
            cur = self.maxNumberDual(A1, A2)
            if not maxa or self.eval(maxa) < self.eval(cur):
                maxa = cur

        return maxa

    def eval(self, lst):
        return int("".join(map(str, lst)))

    def maxNumberSingle(self, A, k):
        """
        maxNumber of k elements from a single list A
        """
        stk = []
        n = len(A)
        for i in xrange(n):
            while stk and len(stk)-1+(n-1-i+1) >= k and stk[-1] < A[i]: stk.pop()
            if len(stk) < k:
                stk.append(A[i])

        return stk

    def maxNumberDual(self, A1, A2):
        """
        maxNumber of all elements from dual lists A1 and A2.
        """
        ret = []
        p1, p2 = 0, 0
        while p1 < len(A1) and p2 < len(A2):
            ahead1, ahead2 = p1, p2
            while ahead1 < len(A1) and ahead2 < len(A2) and A1[ahead1] == A2[ahead2]:
                ahead1, ahead2 = ahead1+1, ahead2+1

            if ahead2 >= len(A2) or (ahead1 < len(A1) and A1[ahead1] > A2[ahead2]):
                ret.append(A1[p1])
                p1 += 1
            else:
                ret.append(A2[p2])
                p2 += 1

        # dangling
        ret.extend(A1[p1:])
        ret.extend(A2[p2:])
        return ret
