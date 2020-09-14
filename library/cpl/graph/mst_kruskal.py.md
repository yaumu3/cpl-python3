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


# :heavy_check_mark: cpl/graph/mst_kruskal.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#05f98b83664ba3f3f99f8f8001fd60c2">cpl/graph</a>
* <a href="{{ site.github.repository_url }}/blob/master/cpl/graph/mst_kruskal.py">View this file on GitHub</a>
    - Last commit date: 1970-01-01 00:00:00+00:00




## Verified with

* :heavy_check_mark: <a href="../../../verify/test/aoj/GRL_2_A.test.py.html">test/aoj/GRL_2_A.test.py</a>


## Code

<a id="unbundled"></a>
{% raw %}
```cpp
from typing import List, Tuple

from cpl.data_structure.dsu import DSU


def mst_kruskal(N: int, edges: List[Tuple[int, int, int]]):
    edges = sorted(edges, key=lambda x: x[2])

    d = DSU(N)
    mst: List[Tuple[int, int, int]] = []
    sum_cost: int = 0
    for u, v, w in edges:
        if d.same(u, v):
            continue
        d.merge(u, v)
        mst.append((u, v, w))
        sum_cost += w
    return sum_cost, mst

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

