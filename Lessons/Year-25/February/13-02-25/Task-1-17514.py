from itertools import permutations

matrix = '247 148 578 126 38 47 136 235'.split()
graph = 'bh hf fd dc ce ea ab ah eg gc gf'.split()

print(*range(1, 9))

for p in permutations('abcdefgh'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)