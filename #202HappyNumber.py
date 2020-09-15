class Solution:
    def countPrimes(self, n: int) -> int:
        notPrime = set([])
        prime = 0
        for num in range(2,n):
            if num not in notPrime:
                prime += 1
                m = num * 2
                while m < n:
                    notPrime.add(m)
                    m += num
        return prime