# noqa: E501 # verify-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C
from cpl import INF
from cpl.graph.floyd_warshall import floyd_warshall


def main() -> None:
    V, E, *std = map(int, open(0).read().split())
    graph = [[INF] * V for _ in range(V)]
    for i in range(V):
        graph[i][i] = 0
    for s, t, d in zip(*[iter(std)] * 3):
        graph[s][t] = d
    dist = floyd_warshall(graph)
    # If distance of any node from itself is negative,
    # negative cycle is detected.
    if any(dist[i][i] < 0 for i in range(V)):
        print("NEGATIVE CYCLE")
        exit()
    [print(" ".join(map(str, row)).replace(str(INF), "INF")) for row in dist]


if __name__ == "__main__":
    main()
