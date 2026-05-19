class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        Observation:
        1. the equations are node transitions going from A->B where the edge is the result of A/B

        Idea:
        1. Construct an adjacency list S.T. A->B is mapped, but also B->A
        2. Have a parameters list so we know before we run the dfs if it's even possible to find the equation 
        3. Run a dfs for each query that returns the answer
        """

        adj = defaultdict(list)
        valid_params = set()
        for i in range(len(equations)):
            numerator, denominator = equations[i][0], equations[i][1]
            res = values[i]

            valid_params.add(numerator)
            valid_params.add(denominator)

            adj[numerator].append([denominator, res])
            adj[denominator].append([numerator, 1.0/res])

        def dfs(src, dst, curr_prod, visited = set()):
            if src == dst:
                return curr_prod
            visited.add(src)
            for neighbor, val in adj[src]:
                if neighbor not in visited:
                    res = dfs(neighbor, dst, val*curr_prod, visited)
                    if res != -1:
                        return res
            
            return -1

        result = []

        for query in queries:
            src, dst = query[0], query[1]
            if src in valid_params and dst in valid_params:
                result.append(dfs(src, dst, 1, set()))
            else:
                result.append(-1)

        return result