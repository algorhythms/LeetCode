"""
Premium Question
"""
__author__ = 'Daniel'


class Solution(object):
    def __init__(self):
        self.map1 = ["11", "69", "88", "96", "00"]

    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        self.build(n, [], ret)
        return ret

    def build(self, n, cur, ret):
        if n%2 == 1 and len(cur) == 0:
            for i in ["0", "1", "8"]:
                cur.append(i)
                self.build(n, cur, ret)
                cur.pop()
            return

        if len(cur)/2 == n/2:
            ret.append("".join(cur))
            return

        for elt in self.map1:
            if elt != "00" or len(cur) != n-2:
                cur.insert(0, elt[0])
                cur.append(elt[1])
                self.build(n, cur, ret)
                cur.pop()
                cur.pop(0)


class SolutionOutputLimitExceeded(object):
    def __init__(self):
        self.map = {
            "1": "1",
            "6": "9",
            "9": "6",
            "8": "8",
            "0": "0"
        }
        self.middle = ["1", "8", "0"]

    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        self.build(0, n, [], ret)
        return ret

    def build(self, idx, n, cur, ret):
        if idx == n/2:
            if n % 2 != 0:
                for m in self.middle:
                    if m != "0" or idx != 0:
                        temp = list(cur)
                        temp.append(m)
                        for i in xrange(idx-1, -1, -1):
                            temp.append(self.map[temp[i]])
                        ret.append("".join(temp))
            else:
                temp = list(cur)
                for i in xrange(idx-1, -1, -1):
                    temp.append(self.map[temp[i]])
                    ret.append("".join(temp))

            return

        for k in self.map.keys():
            if k != "0" or idx != 0:
                cur.append(k)
                self.build(idx+1, n, cur, ret)
                cur.pop()

if __name__ == "__main__":
    print Solution().findStrobogrammatic(1)