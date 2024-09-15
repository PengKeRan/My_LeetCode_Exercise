"""
834. 树中距离之和
给定一个无向、连通的树。树中有 n 个标记为 0...n-1 的节点以及 n-1条边。
给定整数 n 和数组edges，edges[i] = [ai, bi]表示树中的节点ai和bi之间有一条边。
返回长度为 n 的数组answer，其中answer[i]是树中第 i 个节点与所有其他节点之间的距离之和。
"""


class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # graph = [[] for i in range(n)]
        # for x, y in edges:
        #     graph[x].append(y)
        #     graph[y].append(x)

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
        print(edge)
        print(sons)
        print(farthers)
        # dist_arr = [n for i in range(n)]
        # dist_arr[0] = 0
        # T = 0
        # print(dist_arr)
        #
        # def get_height(root, fa):
        #     if T in graph[root]:
        #         dist_arr[root] = 1
        #     for node in range(n):
        #         dist_arr[node] = min(dist_arr[node], dist_arr[fa] + 1)
        #
        # print(get_height(0, -1))
        # # 计算两结点间的路数
        # # def get_height(fa, start, end):
        # #     print(f"fa:{fa},start:{start},end:{end}")
        # #     if start == end:
        # #         # print('here1')
        # #         return 0
        # #     if end in graph[start]:
        # #         # print('找到了')
        # #         return 1
        # #     if len(graph[start]) == 1:
        # #         # print('here3')
        # #         return 0
        # #     h = 0
        # #     for son in graph[start]:
        # #         if son == fa:
        # #             continue
        # #         else:
        # #             h += (get_height(start, son, end) + 1)
        # #         # print(f"h:{h}")
        # #
        # #     return h
        # #
        # # print(get_height(4, 1, 5))
        # # print(get_height(1, 2, 5))
        #
        # # res = 0
        # # arr = []
        # # for i in range(n):
        # #     for j in range(n):
        # #         res += get_height(i, j, -1)
        # #     arr.append(res)
        # #     res = 0
        # # return arr


n = 6
# edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
edges = [[1, 2], [1, 4], [5, 0], [3, 0], [3, 4]]
sol = Solution()
print(sol.sumOfDistancesInTree(n, edges))  # false
