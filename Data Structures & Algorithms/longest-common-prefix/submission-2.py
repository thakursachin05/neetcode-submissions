class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp = sorted(strs)
        print(temp)
        result = []
        i = 0
        isMidBreak = False
        while i < len(temp[0]):
            c = temp[0][i]
            for s in temp:
                # print(c,s)
                if c != s[i]:
                    i = len(temp[0])
                    isMidBreak = True
                    break
            result.append(c)
            i += 1
        if isMidBreak:
            result.pop()
        return "".join(result)