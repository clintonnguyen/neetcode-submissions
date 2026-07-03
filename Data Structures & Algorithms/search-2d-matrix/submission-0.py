class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix[0][0] > target or matrix [-1][-1] < target:
            return False
        for row in matrix:
            if target >= row[0] and target <= row[-1]:
                for col in row:
                    if col == target:
                        return True
                return False
            else:
                continue
        return False