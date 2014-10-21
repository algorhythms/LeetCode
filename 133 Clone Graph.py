"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
"""
__author__ = 'Danyang'
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
    def __repr__(self):
        return repr(self.label)

class Solution:
    def cloneGraph_TLE(self, node):
        """
        dfs
        :param node: UndirectedGraphNode
        :return: UndirectedGraphNode
        """
        return self.clone_graph_visited(node, set())

    def clone_graph_visited(self, node, visited_set):
        """
        post-order traversal
        Time Limit Exceeded
        :param node:
        :param visited_set:
        :return:
        """
        if not node:
            return
        visited_set.add(node)
        neighbors_cloned = [self.clone_graph_visited(neighbor, set(visited_set)) for neighbor in node.neighbors if neighbor not in visited_set]
        node_cloned = UndirectedGraphNode(node.label)
        for neighbor_cloned in neighbors_cloned:
            if neighbor_cloned not in visited_set:
                neighbor_cloned.neighbors.append(node_cloned)
        node_cloned.neighbors = neighbors_cloned
        return node_cloned

    def cloneGraph(self, node):
        """
        bfs with visited
        similar to 138 Copy List with Random Pointer

        copy_map: dict, 1. book keeping whether it is coped (visited); 2. reserve for being copied as neighbor, # shadow
        q: list, queue of nodes whose the neighbors are to be copied

        :param node: UndirectedGraphNode
        :return: UndirectedGraphNode
        """
        if not node:
            return

        original2copy = {} # dict  #!important
        q = [node]  # queue of nodes whose the neighbors are to be copied

        clone = UndirectedGraphNode(node.label)
        original2copy[node] = clone
        while q:
            cur = q.pop()
            for neighbor in cur.neighbors:
                if neighbor in original2copy:  # already copied
                    original2copy[cur].neighbors.append(original2copy[neighbor])
                else:
                    q.append(neighbor)
                    clone_neighbor = UndirectedGraphNode(neighbor.label)
                    original2copy[neighbor] = clone_neighbor
                    original2copy[cur].neighbors.append(original2copy[neighbor])

        return original2copy[node]


if __name__=="__main__":
    lst = [UndirectedGraphNode(i+1) for i in range(3)]
    for item in lst:
        item.neighbors = list(lst)
        item.neighbors.remove(item)
    cloned = Solution().cloneGraph(lst[0])
    assert cloned.neighbors[0].label in (2, 3)
    assert cloned.neighbors[1].label in (2, 3)


