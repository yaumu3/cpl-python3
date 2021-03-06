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
  code: "from copy import deepcopy\n\nfrom cpl import INF\nfrom cpl.graph import AdjMatrix\n\
    \n\ndef floyd_warshall(graph: AdjMatrix):\n    N: int = len(graph)\n    cost:\
    \ AdjMatrix = deepcopy(graph)\n    for k in range(N):\n        for i in range(N):\n\
    \            for j in range(N):\n                if cost[i][k] == INF or cost[k][j]\
    \ == INF:\n                    continue\n                cost[i][j] = min(cost[i][j],\
    \ cost[i][k] + cost[k][j])\n    return cost\n"
  dependsOn: []
  isVerificationFile: false
  path: cpl/graph/floyd_warshall.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cpl/graph/floyd_warshall.py
layout: document
redirect_from:
- /library/cpl/graph/floyd_warshall.py
- /library/cpl/graph/floyd_warshall.py.html
title: cpl/graph/floyd_warshall.py
---