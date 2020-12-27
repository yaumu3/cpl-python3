# noqa: E501 # verify-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/10/ALDS1_10_C
from cpl.dp.lcs import lcs

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        X = input()
        Y = input()
        print(lcs(X, Y))
