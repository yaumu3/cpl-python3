# noqa: E501 # verify-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_B
from cpl import INF
from cpl.graph.bellman_ford import bellman_ford


def main() -> None:
    V, _, r, *std = map(int, open(0).read().split())
    graph = [[] for _ in range(V)]
    for s, t, d in zip(*[iter(std)] * 3):
        graph[s].append((t, d))
    cost = bellman_ford(graph, r)
    if cost:
        print("\n".join(map(str, cost)).replace(str(INF), "INF"))
    else:
        print("NEGATIVE CYCLE")


if __name__ == "__main__":
    main()
