class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = [[] for i in range(n)]

        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)

        visited = set()
        def dfs(node, par):
            if node in visited:
                return False
            
            visited.add(node)
            for child in adjList[node]:
                if child == par:
                    continue
                if not dfs(child, node):
                    return False
            return True
        return dfs(0,-1) and len(visited) == n
        