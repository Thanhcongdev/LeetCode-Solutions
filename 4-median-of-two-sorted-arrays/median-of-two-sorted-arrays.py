class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findMedian(merged):
            total = len(merged)
            if total % 2 == 1:
                return float(merged[total // 2])
            else:
                middle1 = merged[total // 2 - 1]
                middle2 = merged[total // 2]
                return (float(middle1) + float(middle2)) / 2.0

        m, n = len(nums1), len(nums2)
        if m == 0:
            return findMedian(nums2)
        if n == 0:
            return findMedian(nums1)

        i, j = 0, 0
        merged = []
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        while i < m:
            merged.append(nums1[i])
            i += 1

        while j < n:
            merged.append(nums2[j])
            j += 1

        return findMedian(merged)