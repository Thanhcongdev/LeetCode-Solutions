class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        neg, pos, zeros = [], [], []
        for n in nums:
            neg.append(n) if n < 0 else pos.append(n) if n > 0 else zeros.append(0)
        # > 3 zero
        if len(zeros) >= 3:
            ans.add((0,0,0))
        # at least 1 zero
        set_n = set(neg)
        set_p = set(pos)
        if len(zeros) >= 1:      
            for n in set_n:
                if -n in set_p:
                    ans.add((n, -n, 0))
        # other
        for i in range(len(neg)):
            for j in range(i + 1, len(neg)):
                target = -neg[i] - neg[j]
                if target in set_p:
                    ans.add(tuple(sorted((neg[i], neg[j], target))))
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                target = -pos[i] - pos[j]
                if target in set_n:
                    ans.add(tuple(sorted((pos[i], pos[j], target))))
        return ans