"""
Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.
"""
__author__ = 'Danyang'
class Solution:
    def anagrams_complicated(self, strs):
        """
        sorting
        :param strs: a list of strings
        :return: a list of strings
        """
        temp = list(strs)
        for ind, string in enumerate(temp):
            if string and string!="":  # avoid case of empty string
                string = [char for char in string]
                string.sort()
                string = "".join(string)
                temp[ind] = string


        hash_map = {}
        for ind, string in enumerate(temp):
            indexes = hash_map.get(string, [])
            indexes.append(ind)  # side-effect
            hash_map[string] = indexes

        result = []
        for val in hash_map.values():
            if len(val)>1:
                # result.append([strs[i] for i in val])
                result += [strs[i] for i in val]
        return result

    def anagrams(self, strs):
        """
        Algorithm: sort string and hash map
        :param strs: a list of strings
        :return: a list of strings
        """
        hash_map = {}
        for ind, string in enumerate(strs):
            string = "".join(sorted(string))  # string reversing and sorting are a little different
            if string not in hash_map:
                hash_map[string] = [ind]
            else:
                hash_map[string].append(ind)
            # indexes = hash_map.get(string, [])
            # indexes.append(ind)  # side-effect
            # hash_map[string] = indexes  # reassign

        result = []
        for val in hash_map.values():
            if len(val)>1:
                # result.append([strs[i] for i in val])
                result += [strs[i] for i in val]
        return result

if __name__=="__main__":
    Solution().anagrams(["", ""])