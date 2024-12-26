# 56. 合并区间
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # if len(intervals) == 1:
        #     return intervals
        # intervals = sorted(intervals, key=lambda x: x[0])
        # i = 0
        # while i + 1 < len(intervals):
        #     if intervals[i][1] >= intervals[i + 1][0]:
        #         temp = [intervals[i][0], max(intervals[i][1], intervals[i + 1][1])]
        #         intervals.remove(intervals[i + 1])
        #         intervals.remove(intervals[i])
        #         intervals.insert(i, temp)
        #     else:
        #         i += 1

        # return intervals
        n = len(intervals)
        if n == 1:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(n - 1):
            if end < intervals[i + 1][0]:
                res.append([start, end])
                start = intervals[i + 1][0]
                end = intervals[i + 1][1]
            else:
                end = max(end, intervals[i + 1][1])
        res.append([start, end])
        return res


intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
sol = Solution()
print(sol.merge(intervals))
