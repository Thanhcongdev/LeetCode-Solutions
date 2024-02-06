import random
class RandomizedSet:

    def __init__(self):
        self.dict_ = defaultdict(int)

    def search(self, val):
        if val not in self.dict_:
            return False
        return True
    def insert(self, val: int) -> bool:
        if self.search(val):
            return False
        self.dict_[val] += 1
        return True

    def remove(self, val: int) -> bool:
        if not self.search(val):
            return False
        x = self.dict_[val]
        if x == 1:
            del self.dict_[val]
        else:
            self.dict_val -= 1
        return True

    def getRandom(self) -> int:
        return random.choice(list(self.dict_.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()