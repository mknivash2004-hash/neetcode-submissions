class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        if not word1:
            return word2
        if not word2:
            return word1
        
        p1 = 0
        p2 = 0
        res = ""
        while True:
            if p1 >= len(word1) and p2 >= len(word2):
                return res
            elif p1 < len(word1) and p2 < len(word2):
                res += word1[p1] + word2[p2]
                p1 += 1
                p2 += 1
            elif p1 < len(word1):
                res += word1[p1]
                p1 += 1
            else:
                res += word2[p2]
                p2 += 1
        return res