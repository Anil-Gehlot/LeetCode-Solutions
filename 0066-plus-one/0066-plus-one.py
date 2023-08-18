class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        sum = 0
        for i in range(0, len(digits)):
            sum = (sum*10 ) + digits[i]

        sum +=1
        list1 = []
        index = 0
        while(sum != 0 ):
            last_digit = sum % 10
            list1.insert(0, last_digit)
            index += 1
            sum = sum//10
        
        return list1

