class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:




        monotone_inc = False
        monotone_dec = False


        for i in range(len(nums)-1):


            # condition for monotonic decresing
            if nums[i] < nums[i+1]:
                monotone_dec = True

            # condition for monotonic incresing
            elif nums[i] > nums[i+1]:
                monotone_inc = True
            
            # if both becomd true means it is not increasing and not decreasing
            if monotone_inc==True and monotone_dec==True:
                return False
        
        return True
        



        