class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        
        # an empty list to store the indices of prime numbers
        prime_indices = []

        # Iterate through the indices of the input list
        for index in range(len(nums)):
            
            # if the number at the current index is greater than or equal to 2
            if nums[index] >= 2:
                
                # loop to check for prime numbers
                for divisor in range(2, int(nums[index]**(1/2) + 1)):
                    
                    # If the number at the current index is divisible by divisor, it's not prime
                    if nums[index] % divisor == 0:
                        break
                else:
                    # If the inner loop completes without finding a divisor, the number is prime
                    # Add the index of the prime number to the prime_indices list
                    prime_indices.append(index)
        
        # Return the difference between the last and first indices of prime numbers
        return prime_indices[-1] - prime_indices[0]
