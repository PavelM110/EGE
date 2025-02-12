from itertools import permutations

matrix = '47 57 45 136 236 457 126'.split()
graph = 'bd de ea ag gf fb bc ce cg'.split()

print(*range(1, 8))
for p in permutations('abcdefg'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)