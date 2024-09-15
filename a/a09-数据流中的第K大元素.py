"""
703. 数据流中的第 K 大元素
设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。
请实现 KthLargest类：
KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。
"""


class KthLargest:
    def __init__(self, k: int, nums):
        self.nums = nums
        self.k = k
        self.nums.sort(reverse = True)
        while len(self.nums) > k:
            self.nums.pop()

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse = True)
        if len(self.nums) > self.k:
            self.nums.pop()
        return self.nums[-1]


# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(2, [0])
print(obj.add(-1))
print(obj.add(1))
print(obj.add(-2))
# print(obj.add(9))
# print(obj.add(4))
