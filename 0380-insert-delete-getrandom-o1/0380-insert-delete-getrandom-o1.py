class RandomizedSet:

    def __init__(self):
        self.myset = set()
        

    def insert(self, val: int) -> bool:
        if val not in self.myset:
            self.myset.add(val)
            return True
        else:
            return False
        
    def remove(self, val: int) -> bool:
        if val in self.myset:
            self.myset.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return list(self.myset)[random.randint(0, len(self.myset)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()