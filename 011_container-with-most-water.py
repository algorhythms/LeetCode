__author__ = 'Danyang'
class Solution:
    # @return an integer
    def maxArea(self, height):
        """
        Two pointers scanning
        starting from two ends since x-coordinate is maximized
        :param height: array
        :return: max area
        """
        start = 0
        end = len(height)-1

        max_area = -1<<32
        while start<end:
            area = min(height[start], height[end]) * (end-start)
            max_area = max(area, max_area)

            # move the shorter boarder
            if height[start]<height[end]:
                start += 1
            else:
                end -= 1

        return max_area

