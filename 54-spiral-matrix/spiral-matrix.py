class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m, n = len(matrix), len(matrix[0])
        top, bot, l, r = 0, m -1, 0, n-1
        if not matrix:
            return res
        while top <= bot and l <= r:
            for i in range(l, r+1):
                result.append(matrix[top][i])
            top += 1
            for i in range(top, bot + 1):
                result.append(matrix[i][r])
            r -= 1
            if top <= bot:
                for i in range(r, l-1, -1):
                    result.append(matrix[bot][i])
                bot -= 1
            if l <= r:
                for i in range(bot, top-1, -1):
                    result.append(matrix[i][l])
                l += 1
        return result