class Solution:
    def maxPower(self, s: str) -> int:
        # Initialize variables to keep track of the maximum power and the current consecutive count.
        max_count = 0
        count = 1

        # Iterate through the string starting from the second character (index 1).
        for char in range(1, len(s)):
            # Check if the current character is the same as the previous one.
            if s[char] == s[char - 1]:
                # If it is, increment the consecutive count.
                count += 1
            else:
                # If it's not the same character, compare the count to the current max_count.
                if count > max_count:
                    # If the count is greater, update the max_count.
                    max_count = count
                # Reset the count to 1 for the new character.
                count = 1

        # Check the count after the loop in case the maximum power extends to the end of the string.
        if count > max_count:
            max_count = count

        # Return the maximum power found in the string.
        return max_count









# class Solution:
#     def maxPower(self, s: str) -> int:
        
#         max_count = 0
        
#         count = 1
        
#         for char in range(1, len(s)):
            
#             if s[char] == s[char-1]:
#                 count += 1
#             else :
#                 if count > max_count:
#                     max_count = count
                    
#                 count = 1
                
                
#         if count > max_count:
#                 max_count = count
            
#         return max_count
            
        