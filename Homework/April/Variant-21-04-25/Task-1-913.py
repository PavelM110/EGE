from itertools import permutations

matrix = '235 146 145 236 137 247 56'.split()
graph = 'ae eg gf fb ba bd df dc ac ce'.split()

print(*range(1, 8))

for p in permutations('abcdefg'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)