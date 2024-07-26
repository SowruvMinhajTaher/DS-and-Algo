class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        distance = [[float('inf')] * n for _ in range(n)] # Initialize distance matrix with infinity

        for i in range(n):
            distance[i][i] = 0 # Distance to itself is 0

        for edge in edges:
            distance[edge[0]][edge[1]] = edge[2]
            distance[edge[1]][edge[0]] = edge[2]

        # Floyd-Warshall algorithm to find all-pairs shortest path
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

        ans = -1
        mini = float('inf')
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and distance[i][j] <= distanceThreshold:
                    count += 1
            if count <= mini:
                mini = count
                ans = i

        return ans