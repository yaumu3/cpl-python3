from copy import deepcopy
from typing import List

from cpl import INF


def floyd_warshall(graph: List[List[int]]):
    N: int = len(graph)
    cost: List[List[int]] = deepcopy(graph)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if cost[i][k] == INF or cost[k][j] == INF:
                    continue
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    return cost
