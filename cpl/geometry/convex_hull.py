from cpl.geometry import Polygon, cross


def convex_hull(ps: Polygon) -> Polygon:
    """Andrew's algorithm"""

    def construct(limit, start, stop, step=1):
        for i in range(start, stop, step):
            while len(res) > limit and cross(res[-1] - res[-2], s_ps[i] - res[-1]) < 0:
                res.pop()
            res.append(s_ps[i])

    assert len(ps) >= 3
    s_ps = sorted(ps)
    N = len(s_ps)
    res: Polygon = []
    construct(1, 0, N)
    construct(len(res), N - 2, -1, -1)
    return res[:-1]
