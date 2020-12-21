from collections import Counter
from math import factorial

"""
Numbers of permutations of a sequence.
"""

def num_perms(sequence):
    counts = Counter(sequence)
    res = factorial(len(sequence))
    
    for key, count in counts.items():
        res /= factorial(count)
    
    return int(res)