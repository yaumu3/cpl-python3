---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cpl/__init__.py
    title: cpl/__init__.py
  - icon: ':heavy_check_mark:'
    path: cpl/graph/floyd_warshall.py
    title: cpl/graph/floyd_warshall.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 85, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# noqa: E501 # verify-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C\n\
    from cpl import INF\nfrom cpl.graph.floyd_warshall import floyd_warshall\n\n\n\
    def main() -> None:\n    V, _, *std = map(int, open(0).read().split())\n    graph\
    \ = [[INF] * V for _ in range(V)]\n    for i in range(V):\n        graph[i][i]\
    \ = 0\n    for s, t, d in zip(*[iter(std)] * 3):\n        graph[s][t] = d\n  \
    \  dist = floyd_warshall(graph)\n    # If distance of any node from itself is\
    \ negative,\n    # negative cycle is detected.\n    if any(dist[i][i] < 0 for\
    \ i in range(V)):\n        print(\"NEGATIVE CYCLE\")\n        exit()\n    [print(\"\
    \ \".join(map(str, row)).replace(str(INF), \"INF\")) for row in dist]\n\n\nif\
    \ __name__ == \"__main__\":\n    main()\n"
  dependsOn:
  - cpl/__init__.py
  - cpl/graph/floyd_warshall.py
  isVerificationFile: true
  path: test/aoj/GRL_1_C.test.py
  requiredBy: []
  timestamp: '2020-09-14 11:18:32+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/GRL_1_C.test.py
layout: document
redirect_from:
- /verify/test/aoj/GRL_1_C.test.py
- /verify/test/aoj/GRL_1_C.test.py.html
title: test/aoj/GRL_1_C.test.py
---
