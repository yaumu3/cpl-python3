---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List\n\n\ndef factorize(n: int) -> List[int]:\n    \"\"\
    \"Prime factorization\n    Factorize integer `n` with time complexity O(sqrt(n))\n\
    \n    Args:\n        n: Integer to factorize.\n\n    Returns:\n        List of\
    \ prime factors of `n`.\n\n    \"\"\"\n    res: List[int] = []\n    for i in range(2,\
    \ int(n ** 0.5) + 1):\n        while n % i == 0:\n            res.append(i)\n\
    \            n //= i\n    if n > 1:\n        return res + [n]\n    else:\n   \
    \     return res\n"
  dependsOn: []
  isVerificationFile: false
  path: cpl/math/prime_factorization.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cpl/math/prime_factorization.py
layout: document
redirect_from:
- /library/cpl/math/prime_factorization.py
- /library/cpl/math/prime_factorization.py.html
title: cpl/math/prime_factorization.py
---
