class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        # 1. make an adj list so we can easily traverse the graph
        self.adj_list = defaultdict(list)
        for src, dst in connections:
            self.adj_list[src].append((dst, 1)) # path is valid
            self.adj_list[dst].append((src, 0))

        # 2. DFS through adj_list and count how many edges we need to flip
        self.visited = set()
        self.flipped_edges = 0
        def dfs(city):
            self.visited.add(city)
            for neighbor, weight in self.adj_list[city]:
                if neighbor not in self.visited: # we dont want to keep visiting an already visited city
                    self.flipped_edges += weight
                    dfs(neighbor)
            return self.flipped_edges

        return dfs(0)