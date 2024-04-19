class Solution: 
    def finalString(self, s: str) -> str: 
        
        # Create an empty string called result to store the typed characters
        result = ""  
        
        # Go through each character in the input string s
        for i in s:  
            
            # If the current character is 'i'
            if i == "i":  
                
                # Reverse the string new_s
                result = result[::-1]  
            
             # If the current character is not 'i'
            else: 
                
                # Add the current character to the string new_s
                result += i  
        
        # Return the final string after typing each character
        return result  
