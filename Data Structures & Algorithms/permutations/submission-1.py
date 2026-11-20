class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        temp = []

        def dfs():

            if len(temp) == len(nums):
                result.append(temp.copy())
                return

            
            for x in nums:
                if x not in temp:
                    temp.append(x)
                    dfs()
                    temp.pop()
        
        dfs()
        return result