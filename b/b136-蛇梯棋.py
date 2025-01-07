# 909. 蛇梯棋


class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        target = n * n

        vis = set()
        layer = [(1, 0)]
        while layer:
            start, step = layer.pop(0)
            for i in range(1, 7):
                idx_nxt = start + i
                if idx_nxt > target:
                    break
                curVal = board[n - 1 - (idx_nxt - 1) // n][
                    (
                        n - 1 - (idx_nxt - 1) % n
                        if ((idx_nxt - 1) // n) % 2 == 0
                        else (idx_nxt - 1) % n
                    )
                ]
                if curVal > 0:
                    idx_nxt = curVal
                if idx_nxt == n * n:  # 到达终点
                    return step + 1
                if idx_nxt not in vis:
                    vis.add(idx_nxt)
                    layer.append((idx_nxt, step + 1))  # 扩展新状态

        return -1

        # def walk(board, start, jump=False):
        #     if start == target:
        #         return 0
        #     if start > target:
        #         return target
        #     if start // n % 2:
        #         col = n - 1 - start % n
        #     else:
        #         col = start % n
        #     row = n - 1 - start // n

        #     res = []
        #     if board[row][col] == -1:
        #         for i in range(1, 7):
        #             res.append(1 + walk(board, start + i, False))
        #     else:
        #         res.append(walk(board, board[row][col], True))
        #     return min(res)

        # return walk(board, 0, False)


board = [
    [-1, 1, 2, -1],
    [2, 13, 15, -1],
    [-1, 10, -1, -1],
    [-1, 6, 2, 8],
]
print(Solution().snakesAndLadders(board))
