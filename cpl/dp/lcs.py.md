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
  code: "from typing import Sequence\n\n\ndef lcs(S: Sequence, T: Sequence) -> int:\n\
    \    dp = [0] * (len(S) + 1)\n    for t in T:\n        _dp = [0]\n        for\
    \ j, s in enumerate(S):\n            if s == t:\n                _dp.append(dp[j]\
    \ + 1)\n            else:\n                _dp.append(max(dp[j + 1], _dp[j]))\n\
    \        dp = _dp\n    return dp[-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: cpl/dp/lcs.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cpl/dp/lcs.py
layout: document
redirect_from:
- /library/cpl/dp/lcs.py
- /library/cpl/dp/lcs.py.html
title: cpl/dp/lcs.py
---
