class Solution:
    def jump(self, nums: List[int]) -> int:
        s = len(nums)
        index = 0
        count = 1
        if s == 1:
            return 0
        while index < s - 1:
            num = nums[index]
            if index + num >= s - 1:
                return count
            max_jump = 0
            for i in range(index+1,min(index+num+1, s)):
                if nums[i] + i > max_jump:
                    max_jump = nums[i] + i
                    index = i
            count += 1
        return count 