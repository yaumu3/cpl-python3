# verify-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path
from cpl import INF, pairwise
from cpl.graph.dijkstra import Dijkstra


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
