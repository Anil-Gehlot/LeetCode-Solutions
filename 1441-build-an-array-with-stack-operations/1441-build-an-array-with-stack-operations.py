
        
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        i = 0  # Initialize the target pointer to 0
        num = 1  # Initialize the current number to 1

        while i < len(target):  # Continue looping until we reach the end of the target array
            t = target[i]  # Get the target value at the current pointer position
            if t == num:  # If the target value matches the current number
                ans.append("Push")  # Add "Push" to the result
                i += 1  # Move the target pointer to the next position
            else:
                ans.append("Push")  # If the target value doesn't match the current number, add "Push"
                ans.append("Pop")  # Also add "Pop" to the result to simulate popping an element
            num += 1  # Increment the current number for the next iteration

        return ans  # Return the list of "Push" and "Pop" operations
