class AllOne:

    def __init__(self):
        self.counter = dict()

    def inc(self, key: str) -> None:
        if key in self.counter:
            self.counter[key] += 1
        else:
            self.counter[key] = 1

    def dec(self, key: str) -> None:
        self.counter[key] -= 1
        if self.counter[key] == 0:
            del self.counter[key]
        

    def getMaxKey(self) -> str:
        if not self.counter:
            return ""
        max_key_val = max(self.counter.values())
        for key, val in self.counter.items():
            if val == max_key_val:
                return key
        

    def getMinKey(self) -> str:
        if not self.counter:
            return ""
        min_key_val = min(self.counter.values())
        for key, val in self.counter.items():
            if val == min_key_val:
                return key
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()