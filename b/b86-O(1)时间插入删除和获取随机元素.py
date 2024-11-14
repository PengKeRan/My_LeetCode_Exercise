import random
class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.arr:
            return False
        else:
            self.map[val]=len(self.arr)
            self.arr.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.arr:
            return False
        idx = self.map[val]
        self.arr[idx] = self.arr[-1]
        self.map[self.arr[-1]] = idx 
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
        

obj = RandomizedSet()
param_1 = obj.insert(val)
param_2 = obj.remove(val)
param_3 = obj.getRandom()