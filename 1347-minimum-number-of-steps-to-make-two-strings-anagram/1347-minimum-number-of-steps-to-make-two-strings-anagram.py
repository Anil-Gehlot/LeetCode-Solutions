class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        # Count the occurrences of characters in both strings using Counter
        s_count = collections.Counter(s)
        t_count = collections.Counter(t)
        
        # Initialize a variable to store the count of steps required to make the strings equal
        count = 0
        
        # Check if the lengths of the two strings are different
        if len(s) != len(t):
            
            # If the lengths are different, the strings cannot be made equal
            return count
        
        # Iterate through the unique characters in the first string
        for key in s_count.keys():
            
            # Check if the count of the character in the second string is less than in the first string
            if t_count[key] < s_count[key]:
                
                # If yes, increment the count by the difference in counts
                count += s_count[key] - t_count[key]
        
        # Return the final count of steps required
        return count