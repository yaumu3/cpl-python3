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


# :heavy_check_mark: cpl/combinatronics/enumerator.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#73cd78cad8ef8a4132616770a881e8da">cpl/combinatronics</a>
* <a href="{{ site.github.repository_url }}/blob/master/cpl/combinatronics/enumerator.py">View this file on GitHub</a>
    - Last commit date: 2020-09-13 19:20:22+09:00




## Verified with

* :heavy_check_mark: <a href="../../../verify/test/aoj/DPL_5_B.test.py.html">test/aoj/DPL_5_B.test.py</a>
* :heavy_check_mark: <a href="../../../verify/test/aoj/DPL_5_D.test.py.html">test/aoj/DPL_5_D.test.py</a>
* :heavy_check_mark: <a href="../../../verify/test/aoj/DPL_5_E.test.py.html">test/aoj/DPL_5_E.test.py</a>


## Code

<a id="unbundled"></a>
{% raw %}
```cpp
class Enumerator:
    def __init__(self, N: int, MOD: int) -> None:
        self.fact = [1, 1]
        self.finv = [1, 1]
        self.invs = [0, 1]
        for i in range(2, N + 1):
            self.fact.append(self.fact[i - 1] * i % MOD)
            self.invs.append(-self.invs[MOD % i] * (MOD // i) % MOD)
            self.finv.append(self.finv[-1] * self.invs[-1] % MOD)
        self._MOD = MOD
        self._N = N

    def choose(self, n: int, k: int) -> int:
        if p := self.permutate(n, k):
            return p * self.finv[k] % self._MOD
        else:
            return 0

    def permutate(self, n: int, k: int) -> int:
        if n < k or n < 0 or k < 0:
            return 0
        assert n <= self._N and k <= self._N
        return self.fact[n] * self.finv[n - k] % self._MOD

    def choose_with_duplicates(self, n: int, k: int) -> int:
        return self.choose(n + k - 1, n)

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

