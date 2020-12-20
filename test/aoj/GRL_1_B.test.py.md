---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cpl/__init__.py
    title: cpl/__init__.py
  - icon: ':heavy_check_mark:'
    path: cpl/graph/bellman_ford.py
    title: cpl/graph/bellman_ford.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 85, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# noqa: E501 # verify-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_B\n\
    from cpl import INF\nfrom cpl.graph.bellman_ford import bellman_ford\n\n\ndef\
    \ main() -> None:\n    V, _, r, *std = map(int, open(0).read().split())\n    graph\
    \ = [[] for _ in range(V)]\n    for s, t, d in zip(*[iter(std)] * 3):\n      \
    \  graph[s].append((t, d))\n    cost = bellman_ford(graph, r)\n    if cost:\n\
    \        print(\"\\n\".join(map(str, cost)).replace(str(INF), \"INF\"))\n    else:\n\
    \        print(\"NEGATIVE CYCLE\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn:
  - cpl/graph/bellman_ford.py
  - cpl/__init__.py
  isVerificationFile: true
  path: test/aoj/GRL_1_B.test.py
  requiredBy: []
  timestamp: '2020-09-14 16:03:18+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/GRL_1_B.test.py
layout: document
redirect_from:
- /verify/test/aoj/GRL_1_B.test.py
- /verify/test/aoj/GRL_1_B.test.py.html
title: test/aoj/GRL_1_B.test.py
---
