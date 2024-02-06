class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.dict_ = {}

    def search(self, val):
        return val in self.dict_

    def insert(self, val):
        if self.search(val):
            return False
        self.dict_[val] = len(self.lst) 
        self.lst.append(val)
        return True

    def remove(self, val):
        if not self.search(val):
            return False

        id_x = self.dict_[val]
        self.lst[id_x] = self.lst[-1]
        self.dict_[self.lst[-1]] = id_x
        self.lst.pop()
        del self.dict_[val]
        return True

    def getRandom(self):
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()