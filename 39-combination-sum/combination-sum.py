class Solution(object):
    def combinationSum(self, candidates, target):
        def dfs(start, target, comb):
            if target == 0:
                res.append(comb)
                return
            elif target < 0:
                return
            for i in range(start, len(candidates)):
                dfs(i, target - candidates[i], comb + [candidates[i]])
        res = []
        candidates.sort(reverse=True)
        dfs(0, target, [])
        return res        