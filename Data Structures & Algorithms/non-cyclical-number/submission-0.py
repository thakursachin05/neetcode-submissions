class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        def dfs(n):
            if n == 1:
                return True
            if n in visited:
                return False
            visited.add(n)
            sum1 = 0
            while n:
                digit = n%10
                sum1 += digit*digit
                n = n//10
            return dfs(sum1)
        return dfs(n)
