class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPallindrome(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        l = 0
        r = len(s)-1
        while l < r:
            if s[l] != s[r]:
                return (isPallindrome(l+1,r) or isPallindrome(l,r-1))
            l += 1
            r -= 1
        return True
