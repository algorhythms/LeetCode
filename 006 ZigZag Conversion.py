"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display
this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""
__author__ = 'Danyang'


class Solution:
    def convert(self, s, nRows):
        """
        Algorithm: matrix
        :param s:
        :param nRows:
        :return: a String
        """
        length = len(s)
        matrix = [[] for _ in xrange(nRows)]

        i = 0
        while i < length:
            try:
                # going down
                for j in xrange(nRows):
                    matrix[j].append(s[i])
                    i += 1

                # going up
                for j in xrange(nRows-1-1, 0, -1):
                    matrix[j].append(s[i])
                    i += 1

            except IndexError:
                break

        lst = ["".join(element) for element in matrix]
        return "".join(lst)


if __name__ == "__main__":
    assert Solution().convert("ABCD", 2) == "ACBD"