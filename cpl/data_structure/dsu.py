from typing import List


class DSU:
    def __init__(self, n: int = 0) -> None:
        self._n: int = n
        # root node: -1 * component size
        # otherwise: parent
        self.parent_or_size: List[int] = [-1] * n

    def merge(self, a: int, b: int) -> int:
        assert 0 <= a < self._n
        assert 0 <= b < self._n
        x, y = self.leader(a), self.leader(b)
        if x == y:
            return x
        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        return x

    def same(self, a: int, b: int) -> bool:
        assert 0 <= a < self._n
        assert 0 <= b < self._n
        return self.leader(a) == self.leader(b)

    def leader(self, a: int) -> int:
        assert 0 <= a < self._n
        parent = self.parent_or_size[a]
        while parent >= 0:
            if self.parent_or_size[parent] < 0:
                return parent
            self.parent_or_size[a], a, parent = (
                self.parent_or_size[parent],
                self.parent_or_size[parent],
                self.parent_or_size[self.parent_or_size[parent]],
            )
        return a

    def size(self, a: int) -> int:
        assert 0 <= a < self._n
        return -self.parent_or_size[self.leader(a)]

    def groups(self) -> List[List[int]]:
        leader_buf = [self.leader(i) for i in range(self._n)]
        group_size = [0] * self._n
        for i in range(self._n):
            group_size[leader_buf[i]] += 1
        result = [[] for _ in range(self._n)]
        for i in range(self._n):
            result[leader_buf[i]].append(i)
        return [row for row in result if row]
