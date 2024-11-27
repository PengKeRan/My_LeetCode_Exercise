# 135. 分发糖果
# n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
# 你需要按照以下要求，给这些孩子分发糖果：
# 每个孩子至少分配到 1 个糖果。
# 相邻两个孩子评分更高的孩子会获得更多的糖果。
# 请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        ans = 0
        n = len(ratings)
        left = [0 for _ in range(n)]
        left [0] = 1
        for i in range(n):
            if i > 0 and ratings[i] > ratings[i-1]:
                left[i] += left[i-1] + 1
            else:
                left[i] = 1
        
        right = 0
        for i in reversed(range(n)):
            if i < n-1 and ratings[i] > ratings[i+1]:
                right += 1
            else:
                right = 1
            ans += max(left[i], right)


        return ans

ratings = [1,3,2,2,1]
print(Solution().candy(ratings))




