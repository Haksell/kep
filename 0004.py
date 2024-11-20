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
    a = float(read())
    b = float(read())
    print((a + b) / 2)
    print(sqrt(a * b))
    print(2 / (1 / a + 1 / b))


if __name__ == "__main__":
    main()
