from heapq import heappop, heappush
from typing import List, Tuple

from cpl.constants import INF


class Dijkstra:
    def __init__(self, graph: List[List[Tuple[int, int]]], start: int) -> None:
        N = len(graph)
        pq: List[Tuple[int, int]] = []
        heappush(pq, (0, start))

        cost: List[int] = [INF] * N
        cost[start] = 0
        prev: List[int] = [-1] * N
        while pq:
            w, v = heappop(pq)
            if w > cost[v]:
                continue
            for nv, nw in graph[v]:
                if (nc := cost[v] + nw) >= cost[nv]:
                    continue
                cost[nv] = nc
                prev[nv] = v
                heappush(pq, (nc, nv))
        self.cost = cost
        self.prev = prev

    def min_cost(self, goal: int):
        return self.cost[goal]

    def min_cost_path(self, goal: int):
        nd = goal
        path: List[int] = []
        while nd >= 0:
            path.append(nd)
            nd = self.prev[nd]
        return path[::-1]
