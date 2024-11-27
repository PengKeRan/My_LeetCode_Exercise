# 85
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        matrix2 = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if n==0:
                    if matrix[i][j] == "1":
                        matrix2[i][j] = 1
                else:
                    if matrix[i][j] == "1":
                        matrix2[i][j] += matrix2[i][j-1] + 1

        ans = 0
        for col in range(n):
            nums = [row[col] for row in matrix2]
            leftSmall = [-1 for _ in range(m)]
            rightSmall = [m for _ in range(m)]
            s = []
            for i in range(m):
                while s and nums[s[-1]] >= nums[i]:
                    rightSmall[s[-1]] = i
                    s.pop()
                if s:
                    leftSmall[i] = s[-1]
                else:
                    leftSmall[i] = -1
                s.append(i)
            
            for i in range(m):
                ans = max(ans, (rightSmall[i]-leftSmall[i] - 1) * nums[i])
        return ans        


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(Solution().maximalRectangle(matrix))