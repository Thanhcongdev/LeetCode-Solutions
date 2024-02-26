class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zero_row, zero_col = [False]*m, [False]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_row[i] = True
                    zero_col[j] = True
        for i in range(m):
            for j in range(n):
                if zero_row[i] or zero_col[j]:
                    matrix[i][j] = 0