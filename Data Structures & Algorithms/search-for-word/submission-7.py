class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        st = set()
        def dfs(r,c,i):
            if len(word) == i:
                return True
            if (c < 0 or r < 0 or r >= R or c >= C or (r,c) in st or board[r][c] != word[i]):
                return False
            st.add((r,c))
            res = (dfs(r-1,c,i+1) or dfs(r+1,c,i+1)or dfs(r,c-1,i+1) or dfs(r,c+1,i+1))
            st.remove((r,c))
            return res
        for i in range(R):
            for c in range(C):
                if dfs(i,c,0):
                    return True
        return False
        
        