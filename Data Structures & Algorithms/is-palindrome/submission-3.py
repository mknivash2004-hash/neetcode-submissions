class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s1 = ""
        for i in s:
            if not (ord('a') <= ord(i) <= ord('z')) and not (ord('0') <= ord(i) <= ord('9')):
                continue
            s1 += i

        l = 0
        r = len(s1) - 1
        while l < r:
            if s1[l] != s1[r]:
                return False
            l += 1
            r -= 1
        return True