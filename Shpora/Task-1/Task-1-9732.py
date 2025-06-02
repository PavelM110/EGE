from itertools import permutations

matrix = '47 357 2567 16 236 345 123'.split()
graph = 'cg ga ad db bf fc fe ec be eg'.split()

print(*range(1, 8))

for p in permutations('abcdefg'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)