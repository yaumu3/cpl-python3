---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# noqa: E501 # verify-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_A\n\
    from cpl import INF\nfrom cpl.graph.dijkstra import Dijkstra\n\n\ndef main() ->\
    \ None:\n    V, _, r, *std = map(int, open(0).read().split())\n    graph = [[]\
    \ for _ in range(V)]\n    for s, t, d in zip(*[iter(std)] * 3):\n        graph[s].append((t,\
    \ d))\n    d = Dijkstra(graph, r)\n    print(\"\\n\".join(map(str, d.cost)).replace(str(INF),\
    \ \"INF\"))\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: true
  path: test/aoj/GRL_1_A.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/GRL_1_A.test.py
layout: document
redirect_from:
- /verify/test/aoj/GRL_1_A.test.py
- /verify/test/aoj/GRL_1_A.test.py.html
title: test/aoj/GRL_1_A.test.py
---
