class Solution(object):
    def productExceptSelf(self, nums):
        # n = len(nums)
        # pre = [1 for _ in range(n)]
        # suf = [1 for _ in range(n)]

        # for i in range(1,n):
        #     pre[i] = pre[i-1] * nums[i-1]
        
        # for i in range(n-2,-1,-1):
        #     suf[i] = suf[i+1] * nums[i+1]
        
        # res = [pre[i]*suf[i] for i in range(n)]
        # return res

        n = len(nums)
        res = [1 for _ in range(n)]
        for i in range(1,n):
            res[i] = res[i-1] * nums[i-1]
        r = 1
        for i in reversed(range(n)):
            res[i] *= r
            r *= nums[i]
        return res


nums = [1,2,3,4]
sol = Solution()
print(sol.productExceptSelf(nums))