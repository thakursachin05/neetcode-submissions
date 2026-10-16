class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in dp:
                return dp[i]
            for j in range(i, len(s)):
                if s[i:j+1] in words:
                    dp[i] = dfs(j+1)
                    if dp[i]: 
                        return True
            dp[i] = False
            return dp[i]
        
        return dfs(0)
        