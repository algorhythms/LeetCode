"""
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
"""
__author__ = 'Danyang'
class Solution:
    def multiply(self, num1, num2):
        """
        Google Phone Interview Question, 20 Sep 2013
        Steps:
        * multiply by 1 digit at a time
        * add the temporary results up

        To make the processing easier:
        * order the two numbers
        * reverse the numbers

        Solved around 1 hour

        :param num1: String
        :param num2: String
        :return: String
        """
        result = []

        # pre processing
        if len(num1)<len(num2): # order them first
            num1, num2 = num2, num1

        num2 = num2[::-1]  # reverse them first
        num1 = num1[::-1]

        # multiply by 1 digit at a time
        for i in range(len(num2)):
            result.append(self.multiply_1_digit(num2[i], num1))

        # add the temporary results up
        lst = self.add_list(result)


        # post processing
        lst.reverse()  # reverse back
        result = "".join(str(item) for item in lst).lstrip("0")
        if not result:
            return "0"
        return result

    def multiply_1_digit(self, digit, num):
        """
        :param digit: String
        :param num: String
        :return: list of digit in reverse order
        """
        digit = int(digit)
        temp = [int(item) for item in num]

        carry = 0
        for ind in range(len(temp)):
            val = temp[ind]
            mul = val*digit+carry
            carry = mul/10
            mul = mul%10
            temp[ind] = mul

        if carry!=0:
            temp.append(carry)

        return temp


    def add_list(self, lst):
        """
        add lst of string
        :param lst:
        :return:
        """
        appending_zero = 0
        result = [0]
        for ind, val in enumerate(lst):
            for i in range(appending_zero):
                val.insert(0, 0)  # NOTICE: side-effect
            result = self.add(result, val)
            appending_zero += 1
        return result




    def add(self, num1, num2):
        """
        :param num1: list of digits in reverse order
        :param num2: list of digits in reverse order
        :return: list of digits in reverse order
        """
        num1 = list(num1)  # NOTICE: local copy
        num2 = list(num2)  # NOTICE: local copy
        if len(num1)<len(num2):
            num1, num2 = num2, num1

        carry = 0
        for ind in range(len(num1)):  # longer one
            try:
                result = num1[ind]+num2[ind]+carry
            except IndexError:
                result = num1[ind]+carry
                if result==num1[ind]: break  # prune


            carry = result/10
            num1[ind] = result%10

        if carry!=0:
            num1.append(carry)

        return num1




if __name__=="__main__":
    solution = Solution()
    #assert [1, 2]==solution.add([2,1], [9])
    #assert [1, 9, 9, 8]==solution.multiply_1_digit("9", "999")
    #assert str(123*999)==solution.multiply("123", "999")
    #assert str(0)==solution.multiply("0", "0")
    assert str(123*456)==solution.multiply("123", "456")