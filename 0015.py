# ruff: noqa: E731, E741
from math import factorial
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n = int(input())
    x = factorial(n) >> (n >> 1)
    print(x * x * ((n + 1) >> 1 if n & 1 else n + 1))


if __name__ == "__main__":
    main()
