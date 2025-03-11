"""
You are playing a game that contains multiple characters, and each of the characters has two main properties: attack and defense. You are given a 2D integer array properties where properties[i] = [attacki, defensei] represents the properties of the ith character in the game.

A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. More formally, a character i is said to be weak if there exists another character j where attackj > attacki and defensej > defensei.

Return the number of weak characters.

 

Example 1:

Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the other.
Example 2:

Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a strictly greater attack and defense.
Example 3:

Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has a strictly greater attack and defense.
 

Constraints:

2 <= properties.length <= 10^5
properties[i].length == 2
1 <= attacki, defensei <= 10^5
"""
class Solution:
    def numberOfWeakCharacters(self, A: List[List[int]]) -> int:
        """
        If it is 1D, it is just to find the local min, not global (\exists vs. \forall)
        If it is 1D, just find the max, anything under max is weak 

        Reduce 2D to 1D? 
        Points on the pareto effiency curve, anything below is weak 
        Sort by x-axis, then check y-axis?
        Keep a stack of monotonically decreasing y-axis 
        """
        stk = []  # y monotonically decreasing 
        A.sort(key=lambda x: (x[0], -x[1]))  # sort x asc and then y desc
        ret = 0
        for i, v in enumerate(A):
            x, y = v
            while stk and A[stk[-1]][0] < x and A[stk[-1]][1] < y:
                stk.pop()
                ret += 1
            stk.append(i)

        return ret