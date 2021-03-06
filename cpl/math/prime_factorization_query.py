from typing import List


class SmallestPrimeFactors:
    """High speed prime factorizaton using smallest prime factors
    Precompute the smallest prime factor for each integer less than or equal to `n`
    by Eratosthenes sieve; tiem complexity O(n*log(log(n))).
    Then, factorize integer `x` with time complexity O(log(x))
    Based on `https://atcoder.jp/contests/abc177/editorial/82`.

    Args:
        n: Max number to factorize or judge primality.

    Attributes:
        spf: List of the smallest prime factor whose index is the corresponding integer.
    """

    def __init__(self, n: int) -> None:
        self.spf = list(range(n + 1))
        self.spf[0] = -1
        self.spf[1] = -1
        for i in range(2, int(n ** 0.5) + 1):
            if self.spf[i] == i:
                for j in range(i * i, n + 1, i):
                    if self.spf[j] == j:
                        self.spf[j] = i

    def is_prime(self, x: int) -> bool:
        assert x < len(self.spf)
        return self.spf[x] == x

    def factor(self, x: int) -> List[int]:
        assert x < len(self.spf)
        if x < 2:
            return []
        res = []
        while True:
            if self.is_prime(x):
                res.append(x)
                break
            res.append(self.spf[x])
            x //= self.spf[x]
        return res
