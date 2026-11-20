class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = []
        def backtracking(k):

            if k >= len(nums):
                result.append(temp.copy())
                return
            
            temp.append(nums[k])
            backtracking(k+1)
            temp.pop()
            backtracking(k+1)
        
        backtracking(0)
        return result