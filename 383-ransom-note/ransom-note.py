class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        st1, st2 = Counter(ransomNote), Counter(magazine)
        for letter in st1:
            if st1[letter] > st2[letter]:
                return False
        return True