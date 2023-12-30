class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        # Create an empty dictionary to store character counts
        char_count = {}

        # Iterate through each word in the list
        for element in words:

            # Iterate through each character in the word
            for char in element:
                
                # Update the character count in the dictionary
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

        # Extract the list of character counts from the dictionary
        char_count_list = char_count.values()

        # Check if it is possible to make all strings equal
        for num in char_count_list:
            # If the count is not divisible by the total number of words, return False
            if num % len(words) != 0:
                return False

        # If all character counts are divisible by the total number of words, return True
        return True
        
        