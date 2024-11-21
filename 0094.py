# ruff: noqa: E731
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

# bad translation


def main():
    for n in range(100, 1000):
        m = n
        p = 1
        s = 0
        while m:
            m, d = divmod(m, 10)
            p *= d
            s += d
        if p % s == 0:
            print(n)


if __name__ == "__main__":
    main()
