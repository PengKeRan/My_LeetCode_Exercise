import time


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


def quickSort(nums):
    n = len(nums)

    def sort(nums, left, right):
        if left >= right:
            return
        base = nums[left]
        i, j = left, right
        while i < j:
            while i < j and nums[j] >= base:
                j -= 1
            while i < j and nums[i] <= base:
                i += 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[j] = nums[j], nums[left]

        sort(nums, left, i - 1)
        sort(nums, i + 1, right)

    sort(nums, 0, n - 1)
    return nums


# nums = [i for i in reversed(range(500))]
# start_time = time.time()  # 开始计时
# sorted_nums = quickSort(nums)
# end_time = time.time()  # 结束计时
# print(f"Execution time: {end_time - start_time:.6f} seconds")
layer = [[2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1]]
print([x[0] for x in layer])
