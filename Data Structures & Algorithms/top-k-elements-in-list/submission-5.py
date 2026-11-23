class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # bucket sort solution: have a array size of len of list within that array elements are lists or int. for every count add the element to array within array in that index and return from the last index

        res = []
        hsh = {}
        
        for n in nums:
            hsh[n] = 1+hsh.get(n,0)
        
        counter = [[] for i in range(len(nums))]
        for val,ind in hsh.items():
            counter[ind-1].append(val)

        for i in range(len(counter)-1,-1,-1):
            for n in counter[i]:
                res.append(n)
            if len(res) == k:
                return res
        return res