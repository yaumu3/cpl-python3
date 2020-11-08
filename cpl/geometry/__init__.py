from math import sqrt
from typing import List

Polygon = List["Point"]


class Point:
    EPS = 1e-10

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<Point x={self.x}, y={self.y}>"

    def __eq__(self, other):
        return abs(self.x - other.x) < self.EPS and abs(self.y - other.y) < self.EPS

    def __lt__(self, other):
        return self.x < other.x if self.x != other.x else self.y < other.y

    def __add__(self, other: "Point"):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point"):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Point"):
        return Point(self.x * other.x, self.y * other.y)

    def __div__(self, other: "Point"):
        return Point(self.x / other.x, self.y / other.y)

    def norm(self) -> float:
        return self.x ** 2 + self.y ** 2

    def abs(self) -> float:
        return sqrt(self.norm())


def cross(a: Point, b: Point) -> float:
    return a.x * b.y - a.y * b.x
