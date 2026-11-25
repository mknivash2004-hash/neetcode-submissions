class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur = 0
        hsh = {0:1}

        for n in nums:

            cur += n
            if cur-k in hsh:
                res += hsh[cur-k]
            hsh[cur] = 1+hsh.get(cur,0)
        return res