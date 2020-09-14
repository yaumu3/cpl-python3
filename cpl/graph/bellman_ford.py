from typing import List, Tuple

from cpl import INF
from cpl.graph import WeightedAdjList


def bellman_ford(graph: WeightedAdjList, start: int) -> Tuple[bool, List[int]]:
    N = len(graph)
    cost = [INF] * N
    cost[start] = 0

    for i in range(N):
        is_intact = True
        for v in range(N):
            if cost[v] == INF:
                continue
            for nv, nw in graph[v]:
                if (nc := cost[v] + nw) >= cost[nv]:
                    continue
                cost[nv] = nc
                is_intact = False
                if i == N - 1:
                    return True, []
        if is_intact:
            break
    return False, cost
