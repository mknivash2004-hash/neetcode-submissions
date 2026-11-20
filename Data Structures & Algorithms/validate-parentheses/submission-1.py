class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for i in s:
            if i in closeToOpen:
                if stk and stk[-1] == closeToOpen[i]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(i)
        return len(stk) == 0