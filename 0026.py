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
    q, r = divmod(n, 60)
    xs = [int(i % 12 == 0 or i % 5 == 0) for i in range(1, 61)]
    print(sum(xs) * q + sum(xs[:r]))


if __name__ == "__main__":
    main()
