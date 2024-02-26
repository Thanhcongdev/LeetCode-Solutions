class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(pattern) < len(s):
            return False
        s1, s2 = set(pattern), set(s)
        if len(s1) != len(s2):
            return False
        mapp = {}
        for i in range(len(pattern)):
            if pattern[i] not in mapp:
                mapp[pattern[i]] = s[i]
            else:
                if mapp[pattern[i]] != s[i]:
                    return False
        return True