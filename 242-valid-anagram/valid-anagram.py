class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)
        print(counter_s, counter_t)
        if counter_s == counter_t:
            return True
        return False