class Solution:
    def __init__(self):
        self.step_count = 0 
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return self.step_count 

        if num%2 == 0:
            print(self.step_count)
            self.step_count += 1
            return self.numberOfSteps(num//2)
        else:
            print(self.step_count)
            self.step_count += 1
            return self.numberOfSteps(num-1)
        