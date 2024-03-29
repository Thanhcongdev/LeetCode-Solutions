class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        i = 0
        res = []
        while i < len(nums):
            j = i
            while j < len(nums) - 1 and nums[j+1] == nums[j] + 1:
                j += 1
            if i == j:
                res.append(str(nums[i]))
            else:
                res.append(str(nums[i]) + "->" + str(nums[j]))
            i = j + 1
        return res