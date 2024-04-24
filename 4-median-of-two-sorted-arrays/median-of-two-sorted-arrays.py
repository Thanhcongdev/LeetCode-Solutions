class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findmeadian(merged):
            total = len(merged)
            if total % 2 == 1:
                return float(merged[total // 2])
            else:
                middle1 = merged[total // 2 - 1]
                middle2 = merged[total // 2]
                return (float(middle1) + float(middle2)) / 2.0
        def compare_half(chunk1, chunk2, m, n):
            print(chunk1, chunk2, m, n)
            if m < 2 and n < 2:
                merged = nums1 + nums2
                merged.sort()
                return findmeadian(merged)
            i = m // 2
            j = n // 2
            mean1 = chunk1[i] if m % 2 == 0 else sum(chunk1[i:i+2]) / 2
            mean2 = chunk2[j] if n % 2 == 0 else sum(chunk2[j:j+2]) / 2
            if mean1 >= mean2:
                if n % 2 != 0:
                    j += 1
                return compare_half(chunk1[:i+1], chunk2[j:], m // 2, n // 2)
            else:
                if m % 2 != 0:
                    i += 1
                return compare_half(chunk1[i:], chunk2[:j+1], m // 2, n // 2)

        m, n = len(nums1) - 1, len(nums2) - 1
        if m < 0:
            return findmeadian(nums2)
        if n < 0:
            return findmeadian(nums1)

        num = compare_half(nums1, nums2, m, n)
        return num