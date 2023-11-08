class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        new_nums = []
        
        i = n
        
        for number in range(n):
            new_nums.append(nums[number])
            new_nums.append(nums[i])
            i += 1
            
        return new_nums
            
            
        