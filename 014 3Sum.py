__author__ = 'Danyang'
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum_duplicate(self, num):
        """
        Hash
        O(n^2)
        :param num: array
        :return: a list of lists of length 3, [[val1,val2,val3]]
        """
        reverse_map = {}
        for ind, val in enumerate(num):
            if val not in reverse_map:
                reverse_map[val] = [ind]
            else:
                reverse_map[val].append(ind)

        result = []
        for i in xrange(len(num)):
            for j in xrange(i, len(num)):
                target = 0 - num[i] - num[j]
                if target not in reverse_map:
                    continue
                for index in reverse_map[target]:
                    if i!=index and j!=index:
                        result.append([num[i], num[j], target])
                        break
        return result

    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum_TLE(self, num):
        """
        Hash
        O(n^2)
        :param num: array
        :return: a list of lists of length 3, [[val1,val2,val3]]
        """

        # hash
        reverse_map = {}
        for ind, val in enumerate(num):
            if val not in reverse_map:
                reverse_map[val] = [ind]
            else:
                reverse_map[val].append(ind)


        result = {}
        for i in xrange(len(num)):
            for j in xrange(i, len(num)):
                target = 0-num[i]-num[j]
                if target not in reverse_map:
                    continue
                for index in reverse_map[target]:
                    if index!=i and index!=j:
                        lst = sorted([num[i], num[j], target])
                        lst = tuple(lst)
                        result[lst] = 1 # hash
                        break

        return result.keys()

    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        """
        Two pointers
        http://en.wikipedia.org/wiki/3SUM
        O(n^2)
        Notice:
        0. duplicated element will cause "Output Limit Exceeded" error
        1. set is not implemented in LeetCode
        :param num: array
        :return: a list of lists of length 3, [[val1,val2,val3]]
        """

        # record result
        result = []
        num.sort()
        i = 0
        while i<len(num)-2:
            j = i+1
            k = len(num)-1
            while j<k:
                lst = [num[i], num[j], num[k]]
                if sum(lst)==0:
                    result.append(lst)
                    k -= 1
                    j += 1
                    # remove duplicate
                    while j<k and num[j]==num[j-1]:
                        j += 1
                    while j<k and num[k]==num[k+1]:
                        k -= 1
                elif sum(lst)>0:
                    k -= 1
                else:
                    j += 1

            i += 1
            # remove duplicate
            while i<len(num)-2 and num[i]==num[i-1]:
                i += 1


        return result






if __name__=="__main__":
    print Solution().threeSum([-1, 0, 1, 2, -1, -4])