class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # this is just binary search on 1D matrix
        rows, cols = len(matrix), len(matrix[0])

        # find which row the item sits
        row = 0
        l_row, r_row = 0, rows - 1
        while l_row <= r_row:                    # <= not <, so you don't skip the last candidate
            mid = l_row + (r_row - l_row) // 2
            if matrix[mid][0] <= target:
                row = mid                          # this row is a valid candidate: remember it
                l_row = mid + 1                    # but keep looking right for a possibly better one
            else:
                r_row = mid - 1


        l_col, r_col = 0, cols-1

        while l_col <= r_col:
            mid = l_col + (r_col - l_col) // 2
            val = matrix[row][mid]
            if val == target:
                return True
            elif val < target:
                l_col = mid + 1
            else:
                r_col = mid - 1
        
        return False