__author__ = 'Danyang'
class Solution:
    # @return a string
    def countAndSay(self, n):
        """
        :param n: integer
        :return: output representation in string
        """
        string = "1"
        for i in range(1, n):
            string = self.singleCountAndSay(string)
        return string


    def singleCountAndSay(self, num_string):
        """
        Two pointers algorithm
        :param num_string: input number as string
        :return: output representation as string
        """
        string_builder = ""

        i = 0
        while i<len(num_string):
            # find next different number
            j = i+1
            while j<len(num_string) and num_string[j]==num_string[i]:
                j += 1
            count = j-i
            string_builder += str(count)+str(num_string[i])
            i = j

        return string_builder

if __name__=="__main__":
    print Solution().countAndSay(4)