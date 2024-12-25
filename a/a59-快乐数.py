# 202. 快乐数
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        table = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
        two_digits = [1, 7]
        while True:
            if n < 10:
                if n in two_digits:
                    return True
                else:
                    return False
            temp = 1
            new_n = 0
            while n >= temp:
                new_n += table[(n % (temp * 10)) // temp]
                temp = 10 * temp
            n = new_n


n = 3
sol = Solution()
print(sol.isHappy(n))
