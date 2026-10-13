class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for i in range(n)]

        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = set()

        def dfs(node, par):
            if node in visited:
                return
            
            visited.add(node)

            for child in adjList[node]:
                if child == par:
                    continue
                dfs(child, node)
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i, -1)
        
        return count