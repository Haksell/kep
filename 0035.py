# ruff: noqa: E731
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    a = ir()
    b = ir()
    if a > b:
        a, b = b, a
    print(b // 4 - (a - 1) // 4)


if __name__ == "__main__":
    main()
