# noqa: E501 # verify-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A
from cpl.graph.mst_kruskal import mst_kruskal


def main() -> None:
    V, _, *stw = map(int, open(0).read().split())
    edges = [(s, t, w) for s, t, w in zip(*[iter(stw)] * 3)]
    ans, _ = mst_kruskal(V, edges)
    print(ans)


if __name__ == "__main__":
    main()
