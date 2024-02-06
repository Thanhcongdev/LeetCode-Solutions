import random
class RandomizedSet:

    def __init__(self):
        self.dict_ = {}
        self.lst = []

    def search(self, val):
        if val not in self.dict_:
            return False
        return True
    def insert(self, val: int) -> bool:
        if self.search(val):
            return False
        self.dict_[val] = len(self.lst)
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not self.search(val):
            return False
        index_x = self.dict_[val]
        self.lst[index_x] = self.lst[-1]
        self.dict_[self.lst[-1]] = index_x
        self.lst.pop()
        del self.dict_[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()