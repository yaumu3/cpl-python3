# noqa: E501 # verify-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/6/NTL/1/NTL_1_A
from cpl.math.prime_factorization import factorize


def main() -> None:
    n = int(input())
    factors = sorted(factorize(n))
    print(f"{n}: {' '.join(map(str, factors))}")


if __name__ == "__main__":
    main()
