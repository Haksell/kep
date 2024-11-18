# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    _ = ir()
    a = lmir()
    d = [[], [], []]
    for i, ai in enumerate(a):
        if 1 <= ai <= 3:
            d[ai - 1].append(i + 1)
    print(*[di[i] if i < len(di) else -1 for i, di in enumerate(d)])


if __name__ == "__main__":
    main()
