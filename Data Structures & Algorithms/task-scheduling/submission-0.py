class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-i for i in counts.values()]
        heapq.heapify(heap)

        time = 0
        q = deque()

        while heap or q:
            time += 1
            
            if heap:
                cyc = heapq.heappop(heap)
                cyc += 1
                if cyc:
                    q.append([cyc,time+n])
            if q and q[0][1] == time:
                heapq.heappush(heap,q.popleft()[0])
        return time