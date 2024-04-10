class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        n = len(points)
        arrows = 0
        r = points[0][1]
        for i in range(1, n):
            if r >= points[i][0]:
                r = min(r, points[i][1])
                arrows += 1
            elif i < n - 1:
                r = points[i][1]
        return n - arrows
             