class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        # Convert the dictionary to a set for efficient lookup
        dictionary = set(dictionary)
        
        # Split the sentence into words
        sentence = sentence.split()
        
        # Iterate through each word in the sentence
        for i in range(len(sentence)):
            word = sentence[i]
            
            # Check each prefix of the word
            for n in range(1, len(word) + 1):
                if word[:n] in dictionary:
                    sentence[i] = word[:n]
                    break  # Stop once the shortest root is found
        
        # Join the words back into a sentence
        return " ".join(sentence)