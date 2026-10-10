class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Valid tree if connected and exactly V-1 edges
        if len(edges) == 0:
            return True
        if len(edges) != n - 1:
            return False
        
        adjList = defaultdict(list)
        visited = set()

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adjList[node]:
                dfs(nei)

        dfs(edges[0][0])
        return len(visited) == n

        

