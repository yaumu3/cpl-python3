---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://atcoder.jp/contests/abc177/editorial/82
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List\n\n\nclass SmallestPrimeFactors:\n    \"\"\"High\
    \ speed prime factorizaton using smallest prime factors\n    Precompute the smallest\
    \ prime factor for each integer less than or equal to `n`\n    by Eratosthenes\
    \ sieve; tiem complexity O(n*log(log(n))).\n    Then, factorize integer `x` with\
    \ time complexity O(log(x))\n    Based on `https://atcoder.jp/contests/abc177/editorial/82`.\n\
    \n    Args:\n        n: Max number to factorize or judge primality.\n\n    Attributes:\n\
    \        spf: List of the smallest prime factor whose index is the corresponding\
    \ integer.\n    \"\"\"\n\n    def __init__(self, n: int) -> None:\n        self.spf\
    \ = list(range(n + 1))\n        self.spf[0] = -1\n        self.spf[1] = -1\n \
    \       for i in range(2, int(n ** 0.5) + 1):\n            if self.spf[i] == i:\n\
    \                for j in range(i * i, n + 1, i):\n                    if self.spf[j]\
    \ == j:\n                        self.spf[j] = i\n\n    def is_prime(self, x:\
    \ int) -> bool:\n        assert x < len(self.spf)\n        return self.spf[x]\
    \ == x\n\n    def __traverse(self, x: int) -> List[int]:\n        if self.spf[x]\
    \ == x:\n            return [x]\n        nxt = x // self.spf[x]\n        return\
    \ self.__traverse(nxt) + [self.spf[x]]\n\n    def factor(self, x: int) -> List[int]:\n\
    \        assert x < len(self.spf)\n        if x < 2:\n            return []\n\
    \        return self.__traverse(x)\n"
  dependsOn: []
  isVerificationFile: false
  path: cpl/math/prime_factorization_query.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cpl/math/prime_factorization_query.py
layout: document
redirect_from:
- /library/cpl/math/prime_factorization_query.py
- /library/cpl/math/prime_factorization_query.py.html
title: cpl/math/prime_factorization_query.py
---
