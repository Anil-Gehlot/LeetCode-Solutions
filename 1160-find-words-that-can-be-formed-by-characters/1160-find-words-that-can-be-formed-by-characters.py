class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        # Initialize a string to store valid words
        ans = ''  
        
        # Iterate through each word in the list
        for word in words:
            
            # Check if the word can be formed using the characters in 'chars'
            for letter in word:
                
                if chars.count(letter) < word.count(letter):
                    break  # If the word cannot be formed, break out of the loop
                    
            else:
                ans += word  # If the word can be formed, add it to the result string
        
        # Return the length of the concatenated valid words
        return len(ans)  
