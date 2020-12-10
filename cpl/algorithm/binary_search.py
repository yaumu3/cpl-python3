from typing import Callable


def binary_search(bad: int, good: int, is_good: Callable[[int], bool]) -> int:
    while abs(bad - good) > 1:
        mid = (bad + good) // 2
        if is_good(mid):
            good = mid
        else:
            bad = mid
    return good
