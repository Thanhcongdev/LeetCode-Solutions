class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        nums = sorted(nums)
        for i in range(n-2):
            l = i + 1
            r = n - 1
            while l < r:
                sum_ = nums[i] + nums[l] + nums[r]
                if sum_ < 0:
                    l += 1
                elif sum_ > 0:
                    r -= 1
                else:
                    ans.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        return ans        