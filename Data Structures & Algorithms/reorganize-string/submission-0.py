class Solution:
    def reorganizeString(self, s: str) -> str:
        if s == "":
            return ""

        counts = Counter(s)
        heap = [[-cnt, char] for char, cnt in counts.items()]
        heapq.heapify(heap)

        result = ""
        prev = []
        while heap or prev:
            if not heap:
                return ""

            c,s = heapq.heappop(heap)
            result += s
            c += 1
            if prev:
                heapq.heappush(heap,prev)
                prev = None
            if c < 0:
                prev = [c,s]

        return result
