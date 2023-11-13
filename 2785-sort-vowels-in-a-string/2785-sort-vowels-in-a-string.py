class Solution:
    def sortVowels(self, s: str) -> str:
        
        # Define a set of vowels, both lowercase and uppercase
        vowel_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        # List to store the vowels
        vowels = []

        # Set to store the indices of vowels
        vowel_indices = set()

        # Identify vowels and their indices
        for letter in range(len(s)):
            if s[letter] in vowel_set:
                vowels.append(s[letter])
                vowel_indices.add(letter)

        # Sort the vowels
        vowels = sorted(vowels)

        # Reconstruct the string
        new_str = ''
        sorted_vowel_index = 0

        # Iterate through the original string
        for i in range(len(s)):
            # If the current index is a vowel index
            if i in vowel_indices:
                # Append the sorted vowel to the new string
                new_str += vowels[sorted_vowel_index]
                sorted_vowel_index += 1
            else:
                # Append the original character to the new string (consonant)
                new_str += s[i]

        # Return the final reconstructed string
        return new_str
