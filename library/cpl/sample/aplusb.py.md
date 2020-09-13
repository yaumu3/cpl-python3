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


# :heavy_check_mark: cpl/sample/aplusb.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#7cadb34dd2b4e5dcd6ed1a15dda70c08">cpl/sample</a>
* <a href="{{ site.github.repository_url }}/blob/master/cpl/sample/aplusb.py">View this file on GitHub</a>
    - Last commit date: 2020-09-09 23:37:03+09:00




## Verified with

* :heavy_check_mark: <a href="../../../verify/test/yosupo/aplusb.test.py.html">test/yosupo/aplusb.test.py</a>
* :heavy_check_mark: <a href="../../../verify/test/yosupo/many_aplusb.test.py.html">test/yosupo/many_aplusb.test.py</a>


## Code

<a id="unbundled"></a>
{% raw %}
```cpp
def aplusb(a: int, b: int) -> int:
    return a + b

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
