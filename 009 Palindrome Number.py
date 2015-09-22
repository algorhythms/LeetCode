"""
Determine whether an integer is a palindrome. Do this without extra space.
"""
__author__ = 'Danyang'


class Solution:
    def isPalindrome(self, x):
        """
        Algorithm: int, compare lsb and msb
        No extra space
        If you are thinking of converting the integer to string, note the restriction of using extra space.

        :param x: int
        :return: boolean
        """
        if x < 0:
            return False

        # find order of magnitude
        div = 1
        while x/div >= 10:
            div *= 10  # without touch x

        while x > 0:
            msb = x/div
            lsb = x%10

            if msb != lsb:
                return False

            # shrink
            x %= div
            x /= 10

            div /= 100

        return True


if __name__ == "__main__":
    Solution().isPalindrome(2147483647)