from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def can_load(cap):
            used, load = 1, 0
            for w in weights:
                if load + w > cap:       # strictly greater: equal still fits
                    used += 1
                    load = 0
                load += w
            return used <= days

        l, r = max(weights), sum(weights)
        res = r
        while l <= r:
            m = l + (r - l) // 2         # always low + half the width
            if can_load(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res