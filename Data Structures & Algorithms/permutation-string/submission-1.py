class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if not s1:
            return True

        count1 = {}
        for ch in s1:
            count1[ch] = 1 + count1.get(ch, 0)
        need = len(count1)  # distinct characters to fully match

        for i in range(len(s2)):
            count2 = {}
            tracker = 0
            for j in range(i, len(s2)):
                ch = s2[j]
                count2[ch] = 1 + count2.get(ch, 0)
                if count1.get(ch, 0) < count2[ch]:
                    break
                if count1[ch] == count2[ch]:
                    tracker += 1
                if tracker == need:
                    return True

        return False