class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        count2 = {}
        if len(s) != len(t):
            return False
        
        for i in s:
            count1[i] = 1+ count1.get(i,0)
        for i in t:
            count2[i] = 1+count2.get(i,0)
        
        return count1 == count2