class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        stk = []
        for i in range(len(position)):
            pair.append([position[i],speed[i]])
        pair.sort()
        pair = pair[::-1]
        
        for pos, spe in pair:
            stk.append((target - pos)/spe)
            if len(stk) >= 2 and stk[-1] <= stk[-2]:
                stk.pop()
        return len(stk)