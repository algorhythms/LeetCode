from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        hm = defaultdict(int)
        A = 0
        B = 0
        for c in secret:
            hm[c] += 1

        for i, v in enumerate(guess):
            if v == secret[i]:
                A += 1
                hm[v] -= 1
                if hm[v] < 0:
                    assert hm[v] == -1
                    B -= 1
                    hm[v] = 0

            elif v in hm and hm[v] > 0:
                B += 1
                hm[v] -= 1

        return "%dA%dB" % (A, B)


if __name__ == "__main__":
    print Solution().getHint("0", "1")
