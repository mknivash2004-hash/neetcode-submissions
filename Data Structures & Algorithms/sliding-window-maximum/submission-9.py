class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        heap = [] # val, ind
        l = 0
        for r in range(len(nums)):
            heapq.heappush(heap,[-nums[r],r])

            if r-l + 1 >= k:
                while heap[0][1] <= r - k:
                    heapq.heappop(heap)
                    
                result.append(- heap[0][0])
        return result