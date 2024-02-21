class Solution:
    def romanToInt(self, s: str) -> int:
        dict_ = {"I": 1, "V": 5, "X":10, "L":50, "C":100, "D": 500, "M": 1000}
        num = 0
        for i in range(len(s)-1):
            num1 = dict_[s[i]]
            num2 = dict_[s[i+1]]
            if num1 < num2:
                num -= num1
            else:
                num += num1
        num += dict_[s[-1]]
        return num
            