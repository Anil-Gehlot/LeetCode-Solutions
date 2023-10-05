class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        length = len(nums)/3

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

        # list to store element having occurrence more than n/3 times
        final_list = []

        # finding and appending the element having occurrence more than nums/3 times.
        for key in count.keys():
            if count[key] > length:
                final_list.append(key)

        # returning the final list   
        return final_list    