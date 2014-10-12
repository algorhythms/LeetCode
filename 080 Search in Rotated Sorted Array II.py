"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
"""
__author__ = 'Danyang'
class Solution:
    def search_set(self, A, target):
        """
        Follow up 033 Search in Rotated Sorted Array
        Duplicate allowed

        rotated cases:
        target is 3
        start   mid      end
        case 1:
        1, 1, 1, 1, 1, 3, 1
        case 2:
        1, 3, 1, 1, 1, 1, 1

        Algorithm: eliminate duplicates
        :param A: a list of integers
        :param target: an integer
        :return: a boolean
        """
        A = list(set(A))  # short-cut eliminate duplicates  # but O(n)

        length = len(A)
        start = 0
        end = length-1
        while start<=end:
            mid = (start+end)/2
            # found
            if A[mid]==target:
                return True
            # case 1
            if A[start]<A[mid]<A[end]:
                if target>A[mid]:
                    start = mid+1
                else:
                    end = mid-1
            # case 2
            elif A[start]>A[mid] and A[mid]<A[end]:
                if target>A[mid] and target<=A[end]:
                    start = mid+1
                else:
                    end = mid-1
            # case 3
            else:
                if target<A[mid] and target>=A[start]:
                    end = mid-1
                else:
                    start = mid+1

        return False

    def search(self, A, target):
        """
        Follow up 033 Search in Rotated Sorted Array
        Duplicate allowed

        rotated cases:
        target is 3
        start   mid      end
        case 1:
        1, 1, 1, 1, 1, 3, 1
        case 2:
        1, 3, 1, 1, 1, 1, 1

        Algorithm: advance pointer if undetermined
        :param A: a list of integers
        :param target: an integer
        :return: a boolean
        """
        length = len(A)
        start = 0
        end = length-1
        while start<=end:
            mid = (start+end)/2
            # found
            if A[mid]==target:
                return True
            # undetermined  # the only significant difference.
            if A[start]==A[mid]:
                start += 1
            # case 1
            elif A[start]<A[mid]<=A[end]:
                if target>A[mid]:
                    start = mid+1
                else:
                    end = mid-1
            # case 2
            elif A[start]>A[mid] and A[mid]<=A[end]:  # slight difference compared to A[mid]<A[end]
                if target>A[mid] and target<=A[end]:
                    start = mid+1
                else:
                    end = mid-1
            # case 3
            else:
                if target<A[mid] and target>=A[start]:
                    end = mid-1
                else:
                    start = mid+1

        return False

if __name__=="__main__":
    assert Solution().search([1,1,3,1], 3)==True