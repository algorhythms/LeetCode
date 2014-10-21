"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6
"""
__author__ = 'Danyang'
class Solution:
    def maxProduct_error(self, A):
        """
        dp, collect number of negative number
        notice 0
        :param A: a list of int
        :return: int
        """
        if not A:
            return
        length = len(A)
        if length==1:
            return A[0]

        dp = [-1 for _ in xrange(length+1)]
        dp[length] = 0 # dummy
        for i in xrange(length-1, -1, -1):
            if A[i]<0:
                dp[i] = dp[i+1]+1
            elif A[i]==0:
                dp[i] = 0
            else:
                dp[i] = dp[i+1]

        global_max = -1<<32
        # cur = 1  # starting from 0, encountering problem [-2, 0, -1]
        # for ind, val in enumerate(A):
        #     cur *= val
        #     if cur<0 and dp[ind+1]<1 or cur==0:
        #             cur = 1
        #     global_max = max(global_max, cur)

        cur = 0  # starting from 0
        for ind, val in enumerate(A):
            if cur!=0:
                cur *= val
            else:
                cur = val

            if cur<0 and dp[ind+1]<1:
                cur = 0

            global_max = max(global_max, cur)

        return global_max

    def maxProduct(self, A):
        """
        dp, collect number of negative number (notice 0).
        negative number and 0 will be special in this question

        two pointers, sliding window

        :param A: a list of int
        :return: int
        """
        if not A:
            return
        length = len(A)
        if length==1:
            return A[0]

        dp = [-1 for _ in xrange(length+1)]
        dp[length] = 0 # dummy
        for i in xrange(length-1, -1, -1):
            if A[i]<0:
                dp[i] = dp[i+1]+1
            elif A[i]==0:
                dp[i] = 0
            else:
                dp[i] = dp[i+1]

        global_max = -1<<32
        cur = 0  # starting from 0
        start_ptr = 0
        end_ptr = 0
        while end_ptr<length:  # [start, end), expanding
            if cur!=0:
                cur *= A[end_ptr]
            else:
                cur = A[end_ptr]
                start_ptr = end_ptr

            end_ptr += 1

            if cur<0 and dp[end_ptr]<1:
                # from the starting point, get the first negative 
                while start_ptr<=end_ptr and A[start_ptr]>0:
                    cur /= A[start_ptr]
                    start_ptr += 1
                if A[start_ptr]<0:
                    cur /= A[start_ptr]
                    start_ptr += 1
                if start_ptr==end_ptr:  # consider A=[-2, 0, -1] when processing [-1]
                    cur = 0 # otherwise 1
                    
            global_max = max(global_max, cur)



        return global_max


if __name__=="__main__":
    assert Solution().maxProduct([2,-5,-2,-4,3])==24
    assert Solution().maxProduct([-2, 0, -1])==0
    assert Solution().maxProduct([-2])==-2
    assert Solution().maxProduct([2, 3, -2, 4, -2])==96
    assert Solution().maxProduct([2, 3, -2, 4, 0, -2])==6
    assert Solution().maxProduct([2,3,-2,4])==6
