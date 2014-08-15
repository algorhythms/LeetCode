__author__ = 'Danyang'
class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        lst = []
        self.generateParenthesisDfs(lst, "", n, n)
        return lst

    def generateParenthesisDfs(self, lst, cur, left, right):
        """
        DFS
        Catalan Number
        :param lst: result list
        :param cur: currently processing string
        :param left: number of left parenthesis left
        :param right: number of right parenthesis left
        """
        # trivial
        if left==0 and right==0:
            lst.append(cur)
        # add left parenthesis
        if left>0:
            self.generateParenthesisDfs(lst, cur+"(", left-1, right)
        # add right parenthesis
        if right>left:
            self.generateParenthesisDfs(lst, cur+")", left, right-1)
