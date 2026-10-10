

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        components = set()

        def dfs(node, setVal, prev):
            # If node is at end
            if adjList[node] == []:
                adjList[node].append(setVal)
                components.add(setVal)
                return
            # Doing dfs on repeated nodes
            if adjList[node][0] in components:
                setVal = adjList[node][0]
            
            #print(setVal)
            components.add(setVal)

            for i, nei in enumerate(adjList[node]):
                if nei == setVal:
                    continue
                if nei == prev:
                    adjList[node][i] = setVal
                    continue
                adjList[node][i] = setVal
                dfs(nei, setVal, node)

        for node in range(n):
            dfs(node, node, -1)
        
        return len(components)
