class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        # Defining a set of good integers in descending order
        good_integers = ['999', '888', '777', '666', '555', '444', '333', '222', '111', '000']

        # Iterate through each good integer
        for good_integer in good_integers:
            
            # Check if the current good integer is present as a substring in the given num
            if good_integer in num:
                
                # If found, return the current good integer as the largest good integer
                return good_integer

        # If no good integer is found, return an empty string
        else:
            return ""
