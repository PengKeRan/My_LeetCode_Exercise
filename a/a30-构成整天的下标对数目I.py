# 3184. 构成整天的下标对数目 I
# 给你一个整数数组 hours，表示以 小时 为单位的时间，返回一个整数，表示满足 i < j 且 hours[i] + hours[j] 构成 整天 的下标对 i, j 的数目。

# 整天 定义为时间持续时间是 24 小时的 整数倍 。

# 例如，1 天是 24 小时，2 天是 48 小时，3 天是 72 小时，以此类推。
def countCompleteDayPairs(hours):
    """
    :type hours: List[int]
    :rtype: int
    """
    n = len(hours)
    map = [0] * 24
    res = 0
    for hour in hours:
        map[hour % 24] += 1
    print(map)
    for i in range(24):
        if map[i]:
            if i == 0 or i == 12:
                res += (map[i] * (map[i]-1)) // 2
            else:
                res += map[i] * map[(24-i) % 24]
    return res

print(countCompleteDayPairs([11,11]))