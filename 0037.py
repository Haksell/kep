# ruff: noqa: E731
from collections import Counter
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    a = [list(map(int, line.split())) for line in sys.stdin][-1]
    c = Counter(a)
    m = max(c.values())
    print(min(k for k, v in c.items() if v == m))


if __name__ == "__main__":
    main()
