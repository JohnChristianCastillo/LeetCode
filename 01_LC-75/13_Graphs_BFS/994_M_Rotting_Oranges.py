class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        idea: to simulate the elapsing minutes, we need a queue that simulates going from t = x to t = x+1
        so: gather all rotting oranges first, then propagate the rot each time
        each iteration compare if the rotten oranges == total oranges
        """
        rows,cols = len(grid), len(grid[0])
        fresh = 0
        rotten = []
        seen = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten.append([r,c])
                    seen.add((r,c))
        if not fresh:
            return 0
        q = deque()
        q.append([rotten, 0])

        while q:
            curr_layer, steps = q.popleft()

            # propagate rot
            for coords in curr_layer:
                x,y = coords
                dirs = [
                    [x+1, y],
                    [x-1, y],
                    [x, y+1],
                    [x, y-1]
                ]
                # filter out: out of bounds, seen, empty cell
                valid_neighbors = []
                for dx, dy in dirs:
                    if (dx,dy) not in seen and dx >= 0 and dx < rows and dy >= 0 and dy < cols and grid[dx][dy] == 1:
                        seen.add((dx,dy))
                        fresh -= 1
                        if fresh == 0:
                            return steps+1
                        valid_neighbors.append([dx,dy])
                if valid_neighbors:
                    q.append([valid_neighbors, steps+1])
        return -1
