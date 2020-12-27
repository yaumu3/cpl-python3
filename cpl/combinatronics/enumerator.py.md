---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/DPL_5_B.test.py
    title: test/aoj/DPL_5_B.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/DPL_5_D.test.py
    title: test/aoj/DPL_5_D.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/DPL_5_E.test.py
    title: test/aoj/DPL_5_E.test.py
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 85, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Enumerator:\n    def __init__(self, N: int, MOD: int) -> None:\n  \
    \      self.fact = [1, 1]\n        self.finv = [1, 1]\n        self.invs = [0,\
    \ 1]\n        for i in range(2, N + 1):\n            self.fact.append(self.fact[i\
    \ - 1] * i % MOD)\n            self.invs.append(-self.invs[MOD % i] * (MOD //\
    \ i) % MOD)\n            self.finv.append(self.finv[-1] * self.invs[-1] % MOD)\n\
    \        self._MOD = MOD\n        self._N = N\n\n    def choose(self, n: int,\
    \ k: int) -> int:\n        if p := self.permutate(n, k):\n            return p\
    \ * self.finv[k] % self._MOD\n        else:\n            return 0\n\n    def permutate(self,\
    \ n: int, k: int) -> int:\n        if n < k or n < 0 or k < 0:\n            return\
    \ 0\n        assert n <= self._N and k <= self._N\n        return self.fact[n]\
    \ * self.finv[n - k] % self._MOD\n\n    def choose_with_duplicates(self, n: int,\
    \ k: int) -> int:\n        return self.choose(n + k - 1, k)\n"
  dependsOn: []
  isVerificationFile: false
  path: cpl/combinatronics/enumerator.py
  requiredBy: []
  timestamp: '2020-12-26 22:10:12+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/DPL_5_B.test.py
  - test/aoj/DPL_5_E.test.py
  - test/aoj/DPL_5_D.test.py
documentation_of: cpl/combinatronics/enumerator.py
layout: document
redirect_from:
- /library/cpl/combinatronics/enumerator.py
- /library/cpl/combinatronics/enumerator.py.html
title: cpl/combinatronics/enumerator.py
---
