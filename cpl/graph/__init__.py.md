---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.0/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.0/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 85, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: 'from typing import List, Tuple


    AdjMatrix = List[List[int]]

    AdjList = List[List[int]]

    WeightedAdjList = List[List[Tuple[int, int]]]



    __all__ = ["AdjMatrix", "AdjList", "WeightedAdjList"]

    '
  dependsOn: []
  isVerificationFile: false
  path: cpl/graph/__init__.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cpl/graph/__init__.py
layout: document
redirect_from:
- /library/cpl/graph/__init__.py
- /library/cpl/graph/__init__.py.html
title: cpl/graph/__init__.py
---
