---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cpl/dp/lcs.py
    title: cpl/dp/lcs.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/10/ALDS1_10_C
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/10/ALDS1_10_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 85, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# noqa: E501 # verify-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/10/ALDS1_10_C\n\
    from cpl.dp.lcs import lcs\n\nif __name__ == \"__main__\":\n    q = int(input())\n\
    \    for _ in range(q):\n        X = input()\n        Y = input()\n        print(lcs(X,\
    \ Y))\n"
  dependsOn:
  - cpl/dp/lcs.py
  isVerificationFile: true
  path: test/aoj/ALDS1_10_C.test.py
  requiredBy: []
  timestamp: '2020-12-27 19:45:38+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/ALDS1_10_C.test.py
layout: document
redirect_from:
- /verify/test/aoj/ALDS1_10_C.test.py
- /verify/test/aoj/ALDS1_10_C.test.py.html
title: test/aoj/ALDS1_10_C.test.py
---
