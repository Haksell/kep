# ruff: noqa: E731, E741
from math import sqrt
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    a = ir()
    b = ir()
    x = (-a + sqrt(a * a - 4 * b)) / -2
    y = a - x
    print(x, y)


"""
x+y=a
xy=b

x=a-y
(a-y)y=b
ay-yy=b
-yy+ay-b=0

d=aa-4b
x1=((-a)+sqrt(aa-4b))/-2
x2=((-a)-sqrt(aa-4b))/-2
"""


if __name__ == "__main__":
    main()
