class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        # Pop the last word from the list to use it as a reference for comparison
        temp_word = words.pop()
        result = []

        # Iterate through each letter in the reference word
        for letter in temp_word:
            count = 0  # Initialize a count to track occurrences of the letter in other words

            # Loop through each remaining word in the list
            for i in range(len(words)):
                word = words[i]
                
                # If the letter is found in the word, increment the count
                if letter in word:
                    count += 1
                    
                    # Replace the first occurrence of the letter in the word to avoid counting it again
                    words[i] = word.replace(letter, "", 1)
            
            # If the letter was found in all remaining words, add it to the result
            if count == len(words):
                result.append(letter)

        return result 