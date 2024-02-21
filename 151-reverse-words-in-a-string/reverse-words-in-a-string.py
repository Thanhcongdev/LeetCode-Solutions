class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()
        ans = ""
        for ch in s[::-1]:
            ans += ch 
            ans += " "
        return ans[:-1]