# ruff: noqa: E731
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    read()
    res = [-1] * 9
    cnt = [0] * 9
    for i, n in enumerate(map(int, input().split())):
        if 1 <= n <= 10:
            cnt[n - 1] += 1
            if cnt[n - 1] == n:
                res[n - 1] = i + 1
    print(*res)


if __name__ == "__main__":
    main()
