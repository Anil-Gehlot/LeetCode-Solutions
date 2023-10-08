class Solution:
  def maxDotProduct(self, A: List[int], B: List[int]) -> int:

    m = len(A)  # Length of list A
    n = len(B)  # Length of list B
    
    # dp[i][j] := max dot product of two subseqs nums[0..i) and nums2[0..j)
    # Initialize a 2D DP array with dimensions (m+1) x (n+1)
    dp = [[-math.inf] * (n + 1) for _ in range(m + 1)] 
    
    # Iterate through list A
    for i in range(m):
      # Iterate through list B
      for j in range(n):
        # Update the DP table based on the maximum dot product considering current elements from A and B
        dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], max(0, dp[i][j]) + A[i] * B[j])

    # Return the maximum dot product
    return dp[m][n]
