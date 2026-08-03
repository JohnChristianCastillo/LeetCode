class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board = board
        def row_check():
            for row in self.board:
                row = [r for r in row if r != '.']
                row_set = set(row)
                if len(row) != len(row_set):
                    return False
            return True

        def col_check():
            grid = zip(*self.board)
            for col in grid:
                col = [c for c in col if c != '.']
                col_set = set(col)
                if len(col) != len(col_set):
                    return False
            return True

        # TODO: FOCUS ON THIS
        def square_check(row_offset, col_offset):
            seen = set()
            for i in range(row_offset, row_offset+3):
                for j in range(col_offset, col_offset+3):
                    val = board[i][j]
                    if val != '.':
                        if val in seen:
                            return False
                        seen.add(val)
            return True

        for r in [0, 3, 6]:
            for c in [0, 3, 6]:
                if not square_check(r, c):
                    return False
        
        return row_check() and col_check()
            

