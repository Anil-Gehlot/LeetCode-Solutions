class Solution:
    def totalMoney(self, n: int) -> int:
        
        # Calculate the total number of complete weeks and the remaining days
        total_weeks = n // 7
        remaining_days = n % 7

        # Initialize the total money
        total_money = 0

        # Calculate the total money for complete weeks
        # The pattern for complete weeks is 28 * total_weeks
        for week in range(total_weeks):
            total_money += 28 + (week * 7)

        # Calculate the total money for remaining days
        # Plus the arithmetic sum of 1 + 2 + ... + remaining_days
        for day in range(total_weeks + 1, total_weeks + 1 + remaining_days):
            total_money += day

        return total_money
