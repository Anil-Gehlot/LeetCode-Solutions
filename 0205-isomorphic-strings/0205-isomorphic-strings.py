class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # Check if the lengths of both strings are not equal
        if len(s) != len(t):
            return False
        
        # Dictionary to store mappings from characters in s to characters in t
        mapping = {}
        
        # keep track of the characters from t that have already been mapped
        mapped_chars = set()

        # Iterate through the characters of both strings
        for i in range(len(s)):
            
            # Current characters from s and t
            char_s = s[i]
            char_t = t[i]

            # Check if the current character from s is already mapped to a character in t
            if char_s in mapping:
                
                # If yes, ensure the mapping is consistent
                if mapping[char_s] != char_t:
                    return False
            else:
                # If the current character from s is not yet mapped
                # Check if the character from t is already mapped to another character
                if char_t not in mapped_chars:
                    
                    # If not, add the mapping from s to t and mark t character as mapped
                    mapping[char_s] = char_t
                    mapped_chars.add(char_t)
                    
                else:
                    # If yes, it indicates a conflict, return False
                    return False
        
        # If the loop completes without any conflicts, return True (strings are isomorphic)
        return True
