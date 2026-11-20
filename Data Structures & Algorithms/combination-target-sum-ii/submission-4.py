class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        temp = []
        candidates.sort()
        def dfs(k):
            
            if sum(temp) == target:
                result.append(temp.copy())
                return
            
            if sum(temp) > target or k >= len(candidates):
                return
            
            temp.append(candidates[k])
            dfs(k+1)
            temp.pop()
            while k + 1 < len(candidates) and candidates[k] == candidates[k+1]:
                k += 1
            dfs(k+1)
        
        dfs(0)
        return result