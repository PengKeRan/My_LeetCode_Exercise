import math
from functools import reduce

w = input()
people = input()
people = list(people.split(' '))
for i in range(int(w)):
    people[i] = int(people[i])

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_multiple(numbers):
    return reduce(lambda x, y: lcm(x, y), numbers)

data1 = lcm_multiple(people)

def min_cut(people, data1):
    cut = [0 for _ in range(data1)]
    for p in people:
        times = data1 // p
        for i in range(1, times):
            cut[i * p] = 1
    return sum(cut)


print(min_cut(people, data1))
