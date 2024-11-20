# ruff: noqa: E731
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    na = ir()
    a = lmir()
    nb = ir()
    b = lmir()
    res = []
    ia = ib = 0
    while ia < na and ib < nb:
        if a[ia] < b[ib]:
            res.append(a[ia])
            ia += 1
        else:
            res.append(b[ib])
            ib += 1
    res.extend(a[ia:])
    res.extend(b[ib:])
    print(*res)


if __name__ == "__main__":
    main()
