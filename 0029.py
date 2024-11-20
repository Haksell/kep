# ruff: noqa: E731
from heapq import nsmallest
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    _, k = mir()
    a = lmir()
    print(nsmallest(k, a)[-1])


if __name__ == "__main__":
    main()
