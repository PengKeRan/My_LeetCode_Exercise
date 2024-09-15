"""
406.根据身高重建队列
假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。
每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面 正好 有 ki 个身高大于或等于 hi 的人。
请你重新构造并返回输入数组people 所表示的队列。
返回的队列应该格式化为数组 queue ，其中 queue[j] = [hj, kj] 是队列中第 j 个人的属性（queue[0] 是排在队列前面的人）。
"""


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        arr = sorted(people, key=lambda x: x[0] * 100 - x[1], reverse=True)
        res = []
        for guy in arr:
            if len(res)<guy[1]:
                res.append(guy)
            else:
                res.insert(guy[1], guy)
        return res


sol = Solution()
people1 = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
people2 = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
print(sol.reconstructQueue(people1))
print(sol.reconstructQueue(people2))
