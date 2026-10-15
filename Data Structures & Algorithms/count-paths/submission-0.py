class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}

        def dfs(i,j):
            if i == n-1 and j == m-1:
                return 1
            if i < 0 or j < 0 or i == n or j == m:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)] = dfs(i+1,j) + dfs(i,j+1)
            return dp[(i,j)]
        return dfs(0,0)
        