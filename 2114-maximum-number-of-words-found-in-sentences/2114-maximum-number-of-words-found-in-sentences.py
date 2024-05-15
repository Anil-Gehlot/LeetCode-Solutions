class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0

        for sentence in sentences:
            
            # Split the sentence into words using space as delimiter
            words = sentence.split()
            
            # Count the number of words in the current sentence
            num_words = len(words)
            
            # Update max_words if the current sentence has more words
            max_words = max(max_words, num_words)

        return max_words