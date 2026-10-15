class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        n, m = len(word), len(abbr)

        while i < n and j < m:
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                subLen = 0   
                while j < m and abbr[j].isdigit():
                    subLen = subLen*10 + int(abbr[j])
                    j += 1
                i += subLen
            else:
                if abbr[j] != word[i]:
                    return False
                i, j = i+1, j+1
        return i == n and j == m
       