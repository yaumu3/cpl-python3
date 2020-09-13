# verify-helper: PROBLEM https://judge.yosupo.jp/problem/sum_of_floor_of_linear
from cpl.math.floor_sum import floor_sum


def main() -> None:
    _, *queries = map(int, open(0).read().split())
    for q in zip(*[iter(queries)] * 4):
        print(floor_sum(*q))


if __name__ == "__main__":
    main()
