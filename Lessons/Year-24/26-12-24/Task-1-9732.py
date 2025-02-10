from itertools import permutations

matrix = '47 357 2567 16 236 345 123'.split()
graph = 'CG GA AD FB BD FC EG EC EF EB'.split()

print(*range(1, 8))

for p in permutations('ABCDEFG'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)