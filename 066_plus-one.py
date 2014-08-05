__author__ = 'Danyang'


class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        """
        Math
        """
        cur = len(digits)-1
        while True:
            if cur>=0:
                digits[cur]+=1
                if digits[cur]<10:
                    break
                else:
                    digits[cur]-=10
                    cur-=1
            else:
                # MSB
                digits.insert(0, 1)
                break

        return digits

if __name__=="__main__":
    digits = [9]
    assert Solution().plusOne(digits)==[1, 0]