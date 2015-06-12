"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as
a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to
finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses,
return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order
is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1
and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering
is[0,2,1,3].

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph
is represented.
"""
__author__ = 'Daniel'


class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        Graph -> Start from V with no predecessor (pi) -> Topological Sorting
        :type numCourses: int
        :type prerequisites: list[list[int]]
        :rtype: list[int]
        """
        V = {}
        for i in xrange(numCourses):
            V[i] = []

        for edge in prerequisites:
            V[edge[1]].append(edge[0])

        return self.topological_sort(V)

    def topological_sort(self, V):
        visited = set()
        marked = set()
        ret = []

        for k in V.keys():
            if k not in visited:
                if not self.dfs(V, k, visited, marked, ret):
                    return []

        ret.reverse()
        return ret

    def dfs(self, V, k, visited, marked, ret):
        """
        dfs construct the ret while at the same time check acyclic

        :return: whether it is acyclic
        """
        if k in marked:
            return False

        marked.add(k)
        for neighbor in V[k]:
            if neighbor not in visited:
                if not self.dfs(V, neighbor, visited, marked, ret):
                    return False

        marked.remove(k)
        visited.add(k)
        ret.append(k)
        return True


if __name__ == "__main__":
    assert Solution().findOrder(2, [[0, 1], [1, 0]]) == []