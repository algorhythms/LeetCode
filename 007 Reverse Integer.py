__author__ = 'Danyang'
class Solution:
    # @return an integer
    def reverse(self, x):
        sign = -1 if x<0 else 1
        x = sign*x
        # leading zeros
        while x:
            if x%10==0:
                x/=10
            else:
                break

        x = str(x)
        lst = list(x)
        lst.reverse()
        x = "".join(lst)
        x = int(x)
        return sign*x

if __name__=="__main__":
    print Solution().reverse(123)

