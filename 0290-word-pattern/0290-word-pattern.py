class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        # Split the string s into a list of words
        s = s.split()
        
        # Check if the lengths of the pattern and the list of words are equal
        if len(s) != len(pattern):
            return False

        # Initialize a dictionary to store mappings from characters in the pattern to words in s
        pattern_dict = dict()
        
        # Initialize a set to keep track of the values (words from s) that have already been mapped
        pattern_val = set()

        # Iterate through the characters of the pattern and the corresponding words in s simultaneously
        for char, word in zip(pattern, s):
            
            # If the current character in the pattern is already mapped to a word
            if char in pattern_dict:
                
                # Check if the mapping is consistent
                if pattern_dict[char] != word:
                    return False
            else:
                # If the current character is not yet mapped
                # Check if the current word is already mapped to another character
                if word not in pattern_val:
                    
                    # If not, add the mapping of the current character to the current word
                    pattern_dict[char] = word
                    
                    # Add the current word to the set of mapped values
                    pattern_val.add(word)
                else:
                    # If the current word is already mapped to another character, return False
                    return False
        
        # If the loop completes without any conflicts, return True (s follows the pattern)
        return True
