class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        result = []
        pac = set()
        atl = set()

        # start from the sides perform dfs or bfs and move in all directions to see if it can reach the ocean 
        R = len(heights)
        C = len(heights[0])


        def dfs(r,c, st,prevHeight):

            if r < 0 or c < 0 or r>= R or c >= C or (r,c) in st or heights[r][c] < prevHeight:
                return 
            st.add((r,c))
            dfs(r+1,c,st,heights[r][c])
            dfs(r-1,c,st,heights[r][c])
            dfs(r,c+1,st,heights[r][c])
            dfs(r,c-1,st,heights[r][c])

        
        for r in range(R):
            for c in range(C):
                if r == 0 :
                    dfs(r,c,pac,heights[r][c])
                if r == R - 1:
                    dfs(r,c,atl,heights[r][c])
        
        for r in range(R):
            for c in range(C):
                if c == 0 :
                    dfs(r,c,pac,heights[r][c])
                if c == C - 1:
                    dfs(r,c,atl,heights[r][c])
        
        for r in range(R):
            for c in range(C):
                if (r,c) in pac and (r,c) in atl:
                    result.append([r,c])
        return result
 

