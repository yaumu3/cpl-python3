---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cpl/sample/aplusb.py
    title: cpl/sample/aplusb.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/aplusb
    links:
    - https://judge.yosupo.jp/problem/aplusb
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.0/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.0/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 85, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verify-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb\nfrom cpl.sample.aplusb\
    \ import aplusb\n\n\ndef main() -> None:\n    A, B = map(int, input().split())\n\
    \    print(aplusb(A, B))\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn:
  - cpl/sample/aplusb.py
  isVerificationFile: true
  path: test/yosupo/aplusb.test.py
  requiredBy: []
  timestamp: '2020-09-13 16:33:52+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/yosupo/aplusb.test.py
layout: document
redirect_from:
- /verify/test/yosupo/aplusb.test.py
- /verify/test/yosupo/aplusb.test.py.html
title: test/yosupo/aplusb.test.py
---
