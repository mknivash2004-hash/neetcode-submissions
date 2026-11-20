class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        R = len(grid)
        C = len(grid[0])
        visited = set()
        max_area = 0
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(r,c):
            que = deque()
            que.append((r,c))
            visited.add((r,c))
            area = 1
            while que:
                row,col = que.popleft()
                for dr,dc in direction:
                    nr,nc = row+dr,col+dc
                    if nr in range(R) and nc in range(C) and grid[nr][nc] == 1 and (nr,nc) not in visited:
                        que.append((nr,nc))
                        visited.add((nr,nc))
                        area += 1
            return area

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = dfs(r,c)
                    max_area = max(max_area,area)
        return max_area