class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []
        def dfs(i,j):
            if i == n and j == n:
                res.append("".join(curr))
                return
            if i < n:
                curr.append('(')
                dfs(i+1,j)
                curr.pop()
            if j < i:
                curr.append(")")
                dfs(i, j + 1)
                curr.pop()
            
        dfs(0,0)

        return res
            
            
        