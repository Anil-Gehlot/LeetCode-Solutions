class Solution:
    def compressedString(self, word: str) -> str:
        temp = [word[0]]

        for i in range(1, len(word)):
            if word[i] == temp[-1][-1]:
                temp[-1] += word[i]
            else:
                temp.append(word[i])
        
        result = ''

        for string in temp:
            length = len(string)
            while length > 9 :
                result += f"9{string[0]}"
                length -= 9
            result += f"{length}{string[0]}"

        return result

        

        