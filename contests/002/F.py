# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    d = ir()
    m = ir()
    y = ir()
    t1 = (y, m, d)
    t2 = (2021, 2, 14)
    print("<" if t1 < t2 else ">" if t1 > t2 else "=")


if __name__ == "__main__":
    main()
