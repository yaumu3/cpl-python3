# verify-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path
from itertools import tee

from cpl.constants import INF
from cpl.graph.shortest_path import Dijkstra


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def main() -> None:
    N, _, s, t, *abc = map(int, open(0).read().split())
    G = [[] for _ in range(N)]
    for a, b, c in zip(*[iter(abc)] * 3):
        G[a].append((b, c))
    d = Dijkstra(G, s)
    mc = d.min_cost(t)
    if mc == INF:
        print(-1)
        exit()

    path = d.min_cost_path(t)
    print(mc, len(path) - 1)
    for u, v in pairwise(path):
        print(u, v)


if __name__ == "__main__":
    main()
