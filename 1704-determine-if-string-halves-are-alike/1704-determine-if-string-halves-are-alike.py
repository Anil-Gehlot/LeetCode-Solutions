class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        # Set of vowels in both uppercase and lowercase
        vowel_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        # Initialize vowel count
        vowel = 0

        # Iterate through the characters of the input string
        for i in range(len(s)):
            
            # For the first half of the string
            if i < len(s)//2 and s[i] in vowel_set:
                vowel += 1
               
            # For the second half of the string
            elif i >= len(s)//2 and s[i] in vowel_set:
                vowel -= 1
                

        # Check if the final count of vowels is equal to 0
        return vowel == 0
