class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        subset = []

        def isValid(s):
            i,j = 0, len(s)-1
            while i <= j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True

        def dfs(i):
            if i == len(s):
                result.append(subset.copy())
                return
            for j in range(i,len(s)):
                if isValid(s[i:j+1]):
                    subset.append(s[i:j+1])
                    dfs(j+1)
                    subset.pop()
        dfs(0)
        return result


      
        
        