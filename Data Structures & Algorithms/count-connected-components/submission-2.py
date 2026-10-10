class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        components = 0
        visited = set()

        def dfs(node):
            if adjList[node] == [] or node in visited:
                return
            visited.add(node)
            for nei in adjList[node]:
                dfs(nei)

        for node in range(n):
            if node in visited:
                continue
            components += 1
            dfs(node)
        
        return components