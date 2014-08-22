__author__ = 'Danyang'
class Solution:
    def generate(self, numRows):
        """
        math
        :param numRows: integer
        :return: a list of lists of integers
        """
        result = []
        for row in xrange(numRows):
            current = []
            for col in xrange(row+1):
                if col==0 or col==row:
                    current.append(1)
                else:
                    current.append(result[row-1][col-1]+result[row-1][col])
            result.append(current)

        return result

if __name__=="__main__":
    print Solution().generate(5)