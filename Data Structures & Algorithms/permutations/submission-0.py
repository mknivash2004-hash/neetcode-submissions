from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        for p in permutations(nums):
            res.append(list(p))
        return res