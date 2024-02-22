class Solution:
    def jump(self, max_top, height):
        ans = 0
        top = 0
        end = -1
        for i in range(len(height)):
            if height[i] == max_top:
                end = i
                break
            if height[i] > top:
                top = height[i]
            else:
                ans += top - height[i]
        return ans, end
    def trap(self, height: List[int]) -> int:
        max_top = max(height)
        ans = 0
        residual, end1 = self.jump(max_top, height)
        ans += residual
        residual, end2 = self.jump(max_top, height[::-1])
        end2 =  len(height) - end2 - 1
        ans += residual
        if end1 != end2:
            for i in range(end1+1, end2):
                ans += max_top - height[i]
        return ans