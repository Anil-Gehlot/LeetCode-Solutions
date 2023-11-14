class Solution:
    def reverseVowels(self, s: str) -> str:
        # Set of vowels (both lowercase and uppercase)
        vowel_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        # List to store vowels in the original order
        s_vowel_list = []

        # Step 1: Collect vowels in the original order
        for char in s:
            if char in vowel_set:
                s_vowel_list.append(char)


        # Step 2: Replace vowels in the string with reversed vowels
        for char in range(len(s)):
            if s[char] in vowel_set:
                # Replace the current vowel with the last vowel in s_vowel_list
                s = s[:char] + s_vowel_list.pop() + s[char + 1:]

        return s