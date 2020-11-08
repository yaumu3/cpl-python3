---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/GRL_1_A.test.py
    title: test/aoj/GRL_1_A.test.py
  - icon: ':heavy_check_mark:'
    path: test/yosupo/shortest_path.test.py
    title: test/yosupo/shortest_path.test.py
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.0/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.0/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 85, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from heapq import heappop, heappush\nfrom typing import List, Tuple\n\nfrom\
    \ cpl import INF\nfrom cpl.graph import WeightedAdjList\n\n\nclass Dijkstra:\n\
    \    def __init__(self, graph: WeightedAdjList, start: int) -> None:\n       \
    \ N = len(graph)\n        pq: List[Tuple[int, int]] = []\n        heappush(pq,\
    \ (0, start))\n\n        cost: List[int] = [INF] * N\n        cost[start] = 0\n\
    \        prev: List[int] = [-1] * N\n        while pq:\n            w, v = heappop(pq)\n\
    \            if w > cost[v]:\n                continue\n            for nv, nw\
    \ in graph[v]:\n                if (nc := cost[v] + nw) >= cost[nv]:\n       \
    \             continue\n                cost[nv] = nc\n                prev[nv]\
    \ = v\n                heappush(pq, (nc, nv))\n        self.cost = cost\n    \
    \    self.prev = prev\n\n    def min_cost(self, goal: int):\n        return self.cost[goal]\n\
    \n    def min_cost_path(self, goal: int):\n        nd = goal\n        path: List[int]\
    \ = []\n        while nd >= 0:\n            path.append(nd)\n            nd =\
    \ self.prev[nd]\n        return path[::-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: cpl/graph/dijkstra.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/GRL_1_A.test.py
  - test/yosupo/shortest_path.test.py
documentation_of: cpl/graph/dijkstra.py
layout: document
redirect_from:
- /library/cpl/graph/dijkstra.py
- /library/cpl/graph/dijkstra.py.html
title: cpl/graph/dijkstra.py
---
