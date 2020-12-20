---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cpl/geometry/__init__.py
    title: cpl/geometry/__init__.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/CGL_4_A.test.py
    title: test/aoj/CGL_4_A.test.py
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 85, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from cpl.geometry import Polygon, cross\n\n\ndef convex_hull(ps: Polygon)\
    \ -> Polygon:\n    \"\"\"Andrew's algorithm\"\"\"\n\n    def construct(limit,\
    \ start, stop, step=1):\n        for i in range(start, stop, step):\n        \
    \    while len(res) > limit and cross(res[-1] - res[-2], s_ps[i] - res[-1]) <\
    \ 0:\n                res.pop()\n            res.append(s_ps[i])\n\n    assert\
    \ len(ps) >= 3\n    s_ps = sorted(ps)\n    N = len(s_ps)\n    res: Polygon = []\n\
    \    construct(1, 0, N)\n    construct(len(res), N - 2, -1, -1)\n    return res[:-1]\n"
  dependsOn:
  - cpl/geometry/__init__.py
  isVerificationFile: false
  path: cpl/geometry/convex_hull.py
  requiredBy: []
  timestamp: '2020-11-08 20:08:09+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/CGL_4_A.test.py
documentation_of: cpl/geometry/convex_hull.py
layout: document
redirect_from:
- /library/cpl/geometry/convex_hull.py
- /library/cpl/geometry/convex_hull.py.html
title: cpl/geometry/convex_hull.py
---
