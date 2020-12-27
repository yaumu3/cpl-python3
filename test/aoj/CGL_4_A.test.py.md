---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cpl/geometry/__init__.py
    title: cpl/geometry/__init__.py
  - icon: ':heavy_check_mark:'
    path: cpl/geometry/convex_hull.py
    title: cpl/geometry/convex_hull.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/4/CGL_4_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/4/CGL_4_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 85, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# noqa: E501 # verify-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/4/CGL_4_A\n\
    from cpl.geometry import Point\nfrom cpl.geometry.convex_hull import convex_hull\n\
    \n\ndef main() -> None:\n    _, *xy = map(int, open(0).read().split())\n    ps\
    \ = [Point(x, y) for x, y in zip(*[iter(xy)] * 2)]\n    ch = convex_hull(ps)\n\
    \    N = len(ch)\n    s = 0\n    for i in range(1, N):\n        if ch[i].y < ch[s].y\
    \ or (ch[i].y == ch[s].y and ch[i].x < ch[s].x):\n            s = i\n    ch =\
    \ ch[s:] + ch[:s]\n    print(N)\n    [print(p.x, p.y) for p in ch]\n\n\nif __name__\
    \ == \"__main__\":\n    main()\n"
  dependsOn:
  - cpl/geometry/convex_hull.py
  - cpl/geometry/__init__.py
  isVerificationFile: true
  path: test/aoj/CGL_4_A.test.py
  requiredBy: []
  timestamp: '2020-11-08 20:08:09+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/CGL_4_A.test.py
layout: document
redirect_from:
- /verify/test/aoj/CGL_4_A.test.py
- /verify/test/aoj/CGL_4_A.test.py.html
title: test/aoj/CGL_4_A.test.py
---
