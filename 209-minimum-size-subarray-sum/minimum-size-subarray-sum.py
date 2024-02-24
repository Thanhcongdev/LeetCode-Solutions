class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, n = 0, len(nums)
        total = 0
        res = float("inf")
        for i in range(n):
            total += nums[i]
            while total >= target:
                res = min(i-l+1, res)
                total -= nums[l]
                l += 1
        return res if res != float("inf") else 0