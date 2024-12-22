# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    r = []
    n = ir()
    p = 1
    while n:
        n, d = divmod(n, 10)
        if d:
            r.append(d * p)
        p *= 10
    print(len(r))
    print(*r)


if __name__ == "__main__":
    main()
