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
  code: "from cpl.geometry import Polygon, cross\n\n\ndef convex_hull(ps: Polygon)\
    \ -> Polygon:\n    \"\"\"Andrew's algorithm\"\"\"\n\n    def construct(limit,\
    \ start, stop, step=1):\n        for i in range(start, stop, step):\n        \
    \    while len(res) > limit and cross(res[-1] - res[-2], s_ps[i] - res[-1]) <\
    \ 0:\n                res.pop()\n            res.append(s_ps[i])\n\n    assert\
    \ len(ps) >= 3\n    s_ps = sorted(ps)\n    N = len(s_ps)\n    res: Polygon = []\n\
    \    construct(1, 0, N)\n    construct(len(res), N - 2, -1, -1)\n    return res[:-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: cpl/geometry/convex_hull.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cpl/geometry/convex_hull.py
layout: document
redirect_from:
- /library/cpl/geometry/convex_hull.py
- /library/cpl/geometry/convex_hull.py.html
title: cpl/geometry/convex_hull.py
---
