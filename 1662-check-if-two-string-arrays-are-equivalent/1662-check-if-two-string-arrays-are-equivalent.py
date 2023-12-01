class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        
        # finding the maximum length between length of both lists
        max_length = max(len(word1), len(word2))
        
        # Initialize empty strings to concatenate the words
        concatenate_word1 = ""
        concatenate_word2 = ""

        # Iterate through indices up to the maximum length
        for index in range(max_length):
            
            # Concatenate the word from word1 if it exists at the current index
            if len(word1) > index:
                concatenate_word1 += word1[index]
            
            # Concatenate the word from word2 if it exists at the current index
            if len(word2) > index:
                concatenate_word2 += word2[index]

        # Check if the concatenated strings are equal
        return concatenate_word1 == concatenate_word2