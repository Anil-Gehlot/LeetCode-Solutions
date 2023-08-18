class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # to hold the number
        sum = 0
        for i in range(0, len(digits)):
            sum = (sum*10 ) + digits[i]

        # increasing value by one according to condition
        sum +=1

        # to return the increased value in the form of array
        list1 = []

        # holding index to insert the element 
        index = 0
        while(sum != 0 ):
            last_digit = sum % 10
            list1.insert(0, last_digit)
            index += 1
            sum = sum//10
        
        # returning new list
        return list1

