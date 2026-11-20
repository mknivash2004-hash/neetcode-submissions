class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i,t in enumerate(tasks):
            t.append(i)
        
        tasks.sort(key = lambda x:x[0])
        result = []
        time = tasks[0][0]
        i = 0
        heap = []
        while heap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(heap,[tasks[i][1],tasks[i][2]])
                i += 1
            if not heap:
                time = tasks[i][0]

            else:
                t,ind=heapq.heappop(heap)
                result.append(ind)
                time += t
        return result

