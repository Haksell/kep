# ruff: noqa: E731
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    _, k = mir()
    for i, x in enumerate(input().split()):
        if x == "1":
            k -= 1
            if k == 0:
                print(i)
                return
    print(-1)


if __name__ == "__main__":
    main()
