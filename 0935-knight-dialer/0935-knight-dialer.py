class Solution:
    def knightDialer(self, n: int) -> int:
        
        
        # Initialize the number of ways to reach each digit from the starting position
        arr = [1] * 10
        
        for index in range(n-1):
            
            # Initialize a new array to store the updated number of ways for each digit
            dp = [0] * 10
            
            # Calculate the new number of ways for each digit based on knight moves
            dp[0] = arr[5] + arr[7]
            dp[1] = arr[6] + arr[8]
            dp[2] = arr[3] + arr[7]
            dp[3] = arr[2] + arr[8] + arr[9]
            dp[4] = 0  # Digit 4 has no valid knight move
            dp[5] = arr[0] + arr[6] + arr[9]
            dp[6] = arr[1] + arr[5]
            dp[7] = arr[0] + arr[2]
            dp[8] = arr[1] + arr[3]
            dp[9] = arr[3] + arr[5]
            
            # Update the array for the next iteration
            arr = dp
        
        # Sum up the final number of ways for each digit and return the result
        return sum(arr) % (10**9+7)