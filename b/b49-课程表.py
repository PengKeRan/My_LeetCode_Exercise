# 207. 课程表
# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
#
# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
#
# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # DFS
        def dfs(cur, flag, adjacency):
            if flag[cur] == 1:
                return False
            if flag[cur] == -1:
                return True
            flag[cur] = 1
            for adj in adjacency[cur]:
                if dfs(adj, flag, adjacency) is False:
                    return False
            flag[cur] = -1
            return True

        adjacency = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        print(adjacency)
        for i in range(numCourses):
            flag = [0 for _ in range(numCourses)]
            if dfs(i, flag, adjacency) is False:
                return False
        return True

        # indegree = [0 for _ in range(numCourses)]
        # adjacency = [[] for _ in range(numCourses)]
        # queue = []
        # for cur, pre in prerequisites:
        #     indegree[cur] += 1
        #     adjacency[pre].append(cur)
        # for i in range(numCourses):
        #     if indegree[i] == 0:
        #         queue.append(i)
        # while queue:
        #     pre = queue.pop()
        #     for cur in adjacency[pre]:
        #         indegree[cur] -= 1
        #         if indegree[cur] == 0:
        #             queue.append(cur)
        # return not sum(indegree)

        # e_groups = []
        # v_sets = []
        # for pre in prerequisites:
        #     merge_list = []
        #     for i in range(len(v_sets)):
        #         if pre[0] in v_sets[i] or pre[1] in v_sets[i]:
        #             merge_list.append(i)
        #
        #     # merge
        #     for j in range(1, len(merge_list)):
        #         v_sets[merge_list[0]].update(v_sets[merge_list[j]])
        #         del v_sets[merge_list[j]]
        #
        #     for j in range(1, len(merge_list)):
        #         e_groups[merge_list[1]] += e_groups[merge_list[j]]
        #         del e_groups[merge_list[j]]
        #
        #     if len(merge_list) != 0:
        #         v_sets[merge_list[0]].update({pre[0],pre[1]})
        #         e_groups[merge_list[0]].append(pre)
        #
        #     if len(merge_list) == 0:
        #         e_groups.append([pre])
        #         v_sets.append({pre[0], pre[1]})
        #
        # for i in range(len(e_groups)):
        #     if len(e_groups[i]) > len(v_sets[i]) - 1:
        #         return False
        # return True


sol = Solution()
numCourses = 8
prerequisites = [[1, 0], [2, 6], [1, 7], [5, 1], [6, 4], [7, 0], [0, 5]]
print(sol.canFinish(numCourses, prerequisites))
