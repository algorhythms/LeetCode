__author__ = 'Danyang'
class Solution:
    # @return an integer
    def romanToInt(self, s):
        roman2int_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }


        result = 0
        for ind, val in enumerate(s):
            if ind>0 and roman2int_map[val]>roman2int_map[s[ind-1]]:  # e.g. XIV
                result -= roman2int_map[s[ind-1]]  # reverse last action
                result += roman2int_map[val]-roman2int_map[s[ind-1]]
            else:
                result += roman2int_map[val]

        return result




