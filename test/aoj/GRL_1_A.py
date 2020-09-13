# noqa: E501 # verify-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_A
from cpl import INF
from cpl.graph.dijkstra import Dijkstra


def main() -> None:
    V, _, r, *std = map(int, open(0).read().split())
    graph = [[] for _ in range(V)]
    for s, t, d in zip(*[iter(std)] * 3):
        graph[s].append((t, d))
    d = Dijkstra(graph, r)
    print("\n".join(map(str, d.cost)).replace(str(INF), "INF"))


if __name__ == "__main__":
    main()
