"""
2477. 到达首都的最少油耗
给你一棵 n个节点的树（一个无向、连通、无环图），每个节点表示一个城市，编号从0到n - 1，且恰好有n - 1条路。0是首都。
给你一个二维整数数组roads，其中roads[i] = [ai, bi]，表示城市ai 和bi之间有一条双向路。
每个城市里有一个代表，他们都要去首都参加一个会议。
每座城市里有一辆车。给你一个整数seats表示每辆车里面座位的数目。
城市里的代表可以选择乘坐所在城市的车，或者乘坐其他城市的车。相邻城市之间一辆车的油耗是一升汽油。
请你返回到达首都最少需要多少升汽油。
"""


class Solution(object):
    def minimumFuelCost(self, roads, seats):
        """
        :type roads: List[List[int]]
        :type seats: int
        :rtype: int
        """
        if len(roads) == 0:
            return 0
        g = [[] for _ in range(len(roads) + 1)]
        for road in roads:
            g[road[0]].append(road[1])
            g[road[1]].append(road[0])
        ans = 0

        def dfs(node, father_node):
            car_num = 1
            for y in g[node]:
                if y != father_node:
                    car_num += dfs(y, node)
            if node != 0:
                nonlocal ans
                ans += (car_num + seats - 1) // seats
            return car_num

        dfs(0, -1)
        return ans


roads1 = [[0, 1], [0, 2], [0, 3]]
seats1 = 5
roads2 = [[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]]
seats2 = 2
roads3 = []
seats3 = 1
sol = Solution()
print(sol.minimumFuelCost(roads1, seats1))  # 3
# print(sol.minimumFuelCost(roads2, seats2))  # 7
# print(sol.minimumFuelCost(roads3, seats3))  # 0
