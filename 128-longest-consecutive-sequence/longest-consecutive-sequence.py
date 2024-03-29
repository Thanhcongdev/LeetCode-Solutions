class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        for num in nums:
            if num + 1 not in nums:
                cur_len = 1
                while num-+ 1 in nums:
                    num -= 1
                    cur_len += 1
                max_len = max(max_len, cur_len)
        return max_len

        