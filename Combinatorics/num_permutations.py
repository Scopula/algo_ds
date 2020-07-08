from collections import Counter
from math import factorial

def num_perms(sequence):
    """
    Returns the number of permutations of a sequence.

    >>> num_perms("abc")
    6
    >>> num_perms("caabbcc")
    210
    >>> num_perms([1,2,3])
    6
    >>> num_perms([5,4,4,4,2])
    20
    >>> num_perms("") == num_perms([]) == 1
    True
    """
    counts = Counter(sequence)
    res = factorial(len(sequence))
    
    for key, count in counts.items():
        res /= factorial(count)
    
    return int(res)