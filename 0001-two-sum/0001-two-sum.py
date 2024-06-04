class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # dictionary to store the nums
        nums_dict = dict()

        # iterating over the nums
        for i in range(len(nums)):

            # calculate the complement for the current num
            complement = target - nums[i]

            # check if present in dict or not
            if complement in nums_dict:
                # if present, then return it and current num
                return [i, nums_dict[complement]]

            else:
                # if not present, add it to dict
                nums_dict[nums[i]] = i
            




        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        