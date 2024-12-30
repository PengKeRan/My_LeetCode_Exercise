# 71. 简化路径
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # path = "/" + "/".join([x for x in path.split("/") if x != ""])
        stack = []
        n = len(path)
        path = path.split("/")
        for x in path:
            if x == "..":
                if stack:
                    stack.pop()
            elif not x or x == ".":
                continue
            else:
                stack.append(x)
        return "/" + "/".join(stack)


sol = Solution()
path = "/.../a/../b/c/../d/./"
print(sol.simplifyPath(path))
