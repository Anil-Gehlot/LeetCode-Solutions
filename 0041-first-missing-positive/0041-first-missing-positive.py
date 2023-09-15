class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        

        '''
        # 1st solution

        max = -math.inf

        for i in nums:
            if i > max:
                max = i

        for i in range(1, max+2):
            if i not in nums:
                return i
            
        return 1'''


        '''
        # 2nd solution
        i = 0
        def missing_positive(i, nums):
            if (i+1) not in nums:
                return i+1
            else:
                i +=1
                return missing_positive(i, nums)

        if missing_positive(i, nums) != None:
            return missing_positive(i, nums)
        else :
            return 1'''


        '''# 3rd solution

        #  sets have an average time complexity of O(1) for this operation, 
        #   while lists have a time complexity of O(n) for linear searches.

        i = 1
        while i in nums:
            i += 1
        
        return i'''

        # converting given lists into set
        set1= set(nums)
        i = 1

        # checking membership of each element
        while i in set1:
            i += 1
        return i



