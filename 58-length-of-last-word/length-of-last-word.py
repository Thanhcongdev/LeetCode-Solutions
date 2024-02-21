class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        pos = 0
        for i, ch in enumerate(s[::-1]):
            if ch == " ":
                pos = i
                break
        if pos == 0:
            return len(s)
        return pos 
            
                