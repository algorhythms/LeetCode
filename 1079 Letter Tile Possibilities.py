"""
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1
 

Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""
import math
from collections import defaultdict


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        brute force backtracking + combinatorics
        """
        cnt = 0
        ret = set()
        self.backtrack(tiles, 0, [], ret)
        for s in ret:
            if s == "":
                continue 
            cur = math.factorial(len(s))
            counter = defaultdict(int)
            for c in s:
                counter[c] += 1
            for v in counter.values():
                cur //= math.factorial(v)
            cnt += cur
        
        return cnt

    def backtrack(self, tiles, i, cur, ret):
        if i == len(tiles):
            ret.add("".join(sorted(cur)))
            return 
        
        self.backtrack(tiles, i+1, cur, ret)

        cur.append(tiles[i])
        self.backtrack(tiles, i+1, cur, ret)
        cur.pop()


class SolutionBruteForce:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        DFS 
        all tile are interconnected as neighbors
        """
        visited = [False for _ in tiles]
        ret = set()
        self.dfs(tiles, visited, [], ret)
        return len(ret) - 1  # exclude ""

    def dfs(self, tiles, visited, cur, ret):
        ret.add("".join(cur))

        for i, v in enumerate(tiles):
            if not visited[i]:
                visited[i] = True
                cur.append(v)
                self.dfs(tiles, visited, cur, ret)
                cur.pop()
                visited[i] = False