class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        # if ch not found in word return word as it is
        if ch not in word:
            return word

        # if ch found then find it's index
        index = word.index(ch)
        
        # return the reversed word till the index and rest as it is
        return word[:index+1][::-1] + word[index+1:]
        