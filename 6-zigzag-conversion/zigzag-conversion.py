class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        direction = -1
        index_row = 0
        
        for ch in s:
            rows[index_row].append(ch)
            if index_row == 0:
                direction = 1
            if index_row == numRows - 1:
                direction = -1
            index_row += direction
        return ''.join([''.join(row) for row in rows])