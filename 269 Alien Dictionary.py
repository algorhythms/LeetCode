"""
Premium Question
"""
__author__ = 'Daniel'


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        V = {}
        self.construct_graph(words, 0, len(words), 0, V)
        visited = set()
        marked = set()
        ret = []

        for k in V.keys():
            if k not in visited:
                if not self.topological_dfs(V, k, visited, marked, ret):
                    return ""

        return "".join(reversed(ret))

    def construct_graph(self, words, up, down, ptr, V):
        """
        :param words:
        :param up: upper bound
        :param down: lower bound + 1
        :param ptr: starting index for the char in the word
        :param V: Vertices
        :return: None
        """
        i = up
        while i < down:
            if ptr >= len(words[i]):
                i += 1
            else:
                if words[i][ptr] not in V:
                    V[words[i][ptr]] = []

                j = i+1
                while j < down and ptr < len(words[j]) and words[j][ptr] == words[i][ptr]:
                    j += 1

                self.construct_graph(words, i, j, ptr+1, V)
                if j < down and ptr < len(words[j]):
                    V[words[i][ptr]].append(words[j][ptr])

                i = j

    def topological_dfs(self, V, cur, visited, pathset, ret):
        """
        :param V: Vertices HashMap
        :param cur: currently visiting letter
        :param visited: visited letters
        :param pathset: marked predecessor in the path
        :param ret: the path, ordered  topologically
        :return: whether contains cycles 
        """
        if cur in pathset:
            return False

        pathset.add(cur)
        for nei in V[cur]:
            if nei not in visited:
                if not self.topological_dfs(V, nei, visited, pathset, ret):
                    return False

        pathset.remove(cur)
        visited.add(cur)
        ret.append(cur)
        return True


if __name__ == "__main__":
    lst = ["ze", "yf", "xd", "wd", "vd", "ua", "tt", "sz", "rd", "qd", "pz", "op", "nw", "mt", "ln", "ko", "jm", "il",
           "ho", "gk", "fa", "ed", "dg", "ct", "bb", "ba"]
    assert Solution().alienOrder(lst) == "zyxwvutsrqponmlkjihgfedcba"