'''
Time Complexity: O(m+n), where m is rows and n is columns
Space Complexity: O(1)
Successfully Executed: Yes
Challenges Faces: No
'''


#CODE
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == [] or len(matrix) == 0:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        i = 0
        j = n-1
        
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif target > matrix[i][j]:
                i += 1
            else:
                j -= 1
        return False
        