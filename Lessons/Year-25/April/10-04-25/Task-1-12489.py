from itertools import permutations

matrix = '235 13 1245678 36 13 347 368 37'.split()
graph = 'ab bg ge ez zx xd dg gv va ag gz gx'.split()

print(*range(1, 9))
for p in permutations('abvgdexz'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)