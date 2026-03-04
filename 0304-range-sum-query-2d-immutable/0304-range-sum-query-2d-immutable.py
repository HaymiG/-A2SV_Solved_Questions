class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row  = len(matrix)
        col = len(matrix[0])
        self.sum_pr = [[0] * (col + 1) for _ in range(row + 1)]
        
        for r in range(row):
            for c in range(col):
                top = self.sum_pr[r][c + 1]
                left = self.sum_pr[r + 1][c]
                topleft = self.sum_pr[r][c]
                self.sum_pr[r + 1][c + 1] = matrix[r][c] + top + left - topleft


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 = row1 +1 
        col1 = col1 +1 
        row2 = row2 + 1 
        col2 = col2 + 1
        total = self.sum_pr[row2][col2]
        left = self.sum_pr[row2][col1 -1]
        top = self.sum_pr[row1 -1][col2]
        topleft = self.sum_pr[row1-1][col1-1]
        return total - left - top + topleft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)