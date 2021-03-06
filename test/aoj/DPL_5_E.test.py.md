---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cpl/combinatronics/enumerator.py
    title: cpl/combinatronics/enumerator.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/7/DPL/5/DPL_5_E
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/7/DPL/5/DPL_5_E
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# noqa: E501 # verify-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/7/DPL/5/DPL_5_E\n\
    from cpl.combinatronics.enumerator import Enumerator\n\n\ndef main() -> None:\n\
    \    n, k = map(int, input().split())\n    e = Enumerator(k, 1_000_000_007)\n\
    \    print(e.choose(k, n))\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn:
  - cpl/combinatronics/enumerator.py
  isVerificationFile: true
  path: test/aoj/DPL_5_E.test.py
  requiredBy: []
  timestamp: '2020-12-26 22:10:12+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/DPL_5_E.test.py
layout: document
redirect_from:
- /verify/test/aoj/DPL_5_E.test.py
- /verify/test/aoj/DPL_5_E.test.py.html
title: test/aoj/DPL_5_E.test.py
---