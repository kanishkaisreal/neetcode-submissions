class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                
                # Skip empty cells
                if cell == '.':
                    continue
                
                # Check if digit already seen in row, column, or box
                box_i, box_j = i // 3, j // 3
                
                if cell in rows[i] or cell in cols[j] or cell in boxes[box_i][box_j]:
                    return False
                
                else: 
                # Add digit to all three constraint sets
                    rows[i].add(cell)
                    cols[j].add(cell)
                    boxes[box_i][box_j].add(cell)
        
        return True