---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cpl/math/floor_sum.py
    title: cpl/math/floor_sum.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/sum_of_floor_of_linear
    links:
    - https://judge.yosupo.jp/problem/sum_of_floor_of_linear
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.0/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.0/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 85, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verify-helper: PROBLEM https://judge.yosupo.jp/problem/sum_of_floor_of_linear\n\
    from cpl.math.floor_sum import floor_sum\n\n\ndef main() -> None:\n    _, *queries\
    \ = map(int, open(0).read().split())\n    for q in zip(*[iter(queries)] * 4):\n\
    \        print(floor_sum(*q))\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn:
  - cpl/math/floor_sum.py
  isVerificationFile: true
  path: test/yosupo/sum_of_floor_of_linear.test.py
  requiredBy: []
  timestamp: '2020-09-13 16:33:52+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/yosupo/sum_of_floor_of_linear.test.py
layout: document
redirect_from:
- /verify/test/yosupo/sum_of_floor_of_linear.test.py
- /verify/test/yosupo/sum_of_floor_of_linear.test.py.html
title: test/yosupo/sum_of_floor_of_linear.test.py
---
