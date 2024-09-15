"""
剑指 Offer II 106. 二分图
785. 判断二分图
存在一个 无向图 ，图中有 n 个节点。其中每个节点都有一个介于 0 到 n - 1 之间的唯一编号。
给你一个二维数组 graph ，其中 graph[u] 是一个节点数组，由节点 u 的邻接节点组成。
形式上，对于graph[u] 中的每个 v ，都存在一条位于节点 u 和节点 v 之间的无向边。
该无向图同时具有以下属性：
不存在自环（graph[u] 不包含 u）。
不存在平行边（graph[u] 不包含重复值）。
如果 v 在 graph[u] 内，那么 u 也应该在 graph[v] 内（该图是无向图）
这个图可能不是连通图，也就是说两个节点 u 和 v 之间可能不存在一条连通彼此的路径。
二分图 定义：如果能将一个图的节点集合分割成两个独立的子集 A 和 B ，并使图中的每一条边的两个节点一个来自 A 集合，一个来自 B 集合，就将这个图称为 二分图 。
如果图是二分图，返回 true ；否则，返回 false 。
"""


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        UNCOLOR, RED, GREEN = 0, 1, 2
        color = [UNCOLOR] * len(graph)
        valid = True

        def dfs(node, c):
            nonlocal valid
            color[node] = c
            next_color = RED if c == GREEN else GREEN
            for next_node in graph[node]:
                if color[next_node] == UNCOLOR:
                    dfs(next_node, next_color)
                    if valid is False:
                        return False
                elif color[next_node] != next_color:
                    valid = False
                    return

        for i in range(len(graph)):
            if color[i] == UNCOLOR:
                dfs(i, RED)
            if valid is False:
                return False
        return True


graph1 = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
graph2 = [[1, 3], [0, 2], [1, 3], [0, 2]]
sol = Solution()
print(sol.isBipartite(graph1))  # false
print(sol.isBipartite(graph2))  # true
