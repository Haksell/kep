# ruff: noqa: E731, E741
from fractions import Fraction
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    p1, p2 = [Fraction(x) for x in input().split()]
    x1 = p1 + (1 - p2) * (1 - p1)
    x2 = 1 - p1
    print("First" if x1 > x2 else "Second" if x2 > x1 else "Equal")


if __name__ == "__main__":
    main()
