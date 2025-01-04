# 207. 课程表
class Node(object):
    def __init__(self, val):
        self.val = val
        self.ind = 0
        self.children = []


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        memo = {}
        if prerequisites == []:
            return True
        for i in range(numCourses):
            memo[i] = Node(i)
        for x, y in prerequisites:
            memo[y].ind += 1
            memo[x].children.append(memo[y])

        queue = [course for course in memo if memo[course].ind == 0]
        walked = 0
        while queue:
            cur = queue.pop(0)
            walked += 1
            for child in memo[cur].children:
                child.ind -= 1
                if child.ind == 0:
                    queue.append(child.val)
        return walked == numCourses


numCourses = 5
prerequisites = [[1, 0]]
print(Solution().canFinish(numCourses, prerequisites))
