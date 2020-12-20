---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cpl/__init__.py
    title: cpl/__init__.py
  - icon: ':heavy_check_mark:'
    path: cpl/graph/dijkstra.py
    title: cpl/graph/dijkstra.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/shortest_path
    links:
    - https://judge.yosupo.jp/problem/shortest_path
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 85, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verify-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path\n\
    from cpl import INF, pairwise\nfrom cpl.graph.dijkstra import Dijkstra\n\n\ndef\
    \ main() -> None:\n    N, _, s, t, *abc = map(int, open(0).read().split())\n \
    \   G = [[] for _ in range(N)]\n    for a, b, c in zip(*[iter(abc)] * 3):\n  \
    \      G[a].append((b, c))\n    d = Dijkstra(G, s)\n    mc = d.min_cost(t)\n \
    \   if mc == INF:\n        print(-1)\n        exit()\n\n    path = d.min_cost_path(t)\n\
    \    print(mc, len(path) - 1)\n    for u, v in pairwise(path):\n        print(u,\
    \ v)\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn:
  - cpl/graph/dijkstra.py
  - cpl/__init__.py
  isVerificationFile: true
  path: test/yosupo/shortest_path.test.py
  requiredBy: []
  timestamp: '2020-09-14 11:18:32+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/yosupo/shortest_path.test.py
layout: document
redirect_from:
- /verify/test/yosupo/shortest_path.test.py
- /verify/test/yosupo/shortest_path.test.py.html
title: test/yosupo/shortest_path.test.py
---
