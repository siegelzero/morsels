def integer_sqrt(n: int) -> int:
    """
    Returns the integer square root of n >= 0 - the integer m satisfying
    m**2 <= n < (m + 1)**2.
    
    Parameters:
        n: int (n >= 0)
    
    Examples:
        >>> integer_sqrt(10)
        3
        >>> integer_sqrt(121)
        11
    """
    if n < 0:
        raise ValueError("integer_sqrt: must have n >= 0.")
    if n <= 1:
        return n
    
    hi = 2**((n.bit_length() + 1)//2)
    lo = n // hi
    
    while lo < hi:
        hi = (hi + lo)//2
        lo = n//hi
    
    return hi


def integer_kth_root(n: int, k: int) -> int:
    """
    Returns the integer kth root of n >= 0 - the integer m satisfying
    m**k <= n < (m + 1)**k.
    
    Parameters:
        n: int (n >= 0)
        k: int (k >= 2)
    
    Examples:
        >>> integer_sqrt(10)
        3
        >>> integer_sqrt(121)
        11
    """
    if n < 0:
        raise ValueError("integer_kth_root: must have n >= 0.")
    if k < 1:
        raise ValueError("integer_kth_root: must have k >= 2.")
    if n <= 1:
        return n
    
    x = 2**((n.bit_length())//k + 1)
    
    while True:
        y = ((k - 1)*x + n//x**(k - 1))//k
        if y < x:
            x = y
        else:
            break
            
    return x
