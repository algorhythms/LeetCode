"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying
DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
"""
__author__ = 'Daniel'


class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        Limited space of possible values --> rewrite hash function

        Rolling hash

        "A": 0 (00)
        "C": 1 (01)
        "G": 2 (10)
        "T": 3 (11)

        :type s: str
        :rtype: list[str]
        """
        if len(s) < 10:
            return []

        s = map(self.mapping, list(s))
        h = set()
        # in_ret = set()
        ret = set()
        cur = 0
        for i in xrange(10):
            cur <<= 2
            cur &= 0xFFFFF
            cur += s[i]
        h.add(cur)

        for i in xrange(10, len(s)):
            cur <<= 2
            cur &= 0xFFFFF  # 10 * 2 = 20 position
            cur += s[i]
            if cur in h and cur not in ret:
                ret.add(cur)
            else:
                h.add(cur)

        return map(self.decode, ret)

    def decode(self, s):
        dic = {
            0: "A",
            1: "C",
            2: "G",
            3: "T"
        }
        ret = []
        for i in xrange(10):
            ret.append(dic[s%4])
            s >>= 2

        return "".join(reversed(ret))

    def mapping(self, a):
        dic = {
            "A": 0,
            "C": 1,
            "G": 2,
            "T": 3,
            }

        return dic[a]

if __name__ == "__main__":
    assert Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT") == ['CCCCCAAAAA', 'AAAAACCCCC']
