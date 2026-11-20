class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_l = 0
        i = 0
        for c in nums:
            if (c-1 in nums):
                continue
            length = 1
            while(c+length in nums):
                length += 1
            max_l = max(length,max_l)
        return max_l