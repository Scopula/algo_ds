"""
Sieve eratosthenes algorithm, returns a set of primes up to and including 'n'.
"""

def sieve_erat(n):
    A = [True] * (n + 2)
    u = int(n**0.5)+1
    primes = set()

    for i in range(2, u):
        if A[i]:
            primes.add(i)
            j = i*2
            while j < n:
                A[j] = False
                j += i
    
    for j in range(u, n+1):
        if A[j]:
            primes.add(j)

    return primes