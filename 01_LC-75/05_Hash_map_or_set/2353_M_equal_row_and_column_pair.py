class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # use map[tuple(rows or cols)] = [[count_rows][count_cols]]
        mp = defaultdict()
        # gather rows
        for row in grid:
            temp = tuple(row)
            if temp in mp:
                mp[temp][0] += 1
            else:
                mp[temp] = [1, 0]
        # gather cols
        for col in range(len(grid[0])):
            temp = []
            for row in range(len(grid)):
                temp.append(grid[row][col])
            temp = tuple(temp)
            if temp in mp:
                mp[temp][1] += 1
            else:
                mp[temp] = [0, 1]
        # calculate:
        # if we have an entry in the map that is greater than 1
        # we then perform the combination calculation:
        # which is just combs += mp[key][0]*mp[key][1]
        total_combs = 0
        for key in mp:
            total_combs += mp[key][0]*mp[key][1]
        return total_combs
