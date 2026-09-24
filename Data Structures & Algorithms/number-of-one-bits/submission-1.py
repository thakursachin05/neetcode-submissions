class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # print(n)
            digit = n & 1
            if digit:
                count += 1
            n = n>>1
        return count
        