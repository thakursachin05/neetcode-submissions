class Solution:
    def countSubstrings(self, s: str) -> int:
        def isValid(l,r,s):
            count = 0
            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    count += 1
                    l, r = l-1, r+1
                else:
                    break
            return count
        
        s1 = list(s)
        res = 0
        n = len(s)
        for i in range(n):
            res += isValid(i,i,s1)
            res += isValid(i, i+1, s1)
        return res

            
        