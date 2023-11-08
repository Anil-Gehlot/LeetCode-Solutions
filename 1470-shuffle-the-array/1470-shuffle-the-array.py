class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        # Initialize an empty list to store the rearranged elements.
        new_nums = []
        
        # Initialize 'mid' to 'n' since 'mid' will track the index in the second half of 'nums'.
        mid = n
        
        # Iterate over a range from 0 to 'n-1' (inclusive).
        for number in range(n):
            
            # Append the element from the first half of 'nums' to 'new_nums'.
            new_nums.append(nums[number])
            
            # Append the element from the second half of 'nums' to 'new_nums'.
            new_nums.append(nums[mid])
            
            # Increment 'mid' to move to the next element in the second half of 'nums'.
            mid += 1
            
        # Return the 'new_nums' list, which contains the rearranged elements.
        return new_nums
