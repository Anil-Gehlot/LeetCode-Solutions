class Solution:
    
    # binary search method
    def binarySearch(self, arr, target):
        
        i = 0
        j = len(arr) - 1
        
        while i <= j:
            mid = (i + j) // 2
            if arr[mid] == target:
                return True
            if arr[mid] > target:
                j = mid - 1
            if arr[mid] < target:
                i = mid + 1
                
        return False

    def searchMatrix(self, matrix, target):
        
        # Iterate through each row in the matrix
        for arr in matrix:
            
            # Check if target is either the first or last element in the current row
            if arr[0] == target or arr[-1] == target:
                return True
            
            # Check if target lies within the range of values in the current row
            elif target > arr[0] and target < arr[-1]:
                
                # If yes, perform binary search in the current row
                result = self.binarySearch(arr, target)
                if result:
                    return True
                
        return False
