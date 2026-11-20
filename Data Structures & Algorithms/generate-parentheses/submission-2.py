class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lst = []
        res = []
        def backtrack(op,cl):
            if op==cl==n:
                res.append("".join(lst))
                return 
        
            if op<n:
                lst.append("(")
                backtrack(op+1,cl)
                lst.pop()
            if cl<op:
                lst.append(")")
                backtrack(op,cl+1)
                lst.pop()
        backtrack(0,0)
        return res