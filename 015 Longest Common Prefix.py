"""
Write a function to find the longest common prefix string amongst an array of strings.
"""
__author__ = 'Danyang'
class Solution:
    def longestCommonPrefix(self, strs):
        """
        O(k*n)
        :param strs: a list of string
        :return: string, prefix
        """
        # checking, otherwise: ValueError: min() arg is an empty sequence
        if not strs:
            return ""

        n = len(strs)

        str_builder = ""
        min_len = min(len(string) for string in strs)
        for i in range(min_len):
            char = strs[0][i]

            j = 0
            while j<n:
                try:
                    if strs[j][i]!=char: break
                    j += 1
                except IndexError:
                    break

            if j==n:
                str_builder += char
            else:
                break

        return str_builder



if __name__=="__main__":
    strs = ["abc", "abcd"]
    print Solution().longestCommonPrefix(strs)