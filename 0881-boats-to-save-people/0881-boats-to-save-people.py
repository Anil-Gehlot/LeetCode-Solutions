class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # Sort the people array
        people.sort()
        
        # Initialize pointers
        left = 0
        right = len(people) - 1
        boats = 0
        
        # Pair people into boats using two pointers
        while left <= right:

            if people[left] + people[right] <= limit:
                # If two people can fit in the boat, move both pointers
                left += 1
                right -= 1
            else:
                # Otherwise, only the heavier person goes in the boat
                right -= 1
            # increment boat count
            boats += 1
        
        return boats

            
        