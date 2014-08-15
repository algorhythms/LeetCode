__author__ = 'Danyang'
class Solution:
    # @return a boolean
    def isValid(self, s):
        """
        Stack
        """
        put_set = ("(", "[", "{")
        pop_set = (")", "]", "}")
        pair = dict(zip(put_set, pop_set))
        stack = []
        for element in s:
            if element in put_set:
                stack.append(pair[element])
            elif element in pop_set:
                if not stack or element!=stack.pop():  # otherwise, IndexError: pop from empty list
                    return False

        return True if not stack else False

if __name__=="__main__":
    Solution().isValid("()")