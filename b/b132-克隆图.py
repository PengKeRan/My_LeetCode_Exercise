# 133. 克隆图
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None
        self.memo = {}
        self.adjList = {}

        self.dfs(node)

        for rootVal in self.adjList.keys():
            self.memo[rootVal].neighbors
            for childVal in self.adjList[rootVal]:
                self.memo[rootVal].neighbors.append(self.memo[childVal])
        return self.memo[node.val]

    def dfs(self, node):
        if node is None or node.val in self.memo.keys():
            return
        self.memo[node.val] = Node(val=node.val)
        self.adjList[node.val] = []
        for neighbor in node.neighbors:
            self.adjList[node.val].append(neighbor.val)
            self.dfs(neighbor)
