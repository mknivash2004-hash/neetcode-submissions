class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        temp = []
        used = [False]*len(nums)

        def dfs():
            
            if len(temp) == len(nums):
                result.append(temp.copy())
                return 
            
            for i in range(len(nums)):
                
                if used[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                

                used[i] = True
                temp.append(nums[i])
                dfs()
                temp.pop()
                used[i] = False
        
        dfs()
        return result

