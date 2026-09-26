class Solution:
    def numDecodings(self, s: str) -> int:
  
        dp = [0] * (len(s)+1)

        def dfs(i):
            if i>=len(s):
                return 1
            
            if s[i] == '0':
                return 0


            if dp[i]:
                return dp[i]
                
            ways = dfs(i+1)

            if i < len(s)-1 and 10 <= int(s[i:i+2]) <= 26:
                ways += dfs(i+2)
            
            dp[i] = ways
            
            return ways
            
        return dfs(0)
                