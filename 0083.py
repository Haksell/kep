from operator import mul

catalan = [1, 1, 2, 5, 14, 42, 132]
print(sum(map(mul, catalan, reversed(catalan))))
