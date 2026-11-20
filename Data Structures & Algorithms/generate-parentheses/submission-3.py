class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        temp = []

        def dfs(start,end):
            
            if start == end == n:
                result.append("".join(temp))
                return 
        
            if start < n:
                temp.append('(')
                dfs(start+1,end)
                temp.pop()
            
            if end < start:
                temp.append(')')
                dfs(start,end+1)
                temp.pop()
        
        dfs(0,0)
        return result