# We define a class called Solution. 
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        # Get the size of the grid (assuming it's square).
        n = len(grid[0])

        # maxLocal to store the maximum values.
        maxLocal = [[-1 for i in range(n-2)] for i in range(n-2)]

        # Loop through the grid to find the maximum values.
        for i in range(n-2):
            for j in range(n-2):
                
                # Get the 3x3 submatrices.
                max1 = grid[i][j:j+3]
                max2 = grid[i+1][j:j+3]
                max3 = grid[i+2][j:j+3]

                # Find the maximum value among the submatrices and store it in maxLocal.
                maxLocal[i][j] = max(max(max1), max(max2), max(max3))
        
        # Return the matrix with maximum values.
        return maxLocal
