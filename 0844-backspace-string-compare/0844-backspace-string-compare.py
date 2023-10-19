class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Initialize two empty lists to store the processed strings.
        s1 = []
        t1 = []
        
        # Process string 's'.
        for letters in s:
            if letters == "#" :
                # If the current character is a backspace ('#'), 
                # check if there are characters in s1 to remove.
                if len(s1) > 0: 
                    s1.pop()  # Remove the last character in s1.
                else:
                    pass  # If s1 is empty, there's nothing to remove.
            else:
                s1.append(letters)  # Add non-backspace characters to s1.
                
        # Process string 't' using the same logic as for 's'.
        for letters in t:
            if letters == "#" :
                if len(t1) > 0:
                    t1.pop()
                else:
                    pass
            else:
                t1.append(letters)
                
        # Check if the processed strings 's1' and 't1' are equal.
        return s1 == t1  # Return True if they are equal, indicating the original strings are equivalent.
