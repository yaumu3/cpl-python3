---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cpl/geometry/convex_hull.py
    title: cpl/geometry/convex_hull.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/CGL_4_A.test.py
    title: test/aoj/CGL_4_A.test.py
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.0/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.0/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 85, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from math import sqrt\nfrom typing import List\n\nPolygon = List[\"Point\"\
    ]\n\n\nclass Point:\n    EPS = 1e-10\n\n    def __init__(self, x: float, y: float):\n\
    \        self.x = x\n        self.y = y\n\n    def __repr__(self):\n        return\
    \ f\"<Point x={self.x}, y={self.y}>\"\n\n    def __eq__(self, other):\n      \
    \  return abs(self.x - other.x) < self.EPS and abs(self.y - other.y) < self.EPS\n\
    \n    def __lt__(self, other):\n        return self.x < other.x if self.x != other.x\
    \ else self.y < other.y\n\n    def __add__(self, other: \"Point\"):\n        return\
    \ Point(self.x + other.x, self.y + other.y)\n\n    def __sub__(self, other: \"\
    Point\"):\n        return Point(self.x - other.x, self.y - other.y)\n\n    def\
    \ __mul__(self, other: \"Point\"):\n        return Point(self.x * other.x, self.y\
    \ * other.y)\n\n    def __div__(self, other: \"Point\"):\n        return Point(self.x\
    \ / other.x, self.y / other.y)\n\n    def norm(self) -> float:\n        return\
    \ self.x ** 2 + self.y ** 2\n\n    def abs(self) -> float:\n        return sqrt(self.norm())\n\
    \n\ndef cross(a: Point, b: Point) -> float:\n    return a.x * b.y - a.y * b.x\n"
  dependsOn: []
  isVerificationFile: false
  path: cpl/geometry/__init__.py
  requiredBy:
  - cpl/geometry/convex_hull.py
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/CGL_4_A.test.py
documentation_of: cpl/geometry/__init__.py
layout: document
redirect_from:
- /library/cpl/geometry/__init__.py
- /library/cpl/geometry/__init__.py.html
title: cpl/geometry/__init__.py
---
