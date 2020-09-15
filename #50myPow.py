class Solution:
    def myPow(self, x: float, n: int) -> float:
        m = 1
        out = x
        if n == 0:
            return 1
        
        while m * 2 <= abs(n):
            m = m * 2
            out = out * out
            
        if n > 0:
            return out * self.myPow(x, n-m)
        else:
            return (1/out) * (1/self.myPow(x, -n-m))