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
  code: "from typing import Tuple\n\n\ndef ext_gcd(a: int, b: int) -> Tuple[int, int,\
    \ int]:\n    \"\"\"Extended euclidean algorithm\n    Solves `ax + by = gcd(a,\
    \ b)`.\n\n    Args:\n        a: Integer1.\n        b: Integer2.\n\n    Returns:\n\
    \        Tuple of gcd, x and y (the coefficients of Bezout's identity).\n\n  \
    \  \"\"\"\n    if b == 0:\n        return a, 1, 0\n    g, x, y = ext_gcd(b, a\
    \ % b)\n    return g, y, x - (a // b) * y\n"
  dependsOn: []
  isVerificationFile: false
  path: cpl/math/ext_gcd.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cpl/math/ext_gcd.py
layout: document
redirect_from:
- /library/cpl/math/ext_gcd.py
- /library/cpl/math/ext_gcd.py.html
title: cpl/math/ext_gcd.py
---
