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


# :warning: test/aoj/GRL_1_C.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#0d0c91c0cca30af9c1c9faef0cf04aa9">test/aoj</a>
* <a href="{{ site.github.repository_url }}/blob/master/test/aoj/GRL_1_C.py">View this file on GitHub</a>
    - Last commit date: 2020-09-13 16:33:52+09:00


* see: <a href="http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C">http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C</a>


## Depends on

* :heavy_check_mark: <a href="../../cpl/__init__.py.html">cpl/__init__.py</a>
* :warning: <a href="../../cpl/graph/floyd_warshall.py.html">cpl/graph/floyd_warshall.py</a>


## Code

<a id="unbundled"></a>
{% raw %}
```cpp
# noqa: E501 # verify-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C
from cpl import INF
from cpl.graph.floyd_warshall import floyd_warshall


def main() -> None:
    V, _, *std = map(int, open(0).read().split())
    graph = [[INF] * V for _ in range(V)]
    for i in range(V):
        graph[i][i] = 0
    for s, t, d in zip(*[iter(std)] * 3):
        graph[s][t] = d
    dist = floyd_warshall(graph)
    # If distance of any node from itself is negative,
    # negative cycle is detected.
    if any(dist[i][i] < 0 for i in range(V)):
        print("NEGATIVE CYCLE")
        exit()
    [print(" ".join(map(str, row)).replace(str(INF), "INF")) for row in dist]


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

