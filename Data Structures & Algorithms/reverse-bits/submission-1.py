class Solution:
    def reverseBits(self, n: int) -> int:
        number = 0
        for i in range(0,32):
            if 1<<i & n:
                number += (1<< (31-i))
        return number
        