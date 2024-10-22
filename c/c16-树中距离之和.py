"""
834. 树中距离之和
给定一个无向、连通的树。树中有 n 个标记为 0...n-1 的节点以及 n-1条边。
给定整数 n 和数组edges，edges[i] = [ai, bi]表示树中的节点ai和bi之间有一条边。
返回长度为 n 的数组answer，其中answer[i]是树中第 i 个节点与所有其他节点之间的距离之和。
"""


class Solution(object):
    def sonPathSum(self, root):
        if len(self.sons[root]) == 0:
            return 0
        res = 0
        for son in self.sons[root]:
            res += self.sonPathSum(son)
            res += self.numOfSonNodes(son)
        return res
    
    def numOfSonNodes(self, root):
        if self.sonsNum[root] != 0:
            return self.sonsNum[root]
        res = 1
        for son in self.sons[root]:
            res += self.numOfSonNodes(son)
        self.sonsNum[root] = res
        return res

    def sumOfDistancesInTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        edge = [[] for _ in range(n)]
        for i,j in edges:
            edge[i].append(j)
            edge[j].append(i)

        sons = [[] for _ in range(n)]
        farthers = [None]*n

        stack = [0]
        while stack:
            node = stack.pop()
            for e in edge[node]:
                if e != 0 and farthers[e] == None :
                    farthers[e] = node
                    sons[node].append(e)
                    stack.append(e)

        self.sons = sons
        self.sonsNum = [0] * n
        self.ans = [0] * n

        self.ans[0] = self.sonPathSum(0)
        self.sonsNum[0] = self.numOfSonNodes(0)

        def reroot(root, fa):
            for son in self.sons[root]:
                if son != fa:
                    self.ans[son] = self.ans[root] + n - self.sonsNum[son] * 2
                    reroot(son, fa)
        reroot(0, -1)
        return self.ans


n = 6
edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
# edges = [[1, 2], [1, 4], [5, 0], [3, 0], [3, 4]]
sol = Solution()
print(sol.sumOfDistancesInTree(n, edges))  # false
