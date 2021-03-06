---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/yosupo/sum_of_floor_of_linear.test.py
    title: test/yosupo/sum_of_floor_of_linear.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def floor_sum(n: int, m: int, a: int, b: int) -> int:\n    ans: int = 0\n\
    \    if a >= m:\n        ans += (n - 1) * n * (a // m) // 2\n        a %= m\n\
    \    if b >= m:\n        ans += n * (b // m)\n        b %= m\n\n    y_max: int\
    \ = (a * n + b) // m\n    x_max: int = y_max * m - b\n    if y_max == 0:\n   \
    \     return ans\n    ans += (n - (x_max + a - 1) // a) * y_max\n    ans += floor_sum(y_max,\
    \ a, m, (a - x_max % a) % a)\n    return ans\n"
  dependsOn: []
  isVerificationFile: false
  path: cpl/math/floor_sum.py
  requiredBy: []
  timestamp: '2020-09-10 00:02:36+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/yosupo/sum_of_floor_of_linear.test.py
documentation_of: cpl/math/floor_sum.py
layout: document
redirect_from:
- /library/cpl/math/floor_sum.py
- /library/cpl/math/floor_sum.py.html
title: cpl/math/floor_sum.py
---
