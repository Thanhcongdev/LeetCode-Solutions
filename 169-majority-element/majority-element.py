class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = len(nums)
        dict_ = defaultdict(int)
        for num in nums:
            dict_[num] += 1
        for k, v in dict_.items():
            if v > s//2:
                return k
        
            
                 