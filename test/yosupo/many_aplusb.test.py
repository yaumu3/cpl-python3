# verify-helper: PROBLEM https://judge.yosupo.jp/problem/many_aplusb
from cpl.sample.aplusb import aplusb


def main() -> None:
    _, *AB = map(int, open(0).read().split())
    for A, B in zip(*[iter(AB)] * 2):
        print(aplusb(A, B))


if __name__ == "__main__":
    main()
