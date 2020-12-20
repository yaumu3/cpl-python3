---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/ALDS1_4_D.test.py
    title: test/aoj/ALDS1_4_D.test.py
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 85, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Callable\n\n\ndef binary_search(bad: int, good: int, is_good:\
    \ Callable[[int], bool]) -> int:\n    while abs(bad - good) > 1:\n        mid\
    \ = (bad + good) // 2\n        if is_good(mid):\n            good = mid\n    \
    \    else:\n            bad = mid\n    return good\n"
  dependsOn: []
  isVerificationFile: false
  path: cpl/algorithm/binary_search.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/ALDS1_4_D.test.py
documentation_of: cpl/algorithm/binary_search.py
layout: document
redirect_from:
- /library/cpl/algorithm/binary_search.py
- /library/cpl/algorithm/binary_search.py.html
title: cpl/algorithm/binary_search.py
---
