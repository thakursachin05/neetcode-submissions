class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def checkValid(l,r,s):
            while l>=0 and r < len(s):
                if s[l] == s[r]:
                    l, r = l-1, r+1
                else: 
                    break
            return (l, r)
        
        s1 = list(s)
        res = 0
        resStr = []
        
        for i in range(len(s1)):
            l,r = checkValid(i-1,i+1,s1)
            l1,r1 = checkValid(i, i+1, s1)
            
            if res < (r - l):
                res = r-l
                resStr = s1[l+1:r]
            
            if res < (r1-l1):
                res = r1-l1
                resStr = s1[l1 + 1 : r1]

        return "".join(resStr)
            
        
                
        