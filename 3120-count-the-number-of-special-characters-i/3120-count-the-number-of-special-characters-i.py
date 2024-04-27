class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        # Convert the word into a set to remove duplicates
        word = set(word)
        
        # a variable to count special characters
        special_count = 0
        
        # Continue until there are characters in the set
        while word:
            
            # Pop a character from the set
            temp = word.pop()
            
            # Check if the lowercase or uppercase form of the character exists in the set
            if temp.lower() in word or temp.upper() in word:
                
                # If so, increment the special character count
                special_count += 1
                
        # Return the count of special characters
        return special_count
