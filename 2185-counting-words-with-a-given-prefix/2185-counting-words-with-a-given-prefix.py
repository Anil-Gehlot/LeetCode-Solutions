class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        # Initialize a variable to count the words that have the specified prefix.
        pref_count = 0

        # Get the length of the prefix string.
        pref_len = len(pref)
        
        # Iterate through each word in the 'words' list.
        for word in words:
            # Check if the first 'pref_len' characters of the current word match the prefix.
            if word[:pref_len] == pref:
                # If they match, increment the 'pref_count'.
                pref_count += 1

        # Return the count of words that have the specified prefix.
        return pref_count
