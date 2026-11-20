class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []
        temp = []

        def dfs(k):

            if sum(temp) == target:
                result.append(temp.copy())
                return

            if sum(temp) > target or k >= len(nums):
                return
            
            temp.append(nums[k])
            dfs(k)
            temp.pop()
            dfs(k+1)
        
        dfs(0)
        return result