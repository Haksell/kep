# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    s = input()
    print(next((i for i, c in enumerate(reversed(s)) if c != "0"), len(s)))


if __name__ == "__main__":
    main()
