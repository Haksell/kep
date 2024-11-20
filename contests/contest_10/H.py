# ruff: noqa: E731, E741
from collections import defaultdict
from functools import reduce
from itertools import accumulate, combinations
from operator import xor
import random
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

MOD = 1_000_000_007
# MOD = 101


def naive(a):
    return (
        sum(
            sum(a[i:j])
            for i in range(len(a))
            for j in range(i + 1, len(a) + 1)
            if reduce(xor, a[i:j]) == 0
        )
        % MOD
    )


def smart(a):
    psum = list(accumulate(a, initial=0))
    pxor = list(accumulate(a, xor, initial=0))
    idx = defaultdict(list)
    for i, px in enumerate(pxor):
        idx[px].append(i)
    res = 0
    for v in idx.values():
        acc = 0
        for cnt, i in enumerate(v, 1):
            acc += psum[i]
            res += cnt * psum[i] - acc
            res %= MOD
    return res


def main():
    if False:
        random.seed(42)
        for i in range(1000):
            a = [random.randint(1, 31) for _ in range(random.randint(1, 10))]
            na = naive(a)
            sa = smart(a)
            if na != sa:
                print(i)
                print(a)
                print(list(accumulate(a, xor, initial=0)))
                print(list(accumulate(a, initial=0)))
                print(na)
                print(sa)
                return
    else:
        _ = ir()
        a = lmir()
        print(smart(a))


if __name__ == "__main__":
    main()
