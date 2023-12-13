class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        m = len(mat)
        n = len(mat[0])

        row_count = [0] * m  # Count of 1s in each row
        col_count = [0] * n  # Count of 1s in each column

        special_position = 0

        # Count the number of 1s in each row and each column
        for i in range(m):
            for j in range(n):

                print(i, j)

                if mat[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1


        # Check for special positions
        for i in range(m):
            for j in range(n):

                # Check if the current position is a special position
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    (special_position) += 1



        return special_position