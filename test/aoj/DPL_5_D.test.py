# noqa: E501 # verify-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/7/DPL/5/DPL_5_D
from cpl.combinatronics.enumerator import Enumerator


def main() -> None:
    n, k = map(int, input().split())
    e = Enumerator(n + k, 1_000_000_007)
    print(e.choose_with_duplicates(k, n))


if __name__ == "__main__":
    main()
