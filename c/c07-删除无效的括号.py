# 301. 删除无效的括号
# 给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。
#
# 返回所有可能的结果。答案可以按 任意顺序 返回。


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []

        def isValid(s):
            cnt = 0
            for i in range(len(s)):
                if cnt < 0:
                    return False
                if s[i] == "(":
                    cnt += 1
                elif s[i] == ")":
                    cnt -= 1
                else:
                    continue
            return cnt == 0

        def min_remove(s):
            leftInvalid = 0
            rightInvalid = 0
            for i in range(len(s)):
                if s[i] == "(":
                    leftInvalid += 1
                elif s[i] == ")":
                    if leftInvalid == 0:
                        rightInvalid += 1
                    else:
                        leftInvalid -= 1
                else:
                    continue
            return leftInvalid, rightInvalid

        def helper(s, start, left, right):
            if left == 0 and right == 0:
                if isValid(s):
                    ans.append(s)
                return
            for i in range(start, len(s)):
                if i > start and s[i - 1] == s[i]:
                    continue
                if left + right > len(s) - i:
                    return
                if left > 0 and s[i] == "(":
                    helper(s[:i] + s[i + 1:], i, left - 1, right)
                if right > 0 and s[i] == ")":
                    helper(s[:i] + s[i + 1:], i, left, right - 1)

        # 回溯 + 剪枝
        leftInvalid, rightInvalid = min_remove(s)
        helper(s, 0, leftInvalid, rightInvalid)

        return ans
        # 广度优先
        # queue = set([s])
        # while True:
        #     print(queue)
        #     for ss in queue:
        #         if isValid(ss):
        #             ans.append(ss)
        #     if ans:
        #         return ans
        #     next_queue = set()
        #     for ss in queue:
        #         for i in range(len(ss)):
        #             if i > 0 and ss[i] == ss[i - 1]:
        #                 continue
        #             if ss[i] == "(" or ss[i] == ")":
        #                 next_queue.add(ss[:i] + ss[i + 1:])
        #     queue = next_queue

sol = Solution()
s = "()())()"
print(sol.removeInvalidParentheses(s))
