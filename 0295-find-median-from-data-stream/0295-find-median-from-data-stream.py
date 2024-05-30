class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        

    def findMedian(self) -> float:
        self.arr.sort()
        
        n = len(self.arr)
        mid = n//2
        
        if n%2 == 0:
            ans = self.arr[mid] + self.arr[mid-1]
            return ans / 2
        else:
            return self.arr[mid]
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()