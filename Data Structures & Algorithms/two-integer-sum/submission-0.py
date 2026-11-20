class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsh = {}
        for i in range(len(nums)):
            if (target-nums[i] not in hsh):
                hsh[nums[i]] = i
            else:
                return [hsh[target-nums[i]],i]