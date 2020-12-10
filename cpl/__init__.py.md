---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/GRL_1_A.test.py
    title: test/aoj/GRL_1_A.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/GRL_1_B.test.py
    title: test/aoj/GRL_1_B.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/GRL_1_C.test.py
    title: test/aoj/GRL_1_C.test.py
  - icon: ':heavy_check_mark:'
    path: test/yosupo/shortest_path.test.py
    title: test/yosupo/shortest_path.test.py
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.0/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.0/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 85, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from itertools import tee\n\n\ndef pairwise(iterable):\n    \"s -> (s0,s1),\
    \ (s1,s2), (s2, s3), ...\"\n    a, b = tee(iterable)\n    next(b, None)\n    return\
    \ zip(a, b)\n\n\nINF = 1 << 64 - 1\n\n__all__ = [\"pairwise\", \"INF\"]\n"
  dependsOn: []
  isVerificationFile: false
  path: cpl/__init__.py
  requiredBy: []
  timestamp: '2020-09-12 19:53:19+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/yosupo/shortest_path.test.py
  - test/aoj/GRL_1_B.test.py
  - test/aoj/GRL_1_C.test.py
  - test/aoj/GRL_1_A.test.py
documentation_of: cpl/__init__.py
layout: document
redirect_from:
- /library/cpl/__init__.py
- /library/cpl/__init__.py.html
title: cpl/__init__.py
---
