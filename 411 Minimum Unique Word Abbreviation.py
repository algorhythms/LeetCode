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
        ret = target
        for abbr in self.dfs(target):
            if self.validate(dictionary, abbr) and len(ret) > len(abbr):
                ret = abbr

        return ret

    def dfs(self, word):
        """
        backtracking, pivoting letter
        :type word: str
        :rtype: List[str]
        """
        if not word:
            return [""]

        ret = []
        for l in xrange(len(word)+1):
            left_num = str(l) if l else ""
            for right in self.dfs(word[l+1:]):
                cur = left_num+word[l:l+1]+right
                ret.append(cur)

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
    print Solution().minAbbreviation("apple", ["blade"])
