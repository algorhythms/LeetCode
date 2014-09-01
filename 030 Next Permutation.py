__author__ = 'Danyang'
class Solution:
    def nextPermutation(self, num):
        """
        Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

        math problem; algorithm: http://fisherlei.blogspot.sg/2012/12/leetcode-next-permutation.html
        :param num: a list of integer
        :return: a list of integer
        """
        length = len(num)

        partition_num_index = 0
        change_num_index = 0

        for i in reversed(xrange(1, length)):
            if num[i]>num[i-1]:
                partition_num_index = i-1
                break
        for i in reversed(xrange(1, length)):
            if num[i]>num[partition_num_index]:
                change_num_index = i
                break

        num[partition_num_index], num[change_num_index] = num[change_num_index], num[partition_num_index]

        if partition_num_index==change_num_index==0:
            # If such arrangement is not possible, to lowest possible order (ie, sorted in ascending order).
            num.reverse()
        else:
            num[partition_num_index+1:] = reversed(num[partition_num_index+1:])
        return num

if __name__=="__main__":
    print Solution().nextPermutation([3, 2, 1])
