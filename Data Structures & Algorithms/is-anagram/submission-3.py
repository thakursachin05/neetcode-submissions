class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = [0] * 26
        if len(s) != len(t):
            return False
        for char in s:
            result[ord(char) - ord('a')] += 1
        for char in t:
            result[ord(char) - ord('a')] -= 1
            if result[ord(char) - ord('a')] < 0:
                return False
        return True
        