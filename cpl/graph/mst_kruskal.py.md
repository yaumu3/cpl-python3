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
  code: "from typing import List, Tuple\n\nfrom cpl.data_structure.dsu import DSU\n\
    \n\ndef mst_kruskal(N: int, edges: List[Tuple[int, int, int]]):\n    edges = sorted(edges,\
    \ key=lambda x: x[2])\n\n    d = DSU(N)\n    mst: List[Tuple[int, int, int]] =\
    \ []\n    sum_cost: int = 0\n    for u, v, w in edges:\n        if d.same(u, v):\n\
    \            continue\n        d.merge(u, v)\n        mst.append((u, v, w))\n\
    \        sum_cost += w\n    return sum_cost, mst\n"
  dependsOn: []
  isVerificationFile: false
  path: cpl/graph/mst_kruskal.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cpl/graph/mst_kruskal.py
layout: document
redirect_from:
- /library/cpl/graph/mst_kruskal.py
- /library/cpl/graph/mst_kruskal.py.html
title: cpl/graph/mst_kruskal.py
---
