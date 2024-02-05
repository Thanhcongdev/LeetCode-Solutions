class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num = nums[0]
        index = 0
        for i in range(1, len(nums)):
            if nums[i] == num:
                continue
            else:
                num = nums[i]
                index += 1
                nums[index] = num
        return index + 1
        