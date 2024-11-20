# ruff: noqa: E731
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n = ir()
    res = 1
    d = 2
    while d * d <= n:
        cur = 1
        while n % d == 0:
            cur += 1
            n //= d
        res *= cur
        d += 1
    if n > 1:
        res <<= 1
    print(res)


if __name__ == "__main__":
    main()
