class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]

        for u, v, wt in edges:
            adj[u].append((v, wt))

        result = [[float('inf')] * (k + 1) for _ in range(n)]

        pq = []

        result[0][1] = 0
        heapq.heappush(pq, (0, 0, 1))

        while pq:
            d, node, count = heapq.heappop(pq)

            if d > result[node][count]:
                continue

            if node == n - 1:
                return d

            for adjNode, wt in adj[node]:
                if labels[adjNode] == labels[node]:
                    newCount = count + 1
                else:
                    newCount = 1

                if newCount > k:
                    continue

                newDist = d + wt

                if newDist < result[adjNode][newCount]:
                    result[adjNode][newCount] = newDist
                    heapq.heappush(pq, (newDist, adjNode, newCount))

        return -1

        