class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        num = 0
        while j < len(abbr):
            if abbr[j] == '0':
                return False
            if ord('a') <= ord(abbr[j]) <= ord('z'):
                if num:
                    i += num
                    num = 0
                if i < len(word) and word[i] != abbr[j]:
                    return False
                i,j = i+1, j+1
            else:
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
        if num:
            i+=num
        return True if i == len(word) and j == len(abbr) else False