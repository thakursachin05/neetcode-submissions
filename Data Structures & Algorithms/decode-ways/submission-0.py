class Solution:
    def numDecodings(self, s: str) -> int:
        letter_to_number = {
            chr(ord('A') + i): str(i + 1)
            for i in range(26)
        }
        
        dp = [0] * (len(s)+1)

        def dfs(i):
            if i>=len(s):
                return 1
            
            if s[i] == '0':
                return 0

            ways = 0
            if dp[i]:
                return dp[i]
            ways += dfs(i+1)
            dp[i] = ways
            if i < len(s)-1 and 10 <= int(s[i:i+2]) <= 26:
                ways += dfs(i+2)
                dp[i] = ways
            
            return ways
            
        return dfs(0)
                