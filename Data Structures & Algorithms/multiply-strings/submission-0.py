class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        num1, num2 = num1[::-1], num2[::-1]

        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])
                total = res[i+j] + digit
                res[i+j] = total%10
                res[i+j+1] += total//10
        
        res, st = res[::-1], 0

        while st < len(res) and res[st] == 0:
            st += 1
        
        res = map(str, res[st:])

        return "".join(res)


        