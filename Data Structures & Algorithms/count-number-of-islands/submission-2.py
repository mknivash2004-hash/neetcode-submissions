class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        R = len(grid)
        C = len(grid[0])
        visited = set()
        
        def bfs(r,c):
            paths = [[0,1],[0,-1],[1,0],[-1,0]]
            q = collections.deque()
            grid[r][c] = '0'
            q.append((r,c))
            while q:
                rw, cw = q.popleft()
                for rv,cv in paths:
                    cr,cc = rw + rv, cw + cv
                    if 0 <= cr < R and 0 <= cc < C and grid[cr][cc] == '1':
                        grid[cr][cc] = '0'
                        q.append((cr,cc))

        
        for r in range(R):
            for c in range(C):

                if (r,c) not in visited and grid[r][c] == '1':
                    bfs(r,c)
                    visited.add((r,c))
                    count += 1
        return count
                