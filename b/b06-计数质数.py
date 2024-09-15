"""
204. 计数质数
给定整数n，返回所有小于非负整数n的质数的数量。
"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        if n == 3:
            return 1
        count = [1 for i in range(n)]
        count[0] = 0
        count[1] = 0
        for num in range(2, int(n ** 0.5) + 2):
            # print(num,int(n ** 0.5) + 1)
            if count[num]:
                count[num * num:n:num] = [0] * len(count[num * num:n:num])
                # for j in range(num*num,n,num):
                #     count[j]=0
        return sum(count)
        # 枚举
        # count = 0
        # primes = [2]
        # flag = False
        # if n == 0 or n == 1 or n == 2:
        #     return 0
        # if n == 3:
        #     return 1
        # for i in range(3, n):
        #     for el in primes:
        #         if el > i**0.5:
        #             flag = True
        #             break
        #         if i % el == 0:
        #             flag = False
        #             break
        #         flag = True
        #     if flag:
        #         primes.append(i)
        #         count += 1
        #         flag = False
        # count += 1
        # return count


sol = Solution()
print(sol.countPrimes(10))
