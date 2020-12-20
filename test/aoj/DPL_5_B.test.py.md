---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cpl/combinatronics/enumerator.py
    title: cpl/combinatronics/enumerator.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/7/DPL/5/DPL_5_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/7/DPL/5/DPL_5_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 85, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# noqa: E501 # verify-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/7/DPL/5/DPL_5_B\n\
    from cpl.combinatronics.enumerator import Enumerator\n\n\ndef main() -> None:\n\
    \    n, k = map(int, input().split())\n    e = Enumerator(k, 1_000_000_007)\n\
    \    print(e.permutate(k, n))\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn:
  - cpl/combinatronics/enumerator.py
  isVerificationFile: true
  path: test/aoj/DPL_5_B.test.py
  requiredBy: []
  timestamp: '2020-09-13 19:20:22+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/DPL_5_B.test.py
layout: document
redirect_from:
- /verify/test/aoj/DPL_5_B.test.py
- /verify/test/aoj/DPL_5_B.test.py.html
title: test/aoj/DPL_5_B.test.py
---
