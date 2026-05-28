class Solution:
    def binary_search(self, arr, target):
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l+r) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                r -= 1
            else:
                l += 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l+r)//2
            if matrix[mid][-1] > target and matrix[mid][0] > target:
                r -= 1
            elif matrix[mid][-1] < target and matrix[mid][0] < target:
                l += 1
            else:
                return self.binary_search(matrix[mid], target)
        return False