class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:
            res += str(len(s))+"#"+s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            de = s.find("#",i)
            length = int(s[i:de])
            st = de+1
            e = st + length
            res.append(s[st:e])
            i = e
        return res
