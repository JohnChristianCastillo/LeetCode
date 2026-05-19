class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
        Idea:
            BFS each "layer" | layer = 4 positions from current position
        """
        rows, cols = len(maze), len(maze[0])
        q = deque([[entrance[0], entrance[1], 0]])

        visit = set(tuple(entrance))
        while q:
            curr = q.popleft()
            pos_x, pos_y, steps = curr

            # check if this is a valid solution. 
            # if so then we know this is the best(shortest) solution since we're using BFS
            if (pos_x == 0 or pos_y == 0 or pos_x == rows - 1 or pos_y == cols - 1) and [pos_x, pos_y] != entrance:
                return steps
            
            neighbors = [
                [pos_x, pos_y+1],
                [pos_x, pos_y-1],
                [pos_x-1, pos_y],
                [pos_x+1, pos_y]
            ]
            # filter out walls and visited
            for x,y in neighbors:
                # make sure the coords does not exist outside the maze
                if x < rows and y < cols and x >= 0 and y >= 0:
                    # make sure we havent visited this, nor is it a wall
                    if (x, y) not in visit and maze[x][y] != '+':
                        # add this position to visited
                        visit.add((x,y))
                        q.append([x,y,steps+1])

        return -1 # if we reach the end of the function it means no solution has been found