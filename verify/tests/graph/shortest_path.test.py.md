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


# :heavy_check_mark: tests/graph/shortest_path.test.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#85578aebac047bd9defb7b2588885855">tests/graph</a>
* <a href="{{ site.github.repository_url }}/blob/master/tests/graph/shortest_path.test.py">View this file on GitHub</a>
    - Last commit date: 2020-09-11 20:57:58+09:00


* see: <a href="https://judge.yosupo.jp/problem/shortest_path">https://judge.yosupo.jp/problem/shortest_path</a>


## Depends on

* :heavy_check_mark: <a href="../../../library/cpl/constants.py.html">cpl/constants.py</a>
* :heavy_check_mark: <a href="../../../library/cpl/graph/shortest_path.py.html">cpl/graph/shortest_path.py</a>


## Code

<a id="unbundled"></a>
{% raw %}
```cpp
# verify-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path
from itertools import tee

from cpl.constants import INF
from cpl.graph.shortest_path import Dijkstra


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def main() -> None:
    N, _, s, t, *abc = map(int, open(0).read().split())
    G = [[] for _ in range(N)]
    for a, b, c in zip(*[iter(abc)] * 3):
        G[a].append((b, c))
    d = Dijkstra(G, s)
    mc = d.min_cost(t)
    if mc == INF:
        print(-1)
        exit()

    path = d.min_cost_path(t)
    print(mc, len(path) - 1)
    for u, v in pairwise(path):
        print(u, v)


if __name__ == "__main__":
    main()

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

