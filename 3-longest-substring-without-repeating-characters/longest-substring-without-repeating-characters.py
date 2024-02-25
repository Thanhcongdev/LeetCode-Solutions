class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, n = 0, len(s)
        subStr = set()
        ans = 0
        for i in range(n):
            if s[i] not in subStr:
                subStr.add(s[i])
            else:
                ans = max(ans, len(subStr))
                while s[i] in subStr:
                    subStr.remove(s[l])
                    l += 1
                subStr.add(s[i])
        ans = max(ans, len(subStr))
        return ans