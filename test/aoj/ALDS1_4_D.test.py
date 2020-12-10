# noqa: E501 # verify-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_4_D
from cpl.algorithm.binary_search import binary_search


def main() -> None:
    def is_loadable(x):
        if x < max_W:
            return False
        cur_w = 0
        cnt = 1
        for w in W:
            if cur_w + w <= x:
                cur_w += w
            else:
                cur_w = w
                cnt += 1
        return cnt <= K

    N, K, *W = map(int, open(0).read().split())
    max_W = max(W)
    print(binary_search(0, sum(W), is_loadable))


if __name__ == "__main__":
    main()
