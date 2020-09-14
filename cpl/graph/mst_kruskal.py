from typing import List, Tuple

from cpl.data_structure.dsu import DSU


def mst_kruskal(N: int, edges: List[Tuple[int, int, int]]):
    edges = sorted(edges, key=lambda x: x[2])

    d = DSU(N)
    mst: List[Tuple[int, int, int]] = []
    sum_cost: int = 0
    for u, v, w in edges:
        if d.same(u, v):
            continue
        d.merge(u, v)
        mst.append((u, v, w))
        sum_cost += w
    return sum_cost, mst
