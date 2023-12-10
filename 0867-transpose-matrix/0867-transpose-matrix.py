class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        # Getting the number of rows and columns in the original matrix
        row = len(matrix)
        column = len(matrix[0])

        # Initialize a new matrix with swapped dimensions
        new_matrix = []
        for i in range(column):
            new_matrix.append( [0] * row )


        # Fill the transposed matrix by swapping rows and columnsing  
        for i in range(row):
            for j in range(column):
                new_matrix[j][i] = matrix[i][j]
                
        print(new_matrix)
        return new_matrix

      