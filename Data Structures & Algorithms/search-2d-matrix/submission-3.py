class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for x in matrix:
            l , r = 0, len(matrix[0]) - 1
            last_ele = x[-1]
            if target <= last_ele:
                while l <= r:
                    m = (l + r) // 2

                    if target > x[m]:
                        l = m + 1
                    elif target < x[m]:
                        r = m - 1
                    else:
                        return True
            else:
                continue
        return False