class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        arr = []
        n = len(number)
        for i in range(n-1):
          if number[i] == digit:
            last = i
            a = int(number[i])
            b = int(number[i + 1])
            if a < b:
              return number[:i] + number[i+1:] 
        if number[-1] == digit:
          last = n - 1
        return number[:last] + number[last+1:] 