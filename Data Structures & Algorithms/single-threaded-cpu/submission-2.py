import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        jobs = sorted((enq, dur, idx) for idx, (enq, dur) in enumerate(tasks))
        res, heap = [], []
        time, i = 0, 0

        while i < len(jobs) or heap:
            if not heap:
                time = max(time, jobs[i][0])          # idle: jump to next arrival

            while i < len(jobs) and jobs[i][0] <= time:
                heapq.heappush(heap, (jobs[i][1], jobs[i][2]))   # (duration, original index)
                i += 1

            dur, idx = heapq.heappop(heap)
            time += dur
            res.append(idx)
        return res