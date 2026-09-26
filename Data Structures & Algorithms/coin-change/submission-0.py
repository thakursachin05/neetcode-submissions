class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1] * (amount + 1) for _ in range(len(coins))]

        def dfs(i, amount):
            if i >= len(coins) or amount < 0:
                return float('inf')
            if amount == 0:
                return 0

            if dp[i][amount]!=-1:
                return dp[i][amount]
            
            dp[i][amount] = min(1+dfs(i, amount-coins[i]), dfs(i+1, amount))
            
            return dp[i][amount]
        
        res = dfs(0, amount) 

        return res if res != float('inf') else -1
            
            
        