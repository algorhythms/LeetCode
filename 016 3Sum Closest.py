__author__ = 'Danyang'
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        """
        two pointers scanning algorithm
        :param num: array
        :param target: target
        :return: sum of the three digits
        """
        min_distance = 1<<32
        num.sort()
        min_summation = 0
        for ind, val in enumerate(num):
            i = ind+1
            j = len(num)-1
            while i<j:
                lst = [val, num[i], num[j]]
                if min_distance>abs(target-sum(lst)):
                    min_summation = sum(lst)
                    if sum(lst)==target:
                        return min_summation
                    min_distance = abs(target-min_summation)
                elif sum(lst)>target:
                    j -= 1
                else:
                    i += 1
        return min_summation

if __name__=="__main__":
    print Solution().threeSumClosest([1, 1, 1, 1], 0)

