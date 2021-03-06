from typing import List


def factorize(n: int) -> List[int]:
    """Prime factorization
    Factorize integer `n` with time complexity O(sqrt(n))

    Args:
        n: Integer to factorize.

    Returns:
        List of prime factors of `n`.

    """
    res: List[int] = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            res.append(i)
            n //= i
    if n > 1:
        return res + [n]
    else:
        return res
