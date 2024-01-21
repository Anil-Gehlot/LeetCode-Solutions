class MyStack:

    def __init__(self):
        self.container = deque()
        

    def push(self, x: int) -> None:
        self.container.append(x)
        

    def pop(self) -> int:
        return self.container.pop()
        

    def top(self) -> int:
        return self.container[-1]

    
    def empty(self) -> bool:
        return len(self.container)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()