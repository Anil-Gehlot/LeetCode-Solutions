class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        # an empty set to store unique alphabet characters
        alphabet_set = set()

        # Checking if the length of the sentence is at least 26 (the number of letters in the English alphabet)
        if len(sentence) >= 26:
            
            # Iterate through each character in the sentence
            for letter in sentence:
                
                # Add each character to the alphabet_set (sets only store unique elements)
                alphabet_set.add(letter)

        # Check if the size of the alphabet_set is equal to 26 (indicating all alphabet letters are present)
        if len(alphabet_set) == 26:
            return True

        return False
