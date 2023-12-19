class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        
        # Checkin that, if the input matrix is empty or has empty rows
        if not img or not img[0]:
            return []

        # Get the number of rows and columns in the input matrix
        m, n = len(img), len(img[0])

        # Initialize a matrix to store the smoothed values, filled with zeros
        result = [[0] * n for _ in range(m)]

        # Iterate over each cell in the input matrix
        for i in range(m):
            for j in range(n):
                
                # Variables to accumulate sum and count of neighbors
                neighbors_sum = 0
                neighbors_count = 0

                # Iterate over a 3x3 window centered at the current cell
                for ni in range(max(0, i - 1), min(m, i + 2)):
                    for nj in range(max(0, j - 1), min(n, j + 2)):
                        
                        # Accumulate values of neighbors
                        neighbors_sum += img[ni][nj]
                        
                        # Increment count of neighbors
                        neighbors_count += 1

                # Calculate the average of the cell and its neighbors,
                # rounding down to the nearest integer
                result[i][j] = neighbors_sum // neighbors_count

        # Return the matrix containing the smoothed values
        return result