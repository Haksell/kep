from itertools import count
from math import comb


q, n1, k1, m = map(int, input().split())
n, k = n1, k1
xs = []
for i in count(1):
    x = comb(n, k) % m
    xs.append(x)
    n = (943 * n + 17) % 25000 + 1
    k = (1999 * k + 24) % 25000 + 1
    if n == n1 and k == k1:
        chunks, remaining = divmod(q, i)
        print((sum(xs) % m * chunks % m + sum(xs[:remaining])) % m)
        break
