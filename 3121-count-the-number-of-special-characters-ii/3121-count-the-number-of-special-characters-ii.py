class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        occurence_dict = dict()

        for i in range( len(word) ) :
            char = word[i] 
            
            if char.lower() == char and char not in occurence_dict :
                occurence_dict[char] = [i, -1]

            elif char.lower() == char and char in occurence_dict :
                occurence_dict[char][0] = i
                
            else:
                if char.upper() == char and char.lower() in occurence_dict and  occurence_dict[char.lower()][-1] == -1: 
                    occurence_dict[char.lower()][-1] = i
                    
                elif char.upper() == char and char.lower() not in occurence_dict: 
                    occurence_dict[char.lower()] = [math.inf , i] 
                    
            # print(occurence_dict)

        special = 0

        for array in occurence_dict.values():

            if array[0] < array[1] and array[-1] != -1:
                special += 1

        return special

         
        
        