class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l ,r = 0,0
        res = 0
        counts = {}
        for r in range(len(s)):
            if s[r] in counts:
                l = max(counts[s[r]]+1,l)
            counts[s[r]] = r
            res = max(r-l+1,res)
        return res