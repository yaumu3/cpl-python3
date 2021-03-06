---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List\n\nfrom cpl import INF\nfrom cpl.graph import WeightedAdjList\n\
    \n\ndef bellman_ford(graph: WeightedAdjList, start: int) -> List[int]:\n    N\
    \ = len(graph)\n    cost = [INF] * N\n    cost[start] = 0\n\n    for i in range(N):\n\
    \        is_intact = True\n        for v in range(N):\n            if cost[v]\
    \ == INF:\n                continue\n            for nv, nw in graph[v]:\n   \
    \             if (nc := cost[v] + nw) >= cost[nv]:\n                    continue\n\
    \                cost[nv] = nc\n                is_intact = False\n          \
    \      if i == N - 1:\n                    return []\n        if is_intact:\n\
    \            break\n    return cost\n"
  dependsOn: []
  isVerificationFile: false
  path: cpl/graph/bellman_ford.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cpl/graph/bellman_ford.py
layout: document
redirect_from:
- /library/cpl/graph/bellman_ford.py
- /library/cpl/graph/bellman_ford.py.html
title: cpl/graph/bellman_ford.py
---
