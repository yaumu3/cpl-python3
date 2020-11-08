# noqa: E501 # verify-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/4/CGL_4_A
from cpl.geometry import Point
from cpl.geometry.convex_hull import convex_hull


def main() -> None:
    _, *xy = map(int, open(0).read().split())
    ps = [Point(x, y) for x, y in zip(*[iter(xy)] * 2)]
    ch = convex_hull(ps)
    N = len(ch)
    s = 0
    for i in range(1, N):
        if ch[i].y < ch[s].y or (ch[i].y == ch[s].y and ch[i].x < ch[s].x):
            s = i
    ch = ch[s:] + ch[:s]
    print(N)
    [print(p.x, p.y) for p in ch]


if __name__ == "__main__":
    main()
