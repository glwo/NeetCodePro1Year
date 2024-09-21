class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                targetMatrix = matrix[mid]
                break
        else:
            return False

        s = 0
        b = len(targetMatrix) - 1
        while s <= b:
            midPoint = (s + b) // 2
            if targetMatrix[midPoint] > target:
                b = midPoint - 1
            elif targetMatrix[midPoint] < target:
                s = midPoint + 1
            else:
                return True

        return False
