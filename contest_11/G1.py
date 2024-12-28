# ruff: noqa: E731, E741
from itertools import product
from math import gcd
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def divs(b, lo, hi):
    return hi // b - (lo - 1) // b


def naive(a, b, x, y):
    if a < b:
        a, b, x, y = b, a, y, x
    for add in range(0, a * a, a):
        print(
            a,
            b,
            x,
            y,
            (add, add + a * (x - 1), divs(b, add, add + a * (x - 1))),
            (add + 1, add + a * x + x - 1, divs(b, add + 1, add + a * x + x - 1)),
        )
        if (
            divs(b, add, add + a * (x - 1))
            <= y
            <= divs(b, add - a + 1, add + a * x - 1)
        ):
            return True
    return False


def smart(a, b, x, y):
    if a == b:
        return x == y
    g = gcd(a, b)
    a //= g
    b //= g
    if a < b:
        a, b, x, y = b, a, y, x
    lo = a * (x - 1) + 1
    hi = a * (x + 1) - 1
    return lo // b <= y <= (hi + b - 1) // b


def main():
    if False:
        for a, b, x, y in product(range(1, 11), repeat=4):
            rs = smart(a, b, x, y)
            rn = naive(a, b, x, y)
            if rs != rn:
                print(a, b, x, y, "!", f"naive={rn} smart={rs}")
                return
    else:
        for _ in rir():
            a, b, x, y = mir()
            print("Yes" if smart(a, b, x, y) else "No")


if __name__ == "__main__":
    main()
