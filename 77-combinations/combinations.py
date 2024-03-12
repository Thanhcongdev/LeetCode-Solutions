class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(i,temp):
            if i>n:
                if len(temp)==k:
                    ans.append(temp.copy())
                return
            temp.append(i)
            backtrack(i+1,temp)
            temp.pop()
            backtrack(i+1,temp)
        ans=[]
        backtrack(1,[])
        return ans