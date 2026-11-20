class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        R = len(grid)
        C = len(grid[0])
        q = deque()
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r,c))
                
        time = 0

        def addQ(r,c):
            if r < 0 or r >= R or c < 0 or c >= C or (r,c) in visited or grid[r][c] != 1:
                return 
            grid[r][c] = 2
            q.append((r,c))
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                addQ(r+1,c)
                addQ(r,c+1)
                addQ(r-1,c)
                addQ(r,c-1)
            time += 1
        for row in grid:
            if 1 in row:
                return -1
        return max(time-1,0)