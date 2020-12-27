from typing import Sequence


def lcs(S: Sequence, T: Sequence) -> int:
    dp = [0] * (len(S) + 1)
    for t in T:
        _dp = [0]
        for j, s in enumerate(S):
            if s == t:
                _dp.append(dp[j] + 1)
            else:
                _dp.append(max(dp[j + 1], _dp[j]))
        dp = _dp
    return dp[-1]
