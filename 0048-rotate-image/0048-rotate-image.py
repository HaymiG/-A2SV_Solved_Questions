class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # transpose
        for i in range(n):
            for j in range(i + 1 , n):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j] 
        # reflection
        for i in range(n):
            for j in range(n //2):
                matrix[i][j] , matrix[i][n - j - 1] = matrix[i][n -j - 1] , matrix[i][j]




















        # edge_length = len(matrix)

        # top = 0
        # bottom = edge_length - 1

        # while top < bottom:
        #     for col in range(edge_length):
        #         temp = matrix[top][col]
        #         matrix[top][col] = matrix[bottom][col]
        #         matrix[bottom][col] = temp
        #     top += 1
        #     bottom -= 1

        # for row in range(edge_length):
        #     for col in range(row+1, edge_length):
        #         temp = matrix[row][col]
        #         matrix[row][col] = matrix[col][row]
        #         matrix[col][row] = temp
        
        # return matrix