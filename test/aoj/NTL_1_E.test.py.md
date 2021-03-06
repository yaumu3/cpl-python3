---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/6/NTL/1/NTL_1_E
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/6/NTL/1/NTL_1_E
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# noqa: E501 # verify-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/6/NTL/1/NTL_1_E\n\
    from cpl.math.ext_gcd import ext_gcd\n\n\ndef main() -> None:\n    a, b = map(int,\
    \ input().split())\n    _, x, y = ext_gcd(a, b)\n    print(x, y)\n\n\nif __name__\
    \ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: true
  path: test/aoj/NTL_1_E.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/NTL_1_E.test.py
layout: document
redirect_from:
- /verify/test/aoj/NTL_1_E.test.py
- /verify/test/aoj/NTL_1_E.test.py.html
title: test/aoj/NTL_1_E.test.py
---
