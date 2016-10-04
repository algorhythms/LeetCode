"""
Premium Question
"""
__author__ = 'Daniel'


class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        ret = (target, len(target))
        for abbr, abbr_l in self.dfs(target):
            if self.validate(dictionary, abbr) and ret[1] > abbr_l:
                ret = (abbr, abbr_l)

        return ret[0]

    def dfs(self, word):
        """
        backtracking, pivoting letter
        :type word: str
        :rtype: List[str]
        """
        if not word:
            return [("", 0)]

        ret = []
        for l in xrange(len(word)+1):
            left_num = str(l) if l else ""
            left_l = 1 if left_num != "" else 0
            left_l += 1 if l < len(word) else 0

            for right, right_l in self.dfs(word[l+1:]):
                cur = left_num + word[l:l+1] + right  # word[l:l+1] possible ""
                ret.append((cur, left_l + right_l))

        return ret

    def validate(self, dictionary, abbr):
        for w in dictionary:
            if self.validWordAbbreviation(w, abbr):
                return False

        return True

    def validWordAbbreviation(self, word, abbr):
        """
        pointers
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        w = 0
        a = 0
        while w < len(word) and a < len(abbr):
            if abbr[a].isdigit() and abbr[a] != '0':
                e = a
                while e < len(abbr) and abbr[e].isdigit(): e += 1
                num = int(abbr[a:e])
                a = e
                w += num
            else:
                if word[w] != abbr[a]:
                    return False

                w += 1
                a += 1

        return w == len(word) and a == len(abbr)


if __name__ == "__main__":
    assert Solution().minAbbreviation("apple", ["blade"]) == "a4"
