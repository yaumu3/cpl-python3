from typing import List

from cpl import INF
from cpl.graph import WeightedAdjList


def bellman_ford(graph: WeightedAdjList, start: int) -> List[int]:
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
                    return []
        if is_intact:
            break
    return cost
