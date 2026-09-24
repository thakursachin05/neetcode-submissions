class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        substr = []
        digitMap = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9':'wxyz'}

        def dfs(i):
            if i >= len(digits):
                if len(substr):
                    result.append("".join(substr))
                return
            for char in digitMap[digits[i]]:
                substr.append(char)
                dfs(i+1)
                substr.pop()
        
        dfs(0)

        return result

        
        