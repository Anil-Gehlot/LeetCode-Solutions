class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        
        # Get the number of rows and columns in the grid
        m = len(grid)
        n = len(grid[0])

        # Initialize the difference matrix with zeros
        diff = [[0] * n for i in range(m)]

        # Lists to store the count of ones and zeros for rows and columns
        ones_row = []
        ones_col = []
        
        zeros_row = []
        zeros_col = []

        # Calculate the count of ones in each row
        for row in grid:
            ones_row.append(row.count(1))

        # Calculate the count of ones in each column
        for col in zip(*grid):
            ones_col.append(col.count(1))

        # Calculate the count of zeros in each row
        for row in grid:
            zeros_row.append(row.count(0))

        # Calculate the count of zeros in each column
        for col in zip(*grid):
            zeros_col.append(col.count(0))

        # Calculate the difference matrix using the given formula
        for i in range(m):
            for j in range(n):
                
                # diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
                diff[i][j] = ones_row[i] + ones_col[j] - zeros_row[i] - zeros_col[j]

        # Return the diff matrix
        return diff