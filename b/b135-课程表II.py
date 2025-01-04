# 210. 课程表 II
class Node(object):
    def __init__(self, val):
        self.val = val
        self.ind = 0
        self.children = []


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        memo = {}
        if prerequisites == []:
            return [i for i in range(numCourses)]
        for i in range(numCourses):
            memo[i] = Node(i)
        for y, x in prerequisites:
            memo[y].ind += 1
            memo[x].children.append(memo[y])

        res = []
        walked = 0
        queue = [course for course in memo if memo[course].ind == 0]
        while queue:
            cur = queue.pop(0)
            res.append(cur)
            walked += 1
            for child in memo[cur].children:
                child.ind -= 1
                if child.ind == 0:
                    queue.append(child.val)
        return res if walked == numCourses else []
