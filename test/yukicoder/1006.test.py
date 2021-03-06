# noqa: E501 # verify-helper: PROBLEM https://yukicoder.me/problems/no/1006
from collections import Counter

from cpl.math.prime_factorization_query import SmallestPrimeFactors


def main() -> None:
    def f(x):
        res = 1
        for v in Counter(spf.factor(x)).values():
            res *= v + 1
        return x - res

    x = int(input())
    spf = SmallestPrimeFactors(x)
    ans = set()
    cur_min = 1 << 62
    for i in range(1, x // 2 + 1):
        a, b = i, x - i
        tmp = abs(f(a) - f(b))
        if tmp < cur_min:
            ans = {(a, b), (b, a)}
            cur_min = tmp
        elif tmp == cur_min:
            ans |= {(a, b), (b, a)}
    for a, b in sorted(ans):
        print(a, b)


if __name__ == "__main__":
    main()
