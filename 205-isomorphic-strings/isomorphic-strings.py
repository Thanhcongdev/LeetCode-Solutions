class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1, s2 = set(s), set(t)
        if len(s1) != len(s2):
            return False
        mapp = {}
        for i in range(len(s)):
            if s[i] not in mapp:
                mapp[s[i]] = t[i]
            else:
                if mapp[s[i]] != t[i]:
                    return False
        return True