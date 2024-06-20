class Solution:
    def recursiveSubset(self, nums,output , result):
        
        if len(nums) == 0:
            result.append(output)
            return

        temp = nums.pop(0)
        
        self.recursiveSubset(nums[:], output, result)
        self.recursiveSubset(nums[:], output+[temp], result )
        


    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        result = []
        self.recursiveSubset( nums, output, result )
        return result