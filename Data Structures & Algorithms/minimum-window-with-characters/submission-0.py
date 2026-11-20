class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count1 = {}
        for c in t:
            count1[c] = count1.get(c, 0) + 1

        need = len(count1)
        count2 = {}
        have = 0
        l = 0
        ls = 0
        shortest = float('inf')

        for r in range(len(s)):
            count2[s[r]] = count2.get(s[r], 0) + 1
            if count2[s[r]] == count1.get(s[r], 0):
                have += 1

            while have == need:
                if shortest > r - l + 1:
                    shortest = r - l + 1
                    ls = l

                count2[s[l]] -= 1
                if count2[s[l]] < count1.get(s[l], 0):
                    have -= 1

                l += 1

        return "" if shortest == float('inf') else s[ls:ls + shortest]