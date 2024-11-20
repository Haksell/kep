# ruff: noqa: E731, E741
import sys
from functools import wraps
from time import time

sys.setrecursionlimit(10000)

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def timing(f):
    @wraps(f)
    def wrap():
        ts = time()
        result = f()
        te = time()
        print(f"{f.__name__}() took {te - ts:.6f}s.", file=sys.stderr)
        return result

    return wrap


@timing
def naive():
    res = " ".join(
        i for i in map(str, range(10**3, 10**4)) if sum(map(ord, i)) & 1 == 0
    )
    print("".join(res))


@timing
def smart():
    def helper(a, b, c, d):
        nonlocal i, res
        if a >= 10:
            return
        if b >= 10:
            helper(a + 1, 0, 0, ~a & 1)
            return
        if c >= 10:
            helper(a, b + 1, 0, ~(a ^ b) & 1)
            return
        if d >= 10:
            helper(a, b, c + 1, ~(a ^ b ^ c) & 1)
            return
        res[i] = a ^ 48
        res[i + 1] = b ^ 48
        res[i + 2] = c ^ 48
        res[i + 3] = d ^ 48
        i += 5
        helper(a, b, c, d + 2)

    i = 0
    res = [32] * (4500 * 5 - 1)
    helper(1, 0, 0, 1)
    print(bytearray(res).decode("ascii"))


@timing
def genius():
    size = 4500 * 5 - 1
    res = [32] * size
    i = 0
    for a in range(49, 58):
        for b in range(48, 58):
            for c in range(48, 58):
                start = ((a ^ b ^ c) & 1) ^ 48
                res[i] = res[i + 5] = res[i + 10] = res[i + 15] = res[i + 20] = a
                res[i + 1] = res[i + 6] = res[i + 11] = res[i + 16] = res[i + 21] = b
                res[i + 2] = res[i + 7] = res[i + 12] = res[i + 17] = res[i + 22] = c
                res[i + 3] = start
                res[i + 8] = start + 2
                res[i + 13] = start + 4
                res[i + 18] = start + 6
                res[i + 23] = start + 8
                i += 25
    print(bytearray(res).decode("ascii"))


def test0017(capfd):
    naive()
    naive_output = capfd.readouterr().out.strip()
    smart()
    smart_output = capfd.readouterr().out.strip()
    genius()
    genius_output = capfd.readouterr().out.strip()
    assert naive_output == smart_output == genius_output


def main():
    genius()


if __name__ == "__main__":
    main()
