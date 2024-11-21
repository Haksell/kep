# ruff: noqa: E731
from math import isqrt
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n = ir()
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            j = n // i
            print(i, j, *[1] * (n - i - j))
            return
    print(-1)


if __name__ == "__main__":
    main()
