class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        # function to sort the array.
        def sort(arr):
            
            # Base case: if the array has 0 or 1 elements, it is already sorted
            if len(arr) <= 1:
                return arr
            
            else:
                # Choose the pivot as the first element of the array
                pivot = arr[0]

                # Create a list of elements less than or equal to the pivot
                less = [x for x in arr[1:] if x <= pivot]

                # Create a list of elements greater than the pivot
                greater = [x for x in arr[1:] if x > pivot]

                # Recursively sort the "less" and "greater" subarrays
                return sort(less) + [pivot] + sort(greater)
        
        # Sort the 'piles' in ascending order
        piles = sort(piles)

        # Initialize the variable to store the maximum number of coins
        max_coins = 0
        
        # Iterate through the 'piles' to select the second-largest element in each triplet
        for my_coins in range( len(piles)//3, len(piles), 2):
            
            # Add the selected element to the 'max_coins'
            max_coins += piles[my_coins]
        
        # Return the final result, which represents the maximum number of coins I can have
        return max_coins
    
    
    
    
    
        '''
        max_coins = 0

        # Sort the 'piles' array in ascending order
        piles.sort()

        # Iterate through the 'piles' array considering triplets
        for i in range(len(piles)//3):
            # Remove the last element from the 'piles' array
            piles.pop()

            # Add the second-to-last element to the 'max_coins'
            max_coins += piles.pop()

            # Remove the first element from the 'piles' array
            piles.pop(0)

        # Return the final result, which represents the maximum number of coins you can have
        return max_coins
        '''
