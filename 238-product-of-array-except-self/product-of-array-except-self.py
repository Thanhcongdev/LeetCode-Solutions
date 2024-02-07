class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_product = 1
        post_product = 1
        res = [1]*n
        for i in range(n-1):
            pre_product *= nums[i]
            res[i+1] = pre_product
        for i in range(n-1)[::-1]:
            post_product *= nums[i+1]
            res[i] *= post_product
        return res
