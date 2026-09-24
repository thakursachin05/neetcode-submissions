class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap1 = {}
        hashmap2 = {}

        for c in s:
            hashmap1[c] = 1 + hashmap1.get(c,0)
        
        for c in t:
            hashmap2[c] = 1 + hashmap2.get(c,0)

        for key in hashmap1:
            if hashmap1[key] != hashmap2.get(key, 0):
                return False
            
        return True
