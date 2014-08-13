__author__ = 'Danyang'
class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum_TLE(self, num, target):
        """
        Two pointers
        O(n^3) typically, O(n^(k-1))

        Notice:
        Algorithm able to pass in Java or C++, but not Python

        :param num: array
        :return: a list of lists of length 3, [[val1,val2,val3]]
        """

        # record result
        result = []
        num.sort()
        length = len(num)

        h = 0
        while h<length-3:
            i = h+1
            while i<length-2:
                j = i+1
                k = length-1
                while j<k:
                    lst = [num[h], num[i], num[j], num[k]]
                    summation = sum(lst)
                    if summation==target:
                        result.append(lst)
                        k -= 1
                        j += 1
                        # remove duplicate
                        while j<k and num[j]==num[j-1]:
                            j += 1
                        while j<k and num[k]==num[k+1]:
                            k -= 1
                    elif summation>target:
                        k -= 1
                    else:
                        j += 1
    
                i += 1
                # remove duplicate
                while i<length-2 and num[i]==num[i-1]:
                    i += 1
            h += 1
            # remove duplicate
            while h<length-3 and num[h]==num[h-1]:
                h += 1

        return result

    def fourSum(self, num, target):
        """
        O(n^2) with Hash Table
        :param num: array
        :param target: int
        :return: a list of lists of length 4, [[val1,val2,val3,val4]]
        """
        length, result_set, sum2index = len(num), set(), {}
        if length<4:
            return []

        num.sort()
        for p in xrange(length):
            for q in xrange(p+1, length):
                # record the pair sum
                if num[p]+num[q] not in sum2index:
                    sum2index[num[p]+num[q]] = [(p, q)]
                else:
                    sum2index[num[p]+num[q]].append((p, q))

        for i in xrange(length):
            for j in xrange(i+1, length-2):
                sum_remain = target-num[i]-num[j]
                if sum_remain in sum2index:
                    for pair in sum2index[sum_remain]:
                        if pair[0]>j:  # avoid duplicate
                            result_set.add(( num[i], num[j], num[pair[0]], num[pair[1]] ))

        return [list(i) for i in result_set]  # convert tuple to list