# ruff: noqa: E731, E741
from math import isqrt
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(n):
    s = isqrt(n)
    smaller = s * (4 * s**2 - 3 * s - 1) // 6
    equal = s * (n - s**2 + 1)
    return smaller + equal


def test0005():
    assert solve(0) == 0
    assert solve(1) == 1
    assert solve(2) == 2
    assert solve(3) == 3
    assert solve(4) == 5
    assert solve(5) == 7
    assert solve(6) == 9
    assert solve(7) == 11
    assert solve(8) == 13
    assert solve(9) == 16
    assert solve(10) == 19
    assert solve(11) == 22
    assert solve(12) == 25
    assert solve(13) == 28
    assert solve(14) == 31
    assert solve(15) == 34
    assert solve(16) == 38


def main():
    print(solve(ir()))


if __name__ == "__main__":
    main()
