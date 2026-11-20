class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxA = 0
        R = len(grid)
        C = len(grid[0])
        
        def bfs(r,c):
            grid[r][c] = 0
            q = deque()
            q.append((r,c))
            area = 1
            paths = [[0,1],[0,-1],[1,0],[-1,0]]
            while q :
                row , col = q.popleft()
                for rd, cd in paths:
                    cr,cc = rd+row, col+cd
                    if 0 <= cr < R and 0 <= cc < C and grid[cr][cc] == 1:
                        grid[cr][cc] = 0
                        q.append((cr,cc))
                        area += 1
            return area

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    maxA = max(maxA,bfs(r,c))
        return maxA