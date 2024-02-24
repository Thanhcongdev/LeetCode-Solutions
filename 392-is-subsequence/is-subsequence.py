class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i_sub =  0
        n = len(s)
        if n == 0:
            return True
        for ch in t:
            if ch == s[i_sub]:
                i_sub += 1
                if i_sub == n:
                    return True
        return i_sub == n 