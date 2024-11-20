# ruff: noqa: E731, E741
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
    print(
        "Yes" if n >= 2 and all(n % i != 0 for i in range(2, isqrt(n) + 1)) else "No",
    )


if __name__ == "__main__":
    main()
