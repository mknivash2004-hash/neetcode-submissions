class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        if not word1:
            return word2
        if not word2:
            return word1
        
        res = ""
        for i in range(max(len(word1),len(word2))):
            if i < len(word1):
                res += word1[i]
            if i < len(word2):
                res += word2[i]
        return res