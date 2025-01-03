# 399. 除法求值
class Node(object):

    def __init__(self):
        self.fa = -1
        self.children = dict()


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        self.memo = dict()
        for i in range(len(equations)):
            equation = equations[i]
            value = values[i]
            x, y = equation
            if x not in self.memo:
                self.memo[x] = Node()
            if y not in self.memo:
                self.memo[y] = Node()
            if self.memo[x].fa == -1 and self.memo[y].fa == -1:
                self.union(x, y, value)
            elif (
                self.memo[x].fa != -1 and self.memo[y].fa == -1 and self.memo[x].fa != y
            ):
                self.union(
                    self.memo[x].fa,
                    y,
                    value * self.memo[self.memo[x].fa].children[x],
                )
            elif (
                self.memo[x].fa == -1 and self.memo[y].fa != -1 and self.memo[y].fa != x
            ):
                self.union(
                    self.memo[y].fa,
                    x,
                    (1 / value) * self.memo[self.memo[y].fa].children[y],
                )
            elif (
                self.memo[x].fa != -1
                and self.memo[y].fa != -1
                and self.memo[x].fa != self.memo[y].fa
            ):
                self.union(
                    self.memo[x].fa,
                    self.memo[y].fa,
                    value
                    * self.memo[self.memo[x].fa].children[x]
                    * (1 / self.memo[self.memo[y].fa].children[y]),
                )
            else:
                pass

        res = []
        for query in queries:
            x, y = query
            if x not in self.memo or y not in self.memo:
                res.append(-1.0)
                continue
            if self.memo[y].fa == x:
                res.append(self.memo[x].children[y])
            elif self.memo[x].fa == y:
                res.append(1.0 / self.memo[y].children[x])
            elif x == y:
                res.append(1.0)
            elif self.memo[y].fa == self.memo[x].fa and self.memo[x].fa != -1:
                res.append(
                    self.memo[self.memo[y].fa].children[y]
                    / self.memo[self.memo[y].fa].children[x]
                )
            else:
                res.append(-1.0)
        return res

    def union(self, x, y, weight):
        print(x, y)
        self.memo[y].fa = x
        self.memo[x].children[y] = weight
        for child in self.memo[y].children.keys():
            self.memo[child].fa = x
            self.memo[x].children[child] = weight * self.memo[y].children[child]
        self.memo[y].children = dict()


equations = [["a", "b"], ["b", "c"], ["a", "e"], ["e", "c"]]
values = [2.0, 2.0, 1.0, 4.0]
queries = [["a", "c"]]
print(Solution().calcEquation(equations, values, queries))
# [1.33333,1.0,-1.0]
