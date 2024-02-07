class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_product = 1
        post_product = 1
        res = [0]*n
        for i in range(n):
            res[i] = pre_product
            pre_product *= nums[i]
        for i in range(n-1, -1, -1):
            res[i] *= post_product
            post_product *= nums[i]
        return res
