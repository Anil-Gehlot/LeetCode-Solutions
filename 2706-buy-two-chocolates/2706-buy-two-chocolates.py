class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        # Initialize the minimum_money 
        minimum_money = math.inf

        # Iterate through all pairs of chocolates
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):

                # Calculate the total price for the current pair of chocolates
                total_price = prices[i] + prices[j]

                # Update the minimum_money if the current total_price is smaller
                if minimum_money > total_price:
                    minimum_money = total_price

        # Check if there is non-negative leftover money after buying the chocolates
        if money - minimum_money >= 0:
            
            # Return the amount of leftover money
            return money - minimum_money

        # If no valid pair is found, return the initial amount of money
        return money