class Solution:
    def canJump(self, nums: List[int]) -> bool:
        energy = 0
        for num in nums:
            if energy < 0:
                return False
            elif num > energy:
                energy = num    
            energy -= 1
        return True      