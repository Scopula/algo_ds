def sieve_erat(n):
    """
    Returns a set of primes up to n (inclusive).

    >>> sieve_erat(11) == {2,3,5,7,11}
    True
    """
    primes = set()

    A = [True] * (n + 2)

    for i in range(2, int(n**0.5)+1):
        if A[i]:
            j = i*2
            while j < n:
                A[j] = False
                j += i
    

    for i in range(2, n+1):
        if A[i]:
            primes.add(i)

    return primes