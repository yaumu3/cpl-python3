---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/unionfind
    links:
    - https://judge.yosupo.jp/problem/unionfind
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verify-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind\nfrom\
    \ cpl.data_structure.dsu import DSU\n\n\ndef main() -> None:\n    N, _, *tuv =\
    \ map(int, open(0).read().split())\n    dsu = DSU(N)\n    for t, u, v in zip(*[iter(tuv)]\
    \ * 3):\n        if t == 0:\n            dsu.merge(u, v)\n        else:\n    \
    \        print(int(dsu.same(u, v)))\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: true
  path: test/yosupo/unionfind.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/yosupo/unionfind.test.py
layout: document
redirect_from:
- /verify/test/yosupo/unionfind.test.py
- /verify/test/yosupo/unionfind.test.py.html
title: test/yosupo/unionfind.test.py
---
