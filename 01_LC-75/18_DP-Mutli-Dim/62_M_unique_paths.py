class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        IDEA:
            have a 2 dimentional grid representing amount of ways to get to grid[i][j]
            HOW to initialize grid?
                Question to ask: How many ways can I get to the tile I am currently in?
                        -> since only way to get to current tile is from top and left
                            we can just sum the top tile and left tile of the current tile
                1. let's start from top row:
                    so:
                    3x7
                    [ ][1][1][1][1][1][1]
                    [ ][ ][ ][ ][ ][ ][ ]
                    [ ][ ][ ][ ][ ][ ][F]

                    since top row tiles does not have another row on top, they can only be traversed
                    from the left --> only 1 way to get to them
                2. what about the 1st column?
                    same:
                    [ ][1][1][1][1][1][1]
                    [1][ ][ ][ ][ ][ ][ ]
                    [1][ ][ ][ ][ ][ ][F]

            After having the grid initialized we can now propagate: to reach grid[1][1]
            we can sum: grid[0][1] + grid[1][0] = 1 + 1 = 2
                [ ][1][1][1][1][1][1]     
                [1][2][ ][ ][ ][ ][ ]       what about the one right of it?
                [1][ ][ ][ ][ ][ ][F]

                grid[1][2] = grid[0][2] + grid[1][1] = 1 + 2 = 3
                [ ][1][1][1][1][1][1]     
                [1][2][3][ ][ ][ ][ ]       what about the one right of it?
                [1][ ][ ][ ][ ][ ][F]
            ==> 
                [ ][1][1][1 ][1 ][1 ][1]     
                [1][2][3][4 ][5 ][6 ][7]       what about the one right of it?
                [1][3][6][10][15][21][F] ==> F = 21 + 7 = 28

        ALGO: 
            1. init 1st row and 1st col to 1
            2. fill their adjacent tiles
            3. return the last element of the grid = F = grid[m-1][n-1]
        """
        # 1. initialize 1st row and 1st col to 1, we can just init all to 1 since we will just overwrite other tiles
        grid = []
        for row in range(m):
            grid.append([1]*n)

        # 2. propagate from grid[1][1]
        for row in range(1, m):
            for col in range(1, n):
                top = grid[row-1][col]
                left = grid[row][col-1]
                grid[row][col] = top + left
        # 3. return last element of grid = # ways to get to last element
        return grid[m-1][n-1]
        