class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        occurance = 1
        for i in range(len(nums)):
            if nums[i] == nums[-i-1]:
                return nums[i]
            
                 