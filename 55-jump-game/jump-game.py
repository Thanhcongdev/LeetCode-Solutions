class Solution:
    def canJump(self, nums: List[int]) -> bool:
        flag = 1
        s = len(nums)
        index_flag = s - 1
        res = True
        if s == 1:
            return True
        for i in range(s)[::-1]:
            if nums[i] == 0 and flag == 1:
                flag = 0
                res = False
                index_flag = i
            elif  flag == 0:
                if nums[i] > index_flag - i or nums[i] + i == s-1:
                    res = True
                    flag = 1
        return res                