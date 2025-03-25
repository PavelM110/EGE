from itertools import permutations

matrix = '36 478 178 258 46 158 23 2346'.split()
graph = 'be eg gh hc cd df fb ba ag ac ad'.split()

print(*range(1, 9))

for p in permutations('abcdefgh'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)