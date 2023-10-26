class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        kMod = 1_000_000_007  # A constant used for taking the modulo of results
        n = len(arr)  # The number of elements in the input array
        # dp[i] represents the number of binary trees with arr[i] as the root
        dp = [1] * n  # Initialize the dp array with 1s, as each element can be a single tree by itself
        arr.sort()  # Sort the input array in ascending order
        numToIndex = {a: i for i, a in enumerate(arr)}  # Create a dictionary to map elements to their indices in the array

        for i, root in enumerate(arr):  # Iterate through the elements of the sorted array
            for j in range(i):  # Iterate through elements before the current root
                if root % arr[j] == 0:  # Check if arr[j] can be the left subtree of arr[i]
                    right = root // arr[j]  # Calculate the possible right subtree value
                    if right in numToIndex:  # Check if the right subtree value exists in the array
                        # Update dp[i] by adding the product of dp[j] (left subtree) and dp[numToIndex[right]] (right subtree)
                        dp[i] += dp[j] * dp[numToIndex[right]]
                        dp[i] %= kMod  # Take the modulo to prevent overflow

        # Return the sum of all elements in the dp array, taking the modulo to get the final result
        return sum(dp) % kMod
