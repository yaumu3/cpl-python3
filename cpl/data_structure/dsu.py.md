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
  code: "from typing import List\n\n\nclass DSU:\n    def __init__(self, n: int =\
    \ 0) -> None:\n        self._n: int = n\n        # root node: -1 * component size\n\
    \        # otherwise: parent\n        self.parent_or_size: List[int] = [-1] *\
    \ n\n\n    def merge(self, a: int, b: int) -> int:\n        assert 0 <= a < self._n\n\
    \        assert 0 <= b < self._n\n        x, y = self.leader(a), self.leader(b)\n\
    \        if x == y:\n            return x\n        if -self.parent_or_size[x]\
    \ < -self.parent_or_size[y]:\n            x, y = y, x\n        self.parent_or_size[x]\
    \ += self.parent_or_size[y]\n        self.parent_or_size[y] = x\n        return\
    \ x\n\n    def same(self, a: int, b: int) -> bool:\n        assert 0 <= a < self._n\n\
    \        assert 0 <= b < self._n\n        return self.leader(a) == self.leader(b)\n\
    \n    def leader(self, a: int) -> int:\n        assert 0 <= a < self._n\n    \
    \    parent = self.parent_or_size[a]\n        while parent >= 0:\n           \
    \ if self.parent_or_size[parent] < 0:\n                return parent\n       \
    \     self.parent_or_size[a], a, parent = (\n                self.parent_or_size[parent],\n\
    \                self.parent_or_size[parent],\n                self.parent_or_size[self.parent_or_size[parent]],\n\
    \            )\n        return a\n\n    def size(self, a: int) -> int:\n     \
    \   assert 0 <= a < self._n\n        return -self.parent_or_size[self.leader(a)]\n\
    \n    def groups(self) -> List[List[int]]:\n        leader_buf = [self.leader(i)\
    \ for i in range(self._n)]\n        group_size = [0] * self._n\n        for i\
    \ in range(self._n):\n            group_size[leader_buf[i]] += 1\n        result\
    \ = [[] for _ in range(self._n)]\n        for i in range(self._n):\n         \
    \   result[leader_buf[i]].append(i)\n        return [row for row in result if\
    \ row]\n"
  dependsOn: []
  isVerificationFile: false
  path: cpl/data_structure/dsu.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cpl/data_structure/dsu.py
layout: document
redirect_from:
- /library/cpl/data_structure/dsu.py
- /library/cpl/data_structure/dsu.py.html
title: cpl/data_structure/dsu.py
---