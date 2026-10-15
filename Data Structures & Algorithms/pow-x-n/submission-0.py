class Solution:
    def myPow(self, x: float, n: int) -> float:
        def getPow(n):
            if n == 0:
                return 1
            half = getPow(n//2)
            if n%2:
                return x * half * half
            return half * half
        return getPow(n) if n >= 0 else 1/getPow(-n)