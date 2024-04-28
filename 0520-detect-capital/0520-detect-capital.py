class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        # Checking that if the word is all capitals, all lowercase, or title case
        if word.upper() == word or word.lower() == word or word.title() == word:
            return True

        # If none of the above conditions are met, return False
        return False
