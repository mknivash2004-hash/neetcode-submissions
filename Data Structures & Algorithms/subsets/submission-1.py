class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        lst = []
        def dfs(i):
            if i >= len(nums):
                res.append(lst.copy())
                return 
            lst.append(nums[i])
            dfs(i+1)
            lst.pop()
            dfs(i+1)
        dfs(0)
        return res