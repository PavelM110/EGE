from itertools import permutations

matrix = '37 367 125 56 34 247 126'.split()
graph = 'ad de eg gc cf fa ab be fb'.split()

print(*range(1, 8))

for p in permutations('abcdefg'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)