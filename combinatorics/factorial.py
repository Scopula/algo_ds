"""
Factorial with memoization.
"""

def memo_factorial(mod=None):
    res = [1,1]
    size = 2

    def ff(k):
        nonlocal size

        while k >= size:
            res.append(res[-1] * size)
            size += 1  
        return res[k]
    
    def ff_mod(k):
        nonlocal size

        while k >= size:
            res.append((res[-1] * (size % mod)) % mod)
            size += 1
        
        return res[k]

    if mod == None:
        return ff
    else:
        return ff_mod
