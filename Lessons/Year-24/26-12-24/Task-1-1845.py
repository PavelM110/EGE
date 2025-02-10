from itertools import permutations

graph = 'AB BG GE EZ ZD DV AV BV DG'.split()
matrix = '67 567 456 35 234 123 12'.split()

print(*range(1, 8))

for p in permutations('ABVGDEZ'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)