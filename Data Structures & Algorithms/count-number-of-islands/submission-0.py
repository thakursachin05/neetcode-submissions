class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[0] * (len(grid[0])+1) for _ in range(len(grid)+1)]

        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        
        def dfs(i,j):
            if i < 0 or i >= len(grid) or j <0 or j>=len(grid[0]):
                return 
            
            if visited[i][j]:
                return
            
            if grid[i][j] == '1':
                visited[i][j] = 1 
                for x,y in directions:
                    dfs(i+x,j+y)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] != 1 and grid[i][j] == '1':
                    count+=1
                    dfs(i,j)
        
        return count
