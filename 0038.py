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
    if n == 0:
        print(0)
    else:
        a, b = divmod(n, 9)
        print((str(b) if b else "") + "9" * a)


if __name__ == "__main__":
    main()
