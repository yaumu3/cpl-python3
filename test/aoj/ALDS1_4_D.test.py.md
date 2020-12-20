---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cpl/algorithm/binary_search.py
    title: cpl/algorithm/binary_search.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_4_D
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_4_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 85, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# noqa: E501 # verify-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_4_D\n\
    from cpl.algorithm.binary_search import binary_search\n\n\ndef main() -> None:\n\
    \    def is_loadable(x):\n        if x < max_W:\n            return False\n  \
    \      cur_w = 0\n        cnt = 1\n        for w in W:\n            if cur_w +\
    \ w <= x:\n                cur_w += w\n            else:\n                cur_w\
    \ = w\n                cnt += 1\n        return cnt <= K\n\n    N, K, *W = map(int,\
    \ open(0).read().split())\n    max_W = max(W)\n    print(binary_search(0, sum(W),\
    \ is_loadable))\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn:
  - cpl/algorithm/binary_search.py
  isVerificationFile: true
  path: test/aoj/ALDS1_4_D.test.py
  requiredBy: []
  timestamp: '2020-12-10 11:25:17+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/ALDS1_4_D.test.py
layout: document
redirect_from:
- /verify/test/aoj/ALDS1_4_D.test.py
- /verify/test/aoj/ALDS1_4_D.test.py.html
title: test/aoj/ALDS1_4_D.test.py
---
