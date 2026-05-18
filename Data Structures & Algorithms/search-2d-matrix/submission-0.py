class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])

        left, right = 0, (rows * columns) -1 
        
        while left  <= right :
            pivot_index  =  ( left + right ) //2 
            pivot_element = matrix[pivot_index//columns][pivot_index % columns]

            if pivot_element < target :
                left = pivot_index + 1 
            elif pivot_element > target:
                right = pivot_index -1 
            else:
                return True 
            
        return False


        