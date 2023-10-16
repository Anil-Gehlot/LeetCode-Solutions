class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Create a list of size (rowIndex + 1) and initialize all elements to 1
        ans = [1] * (rowIndex + 1)

        # Loop through the rows starting from the third row (rowIndex = 2)
        for i in range(2, rowIndex + 1):
            # Loop through the elements within each row
            for j in range(1, i):
                # Calculate the value of the current element based on the previous row's elements
                ans[i - j] += ans[i - j - 1]

        # Return the list representing the rowIndex-th row of Pascal's Triangle
        return ans
