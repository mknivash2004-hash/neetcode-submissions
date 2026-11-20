class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        r = 0
        for l in range(len(min(strs[0],strs[-1]))):
            if strs[0][l] != strs[-1][l]:
                return strs[0][:l]
        return strs[0]