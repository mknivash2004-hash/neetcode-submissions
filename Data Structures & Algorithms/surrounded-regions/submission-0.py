class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        R = len(board)
        C = len(board[0])
        visited = set()

        def dfs(r,c):
            if r < 0 or c < 0 or r >= R or c >= C or (r,c) in visited or board[r][c] != 'O':
                return 
            board[r][c] = 'T'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(R):
            for c in range(C):
                if c == 0 or r == 0 or c == C-1 or r == R - 1:
                    dfs(r,c)
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
