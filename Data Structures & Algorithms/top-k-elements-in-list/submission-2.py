class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1+count.get(n,0)
        
        res = []
        
        for i,j in count.items():
            res.append([j,i])
        res.sort()
        final = []
        for i in range(k):
            final.append(res.pop()[1])
        return final 