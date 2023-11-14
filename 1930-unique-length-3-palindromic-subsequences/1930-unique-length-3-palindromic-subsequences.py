class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Initialize a dictionary to store the indices of each character in the string.
        letter_count = {}

        # Populate the letter_count dictionary with the indices of each character.
        for i in range(len(s)):
            if s[i] in letter_count:
                letter_count[s[i]].append(i)
            else:
                letter_count[s[i]] = [i]

        # Initialize a set to store unique palindromes of length three.
        palindromes_set = set()

        # Iterate through the letter_count dictionary.
        for key in letter_count:
            # Check if there are at least two occurrences of the character.
            if len(letter_count[key]) >= 2:
                # Iterate through the indices of the character to form palindromes.
                for count in range(letter_count[key][0] + 1, letter_count[key][-1]):
                    # Check if the index is within the bounds of the string.
                    if count < len(s) - 1:
                        # Add the palindrome to the set.
                        palindromes_set.add(f"{key}{s[count]}{key}")

        # Return the count of unique palindromic subsequences of length three.
        return len(palindromes_set)

        

        
        
        
        
        
    '''
    
    # Time Limit Exceeded.
        palindorme_set = set()
        
        for i in range(len(s)-2):
            for j in range(i+1, len(s) - 1):
                for k in range(j+1, len(s) - 0):
                    if s[i] == s[k]:
                        palindorme_set.add(f"{s[i]}{s[j]}{s[k]}")
                        
        return len(palindorme_set)
    
    '''