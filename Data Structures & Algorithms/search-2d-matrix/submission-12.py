from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:                 # fix 4
            return False

        lr, rr = 0, len(matrix) - 1                     # fix 1
        while lr <= rr:
            mr = lr + (rr - lr) // 2                    # fix 2
            if target < matrix[mr][0]:
                rr = mr - 1
            elif target > matrix[mr][-1]:
                lr = mr + 1
            else:
                break
        else:
            return False

        l, r = 0, len(matrix[mr]) - 1
        # fix 3: no reassignment of mr here
        while l <= r:
            m = l + (r - l) // 2
            if target < matrix[mr][m]:
                r = m - 1
            elif target > matrix[mr][m]:
                l = m + 1
            else:
                return True
        return False