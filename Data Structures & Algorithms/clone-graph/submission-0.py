
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneNode(self, node: Node) -> Node:
        return Node(node.val)

    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if node is None:
            return None
            
        visited = {node: self.cloneNode(node)}
        queue = deque([node])

        while queue:
            curr = queue.popleft()

            for nei in curr.neighbors:
                if nei not in visited:
                    visited[nei] = self.cloneNode(nei)
                    queue.append(nei)
                visited[curr].neighbors.append(visited[nei])
        
        return visited[node]



