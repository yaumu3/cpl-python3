---
layout: default
---

<!-- mathjax config similar to math.stackexchange -->
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    TeX: { equationNumbers: { autoNumber: "AMS" }},
    tex2jax: {
      inlineMath: [ ['$','$'] ],
      processEscapes: true
    },
    "HTML-CSS": { matchFontHeight: false },
    displayAlign: "left",
    displayIndent: "2em"
  });
</script>

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/jquery-balloon-js@1.1.2/jquery.balloon.min.js" integrity="sha256-ZEYs9VrgAeNuPvs15E39OsyOJaIkXEEt10fzxJ20+2I=" crossorigin="anonymous"></script>
<script type="text/javascript" src="../../../assets/js/copy-button.js"></script>
<link rel="stylesheet" href="../../../assets/css/copy-button.css" />


# :warning: cpl/graph/shortest_path.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#05f98b83664ba3f3f99f8f8001fd60c2">cpl/graph</a>
* <a href="{{ site.github.repository_url }}/blob/master/cpl/graph/shortest_path.py">View this file on GitHub</a>
    - Last commit date: 1970-01-01 00:00:00+00:00




## Required by

* :heavy_check_mark: <a href="__init__.py.html">cpl/graph/__init__.py</a>


## Code

<a id="unbundled"></a>
{% raw %}
```cpp
from heapq import heappop, heappush
from typing import List, Tuple

from cpl import INF


class Dijkstra:
    def __init__(self, graph: List[List[Tuple[int, int]]], start: int) -> None:
        N = len(graph)
        pq: List[Tuple[int, int]] = []
        heappush(pq, (0, start))

        cost: List[int] = [INF] * N
        cost[start] = 0
        prev: List[int] = [-1] * N
        while pq:
            w, v = heappop(pq)
            if w > cost[v]:
                continue
            for nv, nw in graph[v]:
                if (nc := cost[v] + nw) >= cost[nv]:
                    continue
                cost[nv] = nc
                prev[nv] = v
                heappush(pq, (nc, nv))
        self.cost = cost
        self.prev = prev

    def min_cost(self, goal: int):
        return self.cost[goal]

    def min_cost_path(self, goal: int):
        nd = goal
        path: List[int] = []
        while nd >= 0:
            path.append(nd)
            nd = self.prev[nd]
        return path[::-1]

```
{% endraw %}

<a id="bundled"></a>
{% raw %}
```cpp
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.8.5/x64/lib/python3.8/site-packages/onlinejudge_verify/docs.py", line 349, in write_contents
    bundled_code = language.bundle(self.file_class.file_path, basedir=pathlib.Path.cwd())
  File "/opt/hostedtoolcache/Python/3.8.5/x64/lib/python3.8/site-packages/onlinejudge_verify/languages/python.py", line 84, in bundle
    raise NotImplementedError
NotImplementedError

```
{% endraw %}

<a href="../../../index.html">Back to top page</a>

