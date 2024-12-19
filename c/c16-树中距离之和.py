"""
834. 树中距离之和
给定一个无向、连通的树。树中有 n 个标记为 0...n-1 的节点以及 n-1条边。
给定整数 n 和数组edges，edges[i] = [ai, bi]表示树中的节点ai和bi之间有一条边。
返回长度为 n 的数组answer，其中answer[i]是树中第 i 个节点与所有其他节点之间的距离之和。
"""


class Solution(object):
    def getTreeNodesNum(self, root):
        if self.treeNodesNum[root] != 0:
            return self.treeNodesNum[root]
        res = 1
        for son in self.sons[root]:
            res += self.getTreeNodesNum(son)
        self.treeNodesNum[root] = res
        return self.treeNodesNum[root]

    def getSonsPathSum(self, root):
        if self.sonsPathSum[root] != 0:
            return self.self.sonsPathSum[root]
        res = 0
        for son in self.sons[root]:
            res += self.getSonsPathSum(son)
            res += self.getTreeNodesNum(son)
        self.sonsPathSum[root] = res
        return self.sonsPathSum[root]

    def reroot(self, root, fa):

        for son in self.edges[root]:
            if son != fa:
                self.ans[son] = self.ans[root] + self.n - 2 * self.getTreeNodesNum(son)
                self.reroot(son, root)

    def sumOfDistancesInTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.n = n
        self.edges = [[] for _ in range(n)]
        for [i, j] in edges:
            self.edges[i].append(j)
            self.edges[j].append(i)

        self.sons = [[] for _ in range(n)]
        self.father = [None for _ in range(n)]
        self.father[0] = -1

        stack = [0]
        while stack:
            fa = stack.pop()
            for son in self.edges[fa]:
                if self.father[son] is None:
                    self.father[son] = fa
                    self.sons[fa].append(son)
                    stack.append(son)

        self.sonsPathSum = [0 for _ in range(n)]
        self.treeNodesNum = [0 for _ in range(n)]
        self.ans = [0 for _ in range(n)]
        self.ans[0] = self.getSonsPathSum(0)

        self.reroot(0, -1)
        return self.ans


n = 6
edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
# edges = [[1, 2], [1, 4], [5, 0], [3, 0], [3, 4]]
sol = Solution()
print(sol.sumOfDistancesInTree(n, edges))  # false
