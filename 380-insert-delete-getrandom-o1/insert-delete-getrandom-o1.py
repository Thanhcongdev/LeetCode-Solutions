import random
class RandomizedSet:

    def __init__(self):
        self.dict_ = defaultdict(int)
        self.lst = []

    def search(self, val):
        if self.dict_[val] == 0:
            return False
        return True
    def insert(self, val: int) -> bool:
        if self.search(val):
            return False
        self.lst.append(val)
        self.dict_[val] += 1
        return True

    def remove(self, val: int) -> bool:
        self.dict_[val] += 0
        if not self.search(val):
            return False
        self.dict_[val] -= 1
        self.lst.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()