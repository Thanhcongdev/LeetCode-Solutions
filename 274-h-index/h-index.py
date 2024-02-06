class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        for cite in sorted(citations)[::-1]:
            if cite > h:
                h += 1
        return h