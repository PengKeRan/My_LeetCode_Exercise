# 134. 加油站
# 在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。
# 你从其中的一个加油站出发，开始时油箱为空。
# 给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。
# 如果存在解，则 保证 它是 唯一 的。

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        gas = [gas[i]-cost[i] for i in range(n)]
        
        res = -1
        i = 0
        while i < n:
            tank = 0
            cnt = 0
            j = 0
            while cnt < n:
                j = (i + cnt) % n
                tank += gas[j]
                if tank < 0:
                    break
                cnt += 1
            if cnt == n:
                return
            if j < i:
                break
            i = j + 1
        return res


        

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
sol = Solution()
print(sol.canCompleteCircuit(gas, cost))
