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

class Solution2:    
    def countPrimes(self, n: int) -> int:        
        if n <= 2:
            return 0
                
        is_prime = [True] * n
        
        is_prime[0] = False
        is_prime[1] = False
        
        upper_bound = int(n ** 0.5)
        for i in range( 2, upper_bound+1 ):
            
            if not is_prime[i]:
                continue
            
            for j in range( i*i, n, i):
                is_prime[j] = False
                
        return sum(is_prime)