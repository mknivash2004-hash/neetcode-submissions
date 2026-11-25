class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        counter = {}
        for n in nums:
            counter[n] = 1+counter.get(n,0)
            if len(counter) <= 2:
                continue
            new_counter = {}
            for val in counter.keys():
                if counter[val] > 1:
                    new_counter[val] = counter[val] - 1
            counter = new_counter

        for num in counter.keys():
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        return res
