class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        length = len(nums)/2

        # dictionary to store the occurrence of element
        count = { }

        # traversing the given array
        for element in nums:
            
            # increasing occurrence by 1
            if element in count.keys():
                count[element] += 1
            
            # adding occurrence of new element
            elif element not in count.keys():
                count[element] = 1



        # finding the element having occurrence more than nums/2 times.
        for key in count.keys():
            if count[key] > length:
                return key
  