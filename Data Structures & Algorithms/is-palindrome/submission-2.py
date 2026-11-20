class Solution:
    def isPalindrome(self, s: str) -> bool:
        char = ""
        for i in s:
            if i.isalnum():
                char += i
        char = char.lower()
        l , r = 0, len(char)-1
        while(l<=r):
            if char[l] != char[r]:
                return False
            l += 1
            r -= 1
        return True