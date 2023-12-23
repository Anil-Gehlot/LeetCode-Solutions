class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        # Initialize an empty string to store the results
        result = ''

        # Getting each character's alphabatic number and adding it to result. 
        for char in s:
            alphabat_no = ord(char)-96
            result += str(alphabat_no)

        # Perform the transformation k times
        for operation in range(k):
            sum = 0
            
            # Calculating the sum of digits for the current result
            for num in result:
                sum += int(num)
            
            else:
                result = str(sum)
                sum = 0
            
        # return the result in integer format
        return int(result)