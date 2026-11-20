class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        lst = []
        result = []

        def dfs(k):

            if k >= len(nums):
                result.append(lst.copy())
                return 
            
            for i in range(len(nums)):
                if nums[i] not in lst:
                    lst.append(nums[i])
                    dfs(k+1)
                    lst.pop()
        dfs(0)
        return result
