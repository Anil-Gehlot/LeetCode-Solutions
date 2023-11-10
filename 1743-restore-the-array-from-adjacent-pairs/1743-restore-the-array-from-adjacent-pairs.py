class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
    
        # Create an adjacency dictionary to store the neighbors of each element
        adjacency_dict = {}

        # Populate the adjacency dictionary based on the given adjacentPairs
        for arr in adjacentPairs:
            if arr[0] in adjacency_dict:
                adjacency_dict[arr[0]].append(arr[1])
            else:
                adjacency_dict[arr[0]] = [arr[1]]
            
            if arr[1] in adjacency_dict:
                adjacency_dict[arr[1]].append(arr[0])
            else:
                adjacency_dict[arr[1]] = [arr[0]]

        # Find the starting point (element with only one neighbor)
        smallest_key = None
        for key in adjacency_dict:
            if len(adjacency_dict[key]) == 1:    
                smallest_key = key
                break

        # Initialize the result array with the starting point
        nums = [smallest_key]

        # Use a set to keep track of visited elements
        visited = set(nums)

        # Reconstruct the array until it reaches the desired length
        while len(nums) < len(adjacentPairs) + 1:
            current = nums[-1]
            next_candidates = adjacency_dict[current]

            # Iterate through the neighbors of the current element
            for candidate in next_candidates:
                if candidate not in visited:
                    # Add the candidate to the result array
                    nums.append(candidate)
                    # Mark the candidate as visited
                    visited.add(candidate)
                    # Break to move to the next iteration of the while loop
                    break

        # Return the reconstructed array
        return nums

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#--------------------------------------------------------------------------------------------------------------------------------------
        
        '''
        # Getting time limit exeeds in this code.

        # Initialize an empty dictionary to store adjacent pairs
        dict = {}

        # Iterate through each pair in the list of adjacent pairs
        for arr in adjacentPairs:
            # Check if the first element of the pair is already a key in the dictionary
            if arr[0] in dict:
                # If yes, append the second element to the list associated with that key
                dict[arr[0]].append(arr[1])
            else:
                # If no, create a new key with the first element and associate it with a list containing the second element
                dict[arr[0]] = [arr[1]]

            # Repeat the process for the second element of the pair
            if arr[1] in dict:
                dict[arr[1]].append(arr[0])
            else:
                dict[arr[1]] = [arr[0]]

        # Find the starting point (smallest key) of the sequence
        smallest_key = None
        for key in dict:
            if len(dict[key]) == 1:    
                smallest_key = key
                break

        # Initialize a list to store the sequence of numbers, starting with the smallest key
        nums = [smallest_key]

        # Build the sequence until it has the same length as the number of adjacent pairs + 1
        while len(nums) < len(adjacentPairs) + 1:
            # Get the last number in the sequence
            current = nums[-1]

            # Find the next candidates based on the dictionary
            next_candidates = dict[current]

            # Iterate through the candidates
            for candidate in next_candidates:
                # Add the candidate to the sequence if it is not already present
                if candidate not in nums:
                    nums.append(candidate)
                    break

        # return the final sequence
        return nums
        '''