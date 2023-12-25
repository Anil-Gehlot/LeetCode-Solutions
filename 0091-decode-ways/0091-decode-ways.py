class Solution:
    def numDecodings(self, s: str) -> int:
        
        # Check if the string is empty or starts with '0'
        if not s or s[0] == '0':
            return 0

        # Get the length of the input string
        n = len(s)

        # Initialize the dynamic programming array with zeros
        dp = [0] * (n + 1)

        # There is one way to decode an empty string
        dp[0] = 1

        # Initialize dp[1] based on the first digit of the input string
        dp[1] = 1 if int(s[0]) > 0 else 0

        # Loop through the string starting from the second character
        for i in range(2, n + 1):
            # Extract one and two-digit numbers from the string
            one_digit = int(s[i - 1])
            two_digits = int(s[i - 2:i])

            # Update dp[i] based on the current digit
            if one_digit > 0:
                dp[i] += dp[i - 1]

            # Update dp[i] based on the current two digits
            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]

        # The result is stored in dp[n]
        return dp[n]
