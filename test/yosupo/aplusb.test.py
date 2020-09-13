# verify-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb
from cpl.sample.aplusb import aplusb


def main() -> None:
    A, B = map(int, input().split())
    print(aplusb(A, B))


if __name__ == "__main__":
    main()
