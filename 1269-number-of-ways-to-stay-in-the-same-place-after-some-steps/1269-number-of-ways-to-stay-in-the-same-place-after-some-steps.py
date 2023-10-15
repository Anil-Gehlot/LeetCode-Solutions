class Solution:
  def numWays(self, steps: int, arrLen: int) -> int:
    # Define the modulo constant for calculations
    kMod = 1_000_000_007

    # Initialize a dynamic programming array to store the number of ways to stay on each index
    # We limit the size of the array to min(steps // 2 + 1, arrLen) to optimize space
    dp = [0] * min(steps // 2 + 1, arrLen)
    dp[0] = 1  # There is 1 way to start at index 0

    # Iterate through each step
    for _ in range(steps):
      # Initialize a new array to store updated number of ways for each index
      newDp = [0] * min(steps // 2 + 1, arrLen)

      # Iterate through each index and update the number of ways to reach that index
      for i, ways in enumerate(dp):
        if ways > 0:
          # Try moving left, staying in place, and moving right
          for dx in (-1, 0, 1):
            nextIndex = i + dx
            if 0 <= nextIndex < len(dp):
              # Accumulate the number of ways to reach the next index
              newDp[nextIndex] += ways
              newDp[nextIndex] %= kMod  # Apply modulo to avoid overflow

      # Update the dp array with the new number of ways
      dp = newDp

    return dp[0]  # Return the number of ways to stay at index 0 after all steps
