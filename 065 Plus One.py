"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""
__author__ = 'Danyang'
class Solution:
    def plusOne(self, digits):
        """
        Math
        :param digits: a list of integer digits
        :return: a list of integer digits
        """
        cur = len(digits)-1
        while True:
            if cur>=0:
                digits[cur] += 1
                if digits[cur]<10:
                    break
                else:
                    digits[cur] -= 10
                    cur -= 1
            else:
                # MSB
                digits.insert(0, 1)
                break

        return digits

if __name__=="__main__":
    digits = [9]
    assert Solution().plusOne(digits)==[1, 0]