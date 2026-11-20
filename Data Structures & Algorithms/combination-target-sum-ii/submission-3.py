class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        lst = []
        res = []
        candidates.sort()

        def dfs(i,total):
            if total == target:
                res.append(lst.copy())
                return
            if total > target or i >= len(candidates):
                return
            
            lst.append(candidates[i])
            dfs(i+1,total+candidates[i])
            lst.pop()
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1,total)
        dfs(0,0)
        return res