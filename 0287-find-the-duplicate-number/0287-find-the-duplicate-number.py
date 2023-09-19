class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # an empty dictionary to store the occurrence of element
        dict1 = {}
        
        # adding key and value in dictionary
        for i in nums:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        
        # finding the item having occurrence 2 or greater than 2
        for i, j in dict1.items():
            if j >= 2 :
                return i


        