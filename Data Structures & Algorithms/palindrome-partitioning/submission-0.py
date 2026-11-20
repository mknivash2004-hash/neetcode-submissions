class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        lst = []

        def dfs(i):
            if i >= len(s):
                res.append(lst.copy())
                return
            
            for j in range(i,len(s)):
                if self.isPali(s,i,j):
                    lst.append(s[i:j+1])
                    dfs(j+1)
                    lst.pop()
        dfs(0)
        return res


    def isPali(self,s,l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    