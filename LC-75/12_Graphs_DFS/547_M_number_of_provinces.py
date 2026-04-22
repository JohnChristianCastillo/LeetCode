class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        
        """
        idea
        use DFS! 

        keep track of 
            1. visited cities (set)
            2. amount of provinces seen (counter)

        Basically:
        use DFS on EVERY city, everytime we step out of that DFS it means a new province is being searched
        DFS stopping means no more neighbors
        
        """
        self.visit = set()
        self.seen_count = 0
        
        def dfs(city_id):
            self.visit.add(city_id)
            neighbors = isConnected[city_id]
            for neighbor_id in range(len(neighbors)):
                # first check if neighbor has already been visited
                if neighbor_id not in self.visit:
                    # if it's not then AND we're connected we dfs through that neighbor
                    if neighbors[neighbor_id] == 1:
                        dfs(neighbor_id)

        for city_id in range(len(isConnected)):
            if city_id not in self.visit:
                self.seen_count += 1  # only increase the counter when we're visiting a new cluster
                dfs(city_id)
        
        return self.seen_count