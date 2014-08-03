__author__ = 'Danyang'


class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        """
        record how to construct the sentences for a given prefix

        In Word Break, we use a bool array to record whether a prefix could be segmented.
        Now we should use a vector for every prefix to record how to construct that prefix from another prefix.
        """
        # prefix = [[]] * (len(s) + 1) # namespace reuse
        prefix = [[] for _ in range(len(s)+1)]

        prefix[0].append("dummy")

        for i in range(len(s)):
            if not prefix[i]:
                continue
            for word in dict:
                if s[i: i+len(word)]==word:
                    prefix[i+len(word)].append(word)


        # build result
        if not prefix[-1]:
            return []

        out = []
        cur_sentence = []
        self.__build_result(prefix, len(s), cur_sentence, out)
        return out


    def __build_result(self, prefix, cur_index, cur_sentence, out):
        """
        recursive
        """
        if cur_index==0:
            string_builder = ""
            for i in range(len(cur_sentence)-1, -1, -1):
                string_builder += cur_sentence[i]
                if i!=0:
                    string_builder += " "
            out.append(string_builder)
            return


        for i in range(len(prefix[cur_index])):
            cur_sentence.append(prefix[cur_index][i])
            self.__build_result(prefix, cur_index-len(prefix[cur_index][i]), cur_sentence, out)
            cur_sentence.pop()

if __name__=="__main__":
    print Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])