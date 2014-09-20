"""
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
"""
__author__ = 'Danyang'
class Solution:
    def isScramble(self, s1, s2):
        """
        dfs
        partition and compare

        Compare two trees constructed from the two strings respectively. Two trees are scramble of the other iff A's
        left/right subtree is the scramble of B's left/right subtree or A's left/right subtree is the scramble of B's
        right/left subtree.

        .....|... vs. .....|... or
        ...|..... vs. .....|...

        :param s1:
        :param s2:
        :return: boolean
        """
        if len(s1)!=len(s2):
            return False
        chars = [0 for _ in xrange(26)]
        for char in s1:
            chars[ord(char)-ord('a')] += 1
        for char in s2:
            chars[ord(char)-ord('a')] -= 1

        # if filter(lambda x: x!=0, chars):
        #     return False
        for val in chars:
            if val!=0:
                return False

        if len(s1)==1:
            return True


        for i in xrange(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or \
                self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:len(s2)-i]):
                return True

        return False



if __name__=="__main__":
    assert Solution().isScramble("abc", "bca")==True
