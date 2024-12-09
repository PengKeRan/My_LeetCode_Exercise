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