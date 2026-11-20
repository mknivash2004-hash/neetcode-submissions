class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        low = len(matrix) - 1

        while top <= low:
            mid = (top+low)//2
            if matrix[mid][0] > target:
                low = mid-1
            elif matrix[mid][-1] < target:
                top = mid+1
            else:
                break
        
        l = 0
        r = len(matrix[mid]) -1
        while l<=r:
            m = (l+r)//2
            if matrix[mid][m] < target:
                l = m+1
            elif matrix[mid][m] > target:
                r = m - 1
            else:
                return True
        return False