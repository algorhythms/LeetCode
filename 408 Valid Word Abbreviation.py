"""
Premium Question
"""
__author__ = 'Daniel'


class Solution(object):
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
    assert Solution().validWordAbbreviation("internationalization", "i12iz4n") == True
    assert Solution().validWordAbbreviation("apple", "a2e") == False
