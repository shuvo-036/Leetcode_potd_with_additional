from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        chars = [ord(c) - ord('a') for c in s]

        parent = [-1] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        prefix = [0] * n
        timer = 0

        stack = [(0, -1, 0)]

        while stack:
            node, par, state = stack.pop()

            if state == 0:
                parent[node] = par
                tin[node] = timer
                timer += 1

                if par != -1:
                    prefix[node] = prefix[par] ^ (1 << chars[node])
                else:
                    prefix[node] = 1 << chars[node]

                stack.append((node, par, 1))

                for nei in reversed(graph[node]):
                    if nei != par:
                        depth[nei] = depth[node] + 1
                        stack.append((nei, node, 0))
            else:
                tout[node] = timer

        LOG = n.bit_length()
        up = [[-1] * n for _ in range(LOG)]

        for i in range(n):
            up[0][i] = parent[i]

        for j in range(1, LOG):
            for i in range(n):
                p = up[j - 1][i]

                if p != -1:
                    up[j][i] = up[j - 1][p]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for j in range(LOG):
                if diff & (1 << j):
                    u = up[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        class Fenwick:
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 1)

            def update(self, i, val):
                i += 1

                while i <= self.n:
                    self.bit[i] ^= val
                    i += i & -i

            def query(self, i):
                result = 0
                i += 1

                while i > 0:
                    result ^= self.bit[i]
                    i -= i & -i

                return result

            def range_update(self, left, right, val):
                self.update(left, val)

                if right < self.n:
                    self.update(right, val)

        bit = Fenwick(n)
        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = ord(parts[2]) - ord('a')

                delta = (1 << chars[u]) ^ (1 << c)

                bit.range_update(tin[u], tout[u], delta)
                chars[u] = c

            else:
                u = int(parts[1])
                v = int(parts[2])

                w = lca(u, v)

                prefix_u = prefix[u] ^ bit.query(tin[u])
                prefix_v = prefix[v] ^ bit.query(tin[v])

                mask = prefix_u ^ prefix_v ^ (1 << chars[w])

                answer.append((mask & (mask - 1)) == 0)

        return answer
# need solve