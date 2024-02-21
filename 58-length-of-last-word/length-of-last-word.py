class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        last_word = s[s.rfind(' ') + 1:]
        return len(last_word)