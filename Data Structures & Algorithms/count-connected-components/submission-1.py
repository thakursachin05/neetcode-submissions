class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for i in range(n)]

        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = set()

        def dfs(node):
            for child in adjList[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child)
        
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        
        return count