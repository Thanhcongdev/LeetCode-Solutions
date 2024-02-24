class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0
        maxHeight = max(height)
        while l < r:
            curArea = min(height[l], height[r]) * (r-l)
            maxArea = max(curArea, maxArea)
            print(l,r)
            if height[l] == maxHeight and height[l] == height[r]:
                curArea = min(height[l], height[r]) * (r-l)
                maxArea = max(curArea, maxArea)
                return maxArea
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea