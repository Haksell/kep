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
    res = sqrt(12) * (
        1
        - 1 / (3 * 3)
        + 1 / (5 * 3**2)
        - 1 / (7 * 3**3)
        + 1 / (9 * 3**4)
        - 1 / (11 * 3**5)
    )
    print(f"{res:.2f}")


if __name__ == "__main__":
    main()
