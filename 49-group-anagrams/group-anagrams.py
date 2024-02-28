class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        ans = []

        for s in strs:
            sorted_s = ''.join(sorted(s)) 
            if sorted_s in mapping:
                ans[mapping[sorted_s]].append(s)
            else:
                mapping[sorted_s] = len(ans)
                ans.append([s])
        return ans