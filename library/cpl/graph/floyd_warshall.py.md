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


# :heavy_check_mark: cpl/graph/floyd_warshall.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#05f98b83664ba3f3f99f8f8001fd60c2">cpl/graph</a>
* <a href="{{ site.github.repository_url }}/blob/master/cpl/graph/floyd_warshall.py">View this file on GitHub</a>
    - Last commit date: 1970-01-01 00:00:00+00:00




## Verified with

* :heavy_check_mark: <a href="../../../verify/test/aoj/GRL_1_C.test.py.html">test/aoj/GRL_1_C.test.py</a>


## Code

<a id="unbundled"></a>
{% raw %}
```cpp
from copy import deepcopy

from cpl import INF
from cpl.graph import AdjMatrix


def floyd_warshall(graph: AdjMatrix):
    N: int = len(graph)
    cost: AdjMatrix = deepcopy(graph)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if cost[i][k] == INF or cost[k][j] == INF:
                    continue
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    return cost

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

