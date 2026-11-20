class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        # analogy count the number of split based on sum of sub array. If the split exceeds then the sum needs to be increased else sum needs to be decreased. 

        l = max(nums)
        r = sum(nums)

        def helper(val):
            sums = 0
            split = 1
            for n in nums:
                sums += n
                if sums > val:
                    sums = n
                    split += 1
            return split <= k
        
        while l<= r:
            mid = l + (r-l)//2
            if helper(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res