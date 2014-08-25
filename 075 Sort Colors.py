__author__ = 'Danyang'
class Solution:
    def sortColors(self, A):
        """
        pivoting
        constant space
        :param A: a list of integers
        :return: nothing, sort in place
        """
        RED, WHITE, BLUE = 0, 1, 2
        red_end_ptr = -1
        blue_start_ptr= len(A)

        i = 0
        while i<blue_start_ptr:
            if A[i]==WHITE: # pivot set
                i += 1
            elif A[i]==RED:
                red_end_ptr+=1
                A[red_end_ptr], A[i] = A[i], A[red_end_ptr]
                i += 1
            else:
                blue_start_ptr -= 1
                A[blue_start_ptr], A[i] = A[i], A[blue_start_ptr]
                # no i+=1, since you need to examine A[i] again

        # print A

if __name__=="__main__":
    Solution().sortColors([1, 2, 0])