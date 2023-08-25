class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dict1 ={
                    "2" : "abc",
                    "3" : "def",
                    "4" : "ghi",
                    "5" : "jkl",
                    "6" : "mno",
                    "7" : "pqrs",
                    "8" : "tuv", 
                    "9" : "wxyz"
                }
        length = len(digits)

        final = []

        if digits == "":
            # return []
            print([])

        if length == 1:
            for i in dict1[digits]:
                final.append(i)

        if length == 2 :
            for i in dict1[digits[0]]:
                for j in dict1[digits[1]]:
                    final.append(i+j)


        if length == 3 :
            for i in dict1[digits[0]]:
                for j in dict1[digits[1]]:
                    for k in dict1[digits[2]]:
                        final.append(i+j+k)

        if length == 4 :
            for i in dict1[digits[0]]:
                for j in dict1[digits[1]]:
                    for k in dict1[digits[2]]:
                        for l in dict1[digits[3]]:
                            final.append(i+j+k+l)
        return final


    


    
    
    