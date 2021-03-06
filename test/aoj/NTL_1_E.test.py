# noqa: E501 # verify-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/6/NTL/1/NTL_1_E
from cpl.math.ext_gcd import ext_gcd


def main() -> None:
    a, b = map(int, input().split())
    _, x, y = ext_gcd(a, b)
    print(x, y)


if __name__ == "__main__":
    main()
