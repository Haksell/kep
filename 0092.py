# ruff: noqa: E731
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    x = ir()
    y = ir()
    print([[1, 2][x < 0], [3, 4][x > 0]][y < 0])


if __name__ == "__main__":
    main()
