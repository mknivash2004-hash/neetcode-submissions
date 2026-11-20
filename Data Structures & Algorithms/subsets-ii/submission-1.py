class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        lst = []
        res = []
        nums.sort()
        def dfs(i):
            if i >= len(nums):
                res.append(lst.copy())
                return
            lst.append(nums[i])
            dfs(i+1)
            lst.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)
        dfs(0)
        return res