class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.dfs(1, [], k, n, ans)
        return ans
    def dfs(self, idx, comb, k, n, ans):
        if k == 0:
            ans.append(comb[:])
            return
        for i in range(idx, n + 1):
            comb.append(i)
            self.dfs(i + 1, comb, k - 1, n, ans)
            comb.pop()
        
