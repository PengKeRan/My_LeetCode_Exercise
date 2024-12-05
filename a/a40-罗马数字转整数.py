class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == "I":
                if i < n - 1:
                    if s[i + 1] == "V":
                        ans += 4
                        i += 1
                    elif s[i + 1] == "X":
                        ans += 9
                        i += 1
                    else:
                        ans += 1
                else:
                    ans += 1
            elif s[i] == "V":
                ans += 5
            elif s[i] == "X":
                if i < n - 1:
                    if s[i + 1] == "L":
                        ans += 40
                        i += 1
                    elif s[i + 1] == "C":
                        ans += 90
                        i += 1
                    else:
                        ans += 10
                else:
                    ans += 10
            elif s[i] == "L":
                ans += 50
            elif s[i] == "C":
                if i < n - 1:
                    if s[i + 1] == "D":
                        ans += 400
                        i += 1
                    elif s[i + 1] == "M":
                        ans += 900
                        i += 1
                    else:
                        ans += 100
                else:
                    ans += 100
            elif s[i] == "D":
                ans += 500
            elif s[i] == "M":
                ans += 1000
            else:
                continue
            i += 1
        return ans


s = "IV"
print(Solution().romanToInt(s))  # 1994
