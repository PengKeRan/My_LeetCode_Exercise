# 452. 用最少数量的箭引爆气球
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        res = 1
        points = sorted(points, key=lambda x: x[0])
        start = points[0][0]
        end = points[0][1]
        for i in range(1, n):
            if points[i][0] <= end:
                start = max(start, points[i][0])
                end = min(end, points[i][1])
            else:
                res += 1
                start = points[i][0]
                end = points[i][1]

        return res


points = [
    [3, 9],
    [7, 12],
    [3, 8],
    [6, 8],
    [9, 10],
    [2, 9],
    [0, 9],
    [3, 9],
    [0, 6],
    [2, 8],
]
sol = Solution()
print(sol.findMinArrowShots(points))
