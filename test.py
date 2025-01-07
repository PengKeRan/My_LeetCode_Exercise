# 堆排序
def heap_sort1(nums):

    def swap(nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def upfilter(nums, i, j):
        temp = j
        n = len(nums)
        if 2 * j + 1 <= i and nums[2 * j + 1] < nums[temp]:
            temp = 2 * j + 1
        if 2 * j + 2 <= i and nums[2 * j + 2] < nums[temp]:
            temp = 2 * j + 2
        swap(nums, j, temp)

    n = len(nums)
    for i in reversed(range(n)):
        for j in reversed(range((i - 1) // 2 + 1)):
            upfilter(nums, i, j)
        swap(nums, 0, i)
    return nums


def heap_sort2(nums):
    def swap(nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def downfilter(nums, n, i):
        left = 2 * i + 1
        right = 2 * i + 2
        temp = i
        if left < n and nums[left] < nums[temp]:
            temp = left
        if right < n and nums[right] < nums[temp]:
            temp = right
        if temp != i:
            swap(nums, temp, i)
            downfilter(nums, n, temp)

    n = len(nums)
    for i in reversed(range((n - 1) // 2)):
        downfilter(nums, n, i)

    for i in reversed(range(n - 1)):
        swap(nums, 0, i)
        downfilter(nums, i, 0)

    return nums


import time

nums = [i for i in reversed(range(1000))]

start_time = time.time()  # 开始计时
sorted_nums = heap_sort1(nums)
end_time = time.time()  # 结束计时
print(f"Execution time: {end_time - start_time:.6f} seconds")

nums = [i for i in reversed(range(1000))]

start_time = time.time()  # 开始计时
sorted_nums = heap_sort2(nums)
end_time = time.time()  # 结束计时

print(f"Execution time: {end_time - start_time:.6f} seconds")
