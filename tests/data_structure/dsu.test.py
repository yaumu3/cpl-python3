# verify-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind
from cpl.data_structure.dsu import DSU


def main() -> None:
    N, _, *tuv = map(int, open(0).read().split())
    dsu = DSU(N)
    for t, u, v in zip(*[iter(tuv)] * 3):
        if t == 0:
            dsu.merge(u, v)
        else:
            print(int(dsu.same(u, v)))


if __name__ == "__main__":
    main()
