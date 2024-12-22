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


def exists(a, b, x, y):
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


def divs(b, lo, hi):
    return hi // b - (lo - 1) // b


def smart(a, b, x, y):
    if a == b:
        return (1, a * x)
    if x == y == 1:
        return (a * b, a * b)

    g = gcd(a, b)
    a //= g
    b //= g
    if a > b:
        a, b, x, y = b, a, y, x
    # a smol

    for lo in (1, a):
        for hi in (a * x, a * x + a - 1):
            if divs(b, lo, hi) == y:
                return (lo * g, hi * g)

    hi = a * b
    lo = hi - b * (y - 1)
    diff = x - divs(a, lo, hi)
    below = (diff) // 2
    above = (diff + 1) // 2
    return (lo - below * a, hi + above * a)


def main():
    if True:
        for a, b, x, y in product(range(1, 11), repeat=4):
            if not exists(a, b, x, y):
                continue
            lo, hi = rs = smart(a, b, x, y)
            if lo <= 0 or hi <= 0 or divs(a, lo, hi) != x or divs(b, lo, hi) != y:
                print(
                    a,
                    b,
                    (x, divs(a, lo, hi)),
                    (y, divs(b, lo, hi)),
                    "!",
                    f"range={rs}",
                )
                return
    else:
        for _ in rir():
            a, b, x, y = mir()
            print(*smart(a, b, x, y))


if __name__ == "__main__":
    main()
