class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()
        count = 0
        R = len(grid)
        C = len(grid[0])

        def bfs(r,c):
            que = deque()
            que.append((r,c))
            visited.add((r,c))
            while que:
                row,col = que.popleft()
                for dr,dc in directions:
                    nr,nc = row+dr, col+dc
                    if nr in range(R) and nc in range(C) and (nr,nc) not in visited and grid[nr][nc]=='1':
                        que.append((nr,nc))
                        visited.add((nr,nc))
                    

        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    count += 1
        return count