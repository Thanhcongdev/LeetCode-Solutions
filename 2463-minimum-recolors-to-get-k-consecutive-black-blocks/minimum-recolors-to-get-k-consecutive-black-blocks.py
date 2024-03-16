class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, num_white, res = 0, 0, k
        for r, block in enumerate(blocks):
            if block == "W":
                num_white += 1
            if r - l == k - 1:
                res = min(res, num_white)
                num_white -= blocks[l] == "W"
                l += 1
                
        return res