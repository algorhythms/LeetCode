__author__ = 'Danyang'
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ""

        str_builder = ""
        min_len = min(len(string) for string in strs)
        for i in range(min_len):
            flag = True
            char = None
            for str in strs:
                try:
                    if not char:
                        char = str[i]
                    else:
                        if str[i]!=char:
                            flag = False
                            break

                except IndexError:
                    flag = False
                    break

            if flag:
                str_builder += char
            else:
                break

        return str_builder



if __name__=="__main__":
    strs = ["abc", "abcd"]
    print Solution().longestCommonPrefix(strs)