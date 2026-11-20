class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        temp = []

        def dfs(k):
            if k >= len(nums):
                result.append(temp.copy())
                return
                
            temp.append(nums[k])
            dfs(k+1)
            while k + 1 < len(nums) and nums[k] == nums[k+1]:
                k += 1
            temp.pop()
            dfs(k+1)
        
        dfs(0)
        return result