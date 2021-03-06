from typing import Tuple


def ext_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """Extended euclidean algorithm
    Solves `ax + by = gcd(a, b)`.

    Args:
        a: Integer1.
        b: Integer2.

    Returns:
        Tuple of gcd, x and y (the coefficients of Bezout's identity).

    """
    if b == 0:
        return a, 1, 0
    g, x, y = ext_gcd(b, a % b)
    return g, y, x - (a // b) * y
