class Solution:
    def binary_search(self, arr, target):
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l+r) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l+r)//2
            if matrix[mid][-1] >= target >= matrix[mid][0]:
                return self.binary_search(matrix[mid], target)
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                r =  mid - 1
        return False