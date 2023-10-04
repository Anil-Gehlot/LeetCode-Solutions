class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.kSize = 10000
        self.lists = [[] for _ in range(self.kSize)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        for pair in self.lists[key % self.kSize]:
            if pair[0] == key:
                pair[1] = value
                return
        self.lists[key % self.kSize].append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map
        contains no mapping for the key
        """
        for pair in self.lists[key % self.kSize]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping
        for the key
        """
        for i, pair in enumerate(self.lists[key % self.kSize]):
            if pair[0] == key:
                self.lists[key % self.kSize].pop(i)
                return

# Example usage:
# obj = MyHashMap()
# obj.put(key, value)
# param_2 = obj.get(key)
# obj.remove(key)
