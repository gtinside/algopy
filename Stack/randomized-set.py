import random
class RandomizedSet:

    def __init__(self):
        self.myDict = dict()
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.myDict:
            return False
        
        self.myDict[val] =  len(self.arr)
        self.arr.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.myDict:
            return False
        
        index = self.myDict[val]
        last_element =  self.arr[-1]

        self.arr[index] = last_element
        self.myDict[last_element] = index
        self.arr.pop()
        self.myDict.pop(val)

        return True

    def getRandom(self) -> int:
        r = random.randint(0, len(self.arr) - 1)
        return self.arr[r]



sol = RandomizedSet()
sol.insert(1)
sol.insert(2)
print(sol.getRandom())

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()