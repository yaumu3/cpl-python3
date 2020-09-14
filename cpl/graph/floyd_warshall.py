from copy import deepcopy

from cpl import INF
from cpl.graph import AdjMatrix


def floyd_warshall(graph: AdjMatrix):
    N: int = len(graph)
    cost: AdjMatrix = deepcopy(graph)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if cost[i][k] == INF or cost[k][j] == INF:
                    continue
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    return cost
