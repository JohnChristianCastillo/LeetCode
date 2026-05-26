class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        use 3 lists of sets (9 each):
        1. rows: 9 sets, 1 for each row
        2. cols: same
        3. grids: 
        --> GRID ID CALCULATION VERY IMPORTANT
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                # we're only interested in checking non '.'
                if val != '.':
                    # we then want to check if val is already seen
                    # in each of the 3 lists of set we have, if so 
                    # return false
                    """
                    calculating grid index we're in: (//: floor of division)
            grid id:  0      1      2    =        (row // 3 * 3) + col // 3 
                    X X X  X X X  X X X  grid 0 = (0 // 3 * 3)   + (0 // 3) = 0
                    X X X  X X X  X X X  grid 1 = (1 // 3 * 3)   + (3 // 3) = 1 
                    X X X  X X X  X X X  grid 2 = (2 // 3 * 3)   + (6 // 3) = 2
                    --3------4------5--
                    X X X  X X X  X X X  grid 3 = (3 // 3 * 3)   + (0 // 3) = 3
                    X X X  X X X  X X X              = 1 * 3     +    0
                    X X X  X X X  X X X
                    --6------7------8--
                    X X X  X X X  X X X  grid 7 = (6 // 3 * 3)   + (3 // 3) = 
                    X X X  X X X  X X X         =     2*3        + 1        = 7
                    X X X  X X X  X X X
                    -------------------
                    """
                    grid_id = (row // 3 * 3) + col // 3
                    if val in rows[row] or val in cols[col] or val in grids[grid_id]:
                        return False
                    else:
                        rows[row].add(val)
                        cols[col].add(val)
                        grids[grid_id].add(val)

        return True