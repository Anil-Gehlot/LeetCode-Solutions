class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        # Check if the lengths of the two words are different
        if len(word1) != len(word2):
            return False
        
        # Count the occurrences of each character in both words
        count1 = collections.Counter(word1)
        count2 = collections.Counter(word2)

        # Check if the sets of keys (characters) are the same in both words
        if set(count1.keys()) != set(count2.keys()):
            return False

        # Check if the sorted lists of values (frequencies) are the same
        return sorted(count1.values()) == sorted(count2.values())