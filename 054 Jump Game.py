__author__ = 'Danyang'
class Solution:
    def canJump_TLE(self, A):
        """
        dp
        TLE
        :param A: a list of integers
        :return: a boolean
        """
        length = len(A)
        dp = [set([index]) for index in range(length)]

        for ind, val in enumerate(A):
            if ind!=0 and len(dp[ind])<2:
                continue

            # jump forward
            for i in xrange(ind+1, ind+val+1):
                if i>=length:
                    break
                for item in dp[ind]:
                    dp[i].add(item)

        return 0 in dp[-1]


    def canJump(self, A):
        """
        dp
        max_reach[i] = max(max_reach[i-1], A[i]+i)  # path not recorded, information overwritten 
        scanning
        :param A: a list of integers
        :return: a boolean
        """
        length = len(A)
        # trivial
        if length<=1:
            return True

        max_reach = [-1]*length

        max_reach[0] = A[0]+0  # reachable index
        for i in xrange(1, length):
            # able to reach the end index
            if max_reach[i-1]>=length-1:
                return True

            # fail to reach current index
            if max_reach[i-1]<i:
                return False

            max_reach[i] = max(max_reach[i-1], A[i]+i)

        return False



if __name__=="__main__":
    print Solution().canJump([2,3,1,1,4])
