class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != ".":
                    res += [(i, val), (val, j), (i//3, j//3, val)]
        return len(res) == len(set(res))